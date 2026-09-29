# Day-16 Bash For Bug Bounty Live Training Capsule Course — English Translation

*Translated from: `072 - Day-16 Bash For Bug Bounty Live Training Capsule Course [ Hindi ].hi-orig.srt`*
*Style: faithful edited translation; repeated live-chat checks and caption stutters are condensed.*

---

Day 16 begins with a more realistic `case` exercise, then moves from decisions to repetition. The instructor's goal is to make students assemble complete scripts rather than memorize isolated syntax.

## A city/country `case` script

The script prompts the user, shows the supported cities, reads a city name, and uses `case` to print the corresponding country. Each pattern ends with `)`, each action arm ends with `;;`, and the entire block ends with `esac`. Cities with equivalent outcomes can be combined using `|`; a final `*` arm reports invalid input. The exercise demonstrates why `case` is preferable to many repeated equality tests.

```bash
read -rp "Choose a city: " city
case "$city" in
  Tokyo)          echo Japan ;;
  London)         echo "United Kingdom" ;;
  Delhi|Mumbai)   echo India ;;
  *)              echo "Unsupported city" ;;
esac
```

Quoting the selected value and providing a default arm makes the script robust. Pattern matching is intentional—`case` patterns are shell patterns, not regular expressions.

## `while` loops

A `while` loop repeats its body as long as its condition succeeds:

```bash
count=1
while [ "$count" -le 5 ]; do
    echo "$count"
    count=$((count + 1))
done
```

The condition is checked before every iteration, so a false initial condition means zero runs. The counter must change or the loop can become infinite. The instructor demonstrates interrupting an accidental endless loop and discusses `break` for leaving a loop and `continue` for skipping to the next iteration.

Practical patterns include reading a file one line at a time (`while IFS= read -r line`), retrying while a command fails, and presenting a menu until the user chooses exit. Avoid pipelines when loop-body variable changes need to survive in the current shell, because pipeline execution may use a subshell.

## `getopts` preview/application

The class connects loops and `case` to command-line option processing. `getopts` visits options one by one; the option letter is handled by `case`, its argument is available in `OPTARG`, and `OPTIND` tracks progress. After parsing, `shift $((OPTIND - 1))` removes processed options. This is the standard foundation for scripts that accept flags such as a target, wordlist, or help option.

The key design lesson is composition: `getopts` supplies repeated input, `case` dispatches each option, and conditions validate required values. Together these constructs form a usable command-line tool.

<!-- DONE-072 -->
