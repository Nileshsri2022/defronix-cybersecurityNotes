# Day-16 Bash For Bug Bounty Live Training Capsule Course [Hindi] — English Translation

*Translated from: `072 - Day-16 Bash For Bug Bounty Live Training Capsule Course [ Hindi ].hi-orig.srt`*
*Style: detailed edited translation. Repeated chat exchanges and caption duplication are consolidated; technical clarifications are marked [TN].*

---

[music] Hello, good evening everyone, and welcome to Day 16 of this Bash Mastery course. Confirm that my voice is audible and then we will move ahead.

In the previous class we studied `if` and `case`. A `case` statement is not a complete replacement for `if`, but there are many situations where it is easier to manage than writing many `if`/`elif` branches. It checks one value against multiple cases. Before today's new topic, I will build one more practical `case` example so the idea becomes clear.

After that we will study the **`while` loop** and an interesting command called **`getopts`**. You see command-line options in real tools every day. Today you will learn how to provide options in your own scripts and perform actions based on them.

# Project 1 — city and country checker

We will create `city-checker.sh`. The script has a list of cities. The user chooses one, and the program prints its country.

A user does not know which city names our script supports, so first offer a numbered list with `select`:

```bash
#!/bin/bash

PS3="Choose a city: "
select city in Tokyo London "New York" Dubai "Abu Dhabi" Paris Bangalore Mumbai Rome Nairobi Berlin; do
    ...
done
```

The semicolon ends the `select` option list. `do` begins the loop body and `done` closes it. Multi-word names such as `New York` and `Abu Dhabi` must be quoted so each remains one option.

Inside `select`, use `case` to map the selected city:

```bash
case "$city" in
    Tokyo)
        country="Japan"
        ;;
    London)
        country="United Kingdom"
        ;;
    "New York")
        country="United States"
        ;;
    Dubai|"Abu Dhabi")
        country="United Arab Emirates"
        ;;
    Paris)
        country="France"
        ;;
    Bangalore|Mumbai)
        country="India"
        ;;
    Rome)
        country="Italy"
        ;;
    Nairobi)
        country="Kenya"
        ;;
    Berlin)
        country="Germany"
        ;;
    *)
        echo "Invalid selection"
        continue
        ;;
esac
```

Then print the result and leave the `select` loop:

```bash
echo "$city is in $country"
break
```

The value is written as `"$city"`: `$` expands the variable and double quotes preserve spaces. With many fixed values, `case` is far clearer than repeating `if`, `elif`, `elif` for every city.

Two cities can share one country branch by separating patterns with `|`, as in `Dubai|"Abu Dhabi")`. `continue` returns to the menu after invalid input; `break` exits after a valid result.

The complete shape is:

```bash
select city in ...; do
    case "$city" in
        ...
    esac
    echo "$city is in $country"
    break
done
```

This combines two earlier lessons: `select` handles a numbered menu, while `case` dispatches the chosen value.

# The `while` loop

A `while` loop runs a set of commands repeatedly **while a condition remains true**. When the condition is no longer true, the loop ends and the shell continues with the command after `done`.

Syntax:

```bash
while CONDITION; do
    commands
done
```

Like `if`, the condition can be any command. Bash repeats the body while that command returns exit status zero.

## First example and the infinite-loop problem

Create a script that asks for a number:

```bash
#!/bin/bash

read -p "Enter your number: " num

while [ "$num" -gt 10 ]; do
    echo "$num"
done
```

Suppose the user enters 15. The condition is true, so the script prints 15. Then it checks again—but `num` is still 15. Nothing in the loop changes it. The condition remains true forever, producing:

```text
15
15
15
...
```

This is an **infinite loop**. Stop it with `Ctrl-C`. An uncontrolled loop can consume CPU, fill logs, or make a system unresponsive.

To make progress, update the state used by the condition:

```bash
while [ "$num" -gt 10 ]; do
    echo "$num"
    num=$((num - 1))
done
```

For input 15, it prints 15 through 11. After decrementing to 10, `[ 10 -gt 10 ]` is false and the loop ends.

The general rule is:

1. initialize a value;
2. test it;
3. perform the body;
4. change something that can eventually make the test false.

Not every `while` loop uses a numeric counter. The condition could be `read`, a network check, process status, or another command. But you must understand what ends it.

## Intentional infinite loop

Sometimes repetition is deliberate:

```bash
while true; do
    command
    sleep 5
done
```

`true` always returns success. Such a loop needs an internal `break`, a signal, or external service supervision. Always include a delay when polling; otherwise it may spin as fast as the CPU allows.

# Why command-line options matter

Look at familiar commands:

```bash
ls
ls -l
ls -a
ls -la
```

The command is the same, but options change its behavior. `-l` requests a long listing and `-a` includes hidden entries. Tools such as Nmap also accept options and option arguments.

If you write your own tool, you may want users to run something like:

```bash
./converter.sh -f 98
./converter.sh -c 37
```

One option means “interpret this value as Fahrenheit,” and another means “interpret it as Celsius.” Bash provides `getopts` for parsing short options.

# `getopts`

Basic structure:

```bash
while getopts "f:c:" opt; do
    case "$opt" in
        f)
            ...
            ;;
        c)
            ...
            ;;
        *)
            ...
            ;;
    esac
done
```

Why put `getopts` inside `while`? `getopts` processes one option on each successful call. The loop calls it repeatedly until no options remain.

The option specification is `f:c:`. Each letter is an accepted option. A colon after a letter means that option requires an argument:

- `f:` accepts `-f VALUE`;
- `c:` accepts `-c VALUE`.

On each iteration:

- the option letter is stored in the variable named after `getopts`—here, `opt`;
- its argument is stored in the special variable `OPTARG`.

`opt` is an ordinary variable name chosen by the script author. `OPTARG` is supplied by Bash for the current option argument.

# Project 2 — temperature converter

The class builds a converter with two modes:

- `-f VALUE`: convert Fahrenheit to Celsius;
- `-c VALUE`: convert Celsius to Fahrenheit.

```bash
#!/bin/bash

while getopts "f:c:" opt; do
    case "$opt" in
        f)
            result=$(echo "scale=2; ($OPTARG - 32) * 5 / 9" | bc)
            echo "$OPTARG°F = $result°C"
            ;;
        c)
            result=$(echo "scale=2; ($OPTARG * 9 / 5) + 32" | bc)
            echo "$OPTARG°C = $result°F"
            ;;
        *)
            echo "Usage: $0 -f FAHRENHEIT | -c CELSIUS" >&2
            exit 2
            ;;
    esac
done
```

The formulas are:

```text
C = (F - 32) × 5 / 9
F = C × 9 / 5 + 32
```

Bash integer arithmetic cannot conveniently preserve decimal results, so the demonstration pipes the expression to `bc`. `scale=2` requests two decimal places.

Example use:

```bash
./converter.sh -f 98
./converter.sh -c 37
```

For `-f 98`, `getopts` stores `f` in `opt` and `98` in `OPTARG`; the `f)` case runs. With `-c 37`, the `c)` branch runs instead.

[TN: The input should be validated before embedding it in a `bc` expression. The detailed explanation supplies a safer version.]

## Missing options and help

A script should not silently do nothing when invoked without options. After parsing, detect that case or provide a help option. A more complete option specification may be:

```bash
while getopts ":f:c:h" opt; do
```

A leading colon requests silent error handling so the script can distinguish unknown options (`?`) from missing arguments (`:`). `h` needs no argument because it has no following colon.

# How `while`, `getopts`, and `case` cooperate

This example is important because three constructs each have one job:

```text
while   → repeatedly request the next option
getopts → parse one option and its argument
case    → choose the action for that option letter
```

This is the basis of many practical Bash command-line tools. Later you can add target files, output paths, modes, verbosity, and help text in exactly this pattern.

# Closing

Today we:

- combined `select` and `case` in a city/country menu;
- learned that `while` repeats while its condition succeeds;
- created and corrected an accidental infinite loop;
- explained why the loop state must change;
- introduced options and option arguments;
- used `getopts`, `OPTARG`, and `case`;
- built a Celsius/Fahrenheit converter with `bc`.

Practise by adding a help option, rejecting invalid numeric input, and making the city menu return cleanly after invalid selections.

<!-- DONE-072 -->
