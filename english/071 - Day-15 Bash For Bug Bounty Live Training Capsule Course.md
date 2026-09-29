# Day-15 Bash For Bug Bounty Live Training Capsule Course — English Translation

*Translated from: `071 - Day-15 Bash For Bug Bounty Live Training Capsule Course [ Hindi ].hi-orig.srt`*
*Style: faithful edited translation; repeated live-chat checks and caption stutters are condensed.*

---

After revising command chains and `test`, the instructor begins Bash decision-making. Every useful script needs logic: inspect a condition, choose an action, and handle failure explicitly.

## Basic `if`

The form is `if CONDITION; then ... fi`. The semicolon (or a newline) ends the condition; `then` begins the commands to execute when its exit status is zero; `fi` closes the block. The first demonstration compares two numbers and prints a success message. Execution permission is added with `chmod`, and changing the comparison shows that a false branch produces no output when no `else` exists.

```bash
if [ 2 -gt 1 ]; then
    echo "test passed"
fi
```

Spacing is emphasized repeatedly: brackets are commands, so `[`, the operands, operator, and `]` need separate shell words.

## `if` / `else`

An `else` branch makes failure visible and lets a script choose an alternative action. The instructor modifies the numeric example to print one message for true and another for false, then applies the same pattern to files and user input. Conditions can be commands directly; a successful command selects `then`, while a failed command selects `else`.

## Multiple choices with `elif`

`elif` adds another condition without deeply nesting complete `if` blocks. Conditions are tested from top to bottom and only the first successful branch runs. A final `else` catches everything unmatched. The ordering therefore matters: put specific cases before broad ones.

```bash
if [ "$score" -ge 80 ]; then
    echo excellent
elif [ "$score" -ge 50 ]; then
    echo pass
else
    echo retry
fi
```

Quote variable expansions when an empty value or spaces are possible. For arithmetic-heavy scripts, Bash arithmetic contexts can be clearer, but the lesson keeps using `test` so its exit-status model remains visible.

## Introduction to `case`

For one value matched against many fixed patterns, `case` is cleaner than a long `elif` ladder. Syntax is `case WORD in`, followed by patterns and commands; `;;` terminates each arm and `esac` closes the statement. `*` is the default pattern. Multiple alternatives can share an arm with `pattern1|pattern2`.

The closing message is practical: use `if` for general tests and ranges; use `case` for menus, command-line choices, and recognizable string patterns.

<!-- DONE-071 -->
