# Day-12 Network Security Free Capsule Course [Hindi] — English Translation

*Translated from: `069 - Day-12 Network Security Free Capsule Course [ Hindi ].hi-orig.srt`*
*Style: detailed, verbatim-style edited translation. Repeated captions, stream checks, and obvious auto-caption stutters are consolidated. Commands reconstructed from the spoken demonstration are marked where necessary.*

---

Hello guys, welcome to our YouTube channel. My name is Ayush Pathak, and today we are going to do Day 12 of Network Security. You already know that all the lectures through Day 11 have been uploaded. I hope you watched them completely and understood everything properly.

Alongside this, the Bash series by Sachin Sir is also running live. It too has reached around Day 12, so you can follow both series and practise. Turn on notifications if you want the latest updates. And if you are following the classes, post about what you learn. That feedback tells us which series people find useful and gives us motivation to continue it.

## Today's room: Network Services 2

In the previous class we completed the **Network Services** room. Today we will do **Network Services 2**. In the first room we covered and enumerated familiar services such as SMB, Telnet and FTP. Today we will look at some protocols that you may encounter less often in beginner CTFs, but which are still very important:

1. NFS — Network File System
2. SMTP — Simple Mail Transfer Protocol
3. MySQL

The method remains the same. First understand what the service normally does. Then enumerate it. Only after that should you think about exploitation. If you do not understand the protocol, copying an exploit command will not teach you anything.

# Part 1 — NFS

## What is NFS?

NFS means **Network File System**. It is a protocol through which a server shares a directory over the network. A client can mount that remote directory into its own local filesystem and then work with the files almost as though they were local.

Imagine that my server is sharing `/home/ayush`. As an NFS client, I can mount that share at a directory on my own system—for example `/tmp/mount`. After it is mounted, opening `/tmp/mount` shows the files from the server's shared `/home/ayush` directory.

The server and client communicate through **RPC**, Remote Procedure Call. NFS operations have to identify a file or directory on the remote filesystem. A file handle is used for this. The request also carries information such as the operation to perform and the user/group identity involved. The exact internals vary by NFS version, but for this room you should understand the larger idea: the client sends remote filesystem operations to the server, and the server decides whether they are permitted.

The room asks: which protocol does NFS use to communicate between the server and client? The answer is **RPC**. It also asks which two pieces of user data the server considers. Those are the **UID** and **GID**—the user ID and group ID.

## NFS utilities

On Debian/Kali systems, install the common NFS client tools with:

```bash
sudo apt install nfs-common
```

This package provides utilities such as `showmount` and `mount.nfs`. The AttackBox already has what we need. If your own Kali system does not, install the package there.

`showmount` asks an NFS server what it exports:

```bash
showmount -e <target-ip>
```

The `-e` option means exports. An export is a server-side path offered to clients.

## Start with a port scan

As with every target in this network-security series, begin by identifying the host and scanning its ports. The demonstration uses Nmap against the room's target IP. The scan is slow, so we wait rather than assuming the machine is broken.

```bash
nmap -A -p- <target-ip>
```

A full scan is useful in the lab because NFS/RPC can involve several ports. Port **2049** is the standard NFS port. RPC services and `rpcbind` are also visible. Once the scan confirms NFS, enumerate exports:

```bash
showmount -e <target-ip>
```

The result shows the available share—in this room, a home-directory export.

## Mounting the exported directory

First create a local directory to use as the mount point:

```bash
mkdir /tmp/mount
```

Then mount the remote export:

```bash
sudo mount -t nfs <target-ip>:/home /tmp/mount -o nolock
```

Let us break that down:

- `sudo` is required for the local mount operation.
- `mount` attaches a filesystem.
- `-t nfs` tells `mount` that the filesystem type is NFS.
- `<target-ip>:/home` is the server and exported path.
- `/tmp/mount` is our local mount point.
- `-o nolock` disables NLM locking, which is useful for this lab setup.

The exact export must match what `showmount -e` displays. Do not blindly assume every server shares `/home`.

After mounting, list the contents:

```bash
cd /tmp/mount
ls -la
```

The mounted home directory contains a user's files, including an `.ssh` directory. This is why enumeration matters: a carelessly exported home directory can expose private keys and other credentials.

## Using the exposed SSH key

Inside the mounted share we find a private key. Copy it to our attacking machine, give it restrictive permissions, and use it with SSH:

```bash
cp /tmp/mount/<user>/.ssh/id_rsa /tmp/id_rsa
chmod 600 /tmp/id_rsa
ssh -i /tmp/id_rsa <user>@<target-ip>
```

SSH refuses to use a private key if its local permissions are too open, hence `chmod 600`. The room provides clues to the username through the exported directory. With the correct user and key, we obtain a shell on the target and retrieve the requested user flag.

Notice an important distinction: SSH gave us initial access, but the exposure happened through the NFS share. NFS did not itself create an SSH session; it leaked material that SSH accepted.

# NFS privilege escalation

## Root squashing

Now we look at an NFS-specific privilege-escalation condition. NFS normally enables **root squashing**. If a client-side root user creates a file on the share, the server maps that identity to an unprivileged anonymous account rather than trusting remote root as local root.

That protection prevents anyone who can mount a share from automatically obtaining root-owned files on the server.

The dangerous opposite is **`no_root_squash`**. If an export uses that option, root on the client can create a file that remains owned by root on the server. Combined with an executable and the SUID permission, that can become local privilege escalation.

After obtaining a shell on the target, inspect the export configuration:

```bash
cat /etc/exports
```

The room's vulnerable export includes `no_root_squash`. That is the misconfiguration we will exploit.

## Creating a root-owned SUID shell through the share

Because the same directory is mounted on our attacking machine, actions performed there affect the target's exported directory. On the attacking system, as root, copy a Bash executable into the mounted share and set its owner and SUID bit:

```bash
sudo cp /bin/bash /tmp/mount/bash
sudo chown root:root /tmp/mount/bash
sudo chmod +s /tmp/mount/bash
ls -l /tmp/mount/bash
```

In the permissions, the owner's execute position now contains `s`, indicating SUID. On the target shell, go to the shared directory and execute the copied Bash while preserving privilege:

```bash
./bash -p
id
```

The `-p` option tells Bash not to drop the effective privileged identity. `id` should now show an effective UID of root, allowing us to read the root flag.

The room may use a downloaded or supplied Bash binary rather than copying the attacker's `/bin/bash`; binary compatibility matters. The core sequence is the same:

1. Find an export with `no_root_squash`.
2. Mount it as a client.
3. As client root, place a root-owned executable there.
4. Set SUID.
5. Run it from the target.

This works because of the insecure export option, not because every NFS server is automatically vulnerable.

# Part 2 — SMTP

## What SMTP does

SMTP stands for **Simple Mail Transfer Protocol**. It is used for sending mail. An SMTP server performs basic tasks such as identifying the sender and recipient, accepting outgoing mail, relaying or delivering it, and returning a failure message when delivery cannot be completed.

Do not confuse SMTP with message-retrieval protocols. **POP3** and **IMAP** retrieve mail for users. As discussed previously, POP3 has traditionally downloaded messages in a way that may remove them from the server, while IMAP keeps server state synchronized across multiple devices. SMTP handles sending/transfer.

SMTP commonly listens on TCP port **25**, with ports **465** and **587** used in other secure/submission configurations. In this room, Nmap shows port 25 open.

## Why enumerate SMTP?

A badly configured SMTP server may reveal its software version and whether particular usernames exist. A valid username can then become input to another authorized test—for example SSH credential auditing in this CTF.

Start with Nmap:

```bash
nmap -A -p- <target-ip>
```

Then open Metasploit:

```bash
msfconsole
```

Search for the SMTP version scanner:

```text
search smtp_version
use auxiliary/scanner/smtp/smtp_version
show options
set RHOSTS <target-ip>
run
```

This identifies details such as the SMTP banner, software and hostname. Pay attention to Metasploit's required options rather than pasting commands without checking them.

## SMTP user enumeration

Next search for and use the SMTP enumeration module:

```text
search smtp_enum
use auxiliary/scanner/smtp/smtp_enum
show options
set RHOSTS <target-ip>
set USER_FILE <path-to-user-list>
run
```

The module tests candidate names using SMTP behavior supported by the target. The room's vulnerable server reveals a valid account: `administrator`.

In a real assessment, user enumeration may be blocked, ambiguous, or prohibited by rate limits. In this room it is intentionally enabled so you can understand the information leak.

## Credential auditing with Hydra

Now that we have a confirmed username, the room asks us to audit SSH using a supplied password list:

```bash
hydra -l administrator -P <password-list> ssh://<target-ip>
```

`-l` supplies one login name and `-P` supplies a file of candidate passwords. Hydra highlights the valid password when found. Use the discovered credential to connect through SSH and retrieve the SMTP task's flag:

```bash
ssh administrator@<target-ip>
```

The important lesson is the chain: SMTP enumeration disclosed the user, and that precise user made the authorized SSH password test practical. Enumeration came before brute force.

# Part 3 — MySQL

## What MySQL is

MySQL is a relational database management system. It stores information in databases containing tables, columns and rows, and it is normally queried with SQL. Its standard TCP port is **3306**.

The room gives us a scenario: during an assessment or CTF, we found credentials in the form `root:password`. They did not work for SSH. Credentials are often reused across services, so we test them against the MySQL service that we have identified—within this lab's authorization.

## Installing the client and connecting manually

Our machine needs a database client:

```bash
sudo apt update
sudo apt install default-mysql-client
```

Depending on the distribution, the executable may come from a MariaDB-compatible client package. Connect remotely with:

```bash
mysql -h <target-ip> -u root -p
```

Enter the password when prompted rather than placing it directly in the shell command, where it may enter shell history or appear in process listings.

Once connected, useful SQL commands include:

```sql
SHOW DATABASES;
USE <database_name>;
SHOW TABLES;
DESCRIBE <table_name>;
SELECT * FROM <table_name>;
```

Each statement ends with a semicolon. The lab asks us to identify the server version and the number and names of databases.

## Enumerating MySQL with Metasploit

Metasploit contains auxiliary modules that automate common database enumeration. Search first rather than guessing a path:

```text
search mysql
```

Configure the selected module with the target and known credentials. A SQL-query module can run a harmless query such as `select version()` to verify access and report the server version. The schema-dump module enumerates database structure:

```text
use auxiliary/scanner/mysql/mysql_schemadump
show options
set RHOSTS <target-ip>
set USERNAME root
set PASSWORD password
run
```

The output includes schemas such as `information_schema` and `performance_schema` along with the room's application database. A schema describes database structure and metadata—databases, tables, columns and relationships—not merely one table's records.

The room also discusses password hashes. Secure systems do not normally store reusable plaintext passwords; they store one-way password hashes with suitable salting and a password-specific algorithm. If database account hashes are exposed, they may be audited offline in an authorized lab. Do not confuse database-account hashes with arbitrary application-user passwords; they may live in different tables and use different formats.

Other MySQL modules can enumerate accounts or dump hashes when the authenticated account has sufficient privileges. Metasploit is making manual work faster; it does not remove the need to understand what query is being issued or what permissions the credential possesses.

# Closing

Today we completed three service workflows:

- With **NFS**, we enumerated exports, mounted a share, used a leaked SSH key for initial access, and exploited `no_root_squash` for privilege escalation.
- With **SMTP**, we identified the server, enumerated a valid user, and used that information in the room's SSH credential-auditing step.
- With **MySQL**, we reused supplied credentials appropriately, connected with a native client, and enumerated version, databases, schemas and account information.

Keep a command sheet, but do not turn it into a copy-paste sheet. For each command, know what service you are talking to, what information you expect, and why the action is authorized. We will continue the network-security series in the next lectures.

<!-- DONE-069 -->
