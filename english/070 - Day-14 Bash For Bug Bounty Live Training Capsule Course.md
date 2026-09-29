# Day-14 Bash For Bug Bounty Live Training Capsule Course [Hindi] — English Translation

*Translated from: `070 - Day-14 Bash For Bug Bounty Live Training Capsule Course [ Hindi ].hi-orig.srt`*
*Style: detailed edited translation. Repeated live-chat prompts and caption duplication are consolidated. Technical corrections are marked [TN].*

---

[music] Hello everyone, good evening. First tell me in the chat whether my voice is audible—yes or no—and then we will start without wasting time. Thank you.

Today is Day 14 of our Bash Mastery course. We are now gradually entering the interesting topics where you will begin applying logic. In the previous class we learned how a script can request input from a user: positional and special parameters for command-line input, `read` for interactive input, and `select` for offering multiple choices like the menus you see in tools.

I gave you assignments based on those commands. I do not think many people completed them, so at the end of today's class I will solve one assignment. It is simple, but it will give you hands-on practice writing a small script around user input.

Before beginning `if`, `for`, and `while`, there are two foundations to cover:

1. How to create chains of commands with **list operators**.
2. How to check conditions with the **`test` command**.

# Command chains and list operators

A command chain means putting multiple commands on one command line and deciding how they relate to one another. List operators are a type of control operator. They control whether the shell waits, and whether the next command should run after success or failure.

The four operators we will study are:

| Operator | Name | Meaning |
|---|---|---|
| `&` | ampersand/background operator | run the preceding command asynchronously |
| `&&` | AND operator | run the next command only if the previous one succeeds |
| `;` | semicolon | run commands sequentially regardless of success/failure |
| `||` | OR operator | run the next command only if the previous one fails |

## Single ampersand: `&`

Suppose you start a command that takes a long time. Normally, your terminal waits for it to finish before returning the prompt. If you do not want to wait, put a single ampersand after it:

```bash
command &
```

This runs the command asynchronously—in the background—and gives the terminal back to you so you can do other work. The shell generally prints a job number and process ID. When the background job finishes, Bash can notify you that it is done.

This does not mean the command has magically become faster. It only means your interactive shell is not blocked while it runs.

## Double ampersand: `&&`

The double ampersand is the AND operator:

```bash
command1 && command2
```

The second command runs **only when the first command succeeds**. For example:

```bash
ls && echo "The listing succeeded"
```

If `ls` succeeds, the `echo` runs. But if I deliberately ask `ls` for a path that does not exist:

```bash
ls /no-such-path && echo "second command"
```

`ls` prints an error, and the second command does not run because it depended on the first command's success.

## Double pipe: `||`

The double pipe is the OR operator:

```bash
command1 || command2
```

Here, the second command runs **only when the first command fails**. Using the same failing example:

```bash
ls /no-such-path || echo "The first command failed"
```

The path does not exist, so `ls` fails and the fallback `echo` runs. If the first command succeeds, the second one is skipped.

That is the major difference:

- `A && B`: run B if A succeeds.
- `A || B`: run B if A fails.

## Semicolon: `;`

A semicolon separates commands but does not make the second depend on the first:

```bash
command1; command2
```

Bash runs the first command, waits for it to finish, and then runs the second whether the first succeeded or failed.

For example:

```bash
ls /no-such-path; echo "This still runs"
```

The `ls` command fails, but `echo` still runs. This is different from `&&` and `||`, where the second command is conditional.

## Mixing list operators

These operators can be combined:

```bash
mkdir reports && cd reports || echo "Setup failed"
```

If `mkdir reports` succeeds, Bash attempts `cd reports`. If the AND-list fails, the fallback after `||` runs. You need to understand evaluation order when chains become longer; for scripts, parentheses or a clear `if` block may be easier to read than a complicated one-liner.

The practical point is that command chains already create simple logic. You can say: do this only after success, otherwise perform a fallback.

# Exit status

How does Bash know whether a command succeeded? Every command returns an **exit status**.

- `0` means success/true.
- A non-zero value means failure/false.

Some people coming from other languages expect one to mean true and zero false, but shell command status follows this convention: zero is success.

The special parameter `$?` contains the exit status of the most recently completed foreground command:

```bash
ls
 echo $?
```

If `ls` succeeds, the status is zero. If we run an invalid command or ask for a nonexistent file and immediately check `$?`, we receive a non-zero result.

Check it immediately. Running `echo`, `clear`, or anything else replaces `$?` with that new command's status.

`&&` and `||` operate on this status. They do not inspect the words printed on screen.

# The `test` command

Now we need a way to ask questions such as:

- Is one number greater than another?
- Are two strings equal?
- Does a file exist?
- Is a file writable or executable?

Bash's `test` command evaluates such expressions and communicates true or false through its exit status.

These forms are equivalent:

```bash
test EXPRESSION
[ EXPRESSION ]
```

The square brackets are not decorative punctuation; `[` is a command. Therefore spacing is compulsory:

```bash
[ 2 -gt 1 ]     # correct
[2 -gt 1]       # wrong
```

Always put a space after `[` and before `]`, and separate the operands and operator.

After a test, use `echo $?` to see whether it was true:

```bash
[ 2 -gt 1 ]
echo $?
```

The result is zero because two is greater than one.

# Integer tests

For integer values, the important operators are:

| Operator | Meaning |
|---|---|
| `-eq` | equal |
| `-ne` | not equal |
| `-gt` | greater than |
| `-lt` | less than |
| `-ge` | greater than or equal |
| `-le` | less than or equal |

Examples:

```bash
[ 10 -eq 10 ]
[ 10 -ne 5 ]
[ 10 -gt 5 ]
[ 5 -lt 10 ]
[ 10 -ge 10 ]
[ 5 -le 10 ]
```

Each true expression returns zero. Change one value so the statement is false and it returns a non-zero status.

These operators are for integers. They do not directly handle decimal/floating-point arithmetic. If you need decimals, use an appropriate tool such as `awk` or `bc` rather than assuming `test` will compare them numerically.

# String tests

I create two variables for demonstration:

```bash
a="hello"
b="goodbye"
```

Common string tests include:

```bash
[ "$a" = "$b" ]      # equal
[ "$a" != "$b" ]     # not equal
[ -z "$a" ]           # zero length / empty
[ -n "$a" ]           # non-zero length / non-empty
```

With `a=hello` and `b=goodbye`, equality is false and inequality is true.

Quote the variable expansions. If a variable is empty or contains spaces, unquoted expansions can change the number of arguments passed to `[`, creating errors or misleading results.

During the live demonstration, the non-empty check behaves unexpectedly in one attempt. The concept remains: `-z STRING` is true for an empty string and `-n STRING` is true for a non-empty string. [TN: Some spoken/captioned attempts omit quotes or confuse the operator, which can explain inconsistent output.]

There are more string operators in the Bash manual; I will try to provide the reference. You do not have to memorize every operator today. Understand the pattern and know where to look them up.

# File tests

File test operators let a script examine filesystem objects before acting on them.

## Existence: `-e`

```bash
[ -e demo.txt ]
echo $?
```

If `demo.txt` does not exist, the result is non-zero. Create it and test again:

```bash
touch demo.txt
[ -e demo.txt ]
echo $?
```

Now the status is zero.

## Object type

```bash
[ -f demo.txt ]     # true if it is a regular file
[ -d reports ]      # true if it is a directory
```

A path can exist but not be a regular file—for example, it may be a directory. That is why `-e` and `-f` answer different questions.

## Permissions

```bash
[ -r demo.txt ]     # readable by the current user
[ -w demo.txt ]     # writable by the current user
[ -x demo.txt ]     # executable/searchable by the current user
```

The test is relative to the user running the script. Root can sometimes pass permission tests that an ordinary user cannot.

The live terminal shows some confusion while trying to test executable and writable permissions through a variable and command substitution. [TN: `-x` expects a pathname directly; it does not test whether a file “contains a command prompt.” Correct form: `[ -x "$file" ]`. A variable can hold the path, but command substitution with backticks is unnecessary.]

For example:

```bash
file="demo.sh"
[ -x "$file" ]
echo $?
```

If necessary, grant execute permission and repeat:

```bash
chmod +x demo.sh
[ -x demo.sh ]
echo $?
```

The exact result depends on the file mode, ownership, ACLs, filesystem mount options, and current user.

# Assignment solution: employee phone information collector

Now we solve one of the previous assignments.

## Scenario

Imagine you work in an office and must collect telephone information from every colleague. For each person, you need:

1. First name
2. Family/last name
3. Current extension number
4. Access/PIN code used while dialing

There is no internal phone system through which you can request it automatically, and walking to every desk would be inefficient. So you decide to write a Bash script that each colleague can run. It asks the questions and appends the responses to a CSV file for later processing.

Create a script named `info-collection.sh`:

```bash
nano info-collection.sh
```

Start with the shebang:

```bash
#!/bin/bash
```

## Prompting with `read -p`

Ask for the first and last names:

```bash
read -p "What is your first name? " first_name
read -p "What is your last name? " last_name
```

The `-p` option displays the prompt on the same line and stores the entered text in the named variable.

For the extension and access code, the demonstration limits input to four characters with `-n 4`:

```bash
read -n 4 -p "What is your current extension number? (4 digits): " extension
printf '\n'
read -n 4 -p "What access code would you like to use? (4 digits): " access_code
printf '\n'
```

Once four characters are entered, `read` returns without waiting for Enter, so print a newline afterward to keep the terminal tidy.

[TN: `-n 4` limits the number of characters but does **not** prove they are digits. Proper numeric validation comes later with tests/regular expressions and loops.]

## Writing CSV output

Append the four values as one comma-separated row:

```bash
printf '%s,%s,%s,%s\n' \
  "$first_name" "$last_name" "$extension" "$access_code" \
  >> information.csv
```

The class demonstration uses `echo` with comma-separated variables and `>>`. The double redirection operator appends rather than overwriting previous colleagues' information.

After making the script executable:

```bash
chmod +x info-collection.sh
./info-collection.sh
```

enter sample data and inspect the file:

```bash
cat information.csv
```

Each run adds another row, for example:

```csv
Sachin,Singh,1234,5678
Nitesh,Singh,7890,1234
```

The instructor removes the test file once to clear malformed practice output and runs the script again so the final CSV is easy to see. Blank `echo` statements are also added around prompts for cleaner display.

## What the assignment combines

This small script combines concepts already covered:

- a shebang and executable script file;
- variables;
- interactive input through `read`;
- `-p` prompts;
- `-n` character limits;
- output redirection;
- `>>` append behavior;
- a simple CSV record.

Later, conditions can validate that names are non-empty and phone fields contain exactly four digits. Loops can keep asking until valid input is supplied.

# Closing

Today we learned the foundation for logic:

- `&` for background execution;
- `&&` for success-dependent execution;
- `||` for failure-dependent execution;
- `;` for unconditional sequential execution;
- exit status and `$?`;
- integer, string and file expressions with `test` / `[ ... ]`;
- and a complete interactive information-collection script.

In the next class, these tests will become the conditions inside `if`, `else`, and related logic. Practise the commands rather than only watching them.

<!-- DONE-070 -->
