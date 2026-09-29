# Day-15 Bash For Bug Bounty Live Training Capsule Course [Hindi] — English Translation

*Translated from: `071 - Day-15 Bash For Bug Bounty Live Training Capsule Course [ Hindi ].hi-orig.srt`*
*Style: detailed edited translation. Repeated chat checks and caption duplication are consolidated; technical clarifications are marked [TN].*

---

[music] Hello everyone, good evening, and welcome to Day 15 of the Bash Mastery course. First confirm in chat that my voice is reaching you. Thank you. Someone has asked for the assignment solution; I will discuss it after today's main topic.

The last class prepared us for logic. We studied command chaining and the `test` command: how a condition reports success or failure. Today we will use those tests in two important decision structures:

1. `if`, including `else` and `elif`;
2. `case` statements.

We will learn the syntax and build examples. Between them, I will also create a small memory-logging script so you can see how conditions solve a realistic problem.

# The `if` statement

Any useful program or script needs logic. Without logic, a script performs the same commands blindly. An `if` statement checks whether a condition succeeds and runs commands accordingly.

The basic syntax is:

```bash
if CONDITION; then
    commands
fi
```

You write the reserved word `if`, followed by the condition. A semicolon or newline marks the end of that condition. `then` begins the commands that should run if it is true. The block ends with `fi`—`if` written backward.

This is a compound command: it starts and ends with shell reserved words.

## First script: numeric condition

Create a file for the example and begin with the shebang:

```bash
#!/bin/bash
```

Now test whether two is greater than one:

```bash
if [ 2 -gt 1 ]; then
    echo "Test passed"
fi
```

Remember the spaces around the square brackets. The test `[ 2 -gt 1 ]` returns exit status zero, so Bash enters the block and prints `Test passed`.

Save it and give it permission:

```bash
chmod 744 if-condition.sh
./if-condition.sh
```

The script prints the success message. If we change the condition to something false, nothing prints because we have not supplied an alternative branch.

# `if` and `else`

Usually we also want an action for a false condition:

```bash
if CONDITION; then
    commands_for_true
else
    commands_for_false
fi
```

For example:

```bash
if [ 2 -gt 10 ]; then
    echo "Test passed"
else
    echo "Test failed"
fi
```

Two is not greater than ten, so the first block is skipped and the `else` block runs.

An `if` condition is not limited to square brackets. Any command can be the condition because commands return an exit status. The bracket form is simply convenient for comparisons and filesystem checks.

# User input and multiple branches

Now let us request a number and decide what it means:

```bash
read -p "Enter an integer value: " number
```

We can test it with `if` and add another condition using `elif`:

```bash
if [ "$number" -gt 1 ]; then
    echo "Number is greater than one"
elif [ "$number" -eq 1 ]; then
    echo "Number is equal to one"
else
    echo "Test failed"
fi
```

`elif` means “else if.” Bash checks branches from top to bottom:

1. If the first condition is true, its commands run and the remaining branches are skipped.
2. Otherwise the `elif` condition is tested.
3. If none are true, `else` runs.

The class modifies the thresholds while demonstrating, including a greater-than-100 test. The important rule is that branch order matters. The first successful branch wins.

[TN: Numeric input should be validated before `-gt`/`-eq`; non-numeric or empty input can produce an “integer expression expected” error.]

# Comparing files and debugging word splitting

The next example compares content from files. Several text files are created with the same sample content. The script reads or substitutes file content and attempts to compare the values.

During the first run Bash reports:

```text
too many arguments
```

Why? A file's content contains spaces. If the expansion is unquoted, word splitting turns one intended string operand into many separate arguments to `[`. The test command no longer receives the expression shape it expects.

The fix is to quote expansions:

```bash
file_one=$(<file01.txt)
file_two=$(<file02.txt)

if [ "$file_one" = "$file_two" ]; then
    echo "File content matches"
else
    echo "File does not match"
fi
```

This live error is useful because debugging means reading the message, asking where argument count changed, and checking quoting. Do not merely rewrite the whole script when a small expansion error is responsible.

Command substitution captures command output. `$(...)` is preferred over old backticks because it is easier to read and nest. For exact file comparison, however, a native tool is better:

```bash
if cmp -s file01.txt file02.txt; then
    echo "Files match"
else
    echo "Files differ"
fi
```

[TN: Capturing files into shell variables removes trailing newline characters and is unsuitable for binary data; `cmp -s` is the robust exact-comparison method.]

# Practical assignment: memory logger

Now imagine you have joined a company as a new employee. You receive a small task: periodically record the system's memory usage in a file so it can be reviewed later for performance monitoring.

The log should live under a particular directory in your home folder. But that directory may not exist yet. Your script must:

1. check whether the directory exists;
2. create it if it does not;
3. append the current memory report to a log file.

Create `memory-logger.sh`:

```bash
#!/bin/bash

log_directory="$HOME/performance"
log_file="$log_directory/memory.log"

if [ ! -d "$log_directory" ]; then
    mkdir "$log_directory"
    echo "Performance directory created"
fi

free >> "$log_file"
```

The condition uses:

- `-d` — true if the path is a directory;
- `!` — negates the result, so the branch runs when the directory does **not** exist.

You can equivalently write an `if`/`else` that prints whether it already exists. The important behavior is to avoid blindly creating it on every run.

Why put `echo` messages during development? They reveal which branch the program reached. This helps troubleshooting. Once the script is stable, remove noisy debug messages or replace them with intentional logging.

## Appending the memory report

The `free` command displays memory usage, including total, used, free, shared, buffer/cache, available memory, and swap. We append it using `>>`:

```bash
free >> "$HOME/performance/memory.log"
```

A single `>` would replace the previous contents every time. Double `>>` preserves earlier reports and adds the new one at the end.

Run the script several times, then inspect:

```bash
cat "$HOME/performance/memory.log"
```

Each execution adds another report. The demonstration explains the values shown by `free` and emphasizes the distinction between overwriting and appending.

A real monitoring log should also contain a timestamp; otherwise you cannot tell when a sample was recorded. [TN: A production improvement is shown in the explanation file.]

This is the beauty of `if`: before performing an action, check whether its prerequisite is already satisfied. If the directory exists, do not recreate it; if it is absent, create it.

# The `case` statement

Now we move to the second logic structure. A `case` statement compares one value against several patterns. It is often cleaner than a long chain of equality-based `elif` conditions.

Basic syntax:

```bash
case "$value" in
    pattern1)
        commands
        ;;
    pattern2)
        commands
        ;;
    *)
        default_commands
        ;;
esac
```

Important elements:

- `case` starts the compound command.
- The value being inspected follows it.
- `in` begins the pattern list.
- Each pattern ends with `)`.
- Each normal branch ends with `;;`.
- `esac`—`case` backward—closes the statement.

The instructor strongly emphasizes writing the variable expansion with `$` and wrapping it in double quotes:

```bash
case "$number" in
```

The `$` obtains the variable's value. Quotes preserve it as one shell word and avoid unintended splitting or glob expansion before `case` examines it.

# How matching works

Patterns are tested from top to bottom. The first matching pattern has its commands executed. Bash then leaves the `case` statement after `;;`.

The final `*` pattern is the default because it matches anything. It must come last. If you put it first, it matches immediately and no later pattern gets a chance.

`case` patterns are shell glob patterns, not regular expressions. Examples:

```bash
[0-9]       # one digit
[0-9][0-9] # two digits
[0-9]*)     # begins with a digit (not necessarily all digits)
*           # anything
```

# Number-pattern example

Create `case.sh`:

```bash
#!/bin/bash

read -p "Please enter a number: " number

case "$number" in
    [0-9])
        echo "You entered a one-digit number"
        ;;
    [0-9][0-9])
        echo "You entered a two-digit number"
        ;;
    [0-9][0-9][0-9])
        echo "You entered a three-digit number"
        ;;
    *)
        echo "You entered a number that is more than three digits, or invalid input"
        ;;
esac
```

Run it with several values. A single digit matches the first branch; two digits match the second; three digits match the third. A longer value reaches the default.

The instructor moves the `*` branch to the top as a demonstration. It then captures every input, proving why the default belongs at the end. A temporary syntax error also appears because a branch terminator/closure is missing. After adding the missing syntax, the script again runs—another reminder that each pattern arm must be properly terminated.

[TN: The spoken message says the default means “more than three digits,” but `*` also catches letters, empty input, signs, whitespace, and any other unmatched value. Its message should say “invalid or unsupported input” unless input was validated first.]

# When to use `if` and when to use `case`

Use `if` when conditions involve:

- numeric ranges;
- file tests;
- command success/failure;
- combinations of different expressions.

Use `case` when one value is being matched against recognizable string/glob patterns:

- menu commands such as `start|stop|status`;
- command-line option values;
- filename patterns;
- categories of input.

You could express many cases with `if`, but `case` is often easier to read and maintain.

# Closing

Today we covered:

- `if CONDITION; then ... fi`;
- false handling with `else`;
- multiple ordered conditions with `elif`;
- debugging an unquoted multi-word expansion;
- a practical memory-logging script;
- `case ... in ... esac`;
- first-match behavior and the final `*` default pattern.

The logic section will continue with further script-building and then loops. Practise by changing values, deliberately causing false conditions, and observing which branch executes.

<!-- DONE-071 -->
