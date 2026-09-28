# 008 — Kali Linux Free Capsule Course — Day 8

**Source transcript:** `transcripts/008 - Kali Linux Free Capsule Course - Day 8 [ Hindi ].hi-orig.srt`
**Topics:** `sudo` and the sudoers file · Password Management · `/etc/shadow` · `chage` · Disabling accounts
**Type:** Verbatim English translation of the spoken Hindi/Hinglish session

> **Note on this transcript:** captions are heavily garbled in places (`सुडो`/`छोड़ो`/`स्टूडियो`/`सोडो`/`पीएसईउदो` = `sudo`, `सुवॉयर`/`सोडोफिल` = `sudoers` file, `स`/`एस यू` = `su`, `शैडो`/`साडो`/`सेड हो` = `shadow`, `पास डी`/`पांच डी`/`पार्ट डी` = `passwd`, `सीटीसी`/`ईटीसी`/`एटीसी`/`डीसी` = `/etc`, `लाइनेक्स`/`लिरिक्स`/`क्लीनिक` = "Linux", `चेंज` (as a command) = `chage`, `लॉगिन दास`/`लॉगिन देव`/`लॉगिन पोली` = `login.defs`, `रोटी`/`रोड` = "root", `सेल` = "shell", `बेस्ट` = "bash", `फेडेक्स`/`एफडीएस` = `fdisk`, `हेसिंग`/`हैकिंग एल्गोरिथम` = "hashing algorithm", `साफ 512`/`साफ आई वांट तू` = `SHA-512`, `वे आई` = `vi`). The intended technical term has been restored where unambiguous.

---

Hello everyone, very good evening to you, welcome. Okay, let's wait one more minute.

Do [this] — you people, put the notification of the live class in your local group. You will get the YouTube channel's link; going there, we have an option. Going there, what you have to do — as soon as the day's class is over, after that go there and comment out whatever you learned.

Everyone knows; let me tell you once again: from here, go to the **LinkedIn page**. What you have to do after going there is provide your comments in the comments: whatever you learned in this class — so that others come to know what happened in this day, what was taught to you people. Okay.

Not many will come. So today's topic — I have already told you: there is a file, the **shadow file**; **how password management is done**, I will tell you about that. Before that, there is an important concept — [both are] important concepts; let's discuss those.

---

## Part 1 — `sudo`

So let's start: how do we maintain [it]?

So look — like, if you have to perform some task which only an **admin** or **root** can do, then how can you do it? So you know — simply, what will we do: **a normal user has no privileges at all.** So I will become the root user, and after that I will try to perform that task.

Now, like, I have a user; so what do I do — I switch:

```bash
su - defronix
```

And I hit enter; after that I put in its password. And what is mine — because of the bash shell, the shell shows something. If I show you with `pwd`, then you will come to know. Okay, so you know about this.

### The permission wall

So now what we do — a user has to be added. So simply what do I do — `useradd`, and you know how it is done — the command; after that a name, I want to do it with the name `sachin`. Simply — okay, it's already showing... okay, okay. [Music]

**"Try again later"** — the meaning of the English here is that **this user does not have permission**; this is a normal account and it does not have permission to do the root-type work. The work that [root] can do, this one cannot do.

Now what happens is that **a normal user does not have permission to do all those tasks which any root/admin can do.** So how can they do it? There is a small concept for that; let me try to explain it.

### How real organizations handle the root password

Now what happens is that in all the big organizations — inside all the big organizations — **only limited people have this root, this super user access.**

Generally, what happens to the root's password: there is a **digital tool**, and it is kept inside that. And in that, what happens is that root's password is **continuously changing** — after a particular time, after 15 days, 20 days, 30 days, or whatever.

But in both cases what happens is that **to take the password you have to give a reason**, you have to request it. But **due to security reasons, the root password is never shared with anyone.**

In this case what happens is that a **user cannot log in to the system** [as root]. Because if you have to switch, for that you would have to use the `su` command, [and] you would need the root password — but you don't have the root password.

### Enter `sudo`

Now what happens — to do all this, when we don't have root's password... normally, the root password simply cannot be shared. So for that, in this case, a **tool** is used whose name is **`sudo`**.

What does it mean — [with it] we can become [root]. For that we have the **username**.

**Normally what happens with `sudo`:** whenever you use `sudo`, normally what happens is that the password used is **a normal user's password**. Because whenever you want to switch into any user with the help of `sudo`, what happens is that **the password you enter inside it is that of the user on whose terminal you ran `sudo`** — not of the place you want to switch to.

> **This is the best [part]** — a good benefit: **you don't even need [root's] password, and you can become root.**

But for that, what is the condition — [an entry] has to be inside it.

### Logging

When you execute [`sudo`], then **logs are maintained**. In your machine there is a file [where it] is maintained; it plays a role in managing any user.

[Music] If you have to do root-type work, or admin-type work, then what will you have to do for that — **there will have to be an entry in this sudoers file.**

And whichever user's entries are made inside the file — or whichever user is given sudo permission — **we call them a sudo user**.

### The sudoers file location

And where is its location found? Let me tell you — it is inside **`/etc`**; there is a **`sudoers`** file, S-U-D-O-E-R-S. Inside `/etc` you get to see this file; this is the file's location:

```
/etc/sudoers
```

### Why this file matters in attacks

So basically what happens is — if I talk about an attack: you do **enumeration**, after that what — you get into some one user account, a normal user account. Right now I am talking especially about Linux.

So what happens is that **the very first thing you check is: what all can I do inside this, what can I not do; is there sudo permission or not?**

And normally what is it — **due to security reasons**, somewhere outside, the `sudo` / `su` command is **disabled** for one particular user — meaning, except root, or except the admins, for the rest the `sudo` command is disabled, due to security reasons.

And whenever you are talking about **privilege escalation**, then there, what is it — you check through `sudo`: "can I go inside this particular service or not?"

> **So it's a very important file**, because if any user has to do admin-type work, then their entry is made inside this very file.

---

## Part 2 — The sudoers entry format

So how is the entry made in it? Let me [show]. Give me one minute's time. Okay, sorry for the disturbance.

**Until a normal user's entry is inside this file, they cannot do superuser-type work.** That too is done here. How can you do it — let me tell you.

[Music] Let me show with `cat`. One minute.

Here the entry is made. What do you get from making an entry here: root has [everything]; or there is a **group** — what is this — a group which has all root [privileges]. And `root` is a user, [and] it too gets all [privileges].

Let me explain to you what it means. One minute. Okay.

### The four parts of an entry

Now, **host** — what can it be? For example, it can be **any IP address**; any IP. It depends here for whom you are defining the permission — what you are doing, or for a particular IP; you would be getting to see a particular name.

After that — so here, what is it — **whichever command you want**. Okay, the spelling meant this — here, just for the commands.

And the second one, let me show you: the entry with the **percentage** — let me show you; everything else is the same. Let me do [the one with] the percentage, and here you will get to see [it].

Now, what is it — you would have come to know. Now here, one thing: you can **define permissions in two ways**; you can give it to any user in two ways.

Which two ways do we want? **Our first way** — [by] command, by modifying the permission of [a user]; for that user, grant them the permission.

**The second way — number two** — is with **`%`**; simply, [the percentage] means [a group].

Like, here, what is it — the **root user** is a super user, and the root user has the freedom to do anything on every file.

### Building an entry — worked example

So now what can you do here? Like, let me show you an example: if you have to permit [something] for any normal [user], then what I want to say — like, I had a user, `defronix`. How will I make the entry here?

D-E-F-R-O-N-I-X — the **number two** [style] which in this **allows him to execute the command as another user which already has the permission**.

So `defronix`; after that what will I do — just for now I am defining for **host**; I will use the **equals sign**; then inside it I will do **`root`**, because root is such a user who has all the permissions for [any] file.

And on top of which file do I want to give [it] — basically what we have done is doing it for **all users**, but we want **only root**; [so] I'm doing it in **brackets**. Then, coming to the **commands** —

Now, which commands? **You will have to give its full path** — with the binary file, the command which is inside `/usr`, inside my `bin` directory. Inside `bin` there is a command, `cat`.

First of all, what I want to do — this work: because whichever command's name you mention here, its meaning is that **this particular user has permissions on those commands**.

So now `/usr/bin/cat` — they can use the `cat` command. Well, they can use it normally anyway; but now what is it — **only the `cat` command**, and on which file? Inside `/etc`, the one that is `shadow`, S-H-A-D-O-W — the **shadow file**.

Now, the shadow file — **only the root user can access it**; apart from that nobody can access it, or that user can access it who has been given permission.

Right now what I want to say is: the `defronix` user — the `defronix` user — can **only `cat`** this; they get the permission on the shadow file. But what is it — that `/etc/shadow` file, they can `cat` it.

```
defronix ALL=(root) /usr/bin/cat /etc/shadow
```

### Before the entry

Now what I do — if I show you with `cat`:

```bash
cat /etc/shadow
```

Now what is it saying — **"Permission denied"**; you don't have permission.

### Making the entry

Right here, if I make these entries inside the file, then you will get this permission. How? I will exit, come out of the shell, and simply do `nano` for now:

```bash
nano /etc/sudoers
```

N-A-N-O `nano`, after that enter. **In read-only**, okay. Then, then, then, then — here I [enter] that user's name, `root`, and I want to permit it. Press **Ctrl+X** and do **yes**. [Music]

### Verifying with `sudo -l`

Now look here — you would also be coming to know that what the `defronix` thing is, what all it can do: **if you use `sudo -l`** for any user, you will come to know for that particular [user] what all permissions are defined — whether they can do superuser-type work.

Look here — it has permissions on these two files; so those are those commands, it can use them: these are the files, and one, it can `cat` [this].

Now how do I do it — brother, `sudo`; I do `sudo`, after that what do I do — I do `cat`, and I do `/etc/`, then `shadow`. **You can read it** — now what is it, you can read all the details. Otherwise, without this, you cannot read it.

So let me exit. So from this you would have come to know.

### `visudo` — the safe way to edit

By the way, the `sudoers` file — **you can open it in one more way: `visudo`**. V-I-S-U-D-O — simply, directly. Here [I] am using `nano`; if it is any **Fedora-based system**, then inside that, what it does, it will open it inside the **vi editor**.

---

## Part 3 — `NOPASSWD` and restricting commands

Now what I want to do: the `defronix` user — I don't want to give it permission like that; what I want to say is that we'll give permission inside it. Let me show you — there is one more, a second way.

Simply, what I am doing here — inside this, what about the **password**? What I want is that on whichever command I want to give it permission, on this command **it should not [ask for the] password, should not prompt for the password**; otherwise, if you use it, it will prompt for this user's password, a different user's password.

Right now, why didn't it [prompt]? Because just a few seconds before, what did we do — we entered the password into `sudo`; so for a few seconds it stays in memory.

So now what do I do here — write `passwd`, and after that, then I am saying that **it has permission for all commands, except** — except this command; it can be excepted. Now, **without a password**.

So simply, okay — inside the sudoers file, for this [user] there is this permission: you can do [everything]; for [those] commands you will not be prompted for a password; you can run all commands **except this command**.

So I hope — tell me — you would have understood this: for any normal user, if what you want to do is make a change inside the sudoers file, you can do it like this. You can make any entry here; basically you can write `NOPASSWD`, you can [ban] a particular command, or add those commands.

What I do — I exit. Here, basically, what you can do — if I show you: here it is. For this, what can you do — basically here you can **write the names of those commands** which you want to allow; only write the names of the commands you want to allow, that's it.

And however many commands you write the name of here, then too what will happen — **only those commands will be allowed to them** with the whole machine; otherwise, apart from those commands, no command will be allowed to them.

### ⚠ Don't give ALL

Look, what is it — what you are saying is like root's [entry]. Look, if you write root's `ALL=(ALL:ALL) ALL`, then what — **they would simply become the root user**, in a way, because you gave all the permissions to them.

Then tell me one thing: **what will be the difference between root and a normal user?** Because you are making them a super user.

But **in the real industry, in real life, this does not happen**; no one gives such [complete] permissions to any one user, a normal user.

### The shortcut: the `sudo` group

And if you — simply, I had taught you one thing: how you can add a secondary group for any user, or how you can change someone's primary group.

**If you made any normal user a member of the `sudo` group, then too they will get root-user permissions.** You don't need to do this much [work].

This is basically — when there is the concept of **[OS] hardening**, then those are hardening things. There, what is it: **how much access root has** — meaning, apart from root, who has how much access; all those things — which command will be allowed, which command will not be allowed — all those things are defined right here, for any particular [user].

So tell me this: what I just told, did it become clear or not — for any one normal user? Because here this is the entry:

| Position | What goes there |
|---|---|
| 1 | the **user's name** (or `%group`) |
| 2 | **hosts** — you can write the hostname or mention the **IP address** |
| 3 | the **user's name** you may run as (e.g. `root`) or a **group name** |
| 4 | the **commands** — `ALL` or specific commands |

Here, in place of `ALL` you can also **mention commands**.

If you want that "no, this is my admin user and I have to give permission for these many commands, but it should not prompt for a password" — then what will you do for that? Before that you will mention **`NOPASSWD`**.

Like, if I now do **Ctrl+X**, simply yes. Okay, for all — and here I wrote [the user], and what I want is `NOPASSWD` now, so it should not prompt.

After that here I am writing the names of those commands which are allowed to them. Like, I want — there is a command `fdisk`; like I want that only this command is allowed to them:

```
/usr/sbin/...
```

— you will have to give the **full path**; you have to give the full path. After that `useradd`, `useradd`; and after that, what is it — I can also give them **space-separated**.

And what I want is that they can also change the password. If they have to do root-type work aside — so for that, permission was given, because the requirement was for them to do `useradd`, for this normal [user], and one, to change a password; because someone has to be added, their password has to be changed. So they needed permission on these two binary files.

But for that, what — `NOPASSWD` means it will not prompt for the password. Otherwise, if you simply write it like this — don't [add it] — Ctrl+X, what I'm doing — then **it will prompt for the password**, `defronix`'s.

So this was the way — for any normal user, how you can make an entry for the sudoers file.

Actually, brother, I don't have an example to put up for IP right now, because in the machine there aren't that many IPs available; I don't have more machines, because my machine — that's probably a **sandbox environment**, and I cannot touch the sandbox environment. Because apart from this machine, the free machines I have — three machines — they are running in a sandbox environment; I cannot make changes in their settings to show you practically.

Yes, but do one thing: **you people try this yourself once**, because if you do it yourself you will enjoy it more. [Music] [If] you want, there is an article — you can take a screenshot for yourself.

---

## Part 4 — Giving sudo access to a group (practice task)

So I hope — tell me this, [whether] you understood this now.

Yes, let me tell you one thing: **if you want to do it for a group** — if in your environment some people are working and they need **admin access** for some particular command, for binary files, but they are not one, they are three or four people — then **I will not make an entry for each one**.

Simply, what I will do: **I will create a group**, and after creating the group I will make those three people members of that group. [I] took the example that three people have to do some admin-type work; they need permission, inside the sudoers file. But instead of making three entries, what can I do — I will add them into one group, and I can give the permission to that group too.

How? Like — here it is. How will I do it? Here, we [say] — **practise this yourself once**, you people. [If you ask me to] I will show it by doing it, no issue, but [I'd like] you people to practise it. If it doesn't work out, then tell me; I will show the practical.

### The steps

**Step 1:** Create a group — a group name. [Music] Start it.

**Step 2:** And there, what you have to do is make the entry. Which entry has to be made — where, **with the percentage symbol** and the group's name.

What is [next] — the **root** one, because root is a user; so I am referring to root's [privileges].

Then, what am I doing — I am giving **only these permissions** to it, [so] these three groups — what work can they do: they can add [users], `useradd`, and after that they can define passwords. So I was giving these two permissions, and only [those] — apart from that I am not giving any permission.

**What you have to do** — this is done. Look, "okay, you can only use [those] commands" — and note, you have to find this out.

Look, you can send [it] with a screenshot in the profile, or with a screenshot you can send it over there too: tell what all you did. Tell me, tell me in the chat; it will happen.

Using that, you have to make these three users part of the **secondary group**, and then do [it].

### The verification task

And whatever the recording will be — this is the last minute, you are getting to see: **you have to try the `useradd` command for any one user; you have to change their password.** Apart from this, run one more command and see.

Apart from this — you can verify: there is one more command which a normal user cannot run, the **`fdisk`** command; there is that command. So run it and see whether it is working. **Apart from these two, for these three users, can you do it?** Otherwise... and I have verified. Add [them], and you should not be able to verify it.

There too, do one thing: take a screenshot and send it. Tell me once when it's done.

---

## Part 5 — Password Management

Come on, let's continue; we have a new topic to study, our second one: **password management.** Yes? No? Okay, come on, let's talk, let's continue.

### `passwd` — changing a password

Look, now let's talk about password management. Right now, changing any user's password — for that there is the command [`passwd`].

```bash
passwd              # changes YOUR OWN password
passwd <username>   # changes THAT user's password
```

I want to change its password — simply, the user's name. **If, without a username, you simply fire the command, it will change [your own] password.** If what you do is put the name with `passwd`, then what it will do is change **that username's** password.

Here what will you write — the **new password**; I am adding some new password, [and] after that you have to type it again. This is for the password change.

### What if you forget your password?

Now, in case we forgot our password, then how will we change our password?

Look, what is it — if we forgot the password, [and] you are working in some organization but you forgot your password — then, first thing: if you need your password, then for that what do you need? **To change your password you would need the root user**, which is not given to you.

What you will have to do is **request from your admin authority**: "I forgot the password, please provide me the password." But this [needs] some reason.

Because yes, if you are doing such a job that you look after the Linux admin work itself — [if] you have the root user [access] — then you can change your password in this manner.

---

## Part 6 — The `/etc/shadow` file

But now look, here a small question should come into your mind: **how did the system come to know this password?** From somewhere, actually, the password would be [stored], right? And how — you take the reference: "yes, this is the password"; it has to be stored here. And when you log in with the password, then it **matches**, and [if] this is the password, your login becomes successful.

So how did the system come to know? Let me tell you.

There is a file inside `/etc` — the **shadow** file. And **a normal user has no permission at all on that file; only the root user can access it.**

So which file am I talking about? Let me `cat`:

```bash
cat /etc/shadow
```

Inside `/etc` there is a file, `shadow`, S-H-A-D-O-W — the shadow file, **inside which all the passwords of this machine are stored.** However many users there are, all of their passwords: my root user — this is its password; and my `defronix` user — this password of mine is stored here.

Inside it there are many more entries; what each means, let me tell you in detail.

> **But keep one thing in mind: on this file, only root has permissions; root can access it. Otherwise nobody at all is given access to it.**

### The fields of `/etc/shadow`

Let me explain each of its entries to you. Come on, let's talk about what these mean; let's talk about them. **Very interesting topic** — you're going to enjoy this topic a lot. [Music]

Let me show you on full screen; let me separate it a bit so that all the parameters are understood well once. Let me give this much space — normally there wouldn't be space, but let me show you these parameters separated so you understand well.

1, 2, 3, 4, 5, 6, 7, 8 — these are the entries inside it; what do they mean?

**The first one** you get to see is the **name** entry.

Now let's break this entry down. Now, in this, the first entry in it — from this we come to know **which hashing algorithm** [is used for] hashing the password, and **which salt** [is used]; that information stays in these two.

Now after that, what you get to see next — this is your **encrypted password**; I can call it that, E-N-C-R-Y-P-T-E-D. This is the whole encrypted password; **two pieces of information stay here** in it: one of the hashing algorithm and one of the salt.

Basically, **SHA-512** is being used — basically, because recently SHA-512 algorithm is being used.

Now let's talk next. Next, what you are seeing here, `19536` — what does it mean? It is its **date**. And from where does it count — this is **January 1st** [1970]. And this number that is coming — this is the **number of days**: meaning, the day my password was changed for this machine; that many days ago the password was changed for this machine.

Okay — this is the **last password change date**: when the password was changed for this machine. This has come in number of days.

Here you would be seeing **zero** — what does it mean? Here a zero entry has come. One minute. The entry that has come here — it stays [as] **minimum days**; meaning, that until so many days [you cannot change your password].

Now next — what does this mean? Here its meaning is the **maximum number of days**: meaning, after how many days you have to change the password. [If it says never], meaning you never have to change the password — meaning you were never forced to change the password, that "yes, after these many days you definitely have to change it." That is not mentioned here.

Now, next, the **seven** you are seeing, that you get to see — its meaning is that **so many days beforehand a warning will start**: you have to change the password, because your password is going to expire.

And here, the last one that you get to see — you get the **expiry date** entry. Next you get to see the **inactive** [field] — inactive period. Here the expiry date [is] complete.

1 2 3 4 5 6 7 8 — these are the eight entries. Let me give it serial numbers, then you will understand it well. See — okay, now here it is, this is number three.

| # | Field | Meaning |
|---|---|---|
| 1 | **username** | the account name |
| 2 | **encrypted password** | contains the **hashing algorithm** + **salt** + hash (typically **SHA-512**) |
| 3 | **last password change** | in **days since 1 January 1970** |
| 4 | **minimum days** | how soon you may change it again |
| 5 | **maximum days** | after how many days it must be changed |
| 6 | **warning days** | how many days before expiry the warning starts |
| 7 | **inactive days** | grace period after expiry |
| 8 | **expiry date** | account expiry date |

---

## Part 7 — How the ageing fields work together

Now let me try to explain how it is counted.

**For example:** here, one day my password will be changed — the **last change date**; meaning the day my password was changed. For example, my password was changed just yesterday; for example, my password was changed yesterday.

**Minimum days (`-m`):** now this that you are seeing — **after how many days can I change the password**? After so many days I can change the password. **If here it is zero, what does it mean — at any moment I can change my password.** If a minimum number is mentioned here, its meaning is that **until those many days you cannot change your password**; only after those many days have passed can you change your password.

**Maximum days (`-M`):** now you would be seeing next, days — we set maximum days to **10**. Its meaning is that **after 10 days my password will expire**; after 10 days I definitely have to change the password. That's what this means.

**Warning days (`-W`):** now here, what warning period do I keep? Warning days — I set the warning here; warning days **2**. So its meaning is: as soon as 8 days pass — [since] the password expires in 10 days — it started giving a warning **two days before**: "brother, your password is going to expire, so please change your password." So here, that is what the warning days mean.

**Expiry date:** now here is that expiration date — it comes by itself when you mention maximum days here.

### Inactive days — the forgiveness window

Then, **inactive days** have come. What does this mean?

"Come on, two days are left, so I'll change the password tomorrow." And you thought you'd do it tomorrow, and on that day you didn't get time; you didn't turn on your machine. Or you turned on the machine and thought "okay, I'll do it in the evening, there's still a day left" — and in the evening suddenly some work came up and you left, and you shut down your machine and went, and **you didn't even remember that you have to change the password today.**

So in that case, what will happen? **Your password will expire.**

To save from this thing, what did we do — okay, **a mistake can happen to anyone**. So seeing that thing, what happened here — it mentioned [the inactive field].

So in inactive days, for example, I set **two days**. Okay, so now two days are set here. What does this mean: **that even if you forgot to change the password, after 10 days you have two more days.**

But what are those two more days? **As soon as you log into your machine with the old password, at that same time it will [say]: "this password has expired, please generate a new password."** At that same time you will have to change the second password. As soon as that password is generated, after that, with this password your machine will [work]. That's what it means.

### Crossing the inactive window

Now suppose what you did — on the 11th and after, you didn't log into the machine even for [those] days, and you did not change that password. Now [you] said, "No, I just won't change it; whoever wants to uproot [me], go ahead."

If there is something like that — **if you crossed the inactive days, after that what will happen: your machine's password will expire; you will never be able to log into the machine.**

### Troubleshooting an expired account

Now, once your machine's password expires, [if] you crossed the inactive [period], then how can you troubleshoot it? **You have only two things here:**

1. **You will have to talk to your system administrator** — either they will manually change your password, reset it and give it to you;
2. **Otherwise**, what your system administrator will do is [adjust] this last change date — you will come into this range, in the maximum one, and you will be able to change your password. You will be able to change your password and use the machine again.

The troubleshooting steps were exactly these.

So this was the whole [picture] of password management. **In this manner, inside any Linux machine of yours** — or inside a machine in a server room, which is your real environment, real industry, where passwords are managed — **passwords are managed in this manner.**

**This is also the part of [OS] hardening.** Is it clear to everyone? Tell me; tell me once in the chat. Yes? No? Okay.

---

## Part 8 — `/etc/login.defs`

Come on, now — but before this, let me show you people one thing. Okay, this thing is done.

Now what happens is that all the information — the shadow file information which I just showed you — **where is this information stored?** Where can you see the information? Very easily.

Because the information that's inside `/etc/shadow` — what it did was **number of days**; you will never be able to calculate it, you won't remember it. So if you want to see it in an easy way, for that there is a file in your machine. Let me `cat`:

```bash
cat /etc/login.defs
```

Inside `/etc` there is a file by the name **`login.defs`**. Here you get to see a lot of information.

Basically, **whenever a new user is added in your machine, or you define them, then the default settings inside it — all those settings are taken from here.**

See, so that you come to know what all things are given in it — let me tell you. Here it is, the starting. [Music] Okay okay okay okay okay.

Inside it — look, second, here — with this itself, this information you will come to know: **what your normal [user]'s account ID will be, what the user ID will be, what the group ID will be.** Look here: **UID minimum will be 1000**; okay, and what your maximum will be; and the **system accounts and service accounts** [ranges].

Inside this file a lot is visible — like, here you will get to see that **SHA-512** is being used; in this, the hashing algorithm's **maximum rounds**; a lot — all this information you get to see in it.

**By default, whenever any user is created in your machine** — if you want that in your machine [things are done differently], inside it, if the password ageing that I just showed you with a figure, [you want it] with some changes — if you want that **any new user who comes should have their password changed after 10 days, minimum zero, warning days [so many]** — if you want that, then what will you have to do: **you will have to change the `login.defs` file.**

After that what will happen: **all the new users created in the machine will be created according to this `login.defs` setting.** So **it is a very important file**; now [we] don't need to change it.

---

## Part 9 — `chage` — viewing and changing password ageing

There is one more command for this; [you can] see all this information — but from here the information [comes] quite detailed and quite nicely; now you will get to see clearer information.

Look: **last password change** — when was it done for this machine: **January 27, 2023**. **Password never [expires]. Password inactive. Number of days between password change: zero minimum. Maximum number of days between password change** — you see all these things.

**What is it for you — you neither needed to calculate in days, nor needed to calculate anything.** With the help of the `chage` command, everything is visible.

```bash
chage -l kali        # list password ageing info for a user
```

And **with the help of this command you can also change these parameters now.** How can you do that?

Look, I won't do it by [actually running it], because this is my main attacker machine, my [main] machine; if I change some setting and forget, then there will be a problem for me — because I too have a habit of forgetting many things; if I forgot, there will be a problem.

Next time, what I'll do — inside [a test machine] I will show you how to change it; but if you want, you can practise using it once in your machine. Because with it — [it may] say to change the password, because I have the root [account] problem; because with root I do more tasks, and if I forget once, then [it's] forgotten. **But I will tell you the command, how you have to use it.**

### The `chage` flags

Look, if I do — meaning:

| Flag | Meaning |
|---|---|
| **`-m`** (small) | **minimum** age |
| **`-M`** (capital) | **maximum** age |
| **`-W`** (capital) | **warning** days |
| **`-I`** (capital i) | **inactive** days |
| **`-d 0`** | force password update at next login |
| **`-l`** | **list** current settings |

**Small `m`** means: what minimum age do you want to give? The minimum age — I told you — so here **zero** is the minimum value. If you want to do 1 or 2 — that "[only] after one day; before that it shouldn't be changed" — I don't [want] anything like that; I want minimum age **zero**.

After that, **hyphen capital `M`** means: what maximum age do I want to give? Meaning, I want that my password should **expire after 15 days**; after 15 days, the user should have to change the password.

After that **`-W`** means I want to give **warning days**; `-W`, after that warning days [Music] — how many do I give; I give **seven** days, [or] one day if I want to give that.

Then, after that, **`-I`** — how many do I want to give: **two days**. And after that, for which user do I want to give it — like my `kali`.

```bash
chage -m 0 -M 15 -W 7 -I 2 kali
```

Now, what is this: **after 15 days their password will expire.** If after 15 days — after that there are two more days — [they can] change that password and at the same time [get] a second password to use, and [it stays] with the user. That's what it means: `-m` minimum, `-M` maximum, `-W` warning, `-I` next two days.

### `chage -d 0` — force a change at next login

One more command: if you do this — `chage`, C-H-A-G-E, you used the `chage` command; you used **`-d`**, and if you did **zero**, and after that wrote the username `kali` — **what does this command mean?** Let me explain it to you:

> **It forces the user to update the password on next login.**

```bash
chage -d 0 kali
```

Now, as soon as you — like, today, as soon as you fire this `chage` command in your machine, after that what you did — as soon as you log out from your machine, then when you log in again, at that time **it will tell you that you have to change the password.** That's what this command means.

And what does [the earlier one] mean: that you have **no minimum days** — you can change any time; **after 15 days you have to change**; within 15 days do it any time; **seven days warning period**; your **inactive** [period is set] — and [the rest] for later.

So I hope everyone would have understood this: how you can change any password in your machine, [and] **how password ageing was basically managed**. **Very important topic**; it is used a lot in [OS hardening] settings, and **everywhere in industry you will definitely get to see it**, wherever there is Linux.

---

## Part 10 — Where a user's information lives (three places)

Let me tell you people one thing: **whenever a user is added in your machine:**

| # | Location | What it holds |
|---|---|---|
| 1 | **`/etc/passwd`** | the account record |
| 2 | **`/etc/shadow`** | the password and its ageing |
| 3 | **`/etc/group`** | the user's group entry |

The second place you will get to see is the **shadow** file, S-H-A-D-O-W, inside the shadow file. The third entry — where will you get to see it? In a user's [group] entry.

---

## Part 11 — Disabling / locking a user account

So now let me tell you one thing, a **very important** thing: **how can you disable any user's password?** [How you can] finish that thing — let me show you.

For example, what I do — I do `cat /etc/shadow`; there is a shadow file of mine, S-H-A-D-O-W, the shadow file. [A user] has been working for quite some time; **I want to disable it** — I want to disable this user's password; basically I want to disable this user. How can I do it — because their work is finished?

**You have three ways.**

### Method 1 — edit the shadow file directly ⚠

**The first way:** [Music] Sorry — I will teach you how to use `vi`, don't worry, because in between we [skipped] commands; there are many there too.

What you have to do: when you have to disable this, simply — if you use `vi`, then simply press **`i`** [for] **insert mode**; you would be seeing it. After that, what you have to do is make the change.

So here it is — here my cursor is, right now on the dollar [sign]. Before this, what you have to do: **simply put two bangs (`!!`)** — you added them. And what do you do — after this, [press Esc] on the keyboard, and simply — now what is this, it came into **[command] mode**; then what you have to do [is save].

Now what have you done? If I show you with `cat` — **what you did was disable it.** You disabled it.

Now here [you] are seeing — you see these two signs; what does this mean: **the user will not be able to switch**; meaning, for any reason, **you disabled their password.**

Let me show by switching normally — if [we] can do it. But otherwise, from any other side, [we can] switch inside it, [do] anything at all. Apart from this, if this [user] tries normally, like — let me exit; after that:

```bash
su - defronix
```

D-E-F-R-O-N-I-X, `defronix`. Okay, this means — I type the password; the password is absolutely right. Now what is this — **it stopped; it is showing authentication failure.**

If I show you again — I am putting in the password absolutely right, because what did we do. Okay.

> **⚠ So, one way is this — [but it is not a] good approach**, because if you tamper with the shadow file, [and] made some wrong entry in someone['s record], then your machine will [break]/slow down.

### Method 2 — `usermod -L` / `-U`

What you have to do is **use `usermod`**; after that use **hyphen capital `L`**. Whoever you have to disable — you simply have to take the user's name; like, my user's name is that same one, D-E-F-R-O-N-I-X, `defronix`. Enter:

```bash
usermod -L defronix     # LOCK  (disable)
usermod -U defronix     # UNLOCK (enable)
```

Now in this case it disabled it in the same way. If you want to see [it], then you can check with `cat` — it is already disabled.

If we have to **unlock** it, that is different. Whenever you do — using the `usermod -L` command, [when] you lock [it], then **you will get to see a single bang sign**. Its meaning is that **it got locked.**

Now I have to unlock it — **lock/unlock means disable/enable.** To unlock, simply you will do — I will use **`-U`**, hyphen capital `U`; simply, unlock. Now if I show you with `cat`, here it is — **now it got unlocked.** The difference [you can] shoot [check].

### Method 3 — `passwd -l`

There is one more, a **third** way. Now what will you use — **`passwd`**, after that **hyphen small `l`**, meaning you are locking. Which user — `defronix`:

```bash
passwd -l defronix      # lock
```

I change the password — look at this. Simply, you can do the work.

### Method 4 — remove the shell

If you want to **completely remove any account** — meaning [so that] they can't use it, [so that] they can't get a shell at all — then there is one [more] way. How can you do it?

What you will do: `nano /etc/passwd` — open the file, and come right at the last, where you get [the shell field].

> **If they don't get a shell at all, then what will they do — the user simply won't be able to work**; they won't be able to [log in] to their machine.

So let me do it again like this — [we'll] do it [next time], because in the next class... **Ctrl+X** and `y`, [then] enter.

---

## Wrap-up

This concept would have been understood by you: how it happens in any machine. Basically I wanted to tell you about the **`sudo` command**, and the **sudoers file**, which was the **most important file** — I told you about that, how you can make an entry in it. **Comment to us there on LinkedIn.**

And after that there was **password management**, which I have explained in detail. And do one thing — **your job is to practise.** I will try to answer you.

---

## Doubt session

So right now for you [there's some time]. In two minutes let me tell you — the concept in it will be **File Security**; we will start [that next].

### Q: What if you forget the root password?

Look — if you forgot the root user's password, then what happens is: it's such a Linux machine that **from outside you can crack it**; from outside you can access its password, can reset it.

**At booting time** — in Linux it happens at boot time; you can do it. **In Windows**, what happens — in Windows too you can do it; in Windows what happens is you have to do it **with a Live CD**; so Windows' password too [can be reset] like that.

But in Linux, what is it — either you can **use a Live ISO image**; otherwise what you will have to do: if it's **only** the password problem, then at boot time itself, where some things come for **selection** — the **advanced selection** — you get a few seconds of time there; and it is right there that the thing is, where **you can change root's password** for the machine.

I will teach it; there's nothing [difficult]. **But when you go into a real environment, there are two or three types of protections** — because to get inside that too, a **password is set** there; there, somewhere, security is maintained. **Because otherwise it would become insecure**, [if] it turned out that someone got physical access to your machine, and after that what they did — used a Live ISO image and **reset your root/admin password**.

Very easily it can happen from there. **So to protect from this, again, there is security.** Okay, this type of security is there. So you can do it like that; there's no issue.

But otherwise, in your machine, if before logging in you forgot root's password, then **there is no solution for it.**

### Q: What does the entry format mean again?

Okay, what does it mean here? Here, root's meaning, brother — look here:

- A **percentage** [means a group]; write that **user's name** who has to be given permissions — the work they can do, on their permission they can work.
- Here **root** is such a user who [has access to] the whole machine — meaning, the files and directories or the commands which you require in order to do admin-type work: **who has permission on those? Root.** That's why root's name is written there.
- And there too, what you did — okay, all the work that root can do, [they] will do; after that, in the commands, you put in the [specific commands]: "yes, they have access."

**Meaning: you can use these root-type permissions, but only for these two commands.** These same two commands are allowed to you and all the rest [are not]. That is what it means here.

Tell me more — next. One minute. Okay, then let's get the session over.

And before getting it over, let me remind you once again — [to] you, or the users who will watch the recorded session: **please go to our LinkedIn page**, and as soon as the day's page gets updated, then please go back and take out one minute's time, and tell there what all you people learned in today's day. **Comment there point-wise, point-wise**, so that the [other] people get help there.

So okay, bye bye, good night. See [you] in the next class. Take care.
