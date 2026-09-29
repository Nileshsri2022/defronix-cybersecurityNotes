# Explained — 061 — Day 7: Bash for Bug Bounty (PATH & PS1, Parameter-Expansion Superpowers, Tilde Expansion)

**Source:** Defronix Bash-for-Bug-Bounty live training, Day 7 (~40 min, live Kali — his first class that *begins* in a real `bash_script.sh` file with a shebang).
**Curriculum position:** still inside **STEP 3 (expansion)** — closes out **parameter expansion** (advanced features + slicing) and **tilde expansion**, completing 2 of the 7 expansions. Pipeline confirmations dropped today: **step-4 = QUOTE-REMOVAL, step-5 = REDIRECTION**. Remaining before them: command-substitution, arithmetic, brace, word-splitting, globbing.
**Hidden exam:** the seeded riddle from an earlier class ("can I run my script from ANYWHERE without typing its full path?") gets its answer — and it's a variable.

---

## PART A — two environment variables that rule the session

### `$PATH` — why `ls` works everywhere but your script doesn't

**The observation he builds from:** type `ls`, `pwd`, `cat`, `less` from *any* directory and they just run — how does the shell find their binaries without a path?

**The mechanism:**
1. `which cat` → **`/usr/bin/cat`** — the `which` command is the direct "where does binary X live" probe.
2. **`echo $PATH`** reveals the shell's search list — an *ordered, colon-separated* set of directories (his Kali: `/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games:/home/kali/.dotnet/tools`).
3. When you fire a bare name, bash sweeps the list **left-to-right**, first directory that contains a matching executable wins; that file runs.
4. If the binary sits in **none** of them → full path is compulsory: `/usr/bin/cat file` works even if `cat` won't.

**Answer to the seeded riddle — make YOUR script feel native:** either **drop the script into a directory already inside `$PATH`** (e.g. `/usr/local/bin` — power-user convention he implies), **or append your script's directory to `$PATH`**. Otherwise: full/absolute path forever. That's the entire solution — one variable. *(Persistence of that PATH edit = same profile-file route as any env-var.)*

### `$PS1` — your prompt is just a variable holding a template

- **PS1 = the primary prompt format** — *"it determines what your shell-prompt looks like."* Everything you see (user@host, working dir, `$`/`#`, **colors green/blue segments**, zsh-vs-bash differences) is text in PS1.
- `echo $PS1` shows the current template (his zsh's is predictably baroque); templates are **shell-specific** — bash and zsh ship different ones.
- **Live rebrand:** `PS1="defronixshell $ "` → prompt instantly becomes `defronixshell $` — *temporary* (session-scoped). Printing `$PS1` after shows the new value.
- **The 3-scopes law for ANY environment variable:**
  | Scope | How | Dies when… |
  |---|---|---|
  | **Temporary** | `VAR=value` in the current shell | shell exits / you log out |
  | **Permanent (per-user)** | entry in the user's profile file (`.bashrc`/profile) | you remove the line |
  | **Global (all users)** | export inside the **global** profile file (`/etc/profile`) | root removes the line |

  (He defers the demo to his Linux series — "already covered there" — but names all three file destinations.) Logging out/in restores the original prompt, proving scope temporariness.

## PART B — parameter expansion, the advanced tier (bash-only, `${}`-only)

**The doorway rule (he drills it four times):** every feature below **works *only* inside `${…}`** — the bare `$name` form can't access any of them; and on a non-bash shell (zsh) they throw **`bad substitution`** — the reason he switches to writing `bash_script.sh` with a `#!/bin/bash` shebang, `chmod 744`, and keeps every trick inside the script.

### Case surgery — comma/caret operators

Actor: `name=NITESH`, then `name=sachin`.

| Form | Meaning | On his values |
|---|---|---|
| `${name,}` | **first** character → lowercase | `NITESH` → `nITESH` |
| `${name,,}` | **all** characters → lowercase | → `nitesh` |
| `${name^}` | **first** character → UPPERCASE | `sachin` → `Sachin` |
| `${name^^}` | **all** characters → UPPERCASE | → `SACHIN` |

**The non-mutation guarantee (his core lecture point, restated per feature):** these change only the **representation at expansion time** — the stored value is untouched. He proves it by following each trick with plain `echo ${name}` → original value prints. Curl up under this rule: *parameter-expansion features are lenses, not pens.*

### Length — `${#name}`

`${#sachin}` → **6**. Hash FIRST, then the name. Same braces-only confinement. (Bug-bounty use-case you'll meet later: pre-flight validation — "API key empty? `${#KEY}` == 0 → abort.")

### Slicing — `${var:offset:length}`

**Foundation — everything is indexed:** a stored string is an array of characters; first char = **index 0**, and — he makes you say it — **spaces are index cells too**. (`sachin` = S:0 a:1 c:2 h:3 i:4 n:5.)

**Definition (verbatim):** *"slicing enables us to take just a small section"* of a string. Syntax to screenshot: **`${parameter:offset:length}`**.

Actor line: `name="this is bash master class"` — *after* re-learning the hard way that an unquoted multi-word assignment detonates (`line 2: is: command not found` — `name=this` then tried to RUN `is`) → **double-quote values with spaces**, Day-3 quoting paying rent again.

| Expression | Output | Why |
|---|---|---|
| `${name:2:7}` | `is is b` | offset 2 (`i`), take 7 chars (space counts) |
| `${name:8:4}` | `bash` | offset 8 (`b`), 4 chars |
| `${name:8}` | `bash master class` | **length omitted ⇒ to end of string** |
| `${name:8:}` | *(empty line)* | **colon present, length empty ⇒ length ZERO** — a different beast from the row above |

**Negative offsets** count from the tail as `-1, -2, -3…` (there is NO -0): `${name: -4:4}` → `lass`.
**The compulsory SPACE before the minus** — `${name: -4:4}` works; `${name:-4:4}` makes bash "confused": that spaceless form collides with the *default-value* operator family (`${var:-word}`) — upcoming feature territory he explains behaviorally today. Rule of thumb: **space, then minus, then the number; no other spaces.**

## PART C — tilde expansion (the 10-minute closer)

**Mechanism:** performed by a single special character **`~`** (stage-2 expansion family, same stage as `$param`).

**Base ability** (you already knew it without the name): `~` expands to the **current user's HOME** — `echo ~` → `/home/kali`. His one-liner: *"it lets you refer to the home dir without typing the full path — the hard-work killer."*

**Advanced 1 — `~user` = a zero-cost user-existence probe**
- `echo ~root` → `/root`; (after `useradd sachin` + password) `echo ~sachin` → `/home/sachin` — **valid user ⇒ expands to THEIR home.**
- `echo ~nitesh` (no such user) → prints the literal string **`~nitesh`** — **invalid user ⇒ NO expansion, no error.** 
  → in a script: try expanding `~USERNAME`; if the result still *contains* the tilde, the user doesn't exist. Elegant, zero dependencies.

**Advanced 2 — `~+` and `~-`, the directory pair**
- bash internally maintains two auto-updating shell variables: **`$PWD`** (current dir) and **`$OLDPWD`** (the dir you were in *just before* the last `cd`) — proven live: `cd /etc` → `echo $PWD`=`/etc`, `echo $OLDPWD`=`/home/kali`.
- Their tilde shortcuts: **`~+` = `$PWD`**, **`~-` = `$OLDPWD`**.
- Killer move (his live dance): `cd ~-` teleports you to the previous directory — he toggles `/etc ↔ /home/kali` repeatedly with `echo ~+` as the where-am-I. **Escalation caveat he plants:** values refresh at *every* `cd`, so the pair always describes your *last two* rooms only.

## D) Session mechanics worth keeping

- **First shebang-script ceremony of the series:** `nano bash_script.sh` → `#!/bin/bash` → content → `chmod 744` → `./bash_script.sh`. (The chmod-permissions deep dive belongs to the Linux course; here it's ceremony-by-example.)
- Portability bite: `${var,}` **is bash-4+ syntax** — zsh threw `bad substitution` on-screen, and he immediately reroutes into the `.sh` file; remember script-vs-interactive shell differences when tricks "don't work."
- Community: 2× "did parameter expansion land? YES/NO" → silence; Telegram-group support flow restated (screenshot + problem in the group; description has the link). Doorbell interruption preserved ("someone on my gate").

## E) Pitfall table

| Symptom | Root cause | Cure |
|---|---|---|
| `bash: bad substitution` on `${name,}` | you're in zsh / old shell — feature is bash-4+ | shebang `#!/bin/bash`, run as script; bash-specific: state it |
| `line 2: is: command not found` after `name=this is …` | unquoted multi-word value — bash assigned `this`, then executed `is` | quote: `name="this is …"` |
| trick "didn't save" in the variable | expansion ≠ mutation — representation only | store the result: `name2=${name^^}` |
| `${name:8:}` prints nothing | explicit colon ⇒ length read as 0, not "to-end" | drop the colon entirely for to-end: `${name:8}` |
| `${name:-4:4}` → garbage/error | spaceless minus = bash parses `:-…` as the default-op | `${name: -4:4}` — mandatory space |
| `~nosuchuser` silently prints `~nosuchuser` | invalid user ⇒ no expansion, NO error | check the output still starts with `~` to detect invalids |
| own script needs `./script.sh` or full path | script's dir ∉ `$PATH` | move to a PATH dir or extend `$PATH` |
| PS1 customizations vanished next login | temporary scope | write them to `.bashrc` (per-user) or `/etc/profile` (global) |

## F) Cheat card

```
$PATH  : colon-separated, ordered binary search-list · which cmd = where's the binary
         run-yourself-anywhere = put script in a PATH dir  or  PATH=$PATH:/your/dir
$PS1   : prompt template var · temp: PS1="defronixshell $ " · persist: .bashrc / global: /etc/profile
         any env var scopes: temporary | per-user-permanent | global

parameter expansion ADVANCED (bash-only, ${}-only, NEVER mutates the value):
   ${var,}  ${var,,}  = first/all → lower
   ${var^}  ${var^^}  = first/all → UPPER
   ${#var}            = length
Slicing  : ${var:offset:length}     index 0-based, spaces count
           ${var:8}    = offset→end        ${var:8:}  = length 0 → EMPTY
           ${var: -4:4}= last-4 (NEGATIVE needs the leading SPACE)

tilde expansion:
   ~        = current user's $HOME
   ~user    = that user's $HOME · invalid user ⇒ prints literally (~user) = existence probe
   ~+       = $PWD       ~- = $OLDPWD    (auto-updated every cd; cd ~- = teleport back)
```

**Next class (announced):** expansion tour continues — **command substitution**, **arithmetic expansion**, **brace expansion** (then word-splitting & globbing), keeping the 35–40-minute short format.
