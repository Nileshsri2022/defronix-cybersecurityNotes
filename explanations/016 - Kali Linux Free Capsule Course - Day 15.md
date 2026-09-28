# Explanation — Day 15 (Final): SSH, Encryption & SSH Hardening

**Lecture:** 016 — Kali Linux Free Capsule Course, Day 15 — **the final session**
**Translation:** [`english/016 - Kali Linux Free Capsule Course - Day 15.md`](../english/016%20-%20Kali%20Linux%20Free%20Capsule%20Course%20-%20Day%2015.md)

> **"Until you have knowledge about SSH, you cannot do anything."** — stated in the context of CTFs and practical security work.

---

## Part 1 — What SSH is

> **SSH is a network communication protocol that enables two computers to communicate and share data.**

**SSH = Secure Shell.**

### The practical motivation

You run Kali in a VM. All your work is in the terminal anyway. So why keep switching to the VM window and logging in?

> Leave the VM **running in the background** and **remote into it** from your host OS terminal.

### Why it's "secure"

> **SSH creates a TUNNEL between you and the server — a secure tunnel — through which all data is shared in ENCRYPTED form.**

---

## Part 2 — Encryption fundamentals

### What encryption is

> **Converting plain text into an UNREADABLE form.**

### The two types

| | **Symmetric** | **Asymmetric** |
|---|---|---|
| Keys | **One key** | **Two: public + private** |
| Same key encrypts & decrypts? | Yes | No |
| Private key | — | **Never leaves its owner** |
| Public key | — | **Shared freely** |
| Used by SSH | — | ✅ (RSA) |

### How asymmetric works

```
User 1 generates:  [public key] + [private key]
User 1 shares:     [public key]  →  User 2
User 2 encrypts data with User 1's PUBLIC key
Only User 1 can decrypt it — with their PRIVATE key
```

**The security property:**

> **Even if a hacker captures the data in transit, they cannot decrypt it.** Only the holder of the **private key** can.

### The lock-and-key analogy

> One lock with two keys: **one key always stays with the lock's owner; the second is shared.** Anyone can lock something with the shared key — **but only the owner's key can open it.**

---

## Part 3 — Installing and managing SSH

```bash
sudo apt install openssh-server
```

> **Until this package is installed, you cannot use the SSH service.**

### Service control — two equivalent methods

```bash
# Method 1
sudo service ssh status / start / stop / restart

# Method 2
sudo systemctl status ssh / start ssh / stop ssh / restart ssh
```

### ⚠ VM network setting

> **The adapter must be in BRIDGED MODE**, otherwise remote access within your LAN will not work.

*(This connects back to Day 12's troubleshooting section, where Bridged↔NAT switching was the fix for package problems.)*

---

## Part 4 — Configuration files

Everything lives in **`/etc/ssh/`**.

| File | Role |
|---|---|
| **`ssh_config`** | **CLIENT** configuration — for outgoing connections |
| **`sshd_config`** | **SERVER (daemon)** configuration — the one you harden |
| `ssh_host_*_key` / `.pub` | The host's own key pair |

### What a "daemon" is

> When you install a package, **a SERVICE is created — a PROCESS.** That process is called a service, and **in Linux a service is called a DAEMON.**

The `d` in `sshd` is literally "daemon". **`sshd_config` is the server-side file** — this is the distinction that trips people up.

---

## Part 5 — Remote access

```bash
ssh username@ip_address
ssh username@hostname        # hostname also works
```

**Verify where you actually are:**

```bash
hostname          # which machine
echo $USER        # which user
```

**Client tools mentioned:** **MobaXterm** (preferred — *"you can remote access MULTIPLE machines at once"*) or **PuTTY**.

---

## Part 6 — Running a command without logging in

```bash
ssh kali@192.168.1.148 hostname
ssh kali@192.168.1.148 pwd
```

> **It does NOT log in** — it runs the command remotely and **prints the output on your screen.**

Extremely useful for scripting and for quick one-off checks across machines.

---

## Part 7 — `scp` — secure file copy

```bash
scp <source_full_path> <user>@<ip>:<destination_path>
scp -r <directory>     <user>@<ip>:<path>       # recursive
```

**Example:**

```bash
scp /home/matrix/demo.txt kali@192.168.1.148:/home/kali/
```

### Two details that catch people out

1. **The colon `:`** separates the address from the destination path. Forget it and `scp` treats the whole thing as a local filename.
2. **Use absolute paths** on both sides.

> **"It is a very secure way. If you share a file in this manner, it will not be compromised."**

**Why it matters:** flagged as very useful **in CTFs** — moving files between attacker and target machines.

---

## Part 8 — ⭐ Passwordless authentication

### The motivation

> You are working **in a public place.** People come and go; **someone is sitting behind you watching.**
>
> **Shoulder-surfing** — your password becomes known simply because you typed it where someone could see.

Passwordless auth removes the password from the equation entirely.

### The five steps

#### Step 1 — Ensure `~/.ssh` exists with correct permissions

```bash
mkdir -m 700 ~/.ssh          # create with permissions in one step
# or
mkdir ~/.ssh && chmod 700 ~/.ssh
```

> ⚠ **The permission MUST be 700** — owner only, nobody else. SSH refuses to work with looser permissions.

**Note:** on most systems `.ssh` is created automatically; **on recent Kali it often is not**, so create it yourself.

#### Step 2 — Understand `known_hosts`

> **`known_hosts` holds the PUBLIC KEYS of hosts you have communicated with** — machines with which your communication has been established.

#### Step 3 — Generate the key pair

```bash
ssh-keygen
```

Prompts:
1. **Where to save** — press Enter for the default (`~/.ssh/`)
2. **Passphrase** — optional; see below

**Result:**

| File | What it is |
|---|---|
| **`id_rsa`** | your **PRIVATE** key — **never share** |
| **`id_rsa.pub`** | your **PUBLIC** key — this gets shared |

> `ssh-keygen` creates `~/.ssh` itself if it doesn't exist — the manual step above is belt-and-braces.

#### ⚠ Should you set a passphrase?

> **"IF SOME USER GETS YOUR PRIVATE KEY, then what will you do?"**

| Choice | Trade-off |
|---|---|
| **No passphrase** | Fully passwordless, but **a stolen private key = full access** |
| **With passphrase** | One extra step, but **a stolen key is useless without it** |

> *"If someone steals your private key — even if they steal it — they will not be able to use it."*

#### Step 4 — Prepare the target machine

The **destination** also needs `~/.ssh` at **700**.

> *"The USB route isn't possible, because nobody will give you entry into a server room"* — hence the need for the next step.

#### Step 5 — `ssh-copy-id` — the one-command solution ⭐

```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub username@ip_address
```

**First connection prompt:**

> *"Are you sure you want to continue connecting? yes/no"*
>
> **This appears the FIRST time you connect to a machine via SSH**, because keys are being exchanged in the background.

**Result on the server:** a file called **`authorized_keys`** appears in `~/.ssh/` — containing **exactly your public key**.

```bash
cat ~/.ssh/authorized_keys      # same content as your id_rsa.pub
```

**Now test:**

```bash
ssh username@ip_address         # no password prompt
```

### The three key files, summarised

| File | Lives on | Contains |
|---|---|---|
| `id_rsa` | **your** machine | your private key |
| `id_rsa.pub` | **your** machine | your public key |
| `authorized_keys` | **the server** | public keys allowed to log in |
| `known_hosts` | **your** machine | public keys of servers you've visited |

---

## Part 9 — ⭐ SSH Hardening

Four defensive measures, all configured in **`/etc/ssh/sshd_config`**.

> ⚠ **Restart the service after EVERY change:** `sudo systemctl restart ssh`

### 9.1 Disable root login

```
PermitRootLogin no
```

**Default is often `prohibit-password` and commented out.** Uncomment and set to `no`.

**Result when someone tries:**

```
Permission denied (publickey, password)
```

— **even with the correct root password.**

> This enforces the Day 7 principle directly: log in as a normal user, elevate only when needed.

### 9.2 Change the default port

```
Port 5152
```

**The reasoning:**

> **The default SSH port is 22.** When an attacker **scans your services**, they immediately see *"a service named SSH is running on port 22"* — and will **enumerate and attack it.**
>
> Changing the port removes you from automated scans looking at 22.

**Connecting afterwards requires `-p`:**

```bash
ssh username@ip              # fails — nothing on 22
ssh -p 5152 username@ip      # works
```

> ⚠ **Choose a port that is actually FREE on your machine.**

**Honest assessment:** this is *security through obscurity*. It stops opportunistic bots, not a determined attacker running a full port scan. Useful as one layer, not as the only one.

### 9.3 Restrict which users may connect

Add at the **end of the file**:

```
AllowUsers user1 user2
```

Only those users can log in; everyone else is refused — demonstrated live with a third user being denied.

### 9.4 The full set of access controls

| Directive | Effect |
|---|---|
| `AllowUsers user1 user2` | **Only** these users |
| `DenyUsers user1 user2` | **Block** these users, allow the rest |
| `AllowUsers *@192.168.1.39` | Allow **any user from one IP** |
| `DenyUsers *@192.168.1.39` | Block **any user from one IP** |
| `DenyUsers *@192.168.1.0/24` | Block an **entire subnet** |
| `AllowGroups groupname` | Allow an **entire group** |

### Why `AllowGroups` matters

> **If there are 10 of you — instead of making 10 separate entries, CREATE A GROUP**, add all 10 users to it, and grant SSH access to the group.

This is the **exact same argument as Day 7's group management**: manage membership, not individual permissions. Add or remove a person from the group rather than editing `sshd_config` every time.

---

## Part 10 — Complete cheat sheet

```bash
# ---- install & service ----
sudo apt install openssh-server
sudo systemctl start|stop|restart|status ssh
sudo service ssh start|stop|restart|status
# VM adapter must be in BRIDGED mode

# ---- config files ----
/etc/ssh/ssh_config      # CLIENT config
/etc/ssh/sshd_config     # SERVER (daemon) config  <- harden this

# ---- remote access ----
ssh user@ip
ssh user@hostname
ssh -p 5152 user@ip                  # non-default port
ssh user@ip hostname                 # run a command WITHOUT logging in

# ---- file transfer ----
scp /path/file user@ip:/dest/path    # note the COLON
scp -r /path/dir  user@ip:/dest/     # recursive

# ---- passwordless auth ----
mkdir -m 700 ~/.ssh                  # permissions MUST be 700
ssh-keygen                           # creates id_rsa + id_rsa.pub
ssh-copy-id -i ~/.ssh/id_rsa.pub user@ip
ssh user@ip                          # no password

# key files
~/.ssh/id_rsa            # PRIVATE — never share
~/.ssh/id_rsa.pub        # PUBLIC  — shared
~/.ssh/authorized_keys   # on the SERVER: keys allowed in
~/.ssh/known_hosts       # on the CLIENT: servers you've visited

# ---- hardening (in sshd_config, then RESTART) ----
PermitRootLogin no
Port 5152
AllowUsers  user1 user2
DenyUsers   user1 user2
AllowUsers  *@192.168.1.39
DenyUsers   *@192.168.1.0/24
AllowGroups sshusers
```

---

## Part 11 — Self-check questions

1. What does SSH stand for and what does it enable?
2. What is the practical reason for SSHing into your own VM?
3. Define encryption. What are the two types?
4. Walk through asymmetric encryption between two users. Which key decrypts?
5. Explain the lock-and-key analogy. Why is asymmetric more secure for exchange?
6. Which package must be installed? Give both ways to start the service.
7. Which VM adapter mode is required, and why?
8. Difference between `ssh_config` and `sshd_config`. What does the `d` mean?
9. Give the syntax for SSHing in, and two commands to confirm where you landed.
10. How do you run a remote command without logging in? Give a use case.
11. Write an `scp` command. What are the two details people get wrong?
12. What real-world scenario motivates passwordless authentication?
13. What permission must `~/.ssh` have? What happens otherwise?
14. What does `ssh-keygen` produce? Which file must never be shared?
15. Argue both sides of setting a passphrase on your private key.
16. What does `ssh-copy-id` do, and which file does it create on the server?
17. Distinguish `id_rsa`, `id_rsa.pub`, `authorized_keys` and `known_hosts` — which machine holds each?
18. Why does the yes/no prompt appear only on first connection?
19. Write the directive to block root login. What error does a user then see?
20. Why change the default port? What flag is then needed? Is this real security?
21. Write directives to: allow only two users; block a subnet; allow a group.
22. Why is `AllowGroups` better than listing ten users? Which earlier lecture makes the same argument?
23. What must you do after every `sshd_config` change?

---

## Part 12 — The Kali Linux course is complete

**Day 15 concludes the 15-session capsule course.** The arc across all fifteen:

| Days | Theme |
|---|---|
| **1–2** | Linux history, filesystem hierarchy, basic commands |
| **3–6** | I/O redirection, file descriptors, text processing (`sed`, `grep`, `awk`, `cut`), compression |
| **7–8** | Users, groups, `sudo`, password management |
| **9–10** | File permissions, `umask`, SUID/SGID/sticky, `find` |
| **11–14** | `vi`, packages, variables, globbing, `history`, root recovery |
| **15** | **SSH, encryption, remote access, hardening** |

### The trainer's closing note

> *"I gave 100% from my side, as much as I could give you in 15 days."*
>
> And an open invitation to criticism: *"If you feel that I did not teach you properly, or left gaps in concept delivery — for that we are really sorry."*

### The standing request

> **"Whether you are watching this after 10 days, after a month, or even after 1 YEAR — please go to the LinkedIn page for that video and comment whether you understood or not."**
>
> *"You will benefit not just yourself but other people too, because they will come to know that there is genuinely something to learn here. And if you did NOT get to learn, then please tell that too."*

### What comes next

The **OSINT course** (transcript 015 onward) is already running, and forms **stage two** of the stated roadmap: **Linux → OSINT → Penetration Testing.**
