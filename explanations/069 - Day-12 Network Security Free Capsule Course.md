# Day-12 Network Security — NFS, SMTP, and MySQL — Explained

## Where this lesson fits

This is the practical **Network Services 2** lesson. Day 11 established the basic pattern with SMB, Telnet and FTP. Day 12 applies the same pattern to three different services:

```text
Discover → identify → enumerate → form a hypothesis → validate → document
```

The room is valuable because each service contributes a different link in an attack chain:

| Service | Normal purpose | Lab weakness | Result |
|---|---|---|---|
| NFS | Share filesystems | exposed home data + `no_root_squash` | SSH key disclosure, then local privilege escalation |
| SMTP | Transfer email | version/user enumeration | valid username used in authorized SSH audit |
| MySQL | Store/query relational data | exposed service + known/reused credentials | authenticated database enumeration |

None of these protocols is inherently an “exploit.” The risk comes from exposure, configuration, credentials and permissions.

---

# 1. NFS mental model

## Export versus mount

These two words describe opposite sides of one operation:

- The **server exports** a directory.
- The **client mounts** that export at a local directory.

If the server exports `/home` and the client mounts it at `/tmp/mount`, a file visible as `/tmp/mount/user/a.txt` on the client may physically be `/home/user/a.txt` on the server.

That explains why a key found through the mount can later authenticate to SSH: it is not a copied training prop; it is a server-side file exposed through NFS.

## Why RPC appears

NFS uses remote procedure calls. The client is effectively asking the server to perform filesystem operations—lookup, read, write, get attributes and so on. `rpcbind` helps clients discover RPC services. Consequently, an NFS target often exposes more than one related port, even though TCP/UDP 2049 is the best-known NFS port.

Useful discovery/enumeration commands:

```bash
nmap -sV -p 111,2049 <target>
rpcinfo -p <target>
showmount -e <target>
```

A full lab scan may discover dynamic ports:

```bash
nmap -A -p- <target>
```

Do not run broad scans outside an authorized target range.

## Safe mount workflow

```bash
sudo apt install nfs-common
mkdir -p /tmp/nfs-mount
showmount -e <target>
sudo mount -t nfs <target>:/export /tmp/nfs-mount -o ro,nolock
findmnt /tmp/nfs-mount
```

A useful improvement over the classroom command is `ro`: mount read-only first. That reduces the chance of accidentally changing target data while enumerating. Remount read-write only when the lab explicitly requires writing.

Clean up afterward:

```bash
cd /
sudo umount /tmp/nfs-mount
rmdir /tmp/nfs-mount
```

Do not try to unmount while your shell's current directory is inside the mount.

## UID/GID trust and root squashing

Traditional NFS authorization relies heavily on numeric UID/GID values supplied in requests. This is why server-side export policy is critical.

With `root_squash` (the normal safe default), requests from client UID 0 are mapped to an anonymous identity. With `no_root_squash`, client root is allowed to act as root on files in the export.

Example vulnerable export entry:

```exports
/home *(rw,no_root_squash)
```

The wildcard client range plus read-write access plus `no_root_squash` is especially dangerous.

Safer design:

- restrict clients to necessary addresses/subnets;
- retain `root_squash`;
- use read-only exports where possible;
- export the smallest necessary path;
- protect private material such as `.ssh`;
- firewall RPC/NFS so it is not internet-accessible;
- prefer modern NFS security modes where the environment supports them.

## Why the SUID step works

A SUID executable runs with the file owner's effective UID rather than only the caller's UID. The lab chain is:

```text
client root
   ↓ writes through no_root_squash
a server-visible file owned by root
   ↓ chmod +s
root-owned SUID executable
   ↓ target user executes with privilege-preserving behavior
effective root shell
```

Verification matters:

```bash
ls -ln bash     # numeric owner should be 0 and mode should contain s
./bash -p
id              # verify effective identity
```

Two important caveats:

1. Filesystems can be mounted with `nosuid`, which prevents SUID behavior.
2. Copying a binary from a different architecture or incompatible system can fail. Compile/copy for the target environment in a controlled lab.

The fix is not “remove Bash”; it is correct NFS export policy.

---

# 2. SMTP enumeration as an information leak

## Separate mail roles

| Protocol | Main role | Common ports |
|---|---|---|
| SMTP | sending and server-to-server transfer | 25, 465, 587 |
| POP3 | mailbox retrieval | 110, 995 |
| IMAP | synchronized mailbox access | 143, 993 |

TLS variants and STARTTLS behavior depend on service configuration; a port number alone is not proof that traffic is securely configured.

## What SMTP enumeration can reveal

An SMTP banner can disclose:

- mail software and version;
- hostname/domain naming;
- supported commands/extensions;
- authentication methods;
- whether the service distinguishes valid from invalid users.

Historically, commands such as `VRFY`, `EXPN`, or different recipient responses could reveal account existence. Modern servers often disable or normalize these responses.

Metasploit workflow from the lesson:

```text
msfconsole
search smtp_version
use auxiliary/scanner/smtp/smtp_version
set RHOSTS <target>
run

search smtp_enum
use auxiliary/scanner/smtp/smtp_enum
set RHOSTS <target>
set USER_FILE <wordlist>
run
```

Always run `show options`; module paths and option names can vary by framework version.

## Why the username changes the next step

Testing every username/password combination has a large search space and creates excessive traffic. SMTP enumeration reduces uncertainty by confirming `administrator`. The CTF then supplies a limited password list for an SSH audit:

```bash
hydra -l administrator -P <list> ssh://<target>
```

This is credential testing and requires explicit permission. On real infrastructure, it can lock accounts, trigger monitoring or violate a program's rules even when the web application itself is in scope.

Defensive controls include:

- disable unnecessary SMTP verification behavior;
- return uniform responses where practical;
- patch and minimize banner detail;
- enforce strong unique passwords and MFA for remote administration;
- rate-limit and alert on enumeration/authentication bursts;
- separate public mail roles from management access.

---

# 3. MySQL enumeration with known credentials

## Connection anatomy

```bash
mysql -h <host> -u root -p
```

- `-h` selects the remote database host.
- `-u` selects the MySQL account.
- `-p` prompts securely for its password.

Do not use `-ppassword` in normal work. It can leak through history and process inspection.

A database login is separate from an operating-system login. A credential that fails over SSH may legitimately belong to MySQL, a web application or another service. In an assessment, test reuse only where scope permits it.

## Native SQL enumeration

Start minimally:

```sql
SELECT VERSION();
SELECT USER(), CURRENT_USER();
SHOW DATABASES;
```

`USER()` describes the presented client identity; `CURRENT_USER()` represents the account used for privilege checking. They can differ.

Then inspect only relevant databases:

```sql
USE app_database;
SHOW TABLES;
DESCRIBE users;
SELECT * FROM users LIMIT 10;
```

Use a limit to avoid unnecessarily extracting large datasets. In a real test, demonstrate impact with the minimum data required and follow reporting/data-handling policy.

## Schemas are structure, not merely contents

A schema dump can expose:

- database names;
- table names;
- column names and types;
- keys and relationships;
- stored procedures or other metadata.

Even without dumping every record, names like `password_reset_tokens`, `payments`, or `admin_users` can reveal application design and guide authorized testing.

Metasploit's `mysql_schemadump` automates metadata queries. Treat it as a convenience layer:

```text
use auxiliary/scanner/mysql/mysql_schemadump
set RHOSTS <target>
set USERNAME root
set PASSWORD password
run
```

Confirm results with native SQL where possible. Automation output can be incomplete, version-sensitive, or misunderstood.

## Password hashes

A hash is not encryption: it is intended to be one-way. Secure password storage uses a unique salt and a deliberately expensive password-hashing function such as Argon2id, scrypt, bcrypt or PBKDF2. Fast general-purpose hashes are poor password storage.

Database server account hashes and application user password hashes are separate concepts. Access to MySQL's account metadata depends on version and privileges; application hashes may be stored in an ordinary app table. Handle either as sensitive data.

Defensive controls:

- do not expose port 3306 publicly unless absolutely necessary;
- bind to required interfaces and firewall allowed clients;
- never use a remote all-powerful root account for an application;
- grant each application the minimum database privileges;
- use unique secrets and rotate exposed credentials;
- enable transport encryption where traffic crosses untrusted networks;
- monitor authentication failures and unusual schema enumeration.

---

# 4. Full attack-chain view

Day 12 is best remembered as three different chains rather than a list of commands.

## NFS chain

```text
Nmap/RPC discovery
→ showmount export enumeration
→ mount share
→ discover SSH key
→ SSH as low-privileged user
→ inspect /etc/exports
→ identify no_root_squash
→ place root-owned SUID executable through share
→ local root
```

## SMTP chain

```text
Nmap finds port 25
→ version/banner enumeration
→ SMTP username enumeration
→ confirmed administrator account
→ authorized password-list audit against SSH
→ login and retrieve lab flag
```

## MySQL chain

```text
Nmap finds database service
→ supplied credential hypothesis
→ native client login
→ verify version/account
→ enumerate databases/tables
→ schema/hash modules automate permitted queries
→ document excessive exposure and privilege
```

The common skill is hypothesis-driven enumeration. Every result informs the next narrow action.

---

# Command card

```bash
# NFS
sudo apt install nfs-common
nmap -A -p- <target>
showmount -e <target>
mkdir -p /tmp/mount
sudo mount -t nfs <target>:/export /tmp/mount -o nolock
findmnt /tmp/mount
sudo umount /tmp/mount

# SSH key discovered in an authorized share
chmod 600 id_rsa
ssh -i id_rsa user@<target>

# SMTP framework workflow
msfconsole
# search smtp_version / smtp_enum; show options; set RHOSTS; run

# Authorized CTF credential audit
hydra -l <user> -P <provided-list> ssh://<target>

# MySQL
sudo apt install default-mysql-client
mysql -h <target> -u <user> -p
```

## Review questions

1. What is the difference between an NFS export and a client mount?
2. Why does `root_squash` exist, and what changes under `no_root_squash`?
3. Why should initial NFS enumeration use a read-only mount where possible?
4. How can SMTP disclose information without giving mailbox access?
5. Why is a database account different from an OS/SSH account?
6. What does a schema dump reveal that `SHOW DATABASES` alone does not?
7. For each chain, which result justified the next action?

<!-- DONE-069 -->
