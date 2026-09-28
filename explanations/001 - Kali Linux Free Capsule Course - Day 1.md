# Explanation — Day 1: History of Linux & Data Storage Planning

**Lecture:** 001 — Kali Linux Free Capsule Course, Day 1
**Translation:** [`english/001 - Kali Linux Free Capsule Course - Day 1.md`](../english/001%20-%20Kali%20Linux%20Free%20Capsule%20Course%20-%20Day%201.md)
**Prerequisite mentioned in class:** watch the separate "Installation of Kali Linux" video first.

---

## 1. Why these two topics on Day 1?

The trainer opens with a justification that is worth taking seriously:

- **History** gives you the *why*. Linux design decisions (multi-user, permissions, open source, CLI-first) only make sense once you know what problem the original authors were solving.
- **Data storage planning** gives you the *where*. The single most common beginner frustration in Linux — "I created a file and it won't run / permission denied" — is not a Linux bug. It is the user creating files in a location whose permissions were never meant for them.

> Key takeaway: in Linux, *where* a file lives determines what you can do with it. Location = permission policy.

---

## 2. History of UNIX

| Year | Event |
|---|---|
| 1964 | Bell Laboratories, New Jersey, starts a project to build a **multi-user** operating system (multiple users on one machine). |
| 1969 | Bell Labs **withdraws** the project. |
| 1969+ | Two members, **Dennis Ritchie** and **Ken Thompson**, are unsatisfied and restart the work themselves. |
| — | They produce an OS originally named **UNICS** — *UNIplexed Information and Computing Service* — which colloquially became **UNIX**. It was free and **open source**. |
| 1975 | **UNIX Version 6** is released and becomes very popular. |
| ~1975 onward | Companies take the source, modify it, and ship **commercial "flavours" of UNIX**. |

**Flavours of UNIX named in class:** IBM AIX, Sun Solaris (Sun Microsystems), Mac OS (Apple), HP-UX.

*Note on accuracy:* the lecture presents the timeline in a simplified, exam-friendly form. The 1964 project referred to is **Multics** (MIT + Bell Labs + GE); Bell Labs pulled out in 1969, and UNIX grew out of that withdrawal. The spelling "UNICS" as a pun on "Multics" is the standard story.

---

## 3. History of Linux

- **1991** — **Linus Torvalds**, a university student, needed an operating system for a project.
- Existing UNIX was ageing, and the commercial versions were **very expensive** (thousands of dollars, which was a huge amount then).
- His reasoning: if every company can build its own UNIX-like OS, why can't I?
- **The important distinction the trainer stresses:** the commercial UNIX vendors *modified* existing UNIX source code. Torvalds **wrote the Linux kernel source from scratch**. He used UNIX only to *understand* behaviour, not as a code base.
- His biggest study reference was **MINIX**, a teaching operating system written by **Professor Andrew Tanenbaum** for his students. Linux was built on the *conceptual* base of MINIX.
- The name **Linux** is derived from **Linus** + UNIX.

> So the correct framing is: Linux is **UNIX-like** (same design philosophy and interfaces), not **UNIX-derived** (it does not contain UNIX code).

---

## 4. GNU and the Free Software Movement

- Roughly 1991–1995 a **Free Software Movement** was running, because most software of the era was paid — a blocker for developers and companies alike.
- The **GNU project** released a large body of software freely.
- **Linux by itself is only a kernel.** A usable operating system = **GNU tools + Linux kernel**. That is why the full name is often written **GNU/Linux**.

> Common misconception corrected here: "Linux" in everyday speech means a whole OS, but technically it names only the kernel.

---

## 5. Flavours (distributions) of Linux

| Base | Distributions |
|---|---|
| **Fedora / Red Hat based** | RHEL (Red Hat Enterprise Linux), CentOS |
| **Debian based** | **Kali Linux** (used in this course), Parrot OS, Ubuntu |
| **Others** | Arch Linux, Linux Mint |

Kali and Parrot are the two most commonly heard security distributions; Kali is the one used throughout this course.

---

## 6. What is an operating system?

**Definition given:** an OS is an **interface between the user and the hardware**.

Without an OS, doing even a cut-copy-paste or moving a mouse pointer would require writing many lines of low-level code. The OS abstracts that away.

**Two ways to access an OS:**

| Mode | Meaning | Example |
|---|---|---|
| **CLI** | Command Line Interface | `cmd` on Windows, the Linux terminal |
| **GUI** | Graphical User Interface | Windows 10/11 desktop, Kali's desktop |

Linux can be used graphically, but the course deliberately uses the **CLI**, because it is far faster and is how real administration and pentesting work is done.

---

## 7. Features of Linux (and why companies use it)

1. **Open source** — the source code is *available*. (Careful: "open source" means source is available; it does not automatically mean free of cost.) Microsoft does not share the Windows source; Linux does, so organisations can review and modify it.
2. **Cost / licensing** — Windows requires a paid licence. Pirated Windows is untenable in a company, because Microsoft tracks genuine vs pirated activations and can act against the organisation.
3. **Secure** — Linux suffers far fewer malware hits than Windows. The reason given is **OS hardening** plus the permission model: a service runs confined to its own domain with only the files it needs, and without root permission an intruding process cannot take over the whole machine. On Windows, once an attacker evades the antivirus and lands an executable, full machine control is much more achievable.
4. **Easy to update.**
5. **Lightweight** — small OS footprint and low RAM usage. Kali performs acceptably on ~1 GB RAM, while Windows is sluggish even at 4 GB and really wants 8 GB.
6. Also noted: **Android is Linux-based**, so Linux is already the most widely deployed kernel.

### Terminology map

| Concept | Windows | Linux |
|---|---|---|
| Most privileged account | Administrator | **root** (super user) |
| Installable program bundle | Software | **Package** |
| Storage layout | C:, D:, E: drives | Single tree under **`/`** |

---

## 8. Data storage planning — the core of the lecture

### 8.1 Two categories of data

| Category | Also called | What it is |
|---|---|---|
| **OS-defined data** | Default data | Files/folders created by the OS itself |
| **User-defined data** | Customized data | Anything the user creates afterwards |

**OS-defined data is created in two ways:**
1. **During installation of the OS** — the default directory tree and programs.
2. **After installation, when you install any software/package** — its program and support files are placed into system locations automatically.

**User-defined data** is everything created *after* installation by a user: files, directories, documents, movies, etc.

### 8.2 Windows analogy

- Windows: `C:\` holds OS-defined data; `D:\` / `E:\` typically hold your personal (user-defined) data.
- Linux: **the same idea exists, but there are no drive letters at all.**

### 8.3 The root partition `/`

Everything in Linux lives under a single parent node:

```
/          <-- forward slash
```

Names used for it in class: **root partition**, parent partition, parent folder. The trainer advises sticking to **"root partition"** (or parent partition) to avoid confusion later in the course.

Both OS-defined and user-defined data are created *underneath* `/`. There is no C/D/E concept.

### 8.4 The default directories

- On installation, roughly **16–19 sub-directories** are created directly under `/`. The exact number varies by distribution — it is not fixed.
- **Each has a predefined role**, already decided by Linux: which directory holds configuration files, which holds temporary files, which holds process files, which holds library files, which holds log files.
- The whole operating system depends on these directories, and you must work within the permissions already defined on them.
- Directories *you* create later are extra — they do not become part of that default set.

### 8.5 Where do users actually work?

Of those ~19 default directories:

- **~17 are operated by the operating system.**
- **2 are for humans:**
  - `/root` — the **home directory of the root / super user**.
  - `/home` — contains the home directories of **all normal users** (however many exist: 8, 10, 15...).

**Isolation rule:** one user cannot go into another user's home directory and inspect their data. Analogy used: you cannot walk into your neighbour's house and peer at what they are doing.

---

## 9. Public place vs Private place

This is the mental model the whole lecture builds toward.

| Term | Which paths | What you may do |
|---|---|---|
| **Private place** | Your own home directory (`/root` for root, `/home/<you>` for a normal user) | **Everything** by default — create, delete, execute files and directories. No restrictions. |
| **Public place** | *Everything else* under `/` | Only what the **already-defined permissions** allow. You cannot tamper with those permissions. |

Stated as a rule:

> **Every user has the default right of data creation in their home directory.**
> By default, the root user can create files and directories in *any* place.

### The society/flat analogy

You live in a society of 50 flats. Your flat is your **private place** — dance, play music, do what you like; you are the owner. Walking into a neighbour's flat and doing the same is **trespassing**. You may pass through public areas, but you act by the owner's rules there, not yours.

### Security advice (important)

- Linux admins in real organisations are usually **not given root access**; they work as normal users.
- Many learners get into the bad habit of running everything as root on their own machine. **This is a bad practice** — if an attacker compromises your session, they inherit root directly.
- **Do not become root unless you need to. Use `sudo`** (covered later in the course).

---

## 10. Linux architecture (from the machine demo)

Layer stack, bottom to top:

```
Users
  ↑ ↓
Shell        (the terminal you type into)
  ↑ ↓
Kernel       (this is "Linux")
  ↑ ↓
Hardware
```

Flow of a command: you type it in the **terminal/shell** → the shell hands it to the **kernel** → the kernel drives the **hardware** → the result returns kernel → shell → your screen.

### Kali Linux overview shown

- Kali is a Debian-based distribution, the most popular OS for **pentesters and security professionals**.
- It ships with **600+ packages pre-installed**, grouped by category in the applications menu: Information Gathering, Vulnerability Analysis, Web Application Analysis, Database Assessment, Password Attacks, and more.
- The GUI menu works, but the course will use the terminal.

### Live demo performed

Changing into `/` and listing it showed ~17–18 directories. Two of them were pointed out:

- `/root` → root's private place
- `/home` → all normal users' private places

Every other entry visible at `/` is a **public place** with pre-defined permissions.

---

## 11. Checklist of what you should be able to answer after Day 1

1. Who created UNIX, where, and why was the original project withdrawn?
2. What does UNIX stand for, and how did "UNICS" become "UNIX"?
3. Name four commercial flavours of UNIX.
4. Why is it wrong to say Linux was *derived* from UNIX? What role did MINIX and Andrew Tanenbaum play?
5. What is GNU, and why is the OS properly called GNU/Linux?
6. Classify: RHEL, CentOS, Kali, Parrot, Ubuntu, Arch, Mint — Fedora-based or Debian-based?
7. Define an operating system. Difference between CLI and GUI.
8. List five features of Linux and explain *why* Linux is considered more secure than Windows.
9. Windows → Linux terminology: Administrator, software, C: drive.
10. Difference between OS-defined and user-defined data, and the two ways OS-defined data is created.
11. What is `/`? Why are there no drive letters in Linux?
12. How many default directories exist under `/`, how many are OS-operated, and what are the remaining two for?
13. Define private place and public place, and state the default rights in each.
14. Why should you avoid working as root, and what should you use instead?
15. Draw the Hardware → Kernel → Shell → User architecture and trace a command through it.

---

## 12. Coming up next

**File System Hierarchy** — the meaning and purpose of every directory under `/`. That session turns the "public place" abstraction from this lecture into concrete knowledge of exactly which directory to use for which task.
