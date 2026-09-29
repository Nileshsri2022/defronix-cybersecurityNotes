# Day-15 Bash — `if`, `elif`, `else`, `case`, and a Memory Logger — Explained

## Core idea

Bash does not require a special Boolean data type for control flow. It asks one question:

> Did the condition command return exit status zero?

That condition can be `[ ... ]`, `[[ ... ]]`, `(( ... ))`, `grep -q`, `cmp -s`, `mkdir`, or almost any other command.

```bash
if command; then
    # status 0
else
    # non-zero status
fi
```

This directly connects Day 15 to Day 14's exit-status and `test` lesson.

---

# 1. Anatomy of `if`

```bash
if condition; then
    action
elif another_condition; then
    another_action
else
    fallback
fi
```

The semicolon before `then` is required only when `then` is on the same line. This is equally valid:

```bash
if condition
then
    action
fi
```

Shell indentation is for humans; reserved words define structure. Nevertheless, consistent indentation prevents mistakes in nested logic.

## First successful branch wins

Conditions are evaluated in order. Once one succeeds, its branch runs and Bash skips all remaining `elif`/`else` branches.

Ordering therefore changes meaning:

```bash
# Wrong order for grading: 90 also satisfies >= 50
if (( score >= 50 )); then
    echo pass
elif (( score >= 80 )); then
    echo excellent
fi
```

Correct:

```bash
if (( score >= 80 )); then
    echo excellent
elif (( score >= 50 )); then
    echo pass
else
    echo retry
fi
```

Put narrower or higher-priority ranges before broader ones.

---

# 2. Choosing a conditional form

## POSIX test / single brackets

```bash
if [ "$number" -gt 1 ]; then
    ...
fi
```

Portable and appropriate for standard file/string/integer predicates. Quote expansions.

## Bash extended test

```bash
if [[ $name == S* ]]; then
    ...
fi
```

Safer handling of empty/space-containing expansions and supports glob matching plus `=~` regular expressions. Bash-specific.

## Arithmetic condition

```bash
if (( number > 1 )); then
    ...
fi
```

Usually clearer for integer arithmetic. It still needs input validation if the value came from an untrusted user; arithmetic syntax can interpret variable names and expressions.

## A command as condition

```bash
if grep -q '^enabled=yes$' config.ini; then
    echo enabled
fi
```

Do not write `[ $(grep ...) ]` when the command's exit status already expresses the answer. Direct command conditions preserve intent and avoid output-splitting bugs.

---

# 3. Validate numeric input

The classroom example sends `read` input directly into `-gt`/`-eq`. Improve it:

```bash
read -r -p "Enter an integer: " number

if [[ ! $number =~ ^-?[0-9]+$ ]]; then
    echo "Not an integer" >&2
    exit 2
elif (( number > 100 )); then
    echo "greater than 100"
elif (( number == 1 )); then
    echo "equal to one"
else
    echo "another valid integer"
fi
```

The regular expression permits an optional minus sign followed by one or more digits. Decide separately whether leading plus signs, leading zeros, or huge values should be accepted.

Exit code 2 commonly represents usage/input error, but a script should document its own codes.

---

# 4. File-content comparison and the “too many arguments” error

Consider:

```bash
left=$(<a.txt)
right=$(<b.txt)
[ $left = $right ]
```

If `left` expands to `hello from file`, `[ ... ]` receives multiple words:

```text
[ hello from file = ... ]
```

It cannot parse that as one binary string comparison, so it may report “too many arguments.” Quoting preserves one operand:

```bash
[ "$left" = "$right" ]
```

But shell variables are not a general file-comparison mechanism:

- command substitution removes trailing newlines;
- shell variables cannot preserve NUL bytes;
- large files consume memory;
- binary content is unsafe.

Use the tool designed for the job:

```bash
if cmp -s -- file01.txt file02.txt; then
    echo identical
else
    status=$?
    if (( status == 1 )); then
        echo different
    else
        echo "comparison error" >&2
        exit "$status"
    fi
fi
```

`cmp -s` normally returns 0 for equal, 1 for different, and a larger status for an operational error. Treating every non-zero status as simply “different” can hide a missing or unreadable file.

For line-oriented differences, use `diff` instead.

---

# 5. Building a reliable memory logger

## Classroom version

```bash
#!/usr/bin/env bash

log_dir="$HOME/performance"

if [ ! -d "$log_dir" ]; then
    mkdir "$log_dir"
fi

free >> "$log_dir/memory.log"
```

It demonstrates the core logic correctly:

```text
Does directory exist?
├─ no  → create it
└─ yes → leave it alone
then append memory report
```

## Prefer idempotent directory creation

`mkdir -p` already means “create this path and missing parents; do not fail merely because it exists”:

```bash
mkdir -p -- "$log_dir" || exit 1
```

This can replace the `if` when no distinct branch behavior is required. The lesson's `if` remains pedagogically useful.

## Production-ready revision

```bash
#!/usr/bin/env bash
set -u

log_dir=${XDG_STATE_HOME:-"$HOME/.local/state"}/memory-logger
log_file=$log_dir/memory.log

if ! mkdir -p -- "$log_dir"; then
    printf 'Cannot create log directory: %s\n' "$log_dir" >&2
    exit 1
fi

if ! {
    printf '\n=== %s ===\n' "$(date --iso-8601=seconds)"
    free -h
} >>"$log_file"; then
    printf 'Cannot append to log: %s\n' "$log_file" >&2
    exit 1
fi
```

Improvements:

- records an ISO timestamp;
- uses human-readable `free -h` output;
- checks directory and append failures;
- keeps mutable state under an appropriate state directory;
- quotes every path;
- uses `--` to end options before a path;
- does not claim success when writing failed.

For machine parsing, `free`'s display format may be less suitable than metrics from `/proc/meminfo` or a monitoring system. For long-running systems, use log rotation so the file cannot grow forever.

## Scheduling

A logger becomes periodic through a scheduler, not an infinite busy loop. Options include:

- a user/system `systemd` timer;
- `cron`;
- a controlled loop with `sleep` for a temporary lab.

The scheduler should use absolute paths and a known environment because scheduled jobs often have a smaller `PATH` than interactive shells.

---

# 6. Understanding `case`

## Exact structure

```bash
case "$word" in
    pattern)
        commands
        ;;
    another|alternative)
        commands
        ;;
    *)
        fallback
        ;;
esac
```

`case` compares one word against patterns in source order. The first match executes. `;;` ends that branch and exits the case selection.

Other Bash terminators exist (`;&` and `;;&`) with fall-through/retesting behavior, but they are beyond this class and less portable. Use `;;` until you intentionally need something else.

## Globs, not regex

| Case pattern | Meaning |
|---|---|
| `yes` | exact text `yes` |
| `yes|y|Y` | one of three alternatives |
| `[0-9]` | exactly one digit |
| `[0-9][0-9]` | exactly two digits |
| `*.txt` | any string ending `.txt` |
| `*` | anything, including empty |

A common mistake:

```bash
[0-9]*
```

This means “one digit followed by any characters,” not “one or more digits only.” It matches `1abc`. For strict numeric validation, use `[[ $x =~ ^[0-9]+$ ]]` before categorizing by length, or use repeated digit patterns when the accepted length is fixed.

## Corrected number classifier

```bash
read -r -p "Enter a positive integer: " number

case "$number" in
    [0-9])
        echo one-digit
        ;;
    [0-9][0-9])
        echo two-digit
        ;;
    [0-9][0-9][0-9])
        echo three-digit
        ;;
    *[!0-9]*|'')
        echo "invalid: digits only" >&2
        ;;
    *)
        echo "more than three digits"
        ;;
esac
```

The invalid pattern contains a character that is not a digit, and `''` catches empty input. It must appear before the final catch-all. Now the final branch more accurately means an all-digit value longer than three characters.

Leading zeroes remain characters: `007` is classified as three digits even though its arithmetic value is seven. That may be correct for identifiers and wrong for quantities; requirements decide.

## Why default belongs last

`*` matches every possible value. If it is first:

```bash
case "$x" in
    *) echo default ;;
    start) echo starting ;;
esac
```

`start` can never reach its own branch. This is not merely style; source-order matching determines behavior.

---

# 7. `if` versus `case`

| Requirement | Better starting choice |
|---|---|
| Command succeeded? | `if command` |
| Numeric range | `if (( ... ))` |
| File exists/readable? | `if [[ -r $file ]]` |
| Several unrelated conditions | `if` / `elif` |
| One string against known commands | `case` |
| Filename/glob categories | `case` |
| CLI option dispatch | `case` inside `getopts` loop |

Example subcommand dispatcher:

```bash
case ${1:-} in
    start) start_service ;;
    stop) stop_service ;;
    status) show_status ;;
    -h|--help|'') usage ;;
    *) echo "Unknown command: $1" >&2; exit 2 ;;
esac
```

This is the same structure used by many command-line tools.

---

# 8. Debugging checklist from the live class

When a conditional script fails:

1. Run a syntax check without executing:
   ```bash
   bash -n script.sh
   ```
2. Trace expansions and executed commands:
   ```bash
   bash -x script.sh
   ```
3. Quote variable expansions.
4. Inspect the condition's status immediately.
5. Confirm each `if` has `fi` and each `case` has `esac`.
6. Confirm each case pattern has `)` and normal branch has `;;`.
7. Test empty, spaced, wildcard-containing, and invalid input.
8. Distinguish “false condition” from “condition command failed to execute correctly.”

Temporary `echo`/`printf` messages are useful, but tracing often reveals more precise information.

---

# Cheat card

```bash
if condition; then
    ...
elif condition; then
    ...
else
    ...
fi

case "$value" in
    a|A) ... ;;
    b*)  ... ;;
    *)   ... ;;
esac

[ -d "$dir" ]
[ ! -d "$dir" ]
[[ $input =~ ^[0-9]+$ ]]
(( number > 100 ))
cmp -s -- file1 file2
```

## Review questions

1. Can a normal external command be used directly after `if`? Why?
2. Why does `elif` order matter?
3. What causes `[ $content = $other ]` to report too many arguments?
4. Why is `cmp -s` safer than command substitution for file comparison?
5. Why does a useful monitoring log need timestamps and rotation?
6. Are `case` patterns regular expressions?
7. Why must `*` normally be the final `case` branch?
8. What does `[0-9]*` actually match?

<!-- DONE-071 -->
