# Python for Cyber Security Day 4 — Conditions, Loops aur Control Flow (Hinglish Explanation)

**Source transcript:** `transcripts/032 - Day-4 Python For Cyber Security Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Trainer in transcript:** Nitesh Singh (Defronix)
**Builds on:** Days 1–3 — variables/input, lists/indexing, dictionaries, comparison/logical operators
**Continues:** Day 5 file handling aur OS module
**Note:** Ye exact matching Hindi transcript ko context ke saath samajh kar likha gaya hai; ye literal translation nahi hai. Security examples authorized labs/defensive automation ke liye hain.

---

## 1. Day 4 ka focus

Aaj Python script ko decide aur repeat karna sikhaya jata hai:

- `if`, `elif`, `else`
- Python indentation
- `while`
- `for` and `range()`
- `break`, `continue`, `pass`

Days 1–3 ke values, containers aur Boolean operators aaj working machinery bante hain.

```text
for each host:
    if condition matches:
        record result
```

Port inventory, log filtering, URL checks aur report generation isi pattern par build ho sakte hain.

---

## 2. Python ka indentation contract

C/C++ jaisi languages braces use kar sakti hain:

```c
if (x > y) {
    do_work();
}
```

Python indentation ko block boundary banata hai:

```python
if x > y:
    print("x is larger")
print("always runs after the block")
```

- Header ke end mein colon `:`.
- Indented line block ke andar.
- Dedent hone par block end.
- Consistent spaces use karo; tabs/spaces mix na karo.

Indentation cosmetic formatting nahi; wrong indentation logic ya `IndentationError` create karegi.

---

## 3. `if`, `elif`, `else`

```python
status = "open"

if status == "open":
    print("review service")
elif status == "filtered":
    print("record limitation")
else:
    print("no action")
```

- `if` first condition.
- `elif` alternate branch.
- `else` fallback.
- First true branch execute hoti hai; later branches skip.

Input ke saath:

```python
age = int(input("Age: "))
if age >= 18:
    print("adult")
else:
    print("under 18")
```

Untrusted input cast/validate karna zaruri hai.

---

## 4. Largest of three demo

Transcript Day 3 ke `and` ko practical capstone mein use karta hai:

```python
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
```

Debugging method:

1. Each comparison separately evaluate.
2. `and` ka truth result check.
3. First true branch identify.
4. Equal values ke behavior test.

Aise hi security filter mein multiple conditions combine hoti hain:

```python
if port == 443 and service == "https":
    print("check TLS configuration")
```

---

## 5. `while` loop

```python
i = 0
while i < 10:
    print(i)
    i += 1
```

Three components:

1. Initial value.
2. Condition.
3. Body update.

`i += 1` bhool gaye to condition true reh sakti hai aur infinite loop ban sakta hai.

Counting down:

```python
i = 5
while i > 0:
    print(i)
    i -= 1
```

### 5.1 `while True`

```python
while True:
    command = input("Command: ")
    if command == "quit":
        break
```

`while True` intentionally infinite hai; safe exit/break required. Running program interrupt karne ke liye terminal par `Ctrl+C` common option hai, but program state/partial output lost ho sakta hai.

### 5.2 `while ... else`

Python mein:

```python
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("loop ended normally")
```

`else` normal condition-false termination par run hota hai; `break` se exit hone par generally nahi.

Search pattern:

```python
found = False
for item in items:
    if item == wanted:
        found = True
        break
else:
    print("not found")
```

---

## 6. `for` aur `range()`

```python
for number in range(5):
    print(number)
```

Output 0–4; stop exclusive.

General:

```python
range(start, stop, step)
```

Examples:

```python
range(0, 10, 2)  # 0, 2, 4, 6, 8
range(5, 0, -1)  # 5, 4, 3, 2, 1
```

List values directly:

```python
for port in [22, 80, 443]:
    print(port)
```

Index-based iteration:

```python
ports = [22, 80, 443]
for i in range(len(ports)):
    print(i, ports[i])
```

Modern code mein `enumerate(ports)` often clearer hai, but transcript `range(len(...))` concept demonstrate karta hai.

---

## 7. `break`, `continue`, `pass`

| Keyword | Meaning | Example |
|---|---|---|
| `break` | Loop immediately stop | First match par stop |
| `continue` | Current iteration ka rest skip | Empty/noisy line skip |
| `pass` | Do nothing placeholder | Future function/block stub |

### `break`

```python
for port in ports:
    if port == 80:
        break
    print(port)
```

Break se pehle ka code run hota hai; placement matter karta hai.

### `continue`

```python
for line in lines:
    if not line.strip():
        continue
    process(line)
```

### `pass`

```python
if feature_enabled:
    pass  # implement later
```

`pass` security control nahi; unfinished code ko production mein deploy mat karo.

---

## 8. Cybersecurity use-cases

Control flow se learner:

- host list iterate,
- allowed ports filter,
- logs mein suspicious keyword detect,
- first match par stop,
- empty/noisy records skip,
- retry loop with explicit limit
bana sakta hai.

Safe retry pattern:

```python
attempts = 0
while attempts < 3:
    result = check_authorized_lab()
    if result:
        break
    attempts += 1
```

Unlimited network loops rate-limit, service disruption ya accidental abuse create kar sakte hain. Scope, delay, timeout aur stop condition use karo.

---

## 9. Homework

Transcript tasks:

1. 0–100 mein numbers print jo 5 aur 7 dono se divisible hon.
2. Age input se voting/adult condition check.
3. Number positive ya negative identify.
4. Loop topics—nested loops, `range()` edge cases, `while...else`—independently research.

Divisibility example:

```python
for n in range(101):
    if n % 5 == 0 and n % 7 == 0:
        print(n)
```

---

## 10. Common mistakes aur corrections

1. Python block indentation ko optional samajhna.
2. Colon `:` miss karna.
3. `if` ke baad wrong dedent.
4. `while` update bhool kar infinite loop.
5. `range(stop)` ko stop-inclusive samajhna.
6. `break` aur `continue` confuse karna.
7. `pass` ko completed implementation samajhna.
8. `while True` without safe exit/run limit.
9. Unvalidated input ko comparison/cast karna.
10. Network loop mein timeout/delay/scope na rakhna.
11. `while...else` ko `if...else` jaisa samajhna.
12. Loop result/report ke source inputs record na karna.

---

## 11. Day 4 self-check questions

1. Python indentation block boundary kaise define karta hai?
2. `if`, `elif`, `else` flow explain karo.
3. Largest-of-three program mein `and` kyu required hai?
4. Infinite `while` loop ke causes aur safe escapes kya hain?
5. `while...else` kab execute hota hai?
6. `range(0, 10, 2)` ka output kya hoga aur 10 kyu nahi?
7. `for value in list` aur index-based loop compare karo.
8. `break`, `continue`, `pass` ko security-script examples ke saath explain karo.
9. Authorized network automation mein stop conditions kyu chahiye?
10. 5 aur 7 se divisible numbers ka safe loop likho.

---

## 12. Continuity

Day 4 ke baad Python scripts decide aur repeat kar sakte hain. Day 5 mein file handling, `os` module, `pip` modules aur integer-reversal algorithm se code ko real files/system context se connect kiya jayega.
