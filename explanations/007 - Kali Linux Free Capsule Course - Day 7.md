# Explanation — Day 7: User & Group Management

**Lecture:** 007 — Kali Linux Free Capsule Course, Day 7
**Translation:** [`english/007 - Kali Linux Free Capsule Course - Day 7.md`](../english/007%20-%20Kali%20Linux%20Free%20Capsule%20Course%20-%20Day%207.md)
**Shift in topic:** After six sessions of text-processing commands, the course moves into system administration.

---

## Part 1 — Why user management exists

### 1.1 The principle of least privilege

An organization has many departments — development, accounts, finance, production. The argument made in class:

- A **developer** needs permissions **only on their project** — what would they do with access to the entire server?
- Giving the **accounts department** the tech department's file permissions is **not beneficial**.
- **Unnecessary permission is useless** — and dangerous.

> Each user gets: *"This is your file requirement, this is your area, you have these permissions, work here."*

### 1.2 Why admins don't stay logged in as root

Real system administrators log in as a **normal user**, then use tools to **temporarily become root**, then **exit** again.

**The reasoning — blast radius:**

| Scenario | If a vulnerability is exploited |
|---|---|
| Logged in as **normal user** | Only **that user** is compromised; the machine survives |
| Logged in as **root** | The **entire system** is compromised |

> **"We gave root permission to everyone… so you got your entire machine compromised."**

### 1.3 The root user

| Property | Value |
|---|---|
| Also called | super user, admin |
| **UID** | **0** — always, because root is the first user |
| Power | **Unlimited** — can remove or delete any file |
| Can | **Override** any normal user's privileges |

> If root's account is compromised, **the whole system and its control** is gone — you are no longer the owner.

### 1.4 The offensive-security angle

In **CTFs** and **pen testing**, after enumeration and scanning, gaining a shell is only step one. Because a normal user lacks the necessary permission level, **becoming root is the standard follow-up task** — only then can you actually work with the machine.

---

## Part 2 — Identifying users

| Command | Shows |
|---|---|
| `whoami` | **Which user you are currently logged in as** |
| `who` | **Who is logged in**, on which terminal, since when |
| `w` | **Which user is doing what** — plus idle time |
| `id` | **UID, GID, and all group memberships** |
| `id <user>` | The same for a specific user |

```bash
whoami           # -> root
who              # -> kali  tty7  <login time>
w                # -> kali  logged in 19:13, idle 2m30s, running ...
id               # -> uid=1000(kali) gid=1000(kali) groups=...
id manish        # same, for another user
```

### Aside: SELinux on Red Hat / CentOS

On Red Hat–family systems, `id` also shows an **SELinux context**. SELinux is an **additional security layer** above the OS that keeps the system **isolated**.

> Its rule model is absolute: **if the rule says yes, the action happens; if it says no, nothing anyone tries will work.**

This strictness is why **industry prefers Red Hat** — tight security policy, layered with firewalls, antivirus, IDS and IPS on top, which makes life difficult for attackers.

---

## Part 3 — `su` and the login shell concept

### 3.1 Every user needs an environment

> **Any user — root or otherwise — needs an *environment* in order to run.** That environment is defined in the machine and consists of **environment variables**.

### 3.2 Login shell vs non-login shell

| | **Login shell** | **Non-login shell** |
|---|---|---|
| When | A user logs in with username + password | You switch users from within an existing shell |
| Environment | **Their own** environment variables loaded | **The previous user's** environment is reused |
| Effect | You genuinely *are* that user | You are only **acting as** that user |
| Command | `su - <user>` | `su <user>` |

### 3.3 The demonstration that answers a student question

```bash
su            # no username given -> defaults to ROOT
```

After switching, the prompt still showed `/home/kali` rather than `/root`. **Why?**

> You became the **root user**, but you are still using **`kali`'s environment variables** — so the present working directory is still kali's home. You are *acting* as root, not *logged in* as root.

```bash
su - root     # or just: su -
```

Now the shift is **permanent** — root's own account, root's own environment variables. **Not acting; actually logged in.**

> **Memory rule: the dash `-` loads the target user's environment.** Without it you carry your old environment along.

### 3.4 `$SHLVL` — shell level

```bash
echo $SHLVL
```

Shows how deeply nested your shell is. Value `1` = a single shell. Open a shell inside that shell and it becomes `2`.

---

## Part 4 — The `/etc/passwd` file

Understanding this file is described as **essential** to user management.

```
manish : x : 1102 : 1102 : comment : /home/manish : /bin/bash
   1     2     3      4        5          6              7
```

| # | Field | Meaning |
|---|---|---|
| 1 | **username** | the account name |
| 2 | **password** | just `x` today |
| 3 | **UID** | user ID — unique per user; **root = 0** |
| 4 | **GID** | primary group ID |
| 5 | **comment** | descriptive tag (GECOS) |
| 6 | **home directory** | where the user's home lives |
| 7 | **shell** | which shell they get on login |

> **Why field 2 is just `x`:** the password hash used to live here, but **for security reasons** it was moved to **`/etc/shadow`**.

---

## Part 5 — Creating users

### 5.1 The quick way

```bash
useradd user1
tail -2 /etc/passwd     # verify the entry
```

Everything unspecified is filled in from system defaults.

### 5.2 The recommended way — specify explicitly

```bash
useradd -d /home/user2 -c "Finance team member" -s /bin/bash user2
```

| Flag | Sets |
|---|---|
| `-d` | home **d**irectory |
| `-c` | **c**omment |
| `-s` | **s**hell |
| `-u` | specific **U**ID (otherwise auto-assigned) |

> **Why this is best practice:** if something is misconfigured in the defaults directory, the home directory / shell / comment may not get set correctly. Specifying them from the start avoids that and **you get the benefit later**.

### 5.3 Where the defaults come from — `/etc/default/useradd`

```bash
cat /etc/default/useradd
```

| Setting | Meaning |
|---|---|
| **SHELL** | default shell for new users (e.g. `/bin/sh`) |
| **HOME** | base path for home directories (`/home`) |
| **GROUP** | default group |
| **INACTIVE** | days after password expiry before disable — **`-1` means never expire** |
| **EXPIRE** | default account expiry date — blank means none |
| **SKEL** | the **skeleton directory** to copy from |

UIDs below ~100 (or 1000) are **reserved for the system**; normal users start above that.

> `useradd` is a **binary program** that reads these defaults. If you pass modify options, it applies yours first and takes the remainder from here.

---

## Part 6 — `/etc/skel`, the skeleton directory

> **Whenever a new user account is created, the contents of `/etc/skel` are copied automatically into that user's home directory.**

This is how a **framework** is prepared for every new user.

```bash
ls -a /etc/skel
# .bash_logout  .bashrc  .profile
```

Those same three files appear in every new user's home — demonstrated by creating a user and listing their home directory.

**What it is used for in practice:**
- Default shell configuration and environment variables
- **Organizational policy messages** — the notice a user sees on login telling them what they may and may not do
- Any file every user should start with

---

## Part 7 — Modifying users: `usermod`

```bash
usermod -c "This is my demo" -s /bin/bash user2
```

Same flags as `useradd`. Verify with `tail /etc/passwd`. Use `usermod --help` for the full option list.

---

## Part 8 — Deleting users: `userdel`

```bash
userdel user1        # deletes the user, LEAVES the home directory
userdel -r user1     # deletes the user AND the home directory
```

### ⚠ 8.1 The security warning

**Before deleting any user:**

1. **Check their home directory first.** Is there anything important in it?
2. If yes — **transfer it out**.
3. If not — delete with `-r`.

### 8.2 Why `userdel` without `-r` is a real vulnerability

This is the most important security content in the session. The chain:

1. You delete a user **without `-r`**. Their **home directory survives**, possibly containing **sensitive information**.
2. The deleted user's **UID becomes free**.
3. Later you add a **new user**. The system assigns **the first free UID** — which may be **the deleted user's old UID**.
4. The orphaned files, still owned by that UID number, are now owned by the **new user**.
5. **The new user can read the old user's sensitive data.**

> **Outcome: sensitive information leakage.**

### 8.3 The attacker's version

An attacker who has obtained a normal-user shell can hunt for exactly this:

```bash
find / -nouser -o -nogroup      # files with no valid owner
```

Orphaned files with no owner reveal a freed UID — a foothold for privilege abuse.

### 8.4 The two remediations

| Option | Action |
|---|---|
| **1** | Extract the data you need, then **delete the home directory** |
| **2** | **Transfer the data** manually and **reassign ownership** to someone else |

---

## Part 9 — Group Management

### 9.1 Why groups exist — the scale argument

The scenario given:

- An organization of **1000 people**
- **50 of them** work on one project
- That project needs access to **30–40 files**

**Could you assign permissions individually?** 50 users × 35 files = 1,750 permission assignments — and the same again to revoke them.

> **Is it possible in a real scenario? Not possible.**
>
> 1. You could **never monitor** who is doing what.
> 2. It is hopelessly **time consuming** — nobody has that much time.

**The solution:**

1. Create **one group** of the 50 people.
2. Change the **group ownership of the 35 files** to that group.
3. Set the permissions **once**, on the group.

**The payoff:**

| Task | Without groups | With groups |
|---|---|---|
| Add person #51 | 35 permission changes | **Add to group** |
| Remove someone | 35 permission changes | **Remove from group** |
| Monitoring | 50 individuals | One group |

> The whole point: **you don't limit each individual's access on each file.**

### 9.2 Primary vs secondary groups

| | **Primary group** | **Secondary group** |
|---|---|---|
| Created | Automatically, **named after the user** | Manually, by you |
| Purpose | The user's own default group | Project/team collaboration |
| How many | Exactly one | **As many as you like** |
| Stored in | GID field of `/etc/passwd` | `/etc/group` member list |

### 9.3 The `/etc/group` file

```bash
tail -5 /etc/group
cat /etc/group | grep kali
```

Secondary group memberships appear here as a member list; the primary group is the GID in `/etc/passwd`.

### 9.4 Group commands

| Command | Purpose |
|---|---|
| `groups` | Which groups **am I** in |
| `groups <user>` | Which groups **that user** is in |
| `groupadd <name>` | **Create** a group |
| `groupmod -n <new> <old>` | **Rename** a group |
| `groupdel <name>` | **Delete** a group |

```bash
groupadd UNIX
tail -2 /etc/group           # verify — group exists but has no members yet
groups kali                  # kali adm dialout cdrom sudo ...
groupmod -n unix UNIX        # rename UNIX -> unix
groupdel unix
```

### 9.5 ⚠ The `-a` flag is mandatory

```bash
usermod -aG UNIX sachin2     # ADD to a secondary group, keeping existing ones
usermod -G  UNIX sachin2     # REPLACE all secondary groups with just this one
```

> **Forgetting `-a` removes the user from every other secondary group.** The new group **overrides** them all. This is one of the classic destructive Linux admin mistakes.

### 9.6 Changing the primary group — lowercase `g`

```bash
usermod -g UNIX sachin2      # change PRIMARY group
```

| Flag | Effect |
|---|---|
| `-aG` (capital G, with `a`) | **add** secondary group |
| `-G` (capital G, no `a`) | **replace** all secondary groups ⚠ |
| `-g` (lowercase g) | change **primary** group |

### 9.7 ⚠ You cannot delete a group that is someone's primary group

```bash
groupdel unix
# cannot remove the group ...
```

> **A group must not be the primary group of any user before you can delete it.** Change that user's primary group first, then delete.

---

## Part 10 — Complete cheat sheet

```bash
# Identity
whoami                  # current user
who                     # who is logged in
w                       # who is logged in and doing what
id / id <user>          # UID, GID, group memberships

# Switching
su                      # act as root, KEEP your environment
su <user>               # act as user, keep your environment
su - <user>             # FULL login as user, their environment
echo $SHLVL             # shell nesting level

# Users
useradd user1
useradd -d /home/u2 -c "comment" -s /bin/bash -u 1500 u2
usermod -c "new comment" -s /bin/bash user2
userdel user1           # leaves home directory  ⚠
userdel -r user1        # removes home directory too
tail -2 /etc/passwd     # verify

# Reference files
/etc/passwd             # user records (7 fields)
/etc/shadow             # password hashes
/etc/group              # group records
/etc/default/useradd    # defaults for new users
/etc/skel               # template copied into each new home

# Groups
groups / groups <user>
groupadd UNIX
usermod -aG UNIX user   # ADD secondary group (keep existing) ✔
usermod -G  UNIX user   # REPLACE all secondary groups       ⚠
usermod -g  UNIX user   # change PRIMARY group
groupmod -n newname oldname
groupdel UNIX           # fails if it is anyone's primary group
```

---

## Part 11 — Self-check questions

1. Why shouldn't a developer have access to the whole server?
2. Why do admins log in as a normal user and elevate temporarily?
3. What is root's UID, and why that number?
4. What happens to blast radius if a vulnerability is exploited while logged in as root vs as a normal user?
5. Difference between `whoami`, `who`, `w` and `id`.
6. What is SELinux, and why does industry prefer Red Hat?
7. Define login shell vs non-login shell.
8. After `su`, why did the prompt show `/home/kali` instead of `/root`?
9. What does the `-` in `su -` actually do?
10. Name all seven fields of `/etc/passwd`. Why is field 2 just `x`?
11. Which three `useradd` flags should you specify explicitly, and why?
12. What lives in `/etc/default/useradd`? What does `INACTIVE=-1` mean?
13. What is `/etc/skel` and when does it take effect? Name three files it typically holds.
14. Trace the full security chain from `userdel` without `-r` to sensitive information leakage.
15. What command would an attacker use to find orphaned files?
16. Compute the permission assignments needed for 50 users × 35 files without groups. Why is it unworkable?
17. Difference between a primary and a secondary group. How many of each can a user have?
18. What is the difference between `-aG`, `-G` and `-g` in `usermod`? Which one is destructive?
19. Why does `groupdel` refuse to delete a group, and how do you fix it?

---

## Part 12 — Coming up next

**Password management and privileges:** how to manage passwords, the system files involved, and a deeper look at user privileges.
