# 011 — Kali Linux Free Capsule Course — Day 11

**Source transcript:** `transcripts/011 - Kali Linux Free Capsule Course - Day 11 [ Hindi ].hi-orig.srt`
**Topic:** The `vi` / `vim` editor
**Type:** Verbatim English translation of the spoken Hindi/Hinglish session

> **Note on this transcript:** captions are heavily garbled in places (`भीम`/`बम`/`विम` = `vim`, `वे आई` = `vi`, `लिरिक्स`/`लाइनेक्स`/`नेक्स` = "Linux", `शब्द` = "word" (the `w` key), `क्यूट`/`फिट`/`लिक्विड`/`वीट` = "quit", `कलम`/`कॉलर`/`कोलोन` = "colon", `अरा` = "arrow", `कर्सर`/`कसार`/`कासल`/`करसन`/`कसूर`/`हेक्टर` = "cursor", `एस्केप`/`एस्केलेशन` = "Escape", `डाटा कमांड मोड` = "command mode", `परिसर` = "complex", `ईटीसी` = "etc."). The intended technical term has been restored where unambiguous.

---

[Music] Hello everyone, good evening to you, welcome to the free capsule course. Confirm [the audio]; tell me in the chat. Okay, thank you, Prince.

So tell me this once: whatever I have taught in the last class, up to now, up to Day [10] — whoever has done however much — **did everyone understand? Does anyone have a doubt?** Okay.

So today my topic will be [the `vi`/`vim` editor], which basically [people] call [that]. The second topic will be the **`locate` command**; I'll try, I will deliver both.

---

## Why `vim` matters

So the `vim` command — the `vim` command is a **very, very important command**. Every single Linux admin, any Linux user at all, **should definitely know it** — because **by default, in any Linux machine of yours, the `vi` editor, as it's called, is definitely there**; you will get to see it.

**If you are not familiar with it** — so that... what are you doing, you are doing your attack on some machine, and what will happen: **apart from the `vi` editor, you found no other tool**, and you don't know how to use it — **then you can face challenges.** And if you [do] know how to use it, then you can be in quite a good position if you find it there.

So [let's] start. So please, [let's begin] on time, [talking] about the thing we are going to learn, which will be our topic: **this editor.**

---

## What `vi` is used for

We use it for:
- **Opening a file**
- **Editing** it
- Or **creating a new file**

### The operating modes

It has some **operating modes**. Basically it has many operating modes, but basically it has **four operating modes**, which I am going to tell you about. Which four operators — the ones we call [these]:

| Mode | What you can do |
|---|---|
| **Command mode** | Create or open any file; navigation, cut/copy/paste, delete |
| **Insert mode** | Actually type text |
| **Ex / Last-line mode** | Save, quit, search, and other more complex operations |
| **Visual mode** | Select text, perform text manipulation, highlight |

After this, what can you do — through **command mode** you will create or open any file, etc. Okay, [and the last-line mode is for] **other more complex operations**; okay, you'll come to know.

So I will tell you: "now we have come into this mode and are working," "we are working in this mode," so you will come to know.

And **visual mode** — what is your work in it: you do **text manipulation on the selected [text]**, you **highlight** [it].

So basically these were the four modes. Now what I do — one by one, let me explain to you how this works, how the `vim` command works.

---

## Part 1 — Command mode is the default

So, the `vi` editor: look, **whenever we open any file, whenever we [open] any file, the `vi` editor by default opens in COMMAND MODE.**

For example, what do I do — I do `vim`, and what did I do: opened a file:

```bash
vim www.txt
```

A file is open by that name. **This of yours is command mode.**

---

## Part 2 — Insert mode

If I have to add anything inside it, do any **write operation** — for example, I have to write any data inside it, or do any work at all; it's a new file, [and] I have to write inside it — then what will I have to do?

**For this I will have to go into INSERT MODE.**

### Entering insert mode

And how do you go into insert mode? What you will do: on your machine you will **simply press `i`** — simply `i`, **without Caps Lock on.**

Simply, as I pressed `i` — now look, look below, look carefully at the very bottom: here, what happened — you would be seeing in highlight, **`-- INSERT --`** has come. Meaning **you can now do writing work in it**; you can write.

---

## Part 3 — Saving and quitting

So look, at the start, what did I do first — **to [go] to the command [line], what will you have to do: simply press Shift with the colon.**

As you do **Shift + `:`**, here it gets highlighted, in the bottom-left corner. And after that what do you have to write — after that you have to do **`w`** (**write**), because you have done a write operation. Then you have to do **`q`** (**quit**).

Because, meaning, what did I do — I added that data inside it.

So how did I do this? **Simply pressed `:`, after that `wq`** — here, what I have to do: **save (write) and quit.**

```
:w     write (save)
:q     quit
:wq    write and quit
:q!    quit WITHOUT saving (force)
:wq!   force write and quit
```

---

## Part 4 — Moving the cursor

Okay, so on the `h`, on the `h`, my cursor is — you would be seeing here, the one that was highlighting in white colour.

Now what do I have to do — now what I want is: **if I want to make my cursor move**, then simply what will I do — one by one, I will keep pressing my **arrows: Up, Down arrow, Left, Right arrow.**

Now, one way is this. **But if your file is very large, then you will have a problem** with this way.

### Jumping to the end of a line — `Shift + A`

There is another way. For example, what do I have to do — **I have to move my cursor directly straight to the END** [of the line]. What do I have to do — I have to move it to the end, and from there I have to do writing.

So how will I do it? My cursor is right now here, at the starting, on the [first character]. So **simply what you have to do: press Shift with `a`** — which we call **capital `A`.**

Look, my cursor came directly to the last. Let me show you again; let me tell you once more.

> **And notice one more thing:** as soon as you press Shift with `A`, **it goes into INSERT MODE** — because what are you doing: after [moving to the end] you have to add some content, and to bring [the cursor] there directly you press Shift+A; then you'll go to the [end of the] line, and after that you [can type]; then you are in insert mode.

### Inserting at the start of a line — `Shift + I`

Now what do I have to do: my cursor is here — where is my cursor? On the `h`, at the starting.

Now, what do I have to do: **I want to write right from here, from the starting itself.** But what — you [just] need to write; **simply what will you do: you have to go directly into insert mode.**

So what you [do] — you will press **`I`** [capital], and you will start writing here.

### Appending after the cursor — `a`

Like, now — can I add anything in the middle of this? You would be getting to see: where was it — [the cursor] was [here].

And let me [set the] mode again — on the `h`, on the `h` I can [put the cursor]. Now what did I do: as I pressed **`a`**, then [the cursor] came here; now the cursor came and **from after the `h` I can start writing.**

After the `h`, I could [write] — what did I want to write after the `h`: "hello". "Hello, Mister" — I don't want to write [that]. Okay, so this is "hello". Now I did this.

### Summary of these

So this thing — let me tell you what work I did. What I did: one, I pressed [`A`] and [it moved to the] end of the line, the text from the cursor [to the end].

> I remember the **pronunciation** for you, that is why I am doing a bit of hard work for you — for making notes; otherwise, simply, if I tell you, you'd have to make them yourself. So just make notes of this, then you'll have come to know.

Now what do I have to do — now what I do: **if I want to start writing from before the current cursor** — the current [position]. Just now what I had done, I started after the `h`; **I want to write before this.** Before this, what I want to [write is] "hello", "hello". Okay.

So, right now I was simply pressing **`i`**, which you already know.

| Key | Action | Result |
|---|---|---|
| `i` | insert | write **before** the cursor |
| `a` | append | write **after** the cursor |
| `I` (Shift+i) | Insert at line start | jump to **beginning of line** + insert |
| `A` (Shift+a) | Append at line end | jump to **end of line** + insert |

---

## Part 5 — Opening new lines

Now, for example, what did I say: if [the cursor] is in a particular line — which line is my cursor in? My "hello" line; my cursor is in this line, where "hello" is.

**Now what I want is that I want to enter my text in the NEXT line after this** — in my [new] line I want to enter text. How will I do that?

**Simply what will you press — [`o`].** So simply, as [you press it], then it did this: **it created a new line, an empty line, below this**, and there you can write your text.

After that, what do I want to take — "I have"... I want to add inside this "hello world", I wanted to add some text inside it.

For that, what do you have to do — **you will have to press Shift with `o`**. As soon as you press Shift with `o` — one minute — what you will have to do: **press Shift with `O`.**

[It] adds [a line] for you, to write down — **if you want to add a line ABOVE where your cursor is**, then what will you have to do there: you will only have to [press] **Shift + `o`**.

So there I can write; inside it I can write anything at all — added anything. Okay.

| Key | Action |
|---|---|
| `o` | open a new line **below** and insert |
| `O` (Shift+o) | open a new line **above** and insert |

It is taking quite a lot of time in this. What does this mean — you write this in your own words.

Next I told: Shift plus `O`.

> **But all this work — in which [mode] is it working? In COMMAND MODE.** All of them — up to now, like this Shift+A, [`a`], [`o`], Shift+[`O`] — all these things will work [from command mode].

---

## Part 6 — Deleting characters

So now let's learn: in the editor, how can we **replace and delete**?

### `x` — delete the character under the cursor

Whichever character we want to delete — the useless [text] that I added: I went here; here it is; my cursor is above [it]. Now I want to delete this character, so what will I do?

**Simply, I will press `x`** — normal `x`, **simply press `x`.**

Look, as [I] pressed, the character on which the cursor was, [that] character is getting deleted. Again, press `x` — it went from over the `i`; press `x` [over the] `k`; press `x`. So in this, what did it do — **it deleted that character on which the cursor was.**

### `X` — delete the character before the cursor

**If we want that the character BEFORE the cursor gets deleted**, then how will we do it? Simply what you have to do — [press capital `X`]. Leaving that one aside, **the character before it is what gets deleted**; it deleted it.

### `u` — undo

Now one more thing: **if you have to undo** — undo, you should know, [means to restore] as it was before.

**To undo, simply what will you press — [`u`].** So you would have come to know.

| Key | Action |
|---|---|
| `x` | delete the character **under** the cursor |
| `X` | delete the character **before** the cursor |
| `u` | **undo** |

---

## Part 7 — Replacing a character with `r`

Let me tell you one more thing, yaar. What I did — I told [about] `x`; what does it mean — write it in your own language.

**Normal `r`** means: **press `r` and whatever keyword/character you want to add with it, in place of that character** — you can write that.

Now I did [`r`] `$` — now this got added. And look, **I did not even need to go into insert mode.**

---

## Part 8 — Cut, copy and paste

Again, if I show you — for example, I [have] "hello", [Music] "benefits". Okay.

So what do I do — what do I have to do: **if I have to cut and paste** — meaning, this [text], paste it where the cursor is; so it will become like that. **And for paste, simply what to press** — what was it, undo; let me do [it] again; after that, then what did it do — **it pasted it.** Cut and paste.

So what did I tell — the thing I just told: one, I told you this; the work is **replace**, the work of replacing.

And what I told after that — **if you have to cut and paste, then what you have to do: press `x` and `p`** together; so this will [do it].

### `dd` — cut a whole line

**If I want to cut that line** — I want to cut it; if I want to cut the whole line — then **simply I will press two times**; two times what will I press — **`dd`.**

There, this line will be cut. And where I have to paste it — where to paste; for example, what do I have to do — I have to paste it here, here after "benefits".

**So simply I went here and simply press `p`** — simply press `p` for **paste**; and it pasted it.

So in this, what do you say — you pasted it. Like, what do I have to do — [do it] again like that: "I am delivering this training for the [next] test report", paste. Okay, you'll have to paste. **Copy and paste is done like this.**

### Cutting multiple lines — `2dd`

If you have to do one thing — for example, **you have to cut both these lines at once**; for example, you have to cut both of these at once. So what will you do?

Where the cursor is — one is that line, [and] the second, what you want [is] the line below it, because [it takes] from where the cursor is.

For example, what I [want] is to cut two lines, so **I will simply press [`2`]**; pressed [`2`], which is the number; **after that `d` and `d`.**

In this, what it did: where your cursor is, one, it cut that line; along with it, `2` was written, so **the one line below it — it cut that too.** Again let me undo; I pressed [`u`].

So just now what I told you: for example, if you have to cut two lines, then simply you [press] `2` first — **`2dd` will do two lines.**

| Keys | Action |
|---|---|
| `dd` | cut (delete) the **whole line** |
| `2dd` | cut **2 lines** |
| `p` | **paste** |
| `xp` | swap/transpose — cut a character and paste it |

---

## Part 9 — Moving word by word

**If you have to move** — if you have to move word by word, **jump** [by words].

For example, right now what am I doing — right now, "hello", after that **I am moving one character** [at a time]. **But if I have to move word by word, have to jump** — for that, simply what do I have to do?

**Press `w`.** Look, now I am moving to the next word, word by word. **Pressing `w` [moves] in the forward direction.**

**If you have to move in the BACKWARD direction, word by word**, then **simply press `b`** — simply press `b`. Look, word by word, you will be able to move.

| Key | Action |
|---|---|
| `w` | jump **forward** one word |
| `b` | jump **backward** one word |

---

## Part 10 — Deleting words

**If you have to perform a delete operation** — if you have to delete some word:

For example, if I have to delete this word, then simply what you have to do: to delete, **`d` means delete, `w` for word** — I deleted it.

```
dw      delete one word
2dw     delete two words
3dw     delete three words
```

**If I have to delete 2 words** — for example, the two words below, you have to delete them — [press] two [`2dw`]; it will be done. **To delete three words**, [`3dw`] — deleted it.

So what did I tell you: one, I just told about simply moving [with `w`/`b`].

**`2dw`** — its meaning is I want to delete two words at once. If I did **`3dw`** — what does this mean: **three words at once**, I am getting them deleted.

---

## Part 11 — Saving and quitting, again

And let me tell [you] actively: **if what you have to do** — right now, you are already in **Escape mode** [command mode].

**If you simply have to exit** from this machine — but you only have to **save**; you only have to do the Ctrl+S sort of work, only have to write — then what you have to do: **press Shift with the colon**, which you will get to see in the left corner; after that **simply `w`**, enter. So it **saved** it.

**If you want to quit without saving**, you can do that too. But before that, what do I want to show you...

**If you have to [quit] without [saving]**, then simply — look, you will be able to **quit without [saving]**. **If you have to force-quit, then simply [`q!`]**, and this will quit with Escape.

---

## Part 12 — Save As (renaming while saving)

Now, what you have to do — what is the file's name? It's `testvim.txt`.

Now what I want to do: **when I have written a lot of data in my file, I want that now — it occurred to me — I want to change its name.** What will I do? Understand it as: **I will move it.**

No — **you can do it right from here.** How can you do it? **Simply press [`:`], after that you do `w`; when you write, then, giving a space, you can give the file's name.**

```
:w newname.txt
```

For example, I keep the name [as something] — it changed it.

If I quit and show you — let me quit and show you; if I show you `ls`, here you will get to see it. Okay, okay, **modified** — modified. [It keeps the original and writes] the location.

### The shortcut: `ZZ`

**If you don't want to get into this Shift business, then directly what can you do** — you can save and exit. So how will you do it? **Simply you will press [`ZZ`].**

What does this mean — what does `:w` mean, that you would know; I have told it now. After that, [what] `:q` means — that too I have told you; write it down now.

---

## Part 13 — Searching in `vi`

After that, what do you have to do — what had I told: [`:`]; after that I told you, now press [something]. **If you have to do searching, how will you do it?**

Okay, **you will search like [`/keyword`]** — the next keyword it searched, wherever [it is] in the file.

**If you have to go onto [the next one], then simply press `n`** — simply press `n`; you have to press `n`, simply.

**If you have to search BOTTOM TO TOP** — if you have to search bottom to top, then simply what will you do: **the question mark `?`**, after that what will you write, the [keyword]. This will search bottom to top.

**If [you want to go] to the next [match], then simply press [`n`].**

| Key | Action |
|---|---|
| `/word` | search **forward** (top to bottom) |
| `?word` | search **backward** (bottom to top) |
| `n` | **next** match |
| `N` | **previous** match |

---

## Part 14 — Reading in output from files and commands

**If you [want to] search any other file's output, or any other command's output — I want to [insert] it inside this.** How will you do it?

**Simply, what will you do** — what will you do: you will **redirect** this, add it inside this; you will do it like that.

**The second option:** if you want to save **any command's output** directly inside this, then you can do that too. For that what will you have to do — **first you will have to press [`:r !`].**

For example, we have a command with us, `lsblk`; there is a command. So its output — this, here you get to see it — **the `lsblk` command's output you get to see here.**

```
:r filename        read a FILE into the current buffer
:r !command        read a COMMAND's output into the buffer
```

If you [want] one file where you have opened this file — so this you came to know, the `lsblk` command.

If I show you again — do it with **Shift**, after that what you have to do is use **`r`**, do a space, [and] the **exclamation mark `!`**. Like, now which was the second command of mine — I have one more command whose [output] I can save; for example, `ls -l`.

---

## Part 15 — Visual mode

This was our `vim` command. **If I want, I can tell you about it** — but this is enough for you, because **about this you can study as much as you want**; there is a very great deal to study, because it's a very big command. **If you want, you could spend the next half hour on it** too.

**So as a beginner, this much is enough for you**, because otherwise you will get bored, because there are so many things.

Because there is **visual mode** — yes, let me tell you about visual mode, how it works.

### Character-wise selection — `v`

**If you have to do highlighting work** — like I was saying, **if you have to highlight any word, how will you do it?**

So what you want to do — **to go into [visual] mode, you will simply press `v` first.** As you press [`v`], it came at the bottom.

**If you want to select character by character**, then what will you do — simply, from the keyboard you move forward. Look — all these arrows, the Up, Down, Left, Right arrow keys, right — **through those you go into visual mode and keep highlighting this; you keep selecting it yourself.**

I am not doing anything; I simply did [`v`]. [Then] wherever I [move] — for example, this "music" line, I want to select it; so simply I will go into **visible/visual mode** and I press [the arrows]; I pressed continuously, so it moved forward. Look.

> **So now, instead of the mouse** — because in many places it turns out that **you don't get mouse access**, so what, you will have to do all the work from the keyboard. **So from the keyboard too you can do this selection work.**

### Block-wise selection — `Ctrl + v`

**If you want to select block-wise** — block-wise, in the sense — how, block-wise you want to select? Like, [in columns]; a **block** — like this, this is one block, then this is a block.

**If you want to do selection like this**, then simply what will you do: like my cursor is here, for example my [cursor] is here — then what I did: **Ctrl+v**. As you press Ctrl+v, what is it — **VISUAL BLOCK** came; here it is written "Visual Block."

Okay, alright. Now this whole thing will become a block; like this, like this — I did like this. Look, **it will only select this block, only.**

Look, **before, what was happening — [if] I went up a character, it would select the whole line** where I was present. **But now this will become a block** — here I did [this], this is done; this much at once.

**So this is the selection, block-wise.** So this you would have come to know.

### Line-wise selection — `Shift + v`

If you [want to] do it **line by line**, then you could do that too. But let me come into Escape mode once — so what you have to do: **simply press Shift with `V`.**

Then look — lines: 1, 2, 3, 4 — like this, line by line. Now this selection will [work] line by line.

### Summary of visual modes

So I told you:

| Key | Mode | Selects |
|---|---|---|
| `v` | **Visual** | character by character |
| `Ctrl+v` | **Visual Block** | a rectangular block / columns |
| `V` (Shift+v) | **Visual Line** | whole lines |

**If you had to go into visual mode, you simply have to press `v`.** When you press `v` you will go into visible/visual mode, and where you do the selection you will go into visual mode, and there the selection will be done — **[for] block selection, Ctrl+v; [for line selection] Shift + V.**

> **But keep in mind that you should be in COMMAND MODE** — while doing these three things you should be in command mode; [otherwise] it won't work. Now what is it — **you will have to be in command mode**; so for this what will you do.

[`Shift+V`] — which one is this — **this too will go to Visual Line, visual line mode**; so now you will select line by line; in it, line-by-line-by-line selection.

---

## Wrap-up

This was our `vi` editor / `vim` command, about which you would have got to see [things].

So confirm to me once in the chat — however many people are present, one or two, three — **did you people understand or not?**

Look, this is such a command that about it **you will have to keep a [cheat] sheet**, or what you will have to do is **keep notes of it with you**. And as you use it on a daily basis, you will become familiar.

**Follow the editor and continuously** — whatever editing you have to do, writing you have to do, any work at all — **do it inside this itself**, so that you get into the habit of it. And gradually, its keywords, what they mean, how to do selection, what to do — **cut, copy, paste, replace, how to add output** — all these things, once you become familiar with all of them, **then you will never say [it's difficult].**

Okay, thank you. Please — Lakshmi Narayan, thank you.

---

## Course roadmap

So anyway, our time is up; **the `locate` command we'll do tomorrow.**

So tell me — Prince, Lakshmi — [in the] 11, 12, 13, 14, 15 [classes], the target I had selected for you, that will be done for you, no issue.

Let me tell you one thing, what all I will tell:

1. **Networking** — I will tell you a bit about this: **how you do [network] selection; through networking commands, how you do network settings** through the command line.
2. **Repository** — second, I will tell you about the repository: **how you use the command; any package you have to download, install, uninstall** — I will tell you about that; you have to search [too].
3. **Third**, a bit more that is left — something special: **if you have to do searching a bit faster** — okay, if you have to do searching a bit faster and better, then we can do that too, in a somewhat better way; there are some commands, we will talk about those.
4. And a bit — there is a **history command**.

So we will tell all these things. So **this would make your fundamentals clear**, your fundamental knowledge.

---

## Closing appeals

[Regarding installation:] if you are new, then do one thing: **before we started the series, what we did was tell the installation process.** So go there, you will get the installation process, and from there you can follow the whole thing step by step and install it in your machine.

And the steps for installing any [distro] are [similar] — **not only for Kali; even for CentOS, for Ubuntu, the steps are similar**; a few things differ, yes/no, [but] you understand it. If you have learned to install one machine, then it's fine.

So again, once more, a request — **because you people don't like, comment, share** [Music].

So what we [ask] is: again, after this class ends, **Day 11** will be updated on our Defronix Cyber Security LinkedIn page. So **please go there**, and as you finish the video, and as you make your notes, however you are able — **go there and tell us by liking and commenting**; tell us how it felt to you.

And this is our official page; **tell there what you got to learn** — tell it briefly, no need to tell in detail — **so that whoever follows or refers to it further will come to know: "yes, a series ran here, and in the series we got to learn this."** So **you are helping not just yourself but others too.**

Now look, here on **Day 10 there is no comment** — meaning nobody watched. On Day [x] there are two comments; [someone] has been active in our class from the start, so thank you. [There are] 16 comments [somewhere]... our subscribers are 929; in live 12 come.

> **Meaning, before a class, you people [give] nothing — there isn't even a comment.** You don't comment on our video channel. **[When you do,] your teacher gets motivation** — the biggest thing for [a teacher] is that if you are learning from him, he doesn't need anything more; **and he will make better content than that when you are with him.**
>
> **If you are not with him, then what will he do** — he won't even feel like coming to class, because there are no students; he alone is saying something, nobody is taking interest, so he becomes a bit demotivated.
>
> **So our motivation is from you people.** Those who are watching the recorded session, listen to this too; and for those who come live with us, **very very thank you.**

So our motivation is from you people. If you people are with us, that's good; if not, **we have to deliver anyway** — if not today then tomorrow, whoever needs it, they will watch.

---

## Doubt session note

Okay, so I hope everyone understood. **If anyone has a doubt, then you can go to our doubt session** — our group, [or] on [social media]; going there you can ask; your [doubts] get resolved there.

**I like it when other people help others**; that is quite good. Because we have time, but **we wait a bit to answer, so that you can solve your problem yourself.** We will not always be with you; you will have to solve your problem yourself.

**And to solve your own problem, what will you have to do — you will have to research. So become a researcher.**

Okay, again, let's get the session over. Bye, good night, take care. See you [in the] next session.
