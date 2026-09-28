# Explanation — Day 8: `sudo`, sudoers & Password Management

**Lecture:** 008 — Kali Linux Free Capsule Course, Day 8
**Translation:** [`english/008 - Kali Linux Free Capsule Course - Day 8.md`](../english/008%20-%20Kali%20Linux%20Free%20Capsule%20Course%20-%20Day%208.md)
**Builds on:** Day 7 (users, groups, `su`, `/etc/passwd`)

---

## Part 1 — The problem `sudo` solves

### 1.1 The permission wall

A normal user attempting an admin task:

```bash
useradd sachin
# not permitted
```

> **A normal user does not have permission to do the tasks that root/admin can.**

### 1.2 How real organizations handle the root password

| Practice | Detail |
|---|---|
| Access scope | **Only limited people** have root/super user access |
| Storage | The root password lives in a **digital vault tool** |
| Rotation | **Continuously changed** — every 15, 20 or 30 days |
| Retrieval | You must **give a reason and raise a request** |
| Sharing | **Due to security reasons, the root password is never shared** |

**Consequence:** you cannot use `su` to become root, because `su` requires **root's** password — which you don't have and won't get.

### 1.3 The `sudo` solution

> **The key benefit: you don't need root's password at all, and you can still become root.**

**The crucial distinction:**

| Command | Password it asks for |
|---|---|
| `su` | **the target user's** (i.e. root's) password |
| `sudo` | **your own** password — the user running the command |

The condition: **your entry must exist in the sudoers file.** A user granted this is called a **sudo user**.

Additionally, **`sudo` usage is logged** — an audit trail that `su` does not give you.

### 1.4 Why it matters offensively

In a real attack chain:

1. Enumeration → you land in a **normal user account**.
2. **The very first thing you check:** what can I do here — *is there sudo permission?*
3. This is the core of **privilege escalation** on Linux.

> Conversely, **for security reasons `su`/`sudo` are often disabled** for all users except root and designated admins.

---

## Part 2 — The sudoers file

**Location:** `/etc/sudoers`

### 2.1 Entry format

```
user    host = (runas_user)   commands
root    ALL  = (ALL:ALL)      ALL
%group  ALL  = (root)         /usr/bin/cat /etc/shadow
```

| Position | Meaning |
|---|---|
| **1. user** | the username, or **`%groupname`** for a group |
| **2. host** | hostname or **IP address** the rule applies from |
| **3. (runas)** | which user they may act as — usually `root` |
| **4. commands** | `ALL`, or **specific commands with full paths** |

> **Two ways to grant:** by **username** directly, or by **`%group`** — the percent sign denotes a group.

### 2.2 Worked example

```
defronix ALL=(root) /usr/bin/cat /etc/shadow
```

Grants the `defronix` user the right to run **only** `cat` on **only** `/etc/shadow`, as root.

**Before the entry:**
```bash
cat /etc/shadow
# Permission denied
```

**After the entry:**
```bash
sudo cat /etc/shadow      # works
```

> **Commands must be given by full path** (`/usr/bin/cat`, not `cat`).

### 2.3 Auditing what a user may do

```bash
sudo -l
```

Lists every sudo permission defined for that user — the first thing to run on a new account, defensively or offensively.

### 2.4 Editing the file safely

| Method | Note |
|---|---|
| `nano /etc/sudoers` | Opens read-only by default |
| **`visudo`** | **The proper tool** — opens in `vi` (or the system editor) and **validates syntax before saving** |

On Fedora-based systems `visudo` opens the vi editor.

### 2.5 `NOPASSWD`

```
defronix ALL=(root) NOPASSWD: /usr/sbin/useradd, /usr/bin/passwd
```

Runs the listed commands **without prompting for a password**. Omit `NOPASSWD` and the user's own password is required.

> **Aside explained in class:** after you enter a sudo password it is **cached in memory for a few seconds**, so an immediately following `sudo` may not re-prompt.

### 2.6 ⚠ Never grant `ALL`

```
someuser ALL=(ALL:ALL) ALL      # ← effectively makes them root
```

> **"Then tell me one thing: what will be the difference between root and a normal user?"**
>
> **In the real industry this does not happen.** No normal user is given blanket permissions.

### 2.7 The shortcut nobody mentions

**Adding a user to the `sudo` group grants root-level permissions** without editing sudoers at all:

```bash
usermod -aG sudo username
```

This is exactly why auditing group membership matters during **OS hardening** — the sudoers file is where you define *who has how much access beyond root*, and which commands are and aren't allowed.

---

## Part 3 — Practice task set in class

> **Scenario:** three or four people in your environment need admin access for specific binaries. Don't write three separate sudoers entries.
>
> **Steps:**
> 1. **Create a group.**
> 2. Add the three users to it as a **secondary group** (`usermod -aG`).
> 3. Add **one sudoers entry** using `%groupname`, granting only `useradd` and `passwd`.
>
> **Verification:**
> - Confirm the three users **can** run `useradd` and change a password.
> - Confirm they **cannot** run `fdisk` (a command a normal user cannot run).
>
> Post a screenshot of your result.

---

## Part 4 — `passwd`

```bash
passwd              # change YOUR OWN password
passwd username     # change ANOTHER user's password (needs privilege)
```

### If you forget your password

You cannot reset it yourself — **changing a password requires root**, which you don't have. You must **raise a request with your admin authority**, with a reason.

---

## Part 5 — `/etc/shadow`

### 5.1 The question that motivates it

> *How does the system know your password in the first place?*

It must be stored somewhere, so that at login the entered value can be **matched** against it.

**Answer:** `/etc/shadow` — **only root can access it.** No normal user has any permission on this file.

```bash
cat /etc/shadow      # root only
```

### 5.2 The eight fields

```
defronix : $6$salt$hash : 19536 : 0 : 99999 : 7 : 2 :
    1            2          3     4    5      6   7  8
```

| # | Field | Meaning |
|---|---|---|
| 1 | **username** | account name |
| 2 | **encrypted password** | contains **hashing algorithm ID + salt + hash** |
| 3 | **last change** | **days since 1 January 1970** |
| 4 | **minimum days** | how soon it may be changed again |
| 5 | **maximum days** | after how many days it **must** be changed |
| 6 | **warning days** | days before expiry that warnings begin |
| 7 | **inactive days** | grace period **after** expiry |
| 8 | **expiry date** | absolute account expiry |

### 5.3 Field 2 decoded

The `$` sections carry two pieces of information: **which hashing algorithm** and **which salt**. Modern systems use **SHA-512**.

```
$6$      →  algorithm id (6 = SHA-512)
$salt$   →  the random salt
hash     →  the resulting hash
```

---

## Part 6 — How password ageing actually behaves

A worked scenario with `min=0, max=10, warn=2, inactive=2`:

| Day | What happens |
|---|---|
| 0 | Password changed |
| 0–10 | Normal use. `min=0` means **you may change it at any moment** |
| **Day 8** | **Warning begins** — "your password is going to expire, please change it" |
| **Day 10** | **Password expires** |
| **Days 10–12** | **Inactive grace window** — you can still log in with the old password, but you are **forced to set a new one immediately at login** |
| **After day 12** | **Account is dead.** You can never log in again |

### Why the inactive window exists

The trainer's reasoning is worth keeping:

> *"I'll change it tomorrow" → no time that day → "I'll do it in the evening" → something came up, you shut the machine down and forgot entirely.*
>
> **A mistake can happen to anyone.** The inactive period is the forgiveness buffer.

### Recovering an expired account

Once the inactive window is crossed, you have **two options**, both requiring the system administrator:

1. The admin **manually resets** your password.
2. The admin **adjusts the last-change date** so you fall back inside the maximum window and can change it yourself.

| Field | Effect of `0` | Effect of a number |
|---|---|---|
| minimum | change **any time** | must wait that many days |
| maximum | — | forced change after N days |
| warning | no warning | warn N days before expiry |
| inactive | no grace | N days of forced-change grace |

---

## Part 7 — `/etc/login.defs`

> **The defaults for every new user are taken from here.**

```bash
cat /etc/login.defs
```

Contains:

| Setting | Purpose |
|---|---|
| `UID_MIN` / `UID_MAX` | normal user ID range — **UID_MIN is 1000** |
| `SYS_UID_MIN` / `MAX` | system and service account ranges |
| `GID_MIN` / `GID_MAX` | group ID range |
| `ENCRYPT_METHOD` | hashing algorithm — **SHA-512** |
| `SHA_CRYPT_MAX_ROUNDS` | hashing rounds |
| `PASS_MAX_DAYS` etc. | default password ageing |

**To change the policy for all future users** — e.g. every new password must change after 10 days with a set warning period — **edit `login.defs`**. All users created afterwards inherit those settings.

> **It is a very important file** for organization-wide password policy.

---

## Part 8 — `chage` — the readable way

`/etc/shadow` stores dates as **days since 1970**, which nobody can read at a glance.

```bash
chage -l kali
```

Outputs it in plain language: *Last password change: January 27, 2023. Password expires: never. Password inactive: never. Minimum number of days between password change: 0…*

> **No calculating days required.**

### Changing the ageing parameters

| Flag | Sets |
|---|---|
| `-m` (small) | **minimum** days |
| `-M` (capital) | **maximum** days |
| `-W` (capital) | **warning** days |
| `-I` (capital i) | **inactive** days |
| `-l` | **list** current settings |
| `-d 0` | force change at next login |

```bash
chage -m 0 -M 15 -W 7 -I 2 kali
```

Reads as: change any time, **must** change after 15 days, warn from day 8, 2 days grace afterwards.

### `chage -d 0` — force a reset

```bash
chage -d 0 kali
```

> **It forces the user to update the password on next login.**

Log out, log back in, and the system demands a new password immediately. This is the standard tool for handing out a temporary password that the user must replace.

---

## Part 9 — Where a user's data lives (three files)

| File | Holds |
|---|---|
| **`/etc/passwd`** | the account record (7 fields) |
| **`/etc/shadow`** | the password hash and its ageing (8 fields) |
| **`/etc/group`** | group memberships |

---

## Part 10 — Disabling / locking an account

Four methods, in increasing order of safety:

### Method 1 — edit `/etc/shadow` directly ⚠

Insert `!!` before the password hash using `vi`.

> **Not a good approach.** Tampering with the shadow file risks a malformed entry that will **break your machine**. Use the tools instead.

### Method 2 — `usermod` (recommended)

```bash
usermod -L defronix     # LOCK / disable
usermod -U defronix     # UNLOCK / enable
```

Locking prefixes the hash with a **single `!`**.

### Method 3 — `passwd`

```bash
passwd -l defronix      # lock
passwd -u defronix      # unlock
```

### Method 4 — remove the shell

Edit field 7 of `/etc/passwd` and set the shell to something like `/sbin/nologin`.

> **If they don't get a shell at all, the user simply cannot work.**

### What the user experiences

```bash
su - defronix
# password entered correctly
# Authentication failure
```

The password is right — the **account** is locked.

| Marker in shadow | Meaning |
|---|---|
| `!!` | disabled (manual edit / never set) |
| `!` prefix | locked via `usermod -L` |
| normal hash | active |

---

## Part 11 — Doubt session: forgetting the root password

| OS | Reset method |
|---|---|
| **Linux** | At **boot time**, via the **advanced selection** menu — a few seconds' window where root's password can be changed. Or boot a **Live ISO image**. |
| **Windows** | Boot a **Live CD**. |

### ⚠ The security implication

**Anyone with physical access can reset your root password this way.**

That is precisely why real environments layer protections:

- A **password on the bootloader** itself
- Additional protections before you can reach the boot menu
- Physical access control

> **Otherwise it becomes insecure** — someone reaches the machine physically, boots a live image, and resets the admin password.

If you forget root's password on a properly protected machine **before** login, **there is no solution.**

---

## Part 12 — Complete cheat sheet

```bash
# sudo
sudo <command>                  # run as root using YOUR password
sudo -l                         # list your sudo permissions
visudo                          # safely edit /etc/sudoers

# sudoers entry format
# user   host = (runas)  commands
root     ALL  = (ALL:ALL) ALL
defronix ALL  = (root)    /usr/bin/cat /etc/shadow
%devops  ALL  = (root)    NOPASSWD: /usr/sbin/useradd, /usr/bin/passwd

# passwords
passwd                          # change own
passwd username                 # change another's
passwd -l user / -u user        # lock / unlock

# ageing
chage -l user                   # readable listing
chage -m 0 -M 15 -W 7 -I 2 user # min / max / warn / inactive
chage -d 0 user                 # force change at next login

# locking accounts
usermod -L user                 # lock
usermod -U user                 # unlock

# key files
/etc/sudoers                    # who may run what as root
/etc/shadow                     # password hashes + ageing (root only)
/etc/passwd                     # account records
/etc/group                      # group records
/etc/login.defs                 # defaults for new users
```

---

## Part 13 — Self-check questions

1. Why is the root password never shared, and how do organizations store it?
2. What is the key difference in **whose password** `su` and `sudo` ask for?
3. What is the main benefit of `sudo` over `su`?
4. Where is the sudoers file, and what are the four positions of an entry?
5. What does `%` mean at the start of a sudoers entry?
6. Why must commands be written with their full path?
7. What does `sudo -l` do, and why is it the first thing an attacker runs?
8. Why should you use `visudo` rather than `nano`?
9. What does `NOPASSWD` do? Why might `sudo` not re-prompt within a few seconds?
10. What is wrong with granting `ALL=(ALL:ALL) ALL` to a normal user?
11. What is the shortcut that grants root powers without touching sudoers?
12. How does the system verify your password at login? Which file, and who can read it?
13. List all eight fields of `/etc/shadow`.
14. What two pieces of information are encoded in field 2 besides the hash? Which algorithm is standard?
15. With `min=0, max=10, warn=2, inactive=2`, what happens on day 8? Day 10? Day 11? Day 13?
16. Why does the inactive window exist?
17. Two ways an admin can recover an account whose inactive window has passed.
18. What is `/etc/login.defs` for? What is the default `UID_MIN`?
19. Why is `chage -l` preferable to reading `/etc/shadow` directly?
20. Write the `chage` command for: change any time, must change after 15 days, 7 days warning, 2 days grace.
21. What does `chage -d 0 user` do?
22. Name four ways to disable an account. Which is unsafe and why?
23. Difference between `!!` and a single `!` in the shadow file.
24. How can root's password be reset with physical access, and what protections prevent it?

---

## Part 14 — Coming up next

**File Security** — file permissions and how they are managed.
