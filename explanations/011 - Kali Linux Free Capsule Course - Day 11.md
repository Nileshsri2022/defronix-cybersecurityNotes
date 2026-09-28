# Explanation — Day 11: The `vi` / `vim` Editor

**Lecture:** 011 — Kali Linux Free Capsule Course, Day 11
**Translation:** [`english/011 - Kali Linux Free Capsule Course - Day 11.md`](../english/011%20-%20Kali%20Linux%20Free%20Capsule%20Course%20-%20Day%2011.md)

---

## Part 1 — Why learn `vi` at all

> **By default, `vi` exists on every Linux machine.** Nothing else is guaranteed to.

The security-specific argument made in class:

> *You are attacking a machine. You get a shell. **Apart from the `vi` editor, there is no other tool available** — and you don't know how to use it. **Then you face a challenge.** If you do know it, you are in quite a good position.*

This is the honest reason a security learner needs `vi`: on a stripped-down or compromised host, `nano` may not exist, but `vi` almost certainly will.

---

## Part 2 — The four modes

Everything in `vi` depends on knowing **which mode you are in**.

| Mode | Entered by | Purpose |
|---|---|---|
| **Command mode** | **the default on open**; `Esc` returns here | navigation, delete, cut/copy/paste, replace |
| **Insert mode** | `i` `a` `I` `A` `o` `O` | actually typing text |
| **Ex / last-line mode** | `:` | save, quit, search, read files/commands |
| **Visual mode** | `v` `V` `Ctrl+v` | selecting and highlighting text |

> **The single most important fact: `vi` opens in COMMAND MODE, not insert mode.** Beginners type and nothing appears — because keystrokes are being read as commands.

**`Esc` always returns you to command mode.** When lost, press `Esc`.

---

## Part 3 — Entering insert mode

```bash
vim file.txt        # opens in COMMAND mode
```

Press `i` — the bottom-left shows `-- INSERT --`. Now you can type.

### The six ways in

| Key | Name | Where you end up |
|---|---|---|
| `i` | insert | **before** the cursor |
| `a` | append | **after** the cursor |
| `I` (Shift+i) | Insert at start | **beginning of the line** |
| `A` (Shift+a) | Append at end | **end of the line** |
| `o` | open below | a **new empty line below** |
| `O` (Shift+o) | open above | a **new empty line above** |

> **Why `A` and `I` matter:** they combine *movement* and *mode switch* in one keystroke. Rather than arrowing to the end of a long line, press `A`. This is the whole philosophy of `vi` — compose intent instead of repeating keystrokes.

---

## Part 4 — Saving and quitting

All of these are typed from **command mode**, beginning with `:` (Shift + colon). The command appears in the bottom-left corner.

| Command | Action |
|---|---|
| `:w` | **write** (save), stay in the file |
| `:q` | **quit** |
| `:wq` | **write and quit** |
| `:q!` | **quit without saving** — force, discard changes |
| `:wq!` | force write and quit |
| `:w newname.txt` | **Save As** — write to a different filename |
| `ZZ` | shortcut for save-and-quit, **no colon needed** |

> `:w filename` is the "Save As" of `vi` — useful when you have typed a lot and then decide to rename, without leaving the editor.

---

## Part 5 — Navigation

### Basic

Arrow keys work — but are slow in a large file.

### Word-wise

| Key | Action |
|---|---|
| `w` | jump **forward** one word |
| `b` | jump **backward** one word |

---

## Part 6 — Deleting

### Characters

| Key | Action |
|---|---|
| `x` | delete the character **under** the cursor |
| `X` | delete the character **before** the cursor |
| `u` | **undo** |

### Words

| Keys | Action |
|---|---|
| `dw` | delete **one word** |
| `2dw` | delete **two words** |
| `3dw` | delete **three words** |

### Lines

| Keys | Action |
|---|---|
| `dd` | cut/delete the **whole line** |
| `2dd` | cut **two lines** (current + the one below) |

> **The pattern to internalise:** `[count][operation][target]`. `3dw` = *three, delete, word*. Once you see the grammar, you can compose commands you were never taught.

---

## Part 7 — Replace without entering insert mode

```
r<char>
```

Press `r` then any character — it replaces the character under the cursor.

> **You never enter insert mode.** This is the fastest way to fix a single-character typo.

---

## Part 8 — Cut, copy and paste

| Keys | Action |
|---|---|
| `dd` | cut a line |
| `2dd` | cut two lines |
| `p` | **paste** below the cursor |
| `xp` | cut a character and paste it — effectively **swaps two characters** |

**Workflow:** `dd` to cut → move the cursor to the destination → `p` to paste.

---

## Part 9 — Visual mode

For selecting text **without a mouse** — which matters because, as noted in class, *"in many places you don't get mouse access, so you have to do all the work from the keyboard."*

| Key | Mode | Selects |
|---|---|---|
| `v` | **Visual** | **character by character** |
| `V` (Shift+v) | **Visual Line** | **whole lines** |
| `Ctrl+v` | **Visual Block** | a **rectangular block / columns** |

After entering a visual mode, extend the selection with the **arrow keys**. The mode name appears at the bottom (`-- VISUAL --`, `-- VISUAL LINE --`, `-- VISUAL BLOCK --`).

### The difference that matters

- **`v`** — moving up a line selects everything in between, including the whole line.
- **`Ctrl+v`** — selects **only the column block**, ignoring the rest of each line. This is how you edit aligned columns of text or config files.

> ⚠ **You must be in command mode to enter any visual mode.** Pressing `v` while in insert mode just types the letter `v`.

---

## Part 10 — Searching

| Key | Action |
|---|---|
| `/word` | search **forward** (top → bottom) |
| `?word` | search **backward** (bottom → top) |
| `n` | jump to the **next** match |
| `N` | jump to the **previous** match |

> These are the **same keys as `less`** from Day 4. The consistency is deliberate across Unix tools.

---

## Part 11 — Reading in files and command output

| Command | Effect |
|---|---|
| `:r filename` | insert the **contents of a file** at the cursor |
| `:r !command` | insert the **output of a shell command** at the cursor |

```
:r !lsblk        inserts the block-device listing into your file
:r !ls -l        inserts a directory listing
```

> Genuinely useful: capture command output straight into a report or notes file without leaving the editor or messing with redirection.

---

## Part 12 — Complete cheat sheet

```
MODES
  Esc              return to COMMAND mode (default on open)
  i / a            insert before / after cursor
  I / A            insert at line start / end
  o / O            open new line below / above
  v / V / Ctrl+v   visual / visual-line / visual-block

SAVE & QUIT  (all from command mode, begin with :)
  :w               save
  :q               quit
  :wq              save and quit
  :q!              quit WITHOUT saving
  :w newname.txt   save as
  ZZ               save and quit (shortcut)

NAVIGATION
  arrows           character / line
  w  /  b          next word / previous word

DELETE
  x  /  X          char under / before cursor
  dw / 2dw / 3dw   delete 1 / 2 / 3 words
  dd / 2dd         delete 1 / 2 lines
  u                undo

EDIT
  r<char>          replace a single character
  p                paste
  xp               swap two characters

SEARCH
  /word            forward
  ?word            backward
  n  /  N          next / previous match

READ IN
  :r file          insert a file's contents
  :r !command      insert a command's output
```

---

## Part 13 — The trainer's advice on learning `vi`

> 1. **Keep a cheat sheet or notes** — nobody memorises `vi` from one session.
> 2. **Use it daily.** Do all your editing, writing, and any work inside it, *"so that you get into the habit of it."*
> 3. Familiarity comes gradually — the keywords, selection, cut/copy/paste, replace, adding output. *"Once you become familiar with all of them, you will never say it's difficult."*

He also notes he is deliberately stopping here: *"as a beginner this much is enough, because otherwise you will get bored"* — `vi` could easily consume several sessions.

---

## Part 14 — Self-check questions

1. Why is knowing `vi` specifically important in a security context, as opposed to `nano`?
2. Name the four modes and how you enter each.
3. Which mode does `vi` open in? Why does this confuse beginners?
4. Which key always returns you to command mode?
5. Difference between `i`, `a`, `I` and `A`.
6. Difference between `o` and `O`.
7. Write the commands for: save; quit; save and quit; quit discarding changes; save as a new name.
8. What does `ZZ` do?
9. Difference between `x` and `X`.
10. Decompose `3dw` into its grammar. What would `5dd` do?
11. How do you replace one character without entering insert mode?
12. Describe the cut-and-paste workflow using `dd` and `p`. What does `xp` achieve?
13. Name the three visual modes and what each selects.
14. What can `Ctrl+v` do that `v` cannot?
15. Which mode must you be in to enter visual mode?
16. Search forward, search backward, next match, previous match — give the keys. Which other command uses the same keys?
17. What is the difference between `:r file` and `:r !command`? Give a practical use for the second.

---

## Part 15 — Course roadmap announced

The `locate` command was planned for this session but deferred. Remaining topics for Days 12–15:

| Topic | Content |
|---|---|
| **Networking** | network settings and configuration via the command line |
| **Repositories** | downloading, installing, uninstalling and searching for packages |
| **Faster searching** | additional commands for quicker searches (`locate` and others) |
| **History** | the `history` command |

> Stated goal: *"This would make your fundamentals clear."*
