# Explanation — Day 2: Linux File System Hierarchy & Basic Commands

**Lecture:** 002 — Kali Linux Free Capsule Course, Day 2
**Translation:** [`english/002 - Kali Linux Free Capsule Course - Day 2.md`](../english/002%20-%20Kali%20Linux%20Free%20Capsule%20Course%20-%20Day%202.md)
**Builds on:** Day 1 (root partition `/`, OS-defined vs user-defined data, public vs private place)

---

## 1. Kali desktop orientation

Before the theory, the trainer walks through the Kali GUI so you know where things live:

| Item | Windows equivalent |
|---|---|
| Applications list (taskbar menu) | Start menu / all apps |
| "File System" file manager entry | This PC / My Computer |
| Default text editor | Notepad |
| Firefox | Browser |
| **Terminal** | Command Prompt / PowerShell |

Terminal productivity features shown:
- **New Tab** — run a second shell while a long task occupies the first.
- **Split (horizontal/vertical)** — two shells side by side on one screen.

---

## 2. Reading the shell prompt

A Kali prompt looks like:

```
┌──(root㉿kali)-[~]
└─#
```

| Part | Meaning |
|---|---|
| `root` / `kali` | **Username** currently logged in |
| after `㉿` | **Hostname** of the machine |
| `[~]` or `[/etc]` | **Present working directory**; `~` = that user's home directory |
| `#` | You are the **root / super user** |
| `$` | You are a **normal user** |

> Quick rule: **`#` = root, `$` = normal user.** This is the fastest way to know your privilege level at a glance.

---

## 3. `/` vs `/root` — clearing the confusion

Two different things are both casually called "root":

| Path | Name | What it is |
|---|---|---|
| `/` | **Root partition** (parent partition) | Top of the entire hierarchy. Nothing exists above it. |
| `/root` | **Root user's home directory** | The super user's *private place* — equivalent to `/home/<name>` for a normal user. |

---

## 4. Why directory choice matters

Common beginner objection: *"I can create my file in any directory and it works, so why do these rules matter?"*

Answer given: **permissions.** Linux has pre-defined, policy-driven roles for each directory — where a program downloads to, where it installs, where it executes from, where its config lives. Work with that design and everything is comfortable; work against it and you hit permission problems. Purely mechanically you *can* create a file in `/boot`, `/media` or `/mnt` — but each directory was built for a purpose and should be used for that purpose.

---

## 5. File System Hierarchy — directory by directory

| Directory | Full name | Contents / purpose |
|---|---|---|
| **`/bin`** | binaries | Executable (binary) program files for **commands**. Every command has a program file — a set of instructions compiled into 0s and 1s. |
| **`/boot`** | boot | Files needed to boot the machine, including the **GRUB boot loader** and kernel `config-*` files that define the boot sequence. |
| **`/dev`** | devices | **Device files** — the interface between hardware and software. |
| **`/etc`** | et cetera | System **configuration** and settings. |
| **`/home`** | home | Home directories of **all normal users** — each user's private place. |
| **`/lib`** | libraries | **Library files** required for applications to run (e.g. a web server's libraries). |
| **`/lost+found`** | — | Fragments recovered after a crash / unclean shutdown. **Important for digital forensics.** |
| **`/media`** | media | Auto-mount point for **removable media** (CD/DVD, USB). |
| **`/mnt`** | mount | Manual **mount point** — ISO images, pen drives, hard disks. Normally empty. |
| **`/opt`** | optional | **Third-party / optional software.** |
| **`/proc`** | process | Live, kernel-updated **process information**. Commands like `top` read from here. |
| **`/root`** | root | **Super user's home directory** (Desktop, Documents, Downloads, Music...). |
| **`/sbin`** | system binaries | Binaries for commands **only the super user can run**. |
| **`/srv`** | serve | Data served by services (FTP, NFS, proxy, web) — including cached/temporary data for faster response, *cache-like* in intent. |
| **`/sys`** | system | **Kernel and hardware** details: block devices, buses, classes, firmware, kernel modules (drivers). |
| **`/tmp`** | temporary | Scratch space writable by everyone — protected by the **sticky bit**. |
| **`/usr`** | user | Binaries, libraries and **documentation** for user programs. |
| **`/var`** | variable | Files that **change over time**: logs, caches, mail spools, web content (`/var/www`). |
| **`/run`** | run | Runtime state data. |

### 5.1 Device file types (from `ls -l`)

The first character of the permission string tells you the file type:

| Char | Type |
|---|---|
| `-` | regular file |
| `d` | directory |
| `c` | character device |
| `b` | block device |
| `s` | socket |
| `l` | symbolic link |

**Block vs character transfer:**
- **Block** — data moves in fixed-size chunks/blocks (disks).
- **Character** — data streams character by character (mic → speaker, terminals).

> Core Linux principle stated in class: **everything is a file** — hard disk, pen drive, device, socket.

### 5.2 The boot sequence (from `/boot`)

1. Power button pressed → current flows.
2. **POST** (power-on self test) — hardware components checked.
3. **BIOS**.
4. **Kernel** loads.
5. **Hardware modules / drivers** load alongside the kernel.

The scrolling black-screen text at startup is this sequence. Which step runs when is defined by the configuration files in `/boot`, and GRUB is the boot loader that drives it.

### 5.3 What "mount" means (`/mnt`, `/media`)

**Mounting** attaches a storage device into the directory tree so data can flow to/from it. Until a device is mounted, you cannot use it.

**Analogy used in class:** a room with no door or window — you cannot enter or use it. Mounting is installing the door.

### 5.4 The sticky bit (`/tmp`)

`/tmp` is world-writable, but a **sticky bit** is set on it so that **only the user who created a file can delete that file** (root excepted). Without it, any user could wipe another user's temp files.

### 5.5 Symbolic links at `/`

Several entries directly under `/` — `bin`, `sbin`, `lib`, `lib32`, `lib64` — are not real directories. They are **symbolic links (symlinks)** pointing to their real counterparts inside `/usr`. Conceptually similar to a Windows shortcut. `/media`, `/home`, `/boot` etc. are genuine directories.

### 5.6 Columns of `ls -l`

```
-rw-r--r--  1  root  root  4096  Sep 28 15:58  file.txt
   │        │   │     │      │        │            │
permissions │  user group  size  timestamp      name
         link count
```

---

## 6. Commands taught

### 6.1 Navigation

| Command | Meaning |
|---|---|
| `cd <dir>` | **Change directory.** Only directories can be given, not files. |
| `cd /` | Go to the root partition |
| `cd ~` | Go to your home directory |
| `cd -` | Go back to the **previous** directory you were in |
| `cd ..` | Go up one level (parent) |
| `pwd` | **Print/present working directory** — shows the full path |

> On older UNIX/Red Hat prompts the prompt shows only the current directory name, not the full path — `pwd` is how you get the full path reliably.

### 6.2 Absolute vs relative path

| Type | Starts with | Works from | Example |
|---|---|---|---|
| **Absolute** | `/` | **Anywhere** | `cd /root/Downloads` |
| **Relative** | a name | Only relative to your **current** directory | `cd Downloads` |

Demonstrated failure: sitting at `/`, `cd Downloads` fails; `cd /root/Downloads` works. **Advice: prefer absolute paths**, especially with destructive commands.

### 6.3 `.` and `..`

| Entry | Stores the address of |
|---|---|
| `.` (single dot) | the **current** directory |
| `..` (double dot) | the **parent** directory |

Both are hidden entries — visible only with `ls -a`.

### 6.4 `ls` — listing

| Form | Effect |
|---|---|
| `ls` | List the present working directory |
| `ls /etc` | List a specific directory |
| `ls -a` | Include **hidden** files (and `.` / `..`) |
| `ls -l` | **Long format** — metadata: permissions, links, user, group, size, timestamp, name |
| `ls -al` | Both combined |
| `ls -d` | Directories only |
| `ls -h` | Human-readable sizes |

### 6.5 Getting help

| Command | Use |
|---|---|
| `<command> --help` | Quick summary: syntax, available flags |
| `man <command>` | The full **manual page** — "a whole book" with detailed information |

> This is the real skill: you don't need to memorise flags, you need to know the command name and how to read its help.

### 6.6 Tab auto-completion

Type a prefix and press **Tab**:
- Unique match → the name is **auto-completed**.
- Multiple matches → all candidates are listed (`Desktop`, `Documents`, `Downloads`), so you type one more character and press Tab again.

Remember: **Linux is case-sensitive** — `doc` ≠ `Doc`.

### 6.7 Creating directories

```bash
mkdir capsule-course              # in current directory
mkdir /tmp/unix                   # anywhere, via absolute path
mkdir -p /tmp/unix1/tom           # -p creates the whole parent→child chain
```

`-p` maintains the **parent–child relationship**: it creates each missing level instead of failing.

### 6.8 Removing directories and files

| Command | Behaviour |
|---|---|
| `rmdir <dir>` | Deletes a directory **only if it is empty**; otherwise fails |
| `rm <file>` | Delete a file |
| `rm -r <dir>` | **Recursive** — delete a directory and everything in it |
| `rm -f` | **Force**, no prompts |
| `rm -i` | **Interactive** — prompt before each deletion |
| `rm -d` | Remove an empty directory |

#### ⚠ The `rm -rf` warning

The trainer's strongest safety advice of the session:

> **`rm -rf` is a very powerful and dangerous command. If you are not comfortable with it, do not use it.**

**Why it destroys systems:** the shell splits your line on **spaces** into arguments. A stray space turns one path into two:

```bash
rm -rf /tmp/unix      # deletes /tmp/unix
rm -rf / tmp/unix     # ← accidental space: first argument is  /
```

The first argument is now `/` — the entire root partition — and `rm` will happily start deleting the whole file system. Mitigations: use absolute paths deliberately, use `-i` while learning, and re-read the line before pressing Enter.

### 6.9 `touch` — and the three timestamps

`touch file` does create an empty file, and can create several at once:

```bash
touch linux1 linux2 linux3
```

**But that is not its main purpose.** `touch`'s primary job is to **update timestamps**. Every file carries three:

| Timestamp | Meaning | Changed by |
|---|---|---|
| **Access time (atime)** | when the file was last read/opened | `touch -a` |
| **Modify time (mtime)** | when the file's **content** was last edited | `touch -m` |
| **Change time (ctime)** | when the file's **metadata** last changed (permissions, location, size, name) | **cannot be set directly** — updates automatically whenever atime or mtime changes |

Inspect them with:

```bash
stat file1        # shows Access, Modify, Change and Birth times
```

Demonstrated:
- `touch file1` → all timestamps jump to now.
- `touch -a file2` → only access time (and consequently change time) updates; modify time untouched.
- `touch -m file3` → modify time (and change time) update; access time untouched.

### 6.10 `cat` — create, read, concatenate

```bash
cat > newfile.txt      # create and type content; Ctrl+D to finish
cat newfile.txt        # read the content
cat file1 file2 > merged.txt   # concatenate two files into one
```

`>` is the **redirection symbol** — it sends output into a file instead of the screen. The name `cat` comes from **concatenate**.

### 6.11 `cp` — copy

```bash
cp file3.txt /tmp/                 # copy a file
cp -r /source/dir /destination/    # -r = recursive, copies a directory and its contents
```

Syntax is always `cp <source> <destination>`. Advice repeated: give absolute paths.

### 6.12 `mv` — move **and** rename

```bash
mv file3.txt newfile3.txt       # rename (same directory)
mv newfile.txt /tmp/            # move to another directory
mv newfile.txt /tmp/other.txt   # move and rename in one step
```

One command does both jobs — renaming is just "moving" to a new name in the same place.

### 6.13 `file` — identify file type

```bash
file image.jpg     # -> JPEG image data
file /bin/ls       # -> ELF 64-bit executable
```

Tells you the *actual* type regardless of the extension. Very useful in security work, where extensions lie.

---

## 7. Command quick-reference

```bash
# Navigation
pwd                      # where am I
cd /path                 # absolute
cd dir                   # relative
cd ~ / cd / / cd - / cd ..

# Listing
ls                       # current dir
ls -l                    # long / metadata
ls -a                    # hidden included
ls -al /etc              # both, on a given path

# Directories
mkdir name
mkdir -p a/b/c
rmdir name               # empty only
rm -r name               # recursive

# Files
touch f1 f2 f3
stat f1                  # three timestamps
touch -a f1 / touch -m f1
cat > f1                 # create+write, Ctrl+D
cat f1                   # read
cat f1 f2 > f3           # concatenate
cp src dst / cp -r src dst
mv src dst               # move or rename
rm -i f1                 # safe delete
file f1                  # type

# Help
ls --help
man ls
```

---

## 8. Self-check questions

1. What do `#` and `$` in the prompt tell you?
2. Differentiate `/` and `/root`.
3. Which directory holds: command binaries, super-user-only binaries, configuration, logs, device files, kernel/hardware info, third-party software, recovered crash fragments?
4. What are block and character devices? Which letters identify them in `ls -l`?
5. Explain the boot sequence and the role of GRUB.
6. What does mounting mean, and why is `/mnt` usually empty?
7. What is the sticky bit and which directory demonstrates it?
8. Why are `/bin` and `/lib` symbolic links on a modern Kali install?
9. Absolute vs relative path — give an example of each and say when relative fails.
10. What do `.` and `..` store, and why don't you normally see them?
11. Name the three timestamps on a Linux file. Which one can `touch` not set directly, and why?
12. Why is `rm -rf` dangerous? Reconstruct the stray-space failure.
13. What does `-p` do for `mkdir`, and `-r` for `cp` and `rm`?
14. Two ways to get documentation for an unfamiliar command.
15. Why can't `rmdir` remove `/tmp/unix1` when it contains `tom`?

---

## 9. Coming up next

Continuation of command-line work, building toward file permissions and users — the areas that make the "public place vs private place" model from Day 1 fully concrete.
