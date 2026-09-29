# Bash Day 17 — timer project and read-while loops — Explained

## Lesson reconstruction

Day 17 begins by revising Day 16: `while` repeats while a condition succeeds, and `getopts` lets a script parse short command-line options. The instructor now combines them in a practical countdown timer.

The timer accepts minutes and seconds, for example `./timer.sh -m 1 -s 30`. A `while getopts "m:s:" opt` loop reads each option; `case` stores `OPTARG` in `minutes` or `seconds`. This first loop is only for input parsing. A second loop performs the countdown while time remains. It prints the current values, sleeps one second, reduces seconds, and when seconds reach zero it borrows one minute and resets seconds. The state must change on every pass, otherwise the loop never ends. After both values reach zero, the script prints `Time's up`.

The demonstration deliberately shows why separate responsibilities help: one loop understands options, another updates time, and a final statement runs only after the countdown. Invalid or missing values need usage output. Numeric validation is important because arithmetic contexts should not receive arbitrary text.

The next topic is a **read-while loop**, a combination of `read` and `while` for processing a text file one line at a time:

```bash
while IFS= read -r line; do
    printf '%s\n' "$line"
done < "$1"
```

`read` returns success while it obtains a line, so it naturally serves as the loop condition. `IFS=` preserves leading/trailing whitespace; `-r` preserves backslashes. The redirection sends the file into the loop without repeatedly opening it. The instructor creates a sample file, passes its name to the script, and shows each line being stored in `line` and printed before the next iteration.

This pattern can do more than print: test domains, transform records, count matches, or invoke an authorized tool once per target. The filename should first be checked with `-f` and `-r`. Quote both the filename and line variable. A final line without a newline needs the extended condition `while IFS= read -r line || [[ -n $line ]]` if it must be retained.

The lesson closes the current `while` section by connecting input, loops, and practical automation: parse options, validate them, repeat predictably, and make termination visible.

## Engineering and safety notes

A robust timer normalizes seconds greater than 59, rejects negatives, traps interruption, and formats with `printf '%02d:%02d\r'`. It should use `sleep 1`, not a CPU-burning empty loop. For file processing, avoid `cat file | while read ...` when variables changed in the body must survive afterward; many shells run the pipeline loop in a subshell. Redirect into the loop instead. Static-check scripts with `bash -n` and ShellCheck, and test empty files, whitespace, backslashes, unreadable paths, and missing arguments.

## Verification checklist

- Reproduce the workflow only in an isolated lab or explicitly authorized scope.
- Validate inputs, quote paths and variables, and test failure behavior.
- Preserve source, date, command, and minimal evidence for every observation.
- Distinguish a lead from a verified finding; do not overstate impact.
- Remove secrets and personal data from notes before sharing.

## Review questions

1. What prerequisite or authorization boundary controls this workflow?
2. Which output justifies the next action, and which output is only a lead?
3. How can false positives or stale data appear?
4. What is the safest failure/cleanup behavior?
5. How would a defender prevent or detect the weakness discussed?

<!-- DONE-074 -->
