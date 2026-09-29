# Day-17 Bash For Bug Bounty Live Training Capsule Course — English Translation

*Translated from: `074 - Day-17 Bash For Bug Bounty Live Training Capsule Course [ Hindi ].hi-orig.srt`*
*Style: faithful edited translation; repeated live-chat checks and caption stutters are condensed.*

---

Day 17 revises `while` and `getopts` by building a small timer, then introduces the read-while pattern used by many automation scripts.

## Timer project with options

The script accepts minute and second values as command-line options. `getopts` runs inside a `while` loop, and `case` dispatches each option into the appropriate variable. Invalid options display usage information. The values are then validated before countdown begins.

A second loop performs the countdown. It prints the current time, sleeps for one second, decrements seconds, and when seconds reach zero it decreases minutes and resets seconds appropriately. The condition must eventually become false; otherwise the result is an infinite loop. The message `Time's up` is printed only after the countdown loop finishes.

```bash
while getopts "m:s:" opt; do
  case "$opt" in
    m) minutes=$OPTARG ;;
    s) seconds=$OPTARG ;;
    *) echo "Usage: $0 -m MINUTES -s SECONDS"; exit 2 ;;
  esac
done
```

The exercise reinforces that loops can use any command as a condition, not only bracket expressions, and that separate loops can have separate responsibilities: one parses input; another updates state.

## The read-while loop

To process a text file one record at a time, combine `while` with `read`:

```bash
while IFS= read -r line; do
    printf '%s\n' "$line"
done < "$1"
```

`read` succeeds while another line can be read, stores that line in a variable, and naturally terminates the loop at end-of-file. `IFS=` preserves leading and trailing whitespace; `-r` prevents backslashes from being treated as escapes; quoting `"$line"` prevents splitting and glob expansion. Redirecting the file into the loop is generally preferable to `cat file | while ...` when variables modified inside the loop must remain available afterward.

The instructor demonstrates passing a filename to the script, reading every line, and performing an action per line. In bug-bounty tooling the same pattern can iterate over domains, URLs, IP addresses, or wordlists. Validate that an argument was supplied and that it names a readable regular file before processing it.

<!-- DONE-074 -->
