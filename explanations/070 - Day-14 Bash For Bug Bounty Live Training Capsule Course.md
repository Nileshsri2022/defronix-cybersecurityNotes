# Day-14 Bash — List Operators, Exit Status, `test`, and `read` Project — Explained

## Lesson map

Day 14 builds the bridge from “a script can receive input” to “a script can make decisions.” It has three layers:

1. **List operators** decide whether another command runs.
2. **Exit status** supplies the true/false signal.
3. **`test`** turns comparisons and file facts into that signal.

The information-collection assignment then revises `read` and redirection before the course moves into `if`.

---

# 1. Shell truth means exit status

A shell command does not have to print `true` or `false`. It reports an integer status to its parent process:

```text
0       success / true
1–255   some form of failure / false
```

Non-zero values can carry command-specific meaning. For example, a tool may use one code for “invalid arguments” and another for “network failure.” Do not assume every failure is exactly 1.

Immediately inspect the latest foreground pipeline's status with:

```bash
some_command
echo "$?"
```

Why “immediately”? Because every subsequent command replaces `$?`:

```bash
false
echo hello       # this succeeds
echo "$?"        # prints echo's 0, not false's 1
```

In scripts, normally respond to status directly rather than saving `$?` unnecessarily:

```bash
if some_command; then
    echo "worked"
fi
```

---

# 2. The four list operators

## Quick table

| Form | Does shell wait? | When B runs |
|---|---:|---|
| `A &` | no | A is launched as a background job |
| `A && B` | yes | only if A returns 0 |
| `A || B` | yes | only if A returns non-zero |
| `A; B` | yes | after A, regardless of A's result |

## `&`: asynchronous execution

```bash
long_scan >scan.log 2>&1 &
pid=$!
echo "Started as PID $pid"
```

`$!` stores the process ID of the most recently started background job. Interactive job-control commands include:

```bash
jobs
fg %1
bg %1
wait "$pid"
```

Backgrounding is not persistence. A job may still receive a hangup signal when its terminal/session closes. For durable tasks, use an appropriate service manager, terminal multiplexer, or carefully configured `nohup` rather than assuming `&` is sufficient.

Also redirect input/output deliberately. A background command that still reads the terminal or floods it with output is not truly detached from your workflow.

## `&&`: prerequisite chain

```bash
mkdir -p output && cd output && touch started
```

Each later step runs only if everything needed before it succeeded. This is useful for short setup sequences.

It is **not** equivalent to “run all commands and report whether all passed.” Short-circuiting means execution stops at the first failure.

## `||`: fallback or error action

```bash
curl -fS "$url" -o page.html || echo "Download failed" >&2
```

The fallback runs only if `curl` reports failure. Be sure the first command's exit behavior matches what you mean by failure; for example, `curl` needs suitable flags if HTTP error responses should count as failure.

## `;`: sequencing without dependency

```bash
printf 'starting\n'; run_task; printf 'finished attempt\n'
```

The third command runs even if `run_task` fails. That may be correct for cleanup or logging, but dangerous when the second operation requires the first to succeed.

## Mixing `&&` and `||`

A common idiom is:

```bash
command && echo success || echo failure
```

But it has a trap: the failure message runs if **either** `command` fails **or** `echo success` fails. For clear multi-step logic, prefer:

```bash
if command; then
    echo success
else
    echo failure
fi
```

`&&` and `||` have equal precedence in Bash and are evaluated left-to-right. Use grouping when needed:

```bash
prepare && { run_job; archive_results; }
```

---

# 3. `test`, `[`, and `[[` are related but not identical

The lesson uses POSIX `test` and its bracket spelling:

```bash
test -f "$file"
[ -f "$file" ]
```

In Bash, `[` is a command (often a shell builtin), and `]` is its required final argument. This explains the spacing rule:

```bash
[ -f "$file" ]   # four-plus separate shell words
```

Bash also supports the more powerful `[[ ... ]]` conditional construct:

```bash
[[ -f $file ]]
```

Inside `[[ ]]`, word splitting and pathname expansion do not occur in the same way, and pattern/regex operations are available. But `[[ ]]` is not portable to every `/bin/sh`. The course begins with `[ ]`, so understand it first.

---

# 4. Numeric comparisons

## Operators for `[ ... ]`

```bash
[ "$a" -eq "$b" ]   # equal
[ "$a" -ne "$b" ]   # not equal
[ "$a" -gt "$b" ]   # greater than
[ "$a" -lt "$b" ]   # less than
[ "$a" -ge "$b" ]   # greater/equal
[ "$a" -le "$b" ]   # less/equal
```

Do not write this with single brackets:

```bash
[ "$a" > "$b" ]     # wrong intention: > may become output redirection
```

For arithmetic in Bash, an alternative is:

```bash
(( a > b ))
```

`(( ... ))` returns success when the arithmetic expression is non-zero. Variables inside it need not be prefixed with `$`.

## Validate before comparing

An empty or non-integer value can cause errors or surprising arithmetic interpretation. Validate user input first:

```bash
if [[ $extension =~ ^[0-9]{4}$ ]]; then
    echo valid
else
    echo "Enter exactly four digits" >&2
fi
```

This is one improvement needed by the lesson's project.

---

# 5. String tests

```bash
[ "$a" = "$b" ]
[ "$a" != "$b" ]
[ -z "$a" ]          # empty
[ -n "$a" ]          # non-empty
```

Quote expansions inside single brackets:

```bash
[ -n "$name" ]       # safe
[ -n $name ]         # can change meaning after splitting/globbing
```

Pattern matching is clearer with `[[ ]]`:

```bash
[[ $filename == *.txt ]]
```

The right side is intentionally unquoted there so `*.txt` acts as a pattern. This is different from plain string equality under `[ ]`.

---

# 6. File predicates

## Existence and type

| Test | True when path… |
|---|---|
| `-e` | exists |
| `-f` | is a regular file |
| `-d` | is a directory |
| `-L` / `-h` | is a symbolic link |
| `-p` | is a named pipe |
| `-S` | is a socket |
| `-b` | is a block device |
| `-c` | is a character device |

A broken symbolic link is a useful edge case: `-L` can be true while `-e` is false because the link itself exists but its target does not.

## Access checks

| Test | True when current process can… |
|---|---|
| `-r` | read the path |
| `-w` | write the path |
| `-x` | execute the file or search the directory |

These are checks from the current process's perspective, not merely a textual inspection of `rwx` bits. ACLs, effective identity and other filesystem rules can matter.

Robust script pattern:

```bash
file=${1:-}

if [ -z "$file" ]; then
    echo "Usage: $0 FILE" >&2
    exit 2
elif [ ! -e "$file" ]; then
    echo "Not found: $file" >&2
    exit 1
elif [ ! -r "$file" ]; then
    echo "Not readable: $file" >&2
    exit 1
fi
```

The unary `!` negates the test result.

## Correcting the live `-x` confusion

The class briefly tries to combine command substitution/backticks with `-x`. That is unnecessary. If a variable contains a path:

```bash
script=./demo.sh
[ -x "$script" ]
```

Command substitution executes a command and replaces `$(...)` with its output. It does not make a file predicate more accurate:

```bash
result=$(some_command)   # execute and capture stdout
```

Prefer `$(...)` over legacy backticks because nesting and quoting are clearer.

---

# 7. Improving the CSV assignment

The classroom version correctly demonstrates `read`, variables and append redirection, but production-quality collection needs validation and proper CSV handling.

## Faithful basic version

```bash
#!/usr/bin/env bash

read -r -p "What is your first name? " first_name
read -r -p "What is your last name? " last_name
read -r -n 4 -p "What is your current extension number? (4 digits): " extension
printf '\n'
read -r -n 4 -p "What access code would you like to use? (4 digits): " access_code
printf '\n'

printf '%s,%s,%s,%s\n' \
    "$first_name" "$last_name" "$extension" "$access_code" \
    >> information.csv
```

Changes from casual classroom syntax:

- `-r` prevents backslashes being consumed by `read`.
- `printf` is more predictable than `echo`.
- Every expansion is quoted.

## Why `-n 4` is not validation

`read -n 4` accepts any four characters:

```text
12ab    accepted by read -n 4
```

It can also return fewer characters on newline. Validate separately and repeat until correct:

```bash
while :; do
    read -r -p "Extension (4 digits): " extension
    [[ $extension =~ ^[0-9]{4}$ ]] && break
    echo "Please enter exactly four digits." >&2
done
```

This preview uses a loop taught later in the course.

## CSV correctness

Simple comma joining breaks when a name contains a comma, quote or newline. Proper CSV escapes fields by doubling embedded quotes and enclosing fields in quotes. A Bash helper:

```bash
csv_field() {
    local value=${1//\"/\"\"}
    printf '"%s"' "$value"
}

{
    csv_field "$first_name"; printf ','
    csv_field "$last_name"; printf ','
    csv_field "$extension"; printf ','
    csv_field "$access_code"; printf '\n'
} >> information.csv
```

For complex data, a language with a standard CSV library is safer.

## Security concern: do not store PINs casually

The scenario calls the final value an access/PIN code. Appending real secrets to a plaintext CSV is unsafe. In a real system:

- question whether the secret should be collected at all;
- restrict file permissions (`umask 077`);
- avoid shared writable output susceptible to symlink attacks;
- encrypt sensitive storage appropriately;
- define retention and access policy;
- never commit collected data to Git.

For this course, treat the values as fictional sample data.

## Concurrent writers

If many colleagues run the script at once against one shared file, writes can race. `flock` can serialize appends on Linux:

```bash
{
    flock 9
    printf '%s,%s,%s,%s\n' "$first_name" "$last_name" "$extension" "$access_code" >&9
} 9>>information.csv
```

That is beyond the lesson but follows naturally from its office scenario.

---

# 8. Bug-bounty scripting applications

The day's constructs appear constantly in defensive and authorized security tooling:

```bash
# Stop if a scope file does not exist
[ -f scope.txt ] || { echo "Missing scope.txt" >&2; exit 1; }

# Build only after dependency installation succeeds
install_dependency && build_tool

# Preserve output while a long authorized scan runs
scanner --scope scope.txt >scan.log 2>&1 &
scan_pid=$!

# Process results only when the scanner succeeds
wait "$scan_pid" && parse_results scan.log
```

Be careful with the word “success.” A scanner can exit zero while reporting no findings, and it can find results while returning a special status. Read each tool's exit-code documentation.

---

# Cheat card

```bash
A &          # launch A in background
A && B       # B only if A succeeds
A || B       # B only if A fails
A; B         # B after A regardless
$?           # most recent foreground pipeline status
$!           # PID of most recent background job

[ "$n" -eq 4 ]
[ "$n" -gt 4 ]
[ "$a" = "$b" ]
[ -z "$a" ]
[ -e "$path" ]
[ -f "$path" ]
[ -d "$path" ]
[ -r "$path" ]
[ -w "$path" ]
[ -x "$path" ]
```

## Review questions

1. Why does zero represent shell success?
2. When does B run in `A && B`, `A || B`, and `A; B`?
3. Why must spaces surround expressions in `[ ... ]`?
4. What is the difference between `-e` and `-f`?
5. Why should variable expansions be quoted inside `[ ... ]`?
6. Why does `read -n 4` not guarantee four digits?
7. What privacy problem exists in the sample CSV scenario?
8. When is a full `if` block clearer than a mixed `&&`/`||` chain?

<!-- DONE-070 -->
