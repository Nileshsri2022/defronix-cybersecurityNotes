# Python for Cyber Security Day 6 — Functions aur Exception Handling (Hinglish Explanation)

**Source transcript:** `transcripts/034 - Day-6 Python For Cyber Security Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Trainer in transcript:** Nitesh Singh (Defronix)
**Builds on:** Days 1–5 — variables, containers, operators, loops, files and `os`
**Continues:** Day 7 capstone question-paper maker
**Note:** Ye exact matching Hindi transcript ko context ke saath samajh kar likha gaya hai; ye literal translation nahi hai. Automation examples authorized lab/data ke liye hain.

---

## 1. Day 6 ka focus

Ab tak scripts mostly top-to-bottom statements the. Aaj do upgrades program ko reusable/resilient banate hain:

1. **Functions** — behavior once define, multiple places call.
2. **Exception handling** — expected runtime errors ko controlled way mein handle, user-facing program ko raw traceback se bachana.

Security tools thousands of files/hosts/URLs process kar sakte hain; ek bad input se entire run crash nahi hona chahiye.

---

## 2. Terminology: parameter vs argument

Definition:

```python
def welcome(name):
    print("Hello", name)
```

- `name` = parameter (function definition mein).
- `"Asha"` = argument (call ke time).

```python
welcome("Asha")
```

Programming languages mein concepts mostly same hote hain; syntax vary karta hai.

---

## 3. Functions

### 3.1 Define vs call

```python
def welcome():
    print("Hello")

welcome()
```

`def` block define karna execute nahi karta. Function call hone par body run hoti hai.

### 3.2 Parameters and types

```python
def show_item(item):
    print(type(item), item)

show_item("url")
show_item([80, 443])
```

Python function parameters dynamic values accept kar sakte hain, but input contract/documentation clear rakhna good practice hai.

Missing argument error:

```python
# welcome()  # if name required, TypeError
```

### 3.3 `*args`

```python
def welcome_all(*users):
    for user in users:
        print("Hello", user)

welcome_all("Asha", "Ravi", "Zoya")
```

`users` internally tuple hota hai:

```python
print(users[0])
```

### 3.4 Default parameter

```python
def profile(name, state="Rajasthan"):
    print(name, state)

profile("Asha")
profile("Asha", "Maharashtra")
```

Default omitted par use, supplied value par override. Required parameters generally default ke baad order mein carefully define karo.

### 3.5 Return

```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result)
```

Python return type declaration/`void` syntax require nahi karta. Returned value store nahi karoge to result lose ho sakta hai.

Security helper examples:

```python
def normalize_host(host):
    return host.strip().lower()
```

Function side effects and return values document karo.

---

## 4. Calculator design exercise

Transcript calculator idea deta hai:

- operation input,
- two numbers,
- separate function per operation,
- result return/store.

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

operation = input("+ or -: ")
a = float(input("First: "))
b = float(input("Second: "))

if operation == "+":
    result = add(a, b)
elif operation == "-":
    result = subtract(a, b)
else:
    result = None

print(result)
```

Invalid input/zero division ke liye exceptions/validation next section se handle karo.

---

## 5. Exception handling

Basic structure:

```python
try:
    risky_code()
except SomeError:
    handle_error()
finally:
    cleanup()
```

Flow:

1. `try` first run.
2. First exception par remaining try lines skip.
3. Matching `except` execute.
4. Clean try par except skip.
5. `finally` generally always run—cleanup/logging ke liye.

### 5.1 File example

Without handling:

```python
open("missing.txt")
```

Raw traceback and termination ho sakta hai.

Controlled:

```python
try:
    with open("missing.txt", encoding="utf-8") as f:
        data = f.read()
except FileNotFoundError:
    print("File name ya location galat hai")
```

User ko friendly message; developer logs mein technical detail.

### 5.2 Specific exception preferred

```python
try:
    number = int(input("Number: "))
except ValueError as error:
    print("Valid number enter karo")
    print(error)  # only controlled/debug context
```

Bare `except:` every exception catch kar sakta hai aur programming bugs hide kar sakta hai. Specific exceptions use karo; unexpected errors development/logging mein visible rahne do.

### 5.3 `finally`

```python
f = None
try:
    f = open("data.txt", encoding="utf-8")
    data = f.read()
finally:
    if f:
        f.close()
```

Modern preferred approach `with open(...)` hai, but `finally` cleanup principle samajhna useful hai.

### 5.4 Error object

```python
try:
    risky()
except ValueError as error:
    user_message = "Input invalid"
    developer_detail = str(error)
```

Sensitive path/password/token ko public error output mein print mat karo.

---

## 6. Resilient security automation

Scanner/log parser mein per-item error handling carefully design karo:

```python
for path in paths:
    try:
        process(path)
    except FileNotFoundError:
        record(path, "missing")
    except PermissionError:
        record(path, "permission denied")
```

One unreadable file se complete report stop nahi hoti. But blanket exception se all failures ignore nahi hone chahiye; failure count/report maintain karo.

Network tools mein:

- timeout,
- retry limit,
- rate limit,
- explicit exception types,
- stop condition
rakho.

---

## 7. Blackbox.ai tool mention

Transcript ek AI coding assistant/Blackbox.ai ka short demo mention karta hai. Comment/description ke baad generated code suggestion mil sakta hai, Tab se accept type workflow.

Safe use:

- generated code read/understand,
- secrets/codebase upload na karo,
- dependency/license/privacy check,
- tests and lint run,
- blindly execute network/destructive code nahi.

AI suggestion programmer understanding ka substitute nahi.

---

## 8. Homework aur Day 7 poll

Homework:

- functions ke argument shapes, returns aur un-taught features research,
- code/tests approved Day-6 LinkedIn post comments/Telegram channel mein share.

Day 7 finale project poll se choose hona hai. Socket/networking tool ke liye networking concepts abhi limited hain; Windows Defender/security controls bhi live offensive tool development ko block kar sakte hain. Fallback question-paper maker project selected/teased hai, jo all learned concepts revise karega.

---

## 9. Common mistakes aur technical corrections

1. Function define karke call na karna.
2. Argument/parameter confuse karna.
3. Required/default parameter order incorrect.
4. `return` value store na karna.
5. `*args` ko list samajhna—inside tuple.
6. Bare `except:` se all bugs hide karna.
7. Error message mein sensitive path/secret print karna.
8. `finally` cleanup logic incomplete rakhna.
9. File ke liye `with` use na karna.
10. Exception catch karke failure silently ignore karna.
11. AI-generated code blindly execute karna.
12. Network/socket code ko unauthorized target par test karna.

---

## 10. Day 6 self-check questions

1. Parameter aur argument mein difference kya hai?
2. Function definition aur call ka behavior compare karo.
3. `*args` inside kis type ka hota hai?
4. Default parameter ka use-case kya hai?
5. `return` value lose hone ka example do.
6. `try`, `except`, `finally` ka exact control flow explain karo.
7. Specific `FileNotFoundError` bare `except` se better kab hai?
8. User message aur developer error detail separate kyu honi chahiye?
9. File/network automation mein exception handling resilience kaise improve karti hai?
10. AI-generated code ko security context mein kaise validate karoge?
11. Socket/offensive automation ke liye written authorization kyu chahiye?

---

## 11. Continuity

Day 5 ne files/OS commands diye; Day 6 functions se reuse aur exceptions se resilience aayi. Day 7 capstone question-paper maker mein lists, dicts, loops, files, functions, exceptions aur randomness ek project mein combine honge.
