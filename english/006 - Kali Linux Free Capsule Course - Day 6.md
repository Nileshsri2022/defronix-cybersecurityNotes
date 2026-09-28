# 006 — Kali Linux Free Capsule Course — Day 6

**Source transcript:** `transcripts/006 - Kali Linux Free Capsule Course - Day 6 [ Hindi ].hi-orig.srt`
**Topics:** `cut` · `awk` · `column` · Compression (`gzip`, `bzip2`, `tar`)
**Type:** Verbatim English translation of the spoken Hindi/Hinglish session

> **Note on this transcript:** captions are heavily garbled in places (`अब कमांड`/`ए ब्लू के` = `awk`, `बट`/`कट` = `cut`, `तेल` = `tail`, `ग्राफ` = `grep`, `जीप`/`गंजी`/`अजीप` = `gzip`/`gunzip`/`unzip`, `तार`/`टावर` = `tar`, `कलम` = `column`, `दिल्ली मी`/`डायमीटर`/`डेटर` = "delimiter", `लाइनेक्स` = "Linux", `सीटीसी`/`ईटीसी` = `/etc`, `फ्रेंड` = "field", `दें` = "then"). The intended technical term has been restored where unambiguous.

---

[Music] It has come. [Music] Hello everyone, good evening. So, welcome to [Day] Six of the free capsule course. [If] I'll come to know — please tell me in the comments. Okay, thank you, thank you.

What is going on is that some command-related things are going on. So does it feel like you are getting bored — that right now the topic should be changed a bit and then we should come back to commands? Did anyone feel like that? Tell me once in the comments. It is possible that if continuously in every session there are commands and commands, then it may not be understood properly and there may be a problem too. Tell me once, you people.

Not today — today let's continue. Let's change some commands. Let me tell you the interesting topic first: there will be **User Management**, there will be **Group Management**, and after that, further, in some classes there will be your **File Security** and how **permissions** are managed. After that we will come back again onto the commands, so that you people can revise and practise these commands from behind.

Let me get cleared whatever commands are remaining — and however many I have to tell, all of them are very, very important for every Linux admin. Because when you go forward and work in a [Linux] environment too, or work on a real server, every single Linux admin uses them, does this; **without these, work simply cannot run** in a Linux environment.

And because all its tasks are [command] based — because **every command has its own role**; every command works according to its own role. The task you have to perform is defined according to each command, because a command, after one point, comes into its **limitations**; after that, another command takes over.

So then today we are going to study the **`cut`** command. One more command — if there is time left, we will study one more command; otherwise we will [do] two commands.

---

## `cut`

So let's start. The `cut` command basically is **used to cut records using characters and fields from any file and from any command output.**

Whether it is the output of a file or the output of any command — in that, whatever you have to do, you have to cut any field, and according to that you have to see your output, print it on the screen and save it inside a file — for that the `cut` command is a very good command.

### Syntax

Let me tell you what its syntax is:

```
cut [options] filename
command | cut [options]
```

You use `cut`, after that you use the **options**, after that you use the **file name**. Or — the other way, one more way you can use it: the command name, then the **pipe symbol**, and then `cut`, after that simply you can use the options.

Now these are two ways; you [will] see well how you can use both of these.

### The options

Now what happens — you can call them options, you can call them flags. Okay, sorry for the disturbance.

- **`-c`** — this means **cut by characters**. You can do it character by character; whatever data of yours is in the file, or whatever your command output is, you can cut it.
- **`-f`** — this means **cut by field**. How we do this, I will show you. What "field" means, [I'll explain].
- **`-d`** — after that let's talk about defining the **delimiter**. It can be anything: any symbol at all, even your **comma**, your **semicolon**, your **dollar**, **@** — anything at all.

[The delimiter] gives the indication that "my field is defined up to here" — how far I have to cut. Otherwise, for it, the whole thing is one single field. If you gave the file's name, gave the command — because you didn't [define a] delimiter.

**Example:** like I did `cat` — there's a whole line. Now what do I have to do — out of this, the `manish` that is there, out of this I only want `manish`; I only want `manish`, or I only want the `m` character. First, I only want the `m` character — so how will I extract it?

### Cutting by character — `-c`

So one way is this: I'll say `cut` — it cut it, and it was printed.

For that you know that we can join multiple commands together. How can we do that? What I did — I used the `tail` command; `tail -2`, the last two. Hit enter. Now what it did — the last two lines, it printed out their output on your screen.

Now what do I have to do — now I want the whole character; I only [want]... Let me show you on the screen again — let me show with `cat`. `cat` — here it is.

Now what do I have to do: I want this whole `manish` name on my screen; I only have to cut this character. So how will I do it? I can do this too.

Now, what is this — let's count: 1, 2, 3, 4, 5, 6 — total six. So how can I do it:

```bash
cut -c1-6 filename
```

It cut [character 1]; this one — but the one we want, we can apply `tail`, so it will work for us.

Now what do I have to do — no, what do I have to do is: this `m` that I want — I want the `m` and the `n` out of it, meaning I want the **first and the third**. This too I can do. How? Simply `1`, and after that what will I do — I will use a **comma**, after that `3`:

```bash
cut -c1,3 filename
```

So this gave `m` and `n` — it printed it out on your screen and showed it.

This was how you can cut any character from inside any file, from inside any command.

Now let me show one more thing, to see an even better output. I'll say — what I did, after that I grepped from it, `-w`, [because] I want an **exact match**; I can do it like this too.

Now `sshd` — only `sshd` came. If out of this I [want] only — I can do it; otherwise what can I do: if my output comes of this type without this, then I [would] have a lot of `sshd`s, but what did I do, only this much will be found.

If I had to cut up to here, then I'd have to do up to here — so you can do it nicely. If I had to cut only [a portion], what would I do — I [count] 1 2 3 4 5 6 7 8 9 10 11 12, here then 12 13 14 15 16 — like that you can cut. [So with] `disk update` too, we can cut this and we can filter this out. You can use this method on your machine.

### Cutting by field — `-f` and `-d`

Now let's talk about how to cut a **field**.

Now in this, if I take the example: this is one field, this is one field, and this is one in itself. If you use [`-f`] **without a delimiter**, you cannot use it.

How? What I did — out of this, what do I want to do: **field 1** — which one, this `sachin` one, this `manish` one — how can I see it? Simply, I did the pipe symbol, used it; after that did `cut`, and then `-f1`:

```bash
cut -f1 filename
```

Now what it did in this — it printed out **all of it**. Why? I had already told you: **without a delimiter you cannot use it**, because it says that "until you define something for me, until you tell me up to where your field is defined, then for me it is the **whole field**."

So how can you do it? Simply, first you will have to define the **delimiter**. How will you do that? `-d`, after that you have to tell it: single quote, then the delimiter. I told it: in this, yours is a **colon**. After that `-f1`:

```bash
cut -d':' -f1 /etc/passwd
```

Okay — however much is **colon-separated**, this is its [structure]; for this, field 1 is [the username]. Like [in] `/etc/passwd`, for it field 1 is [that].

If you had to print field 2, you can do that too. If you have to [print] field 1 and [more] — you [want] to print — it printed it out and showed it. If [you wanted] 1, 2, 3, it showed it.

In this manner I showed you how you can use the different flags of the `cut` command.

### A real example — the log file

Now there is a file in front of us. Let me do `cat /var/log/...` — because there are no logs here, inside this; no problem. Let me [use] `messages`.

What do I have to do — now what you have to do is [get] this on your screen; what is it, from inside some file? So how can I do it?

For that: [`tail`] the log messages, after that what will I do — I need the latest [entries]. What do I have to do:

Now, to give a **space** — you will have to give a space inside the single quotes there. Then you have to give — I want this first one, after that I want the second one too. Enter.

Now see this: this is the time, this is the date — which month it was, which date it was, at what time, which user it was who hit our server.

So this will be the latest [entry]. You can forward it to someone: "yes, someone said they need the latest entry with the usernames — who all were there." So in this manner you can cut and give it.

### Where `cut` hits its limitation

Now what happens is that this too, to some extent, can perform your operation easily.

**Here some limitations come in**, when you have to define delimiters. Because — let me show you — there is a command. Now look, here there are **more spaces**. Okay, what I did, after that simply I am doing `cut`, after that `-f`; `-f1` I gave. Simply — now field 1, I cut it easily.

**Now the problem will come here — here [it is] limited.** [Music] So in this case what happens is that if you are **not capable of properly making your delimiter** — you can't make it with the `cut` command — [then] with the `cut` command you cannot perform the operation properly.

**In this case, the `awk` command comes in useful.**

---

## `awk`

Now, `awk` — here it is, let me write the name in front of you.

Now, this is **the most important command in shell scripting**. All these commands I am [covering] right now come in very useful.

Now, what does the `awk` command do? The `awk` command says that "**you don't need to define the space for me**" — you people [don't]. Okay.

So how did this work become easy? What I simply did: I had done `df -h`; I used the pipe; then the `awk` command; after that, **inside single quotes**, inside this you have to [put] **open and close curly braces**; inside that you have to define what you have to **print**.

What do I have to do — I have to print inside this. Simply what do I have to do: `print`, P-R-I-N-T, `print`; after that [the] field.

Now let me show you once: for this, this is `$1`, this is `$2`, this is `$3`, this is `$4`, this is `$5`.

```bash
df -h | awk '{print $1}'
```

So you simply use [`$1`] — it showed the first field. If you have to see the second, in place of `$1` [put `$2`].

**How easy it made the work!** In the `cut` command you had to think about how much space I'll have to give with `-d`, what I have to define. Simply, **it adjusted that space by itself, automatically counted it**, and showed you the output on the screen so easily.

### Multiple fields

Now what did I have to do — if my `df -h` command is there, and what do I have to do: I want to see the **file system, its size, and where it is mounted**. If I have to see these three things, then how can I see them?

Simply, `df -h`, pipe, `awk`, then `print` — what do I have to do, what do I want, [fields] 1, 2, 3, 4, 5, 6 — which field is it of? Okay.

So if I want my output arranged properly, then I can use [something]. How? Now here, with [`column -t`], one uses — the command will **arrange** it. You simply hit [enter] — now what it did, look, [now] there are 3. In this manner you can use the `awk` command; it has made your work very easy, this `awk` command.

Now, like, my `df -h` is there — okay — after that I am using the `awk` command; single quotes, curly braces... it showed `25%` on your screen.

---

## Practice question

So now do one thing — here too, for you people, a last one... someone did [the earlier one]. Meaning, I had told you people, I had given a practice question; nobody even commented, and in the group too nobody [did it].

What I have to do — I have made the work so easy in front of you; look, I extracted **25%** with this command.

> **Now what I have to do here: I want the output — this very one — but I don't want the percentage in it. I only want `25`, only `25` on the screen. So how will that come?**
>
> You have to send it to us in the comments.

How many people did it, didn't do it — [send] the answer with a screenshot; you can send it.

Let me tell you again: I have shown `25%` on my screen using this command. But what I have to do is that in my output, out of this `25%`, **I only want `25`** — only [that], which is appearing on your screen. So I want this; how will `25` come? So that command, you people will send me in the comments.

---

## Announcement: follow the social pages

Now let's talk — before continuing further, let me do [this]: I forgot to tell you people one thing at the start; it got missed out — that today we had a discussion in the group.

So what will you do: our YouTube channel, on which you are logging in right now — now below it, what is there: here is the **Instagram** page, here is the **LinkedIn** page, here is the **Twitter** page, here is the **Facebook** page, here is the **Telegram** page, and here the **website**.

So what you have to do is simply click on the LinkedIn page, and here you have to log in — you have made your ID — and follow it here.

Whatever announcements there will be, and what we have started — however many classes there will be, all of these — we have posted them here with screenshots and the link.

And what you have to do: as you complete class one, complete class two, complete class three — then please, the topics that were in class one, in class two, comment them out and tell, **so that** other people also come to know what is going on. Whatever you have to comment, you can do it on this — whatever you people have studied, whatever is not [clear]. Like, on Day 1 a lot of people have commented, which we can read; if we are able to read — for that I'll have to log in.

So [go] to our [page]; go to the LinkedIn page, and as soon as the day's class finishes — as soon as it finishes — then go there, comment and tell: "in today's [class], what all did you people learn, what all topics happened, and how it was" — you people can tell in the comments.

Secondly, there is one more — our **Instagram** page. On the Instagram page too the same thing is going on, so in that too what you have to do — [it shows] that I have not logged in; so if you log in, then follow this page.

So in both these places you will get the announcements for everything, **for your future benefit** — whatever we will be planning regarding you people, especially those who are continuously staying with us, for whom we would have thought of something in mind. And whatever other announcement there will be, you will get to see it on these two pages.

So please take out 5 minutes, go, and follow these. After following, at the end of the class, go — it will take you two minutes — after going, what you have to do is comment below that particular video: whatever you learned, whatever you studied, so that other people get help; people can come to know: "yes, in which day what content there was, what was taught, what was discussed." So you people knew it; other people will come to know: "yes, this was in Day 1, this was in Day 2, this was in Day 3." Whatever your comments, you can go there and do them.

A small announcement for you people. Let me continue with my commands. Okay then.

So right now we were — you would have come to know what this task is that you have to do. So here too you can do that task, show it by commenting, send it with a screenshot: "we got this practice question and we have done this; this is its command." So this is a good thing too.

---

## `awk` with a custom field separator

So now what do we do — let's continue. [There is a] command which shows your internet details, of the network: which NICs are attached in the machine and what each one's [address] is; `0` and [the loopback] is a local address.

What do I have to do — in this, I only [want] this IP; what do I have to do with it, I have to see it. So I want to see just this — so how will I do it?

So it's simple. What will I do — I used it. Like this you can use multiple commands, from which you came to know how much the commands you have used so far are helping you in doing your work.

`ifconfig | grep`, after that `inet` — because I want `inet`; so I hit enter. Now my output got **narrowed down**. Earlier, what was it — one command's output was this much; now this much is being printed on the screen.

For `inet` there are two things; I need... I want the `192.168...` one. So now, a bit — what is it — I will run my `awk` on top of this; after that, `print`, and simply what you have to do: dollar — which one do you want? You want `2`; you don't want `1`. If you only want `1`, then you'll write `1`; or `1`, after that then `$2` — `1` and `2`.

Now it printed out both on the screen. Now on your screen will come: `inet 192.168.1.45`. Okay.

What do I have to do with this — a bit more. And if you only need [the] `192` one, then you can do that too. How will you do it? For that, what will you do...

I want to make [it]; that too I can do. How can I do that? Like, what will I do — this is my command, this much; so I can use one thing with it.

First let me remove this. Now here, a parameter; after that, what is that thing — we will define here, by which you want to **separate** this. Inside single quotes [you'll] put that thing. Like, what do I want to do — one, two, three, both fields.

So simply, after that the pipe symbol — it feels [right]; you would be understanding what we did here.

If, like — now this was okay; how will I do it? Okay, simply, up to now we do it, we'll do it like this.

What we did: used the command, after that the pipe symbol, after that did `awk`, then single quotes, inside that **parentheses**, after that did `print` and [ran] it.

Because I had already told you: what the `awk` command does — **apart from space**, if you want to give it any other [separator], then you had to define it. So then for this, what will I have to do? An option is used; we call it **`-F`** (hyphen capital F), then single quote — its space will remain.

```bash
ifconfig | grep inet | awk -F':' '{print $2}'
```

If you want a bit better output, then simply what is it — I am adding `tail`, `head`, and then [it's fine]. My problem is quite nicely [solved]; in this, what is it, random.

Just now, when we cut the field, then what happened in that — what it did was, **without space-separating** it, it **merged** it. But `column -h`, okay — in this, what does the `column` command [do]? It has to **arrange** the output that is coming. That's what this means.

If you want to see more — C-O-L-U-M-N, `--help` — you can look at it. About this command: **`-t`** means [create a] table; you have to create a table. What does this mean — it has to show it **in the form of a table**; that's what `column -t` means.

> **Whenever you don't understand any command, simply: the command's name, `--help`** — the meaning of which flag, of which option, what it means, what it is trying to understand — everything is written in it in detail. You can use this.

This was your `awk` command. Now what you have to do — I have told you how to use the `awk` command and the `cut` command. Okay, complete this.

---

## Compression: `gzip`, `bzip2`, `tar`

Now let's talk about the **zip and unzip** commands.

Now, if in the Linux environment we have to **compress or decompress** any file, then how will we do it? That we learn.

Like, I have a file here. If I show you with `ls` — `demo.txt`. If I `cat` it — everyone knows, `demo.txt` is my file.

If I see its size — with `ls -l`, let me see: `demo` and enter. Its size is... let me see in [human-readable] form, `-lh`, enter.

### Why compress?

From this... okay, [suppose] a file has to be shared with someone. Now its size is very large; but you can keep the file in your machine according to that size, [and] after that send it.

Otherwise, what happens — many times, a lot of work is going on in your environment, and there are some files which have not been in use for quite some time, but they are **important**; you cannot delete them. So what will you do?

I will tell you about [these] three commands.

### `gzip` / `zcat` / `gunzip`

So, like, this file's size is [X]. The command is [`gzip`], and simply `demo` — so see, here [now] it means this is a **compressed file**.

If we see its size — how will we see it? **`zcat`** — `zcat`, after that that file's name, `demo` — [and] it did [show]. It hasn't been uncompressed.

So if I have to **uncompress** this, then how will I do it? For that the command is [`gunzip`].

```bash
gzip demo.txt        # compress   -> demo.txt.gz
zcat demo.txt.gz     # view contents without decompressing
gunzip demo.txt.gz   # decompress -> demo.txt
```

### `bzip2` / `bzcat` / `bunzip2`

I have to zip, compress, uncompress — no, I have to compress. So how? For that there is [`bzip2`].

If I do — `bzip2` came. Okay, it will work a bit [better], but the thing is, **in a small file you will not get to see so much difference.**

But how we can [do] its... compress — let me show. Simply, and the file's name, `demo.txt`. Now in this too, what did it do — it zipped it, compressed it.

If we see its size, enter — now its size [is smaller]; **it uses a compression technique**. But what is its extension? **`.bz2`**.

If you have to see the content inside it, the compressed file content — then with the `cat` command you cannot see it at all, and with [`zcat`] too you cannot see it — the one we used in the last command, the one whose extension was `.gz`, we used it for that.

But for the `.bz2` extension, if you have to see the content inside it, for that the command is **`bzcat`**; after that we use its file name, `demo` — it opened it and showed.

There is one more command [`bzless`/`bzmore`] — look, so that you can comfortably scroll down. In [`bzcat`] it showed the whole output at once; now this — comfortably, page by page, you keep [paging] and keep reading the file. Right now let me quit.

If you have to **decompress** this — meaning [undo] it — for that, it's not that you can use the `gunzip` command that was used last; you cannot use that for this. The command for this is [`bunzip2`].

If I show you with `gunzip` — `gunzip demo.txt` — now it [needs] some command whose name is [`bunzip2`]; [then] the whole file will come back again.

```bash
bzip2 demo.txt         # compress -> demo.txt.bz2
bzcat demo.txt.bz2     # view contents
bunzip2 demo.txt.bz2   # decompress
```

### `tar` — archiving many files

Now, up to now what I did — [but suppose] there are 10, 15, 20 files and I have to compress them **inside one single file**, and decompress them from that file. How can we do that?

**With those two commands we cannot do that work.** For that, the command used is the one whose name is **`tar`**.

Now, like, I have two files. If I show with `ls` — `demo` file; let me create `sample`.

What does `tar` mean — inside the command:

- **`-c`** means **create**
- **`-v`** means **verbose mode** — verbose means that whatever work is happening, the compression, you get to see it there on the screen
- **`-f`** means **file name**

Let me zoom in — `-c` means create, `-v` verbose mode... after that you can use `-f`; `-f` means file name.

Now I have to give the name of that file inside which I want to compress all these files. So I want to give its name: P-R-A-C-T-I-C-E, `practice.tar`.

So `demo.txt`, `sample.txt` are mine, which I want to compress inside this.

Let me tell again: **`c` means create, `v` means verbose, `f` means file** — the name of that file inside which those files are given.

```bash
tar -cvf practice.tar demo.txt sample.txt
```

Simply, what I do — I hit enter. So what it did — now `demo.txt` [etc.], the output it will show on the screen; and because of what is it showing? **Because of `v`, because of verbose mode.**

If I do `ls`, do `ls -l`, then see — here you will get to see a file by the name `practice.tar`. If I do `ls` normally, then too you will get to see it; if `ls -l` [as well].

### `tar` with gzip compression — `-z`

Now what do we do — if you have to [compress in another format]... [Music]

I have `demo.txt`. If I do — how will I do it? Like, in the first format, what do I have to do — I have to compress this; after that what do I want to do...

`test1.txt`, `demo.txt`, `test.txt` and `test1.txt`. [Music] It's working. I do `z` — after that then `.gz`. Syntax mistake — `test1`, `test`. Okay, which file am I giving?

**Because the `z` option has to be given before `f`.**

```bash
tar -czvf practice.tar.gz demo.txt test.txt
```

So now in this, what do we do — it did it in **gzip format** too. Now I do `ls`, so see — here, `practice.tar` is there, `practice/test.tar.gz` is there.

### `tar` with bzip2 compression — `-j`

Now if I have to do it in **bz2 format** too, then how can I do it? `tar` — for that I will have to create a file, `.tbz` format, then after that `test.tar.bz2`.

```bash
tar -cjvf practice.tar.bz2 demo.txt test.txt
```

### Why `tar` is the most important of these

[Knowing this] is very, very important. **Even if you are not a Linux admin** — if you are a cyber security engineer, for you too it is very [important].

Because whenever you download any package in your machine, [from a repository], then you will get it in **zipped format**; or otherwise, download from a website — then too what [you'll get]. After that you will have to do a **manual installation**.

If you simply don't know how to unzip, then how will you download that file, or install it, use it? Because **for zipping/unzipping, the `tar` command itself will be used.**

So even if you work anywhere at all, then too it is going to help you very much — this **package installation and uninstallation** — because the `tar` command is the one that can unzip your file.

That is why **this is the most important command**: how you can zip anything, how you can unzip.

For the rest, even though the earlier commands — `gzip`, `gunzip` — you don't need to memorize them. If you have to share some package from here to there, then fine; you can use those for compression, for a higher level of compression.

Otherwise, what you have to do — to **unpack** any downloaded package, to **pack** any package — basically, **it is very, very necessary for you to know the `tar` command.**

### Listing contents of a tar — `-t`

So now let me show you how to unzip whatever tar packages there are.

But one thing: if what you have to do is — there is a zip file, and you want to see inside it **which files have been zipped** inside it — then you can see that. For that there is a command.

"Is there a file by this name inside this zip or not?" Because of space you can search for it. For that there is an option; [give] that file's name, then whatever you have to search.

For example, I have to search: there is a file by the name `demo1.txt`; I want to search for it inside this tar. So I hit enter — then it showed that yes, inside it there is a file named `demo1.txt`.

If what I want [to search for] is not in the [archive], in [the] format — "**not found in archive**", "**error exit delayed from previous errors**". Okay.

```bash
tar -tvf practice.tar              # list contents
tar -tvf practice.tar demo1.txt    # check if a specific file is inside
```

### Extracting — `-x`

Now let's talk about: if you have zipped any file, then how will you **unzip** it? For that the command is the same — we will use `tar`, because you will use **`-x`**; `-x` means [extract].

```bash
tar -xvf practice.tar
```

It did it — because it was already showing for me, that is why you didn't get to see [it]. Otherwise, what it did — it [extracted] it, and you'll get the tar's entry.

Now let me show with `ls`, let me show with `ls -l` — [extracted] data. Okay.

So in this manner you can use the `tar` command: how you can create any file in zipped format, how you can unzip it, how [you can list it].

---

## Wrap-up

So all these things about commands — let's finish, because we won't go ahead more than this. I feel that there would be commands and only commands for [many] days — because **I** enjoy it, but you people are new; you people [need to] understand, keep the commands, do that — because you wouldn't be able to use it, [wouldn't know] where to use it. But when you gradually [progress]...

So let's keep this much for today. Now next will be our **Day 7**; we are going to start with a new interesting topic: **User Management**. It's quite an interesting topic, because managing users is also very, very important:

- How to create [users]
- How to delete them
- How to create groups
- How to add passwords
- How to set the password expiry date

These many things — so in the next class we are going to do all these things.

---

## Doubt session

So for you there are 5 minutes; let me open a 5-minute doubt session. If anyone has a doubt, tell me in the comments section; I am looking at your comments right now. After that we will get the session over.

But before that let me tell you: right now, after five to seven minutes, what will happen — it will be over. So please, [go] to the LinkedIn page, and the one I told you about earlier — go on YouTube, and go to the LinkedIn page, and the Instagram page.

Going there right now — the class session, after 10 minutes of it being over, or after 15 minutes, what will happen: our basic [post] will be updated; inside it the logo and video. And what you have to do after going there is comment on it: whatever you learned in today's class, whatever commands you learned and whatever you understood — you can share that thing there.

And even the practice question I give you — that too you can go and share there: "**this was the question of Day Five**." Immediately after this, as the session is over, the basic [post] will come here; you have to comment. After commenting, from our side, you [can do] anything.

### Q: What is a delimiter? (`-d` and `-f` explained again)

Okay, so tell me. Give [it] once — [the] colon, the `@` symbol — meaning that you define there that "I have to consider this field up to here"; you defined a limited symbol.

Like, the `/etc/passwd` file was in front of you. What did I do — this is from here; the **colon** — I told it that "this is my delimiter, this, brother." Before that, this is **field 1**.

Now, between the delimiters, what is there — because I defined the colon as the delimiter, so between them, what is there — those are all the **fields**.

Now what does **`-f`** mean? You have to define the field — now, the delimiter was defined as the colon. Okay, so according to this, this too is a field, but this is an **empty field**, it is blank; one is this field, one is this field. Okay.

So in this manner the delimiter works. So the simple meaning of a delimiter is that **you are defining a symbol there**; a **criterion** will be defined by it — this defines for you "up to here you have to consider the field."

So this is basically the meaning of **`-d`**, and the meaning of **`-f`**. I think, Ojha, you would have understood.

### Q: Repository / update error

Then — "update is coming"? Do one thing: send a screenshot in the group of what is coming. If your error is related to update, then what had I said — send the link of the two pages, of the official page; so perform all its steps step by step, and yours will go through.

Because when [people] are beginners, everyone faces this same problem — the `sources.list` one — because what would have happened: your Linux machine is either old, or your machine with it, what is it, is not able to get set properly. That's it — that's why you are getting to see that.

It's working — the `sources.list` file: first delete that, and after that what you have to do is go there, to the link I had sent in the group; once more I will share it again. From there, [follow] the whole thing step by step.

But do one thing: **don't [just] follow** — it is written in it [why]. In future, if a problem ever comes to you, then you can do that; then you will remember: "yes, I had performed these steps, this was its meaning." Go there. If even then it doesn't happen, then [send] with a screenshot, absolutely.

### Q: `cut` — is it clear?

Arre, now the `cut` command would have become clear, right? In [it] there is nothing [difficult]:

- One is **`-c`**, which cuts according to **character**. Like, what does `-c1` mean — for it, what is it: this is a character, `i` is a character, `s` is a character. So `c1` means [the first character], `c2`, and `c3` `n` — these are characters.
- And **field** means: this whole thing is a field. But the thing is, for that you will have to give a **delimiter**. Delimiter means you will have to give a **symbol**.

What did I do — I made this the delimiter: "brother, wherever this is found, before that, for you, is the full [field]." Now after that this delimiter came; for it, this whole thing is a field. Now here this delimiter came, so this is a field for it. So simply, this is [it].

Then — with this too, [if] you have an update problem — no, no, it will get solved for you. Even then, if [that] error is happening, it will get solved. Someone [was asking] — anyway, we will tell you ahead: once, whenever you install a package, [how you] install it — we will tell you that, for the repo problem.

Once, [there is] the link of the [page]; follow it and your work will be done. **This error happens with everyone, with beginners.**

So I hope nobody has a doubt. So we can get the session over. Tell me — we can request [that].

And let me remind you people again: you have to go to the LinkedIn page, go to our [Indian] page, and go to the Instagram page. And what you have to do there — the basic class [post] will be updated, and after that what you have to comment: whatever you have studied, whatever commands you are getting to learn — so that other people get motivated by you people and try to join with us.

Bye bye, good night. Take care.
