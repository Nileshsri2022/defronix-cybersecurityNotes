# Day-14 Bash For Bug Bounty Live Training Capsule Course — English Translation

*Translated from: `070 - Day-14 Bash For Bug Bounty Live Training Capsule Course [ Hindi ].hi-orig.srt`*
*Style: faithful edited translation; repeated live-chat checks and caption stutters are condensed.*

---

The class resumes after Day 13's input mechanisms and assignments. Before beginning full `if` logic, the instructor introduces command chains and the operators that decide when each command runs.

## List operators

An ampersand (`command &`) starts a command asynchronously in the background, returning control to the shell without waiting. A semicolon (`cmd1; cmd2`) runs commands sequentially regardless of whether the first succeeds. The AND operator (`cmd1 && cmd2`) runs the second command only when the first exits successfully. The OR operator (`cmd1 || cmd2`) runs the second only when the first fails. These rules depend on exit status: zero means success and non-zero means failure.

The live demonstrations deliberately combine successful and failing commands so students can see which second command executes. The instructor then mixes operators into small chains. The central lesson is not merely syntax: list operators already provide elementary control flow and are useful for setup steps, fallbacks, and scripts that should stop after a failed prerequisite.

```bash
mkdir results && cd results       # enter only if creation succeeded
ping -c 1 host || echo "offline"  # fallback on failure
long_scan &                       # continue without waiting
printf 'one
'; printf 'two
'    # always run both
```

## The `test` command

`test` evaluates an expression and reports the answer through its exit status. It normally prints nothing. Check its result with `echo $?`, combine it with `&&`/`||`, or place the expression in an `if` statement. The bracket form `[ expression ]` is the same basic operation, and spaces around `[` and `]` are mandatory.

The lesson demonstrates numeric comparisons (`-eq`, `-ne`, `-gt`, `-ge`, `-lt`, `-le`), string checks (`=`, `!=`, `-z`, `-n`), and file checks such as `-e` (exists), `-f` (regular file), `-d` (directory), `-r`, `-w`, and `-x`. Numeric operators should be used for numbers; lexical string operators are not substitutes.

```bash
[ 2 -gt 1 ] && echo "true"
[ -f scope.txt ] || echo "scope file missing"
test -x recon.sh; echo "$?"
```

The class closes by connecting these predicates to the next lesson: `if` does not invent a new kind of condition—it acts on the success or failure of commands such as `test`.

<!-- DONE-070 -->
