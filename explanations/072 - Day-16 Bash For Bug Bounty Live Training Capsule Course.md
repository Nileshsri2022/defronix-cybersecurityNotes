# Day-16 Bash — `select`, `case`, `while`, and `getopts` — Explained

## Lesson architecture

Day 16 combines earlier concepts into two complete interaction styles:

```text
Interactive menu: select → case → action → break/continue
CLI options:      while → getopts → case → OPTARG
```

The `while` loop is the bridge. It repeats a condition-controlled activity; in the option parser, that condition is `getopts` itself.

---

# 1. City checker: division of responsibility

## `select` creates the menu

```bash
PS3='Choose a city: '
select city in Tokyo London 'New York'; do
    ...
done
```

Bash prints numbered options and reads a number. It stores:

- selected option text in `city`;
- raw user response in `REPLY`.

If the response is invalid, `city` is empty. `select` repeats until the body executes `break`, receives end-of-input, or the process is interrupted.

## `case` maps a value

```bash
case $city in
    Tokyo) country=Japan ;;
    London) country='United Kingdom' ;;
    'New York') country='United States' ;;
    '') echo "Invalid choice: $REPLY" >&2; continue ;;
esac
```

Within `case`, quoting the expansion is good consistent style, although `case WORD in` does not perform pathname expansion on the expanded word in the same way an ordinary command argument would. Patterns containing literal spaces must be quoted or escaped.

## Multiple patterns, one action

```bash
Dubai|'Abu Dhabi') country='United Arab Emirates' ;;
Bangalore|Mumbai) country=India ;;
```

The vertical bar means alternative patterns, not a pipeline in this syntactic position.

## Make invalid behavior explicit

A robust menu:

```bash
while true; do
    select city in Tokyo London 'New York' Dubai Quit; do
        case $city in
            Tokyo) country=Japan ;;
            London) country='United Kingdom' ;;
            'New York') country='United States' ;;
            Dubai) country='United Arab Emirates' ;;
            Quit) exit 0 ;;
            '') echo "Choose one of the listed numbers." >&2; break ;;
        esac
        printf '%s is in %s.\n' "$city" "$country"
        exit 0
    done
done
```

Understand which construct each `break` leaves. An unnumbered `break` exits the innermost enclosing loop only.

---

# 2. `while` evaluates a command repeatedly

```bash
while condition_command; do
    body
done
```

Execution sequence:

```text
run condition
├─ status 0     → run body → return to condition
└─ status non-0 → leave loop
```

A loop can execute zero times if the first condition is false.

## Counter loop

```bash
num=15
while (( num > 10 )); do
    printf '%d\n' "$num"
    (( num-- ))
done
```

A subtle Bash trap: `(( expression ))` returns failure when the expression evaluates to zero. Under `set -e`, standalone `((num--))` can unexpectedly terminate when its old value is zero. Assignment form avoids status-dependent surprises:

```bash
num=$((num - 1))
```

For this lesson's positive range, either works, but understanding status remains important.

## Infinite-loop diagnosis

The original loop never modifies `num`:

```bash
while [ "$num" -gt 10 ]; do
    echo "$num"
done
```

Ask three questions:

1. Which data determines the condition?
2. Where can that data change?
3. Is every iteration guaranteed to make progress toward termination?

Not all loops should terminate naturally—servers and event loops may be long-running—but they still need blocking I/O, delays, signal handling, and resource control.

## `break` and `continue`

```bash
while condition; do
    if fatal_condition; then
        break       # leave loop
    fi
    if skip_condition; then
        continue    # begin next condition check
    fi
    normal_work
done
```

Be careful that `continue` does not skip the state update required for termination.

---

# 3. `getopts` is stateful

`getopts` parses short options from the script's positional parameters. Bash tracks parsing position in `OPTIND`, initially 1 for a fresh shell/script invocation.

```bash
while getopts ':f:c:h' opt; do
    ...
done
shift "$((OPTIND - 1))"
```

After `shift`, `$@` contains remaining non-option operands.

## Option specification grammar

For `:f:c:h`:

| Part | Meaning |
|---|---|
| leading `:` | script handles parser errors itself |
| `f:` | `-f` requires an argument |
| `c:` | `-c` requires an argument |
| `h` | `-h` takes no argument |

It accepts forms such as:

```bash
./tool -f 98
./tool -f98
./tool -h
```

`getopts` is for short options. It does not natively parse GNU-style `--fahrenheit=98` long options.

## Parser variables

| Variable | Purpose |
|---|---|
| chosen name (`opt`) | current option letter |
| `OPTARG` | current option's argument or offending character in errors |
| `OPTIND` | index of next positional parameter to parse |

If a shell function calls `getopts` repeatedly, reset/localize `OPTIND` appropriately; its state persists in the shell environment.

## Correct error handling

```bash
usage() {
    printf 'Usage: %s (-f FAHRENHEIT | -c CELSIUS)\n' "$0" >&2
}

mode=
value=

while getopts ':f:c:h' opt; do
    case $opt in
        f) mode=f; value=$OPTARG ;;
        c) mode=c; value=$OPTARG ;;
        h) usage; exit 0 ;;
        :) printf 'Option -%s requires an argument.\n' "$OPTARG" >&2
           usage; exit 2 ;;
        \?) printf 'Unknown option: -%s\n' "$OPTARG" >&2
            usage; exit 2 ;;
    esac
done
shift "$((OPTIND - 1))"

if [[ -z $mode || $# -ne 0 ]]; then
    usage
    exit 2
fi
```

A leading colon in the option string causes missing arguments to produce `opt=:` and unknown options to produce `opt=?`, allowing custom messages.

---

# 4. Safer temperature conversion

The classroom expression interpolates `OPTARG` directly into code passed to `bc`. Reject malformed input first:

```bash
is_number() {
    [[ $1 =~ ^[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)$ ]]
}

if ! is_number "$value"; then
    printf 'Not a number: %s\n' "$value" >&2
    exit 2
fi
```

Then calculate:

```bash
case $mode in
    f)
        result=$(bc -l <<<"scale=2; ($value - 32) * 5 / 9") || exit 1
        printf '%s°F = %s°C\n' "$value" "$result"
        ;;
    c)
        result=$(bc -l <<<"scale=2; ($value * 9 / 5) + 32") || exit 1
        printf '%s°C = %s°F\n' "$value" "$result"
        ;;
esac
```

Why validate?

- malformed syntax causes `bc` errors;
- untrusted expression fragments may alter the calculation language;
- the script should distinguish usage errors from calculation failures.

## Exactly one mode

The parser above lets a later `-f` overwrite an earlier `-c`. If modes must be mutually exclusive, reject repetition/conflict:

```bash
if [[ -n $mode ]]; then
    echo 'Choose exactly one conversion mode.' >&2
    exit 2
fi
```

Set this before assigning each mode.

## Formula checks

Known reference points:

| Celsius | Fahrenheit |
|---:|---:|
| 0 | 32 |
| 100 | 212 |
| -40 | -40 |

Use these as tests. Floating-point formatting/rounding rules should be documented.

---

# 5. Applying this to security tooling

The same parser structure can make an authorized reconnaissance wrapper:

```bash
while getopts ':t:o:w:h' opt; do
    case $opt in
        t) target=$OPTARG ;;
        o) output=$OPTARG ;;
        w) wordlist=$OPTARG ;;
        h) usage; exit 0 ;;
        :) usage_error "-$OPTARG needs a value" ;;
        \?) usage_error "unknown option -$OPTARG" ;;
    esac
done
```

But parsing is only the start. Validate:

- target is explicitly in authorized scope;
- output path is writable and not dangerous;
- wordlist exists and is readable;
- conflicting modes are rejected;
- values are passed as quoted arguments, not evaluated as shell code.

Never build a command string and `eval` it:

```bash
# unsafe
cmd="scanner $target"
eval "$cmd"

# safe argument array
cmd=(scanner --target "$target")
"${cmd[@]}"
```

---

# 6. Testing matrix

For the city script, test:

- every menu number;
- zero, negative, too-large, blank, and text responses;
- multi-word cities;
- quit behavior.

For the converter, test:

- `-f 32`, `-c 0`, and `-f -40`;
- decimals;
- missing option argument;
- unknown option;
- no options;
- both modes;
- extra positional operands;
- letters and expression-like input;
- missing `bc` dependency.

Syntax/static checks:

```bash
bash -n converter.sh
shellcheck converter.sh
```

Execution tracing when needed:

```bash
bash -x converter.sh -f 98
```

---

# Cheat card

```bash
while condition; do
    ...
done

while true; do
    ...
    break
 done

while getopts ':a:b:h' opt; do
    case $opt in
        a) a_value=$OPTARG ;;
        b) b_value=$OPTARG ;;
        h) usage; exit 0 ;;
        :) echo "missing argument" >&2; exit 2 ;;
        \?) echo "unknown option" >&2; exit 2 ;;
    esac
done
shift "$((OPTIND - 1))"
```

## Review questions

1. Why can a `while` loop execute zero times?
2. What makes the first numeric example infinite?
3. What is the difference between `break` and `continue`?
4. Why is `getopts` normally called from a loop?
5. What does a colon after an option letter mean?
6. Where is an option's argument stored?
7. What remains in `$@` after shifting by `OPTIND - 1`?
8. Why must values be validated before placing them in a `bc` expression?

<!-- DONE-072 -->
