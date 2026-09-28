# 007 — Kali Linux Free Capsule Course — Day 7

**Source transcript:** `transcripts/007 - Kali Linux Free Capsule Course - Day 7 [ Hindi ].hi-orig.srt`
**Topics:** User Management · Group Management
**Type:** Verbatim English translation of the spoken Hindi/Hinglish session

> **Note on this transcript:** captions are heavily garbled in places (`लिरिक्स`/`लाइनेक्स`/`नेक्स` = "Linux", `सेल`/`शहर` = "shell", `स`/`एस यू` = `su`, `दास` = `-` (the dash in `su -`), `स्केल`/`सकल`/`स्क्वायर` = `/etc/skel`, `सीटीसी`/`ईटीसी` = `/etc`, `पास डी`/`पावर डी` = `passwd`, `गो अप`/`गुरु जी` = `group`/`groups`, `तेल` = `tail`, `ग्राफ`/`रेप` = `grep`, `जी के पास` = `-G`, `यूजर डेल`/`यू ल` = `userdel`/`groupdel`, `बेस्ट` = "bash", `रेड`/`रेड लाइट` = "Red Hat", `ईटीएफ` = "CTF"). The intended technical term has been restored where unambiguous.

---

[Music] Hello everyone. So tell me once whether my voice is reaching you all or not; please confirm once, after that we will start. Tell me, confirm once quickly. Okay, thank you.

I hope you people [have seen] our last discussion — my [session]. So you people too would have come to know something, [about] the basic doubts you have regarding career, regarding all these things.

And I feel you people would have shared it a lot among your friends, among your [seniors] — whichever student it is who needs it. If you haven't done it, then please share it, because really, that is a serious problem and it should reach everybody, I believe. Because this is not my personal problem, it is everybody's problem.

And I believe that a student should have that video; it should reach them, so that they never get mis-guided going forward, and they get many opportunities and [ask] others for guidance; [they should] try, talk a bit with the family, "I want to talk, want to understand" — that's it.

So **at least try to share the max**; in your group, tell your friend that "you too, share with your friends." The vision we have, what we are trying to achieve — through you people, we can make our vision clear, achieve our target. [It] needs time.

So once again, as always, let me remind you: this is from our YouTube channel; inside the YouTube channel there is the **LinkedIn page** — go to that. And as soon as this day's class is over, after going there, what you have to do: simply go there, the **Day 7 class** will be added on the page, and inside it, go into the comments section and comment there: what you people learned in today's class, whatever topic you learned, whatever you people understood — tell us all those things by commenting.

And thank you — you have given so much love in the last few classes, the way you people are commenting, supporting us. Thanks for that; **we get motivated** when you people tell us such things — comment such things, share, tell others. And it feels good to us, and if you keep sharing like this going forward, more people will come to us, and we will [feel] more motivation, so that we can put better and better, **most affordable** content in front of you.

Most affordable — and **a lot of our hard work goes into making one class ready**. What we are doing, we will do, because we have promised, and we always stand on our promise. We planned a class every other day, and ours has been coming until now. Until there is some problem for us, or a technical [issue], until then our classes will go on; nobody can stop that.

Anyway — so many people are here, 10 to 12 people. So this was basically what I had to tell you first: this is our LinkedIn page; go back [there] so that we can practise.

---

## Why we teach from absolute zero

Okay, so today we will start a new topic. So it's not that... whatever the timing, we have brought out the series **thinking about the future**, because the maximum number of people should get its help.

And we have to pick up such a basic concept for this reason: I know that among these there will be many such people — some will be from my class, some such people who already know Linux. Now they must be getting bored, that's why they don't like coming to the live class. **I understand, yaar** — watching things again takes a lot [of patience]. When I am discussing a command, you must be thinking, "what is this thing going on? Okay, do I know this command or not?"

**That thing should automatically come into your mind.** If in your mind that command comes [to you] perfectly, [fine]; otherwise, if it doesn't come, then think — something is missing, you should definitely do it again. I would advise you — personal advice.

But **we have to deliver from absolutely zero**, because there are also many such people — in a live [session] there are 15 people [but] we have to teach [everyone]. No — we want that when this series stays on YouTube, as long as it stays, then if any modification has to be made in it, we will do it; otherwise there is no need to [redo] this concept.

Whenever anyone comes to our channel, they should go having learned something here — and not feel that "we just [watched]". Looking at the present scenario, you people must be seeing — "I am detailing my thing." No, that is not our motive.

**Our motto is:** in future, whenever anyone takes the help of these videos for their reference, they should see [it as] a straight, direct guide: "yes, I got to learn something." Because **I want to make future-proof things**, and we try to deliver that.

So that is the very thing: you people, you people help me and I will help you.

---

## Why user management is needed

So let's start today's topic: **User Management**. There will be a lot of talk; we should start, because for talking there is [never enough] time — already we have talked for one to one-and-a-half hours with our audience, and we have talked among ourselves.

So, first, let's talk about [the reasoning]. Many departments work [in an organization]: there is a production environment somewhere, somewhere there is a [tech] field, somewhere there is something, somewhere hackers work, somewhere [others] work.

Now, why did the need for user management arise?

Now, like — there is [a] task; like there is development work. So this developer should have permissions only **for this project** — where they have to work, there itself the permission should be. Apart from that, **what will they do with access to the whole server or the whole machine?** Because that is not their job.

Now let me take an example in this [area]: there is the **accounts department**. Now if I give the accounts people the file permissions of the whole tech department as well — is that beneficial? Do you people think [it is]? **No it isn't** — because as much as [they need], that much they use; apart from that, **giving unnecessary permission is useless.**

Let me tell you — that is why there is a requirement: "this is your file requirement, this is your area this much, you work in it; you have these many permissions, do it, we have no problem, you can do any work in this." Like this, [and] the finance people [similarly] — according to their permissions, the user interface has been divided here. **That is why we needed user management.**

---

## Privilege discipline: don't run as root

We [talk about it] in Linux — or talk about any machine, but we will talk about what we are taking [as our example], Linux.

All the **system administrators** who work, all the system administrators who log in — first, into their machine, whether they log in remotely or go to their company and log in — whenever they log in, they [log in as a non-]privileged user.

And what do they do — if there is a requirement for [elevated] user [rights], then what do they do: for that there are some **tools**, there are some **commands**; they use those **to become the root user for a temporary time**, and after that they **exit** again — so that because of them there is no problem in the company or in the system.

Now let me take an example. For example, what did you do — in your machine you logged in as **super user**, or as root user, or as admin. Like right now I have logged into my machine as admin; what did I do here — unnecessarily, as administrator.

So **my whole system will get compromised.** How? Because if there is a **vulnerability** in this system — what should have happened is that if a [normal] user had been there, if the super user were not logged in, then what would happen is that **only that particular user would get compromised**; your whole machine would be saved from being infected.

But what did we do — what's the mistake: we gave **root permission** to everyone. The whole desktop environment — the work is happening only a little bit — and unnecessarily what did we do, we gave them full [privileges], left them as a full admin. So what happened — **you got your entire machine compromised.**

So this is a thing you should keep in mind whenever you use your Linux machine.

### The root user

Now let me tell you one thing. Most operating systems — all of them — have a **super user**, a **root user**, who has all the power over the system.

Meaning, this user is [the one who], if they have to do management work or administration work, then they can **override** the permissions, the privileges of the already-privileged users — the normal privileged users — according to that management or administration. If they feel that "no, this user should not have this permission, they are doing wrong," then that super user can overwrite it, can stop it.

So we say that the root user has **unlimited power**. They can remove any file, delete it, do anything.

So think about one thing: **if someone compromised [the root] account, then that means the whole system and its control went to them.** We can have a lot of problems — [they] completely compromised it; now we are not its owners.

So whenever you play **CTF**, or you give any exam, or do any pen testing — then after enumeration, after scanning, when it comes to [exploitation], when you enter the system from somewhere — even if you enter the system, **a normal task of yours is that you have to become the root user**, because only when you become the root user will you be able to [do things] with that machine; otherwise you won't be able to, because a normal user does not have permissions of that level.

Okay, we will also talk about password-related things.

Brother, don't look at it like "I just want the command, and after that I'll leave" — "I came just now, I want the command, I'll see the command, sir will tell me the command, and I'll go." **No.** We will study the topic properly like this.

**Password management** will come; then too you will come to know how a password is managed. So for now let's start.

Today's topic basically: how to switch [users], how to delete them, how to add a group, how to delete a group. Because it is a very easy topic — some will know it, some will not.

So today this much will be there. After that, in the next class, let me tell you first what our topic will be: [privilege management] — how you have to manage the password, or the files that are in the system, meaning the users' privileges; we will talk a bit about those. So basically your **password management** thing will come — how you can manage their passwords. That will be in the next class, because now slightly interesting things will come; some things you will know, some things you won't.

---

## Identifying users

Come on, let me start. First of all, if what you have to do is: you want to see, **from which user I am logged into the machine** — who the user is, what their name is. If I want to check, then how can I [do it]? For that there is a command:

```bash
whoami
```

The one who has logged in — their name is `root`. If [I do it on the other machine] — then I hit enter, `kali`; that's its normal [user].

### `who` — who is logged in

Now if I want **detailed information** — if we want to see who all have logged into our machine, and from where they did it — for that there is a command:

```bash
who
```

Now this told [us] that right now in your machine there is only one user, who is `kali`, and they have used terminal `tty7`; they have been logged in for this much timing, [with] this information — it showed this on your screen.

### `w` — what each user is doing

If you want to see **which user is doing what** in your machine, for seeing that there is the command:

```bash
w
```

Now you will come to know which user is doing what work in your machine. Now see: `kali` is the user, they logged in at that time — they have been logged into this machine since 19:13; idle was 2 minutes 30 seconds. Apart from that... [it's an] actual machine. If you fire the `w` command on it, then you will come to know which user is logged in from where. You will get this information here.

### `id` — user and group IDs

Now let's talk: if I need information about a particular user, then how is it obtained? There is a command:

```bash
id
```

If I wrote the `id` command, here you get to see a lot of information: what this user `kali`'s **user ID** is, what its **group ID** is, and which groups it is a part of. So its groups are — one is the `kali` group, there is the `adm` group, `cdrom`, `floppy`, `sudo`, `audio` — it is a **member** of all these groups. So you will be getting to see all these things.

If I want to see the information of some particular user — like I do — and in my machine there is one more user, M-A-N-I-S-H, `manish`. Now see its information — if we see the information, then look: this is its user ID, this is its group ID, this is its group. So you got to see this information, detailed information.

```bash
id manish
```

### A note on Red Hat / SELinux

If this same thing — if I tell you beforehand as well — if you are using a **Red Hat** machine, or using **CentOS**, if you enter this information, then here one more thing comes: it comes as **SELinux context**.

In Red Hat–type things, what happens is that there is a **security context** — meaning, one more **layer** works for security on top of the operating system. That one thing, it is a very powerful thing, because it keeps your whole system **isolated** in a way.

Its permissions are so dangerous — let me tell you first — [such] good permissions are so strict that in it it's straightforward: **if in the rule it is yes, then you will do that work; if it is no, then no matter what anyone tries, it won't happen**, because it is very strict.

That is why the industry prefers Red Hat more, because its **security policies are very tight**. In it, after one layer, a second security comes. Then in the industry the firewall comes, antivirus comes, after that IDS comes, IPS comes — all these things come. So it becomes trouble for hackers; that's why.

### Why root's UID is 0

Arre — **what is UID?** User ID. For root, `0` will come, because the **admin** in your machine, the super user, their user ID is **zero**.

[Zeros] will come because **root is the super user** and the very first user — root, the super user, their ID is zero. That's why its ID is coming as zero.

---

## `su` — switching users

Now let's continue. Someone in the group — I had seen in our **Telegram group**, someone had asked something: "sir, here I get to see this in one, and in another I get to see the full [path]." Now, look — that thing will be understood here.

Now let me tell you one thing: if you have to **switch from one user account to another user account**, there is a command — the **`su`** command.

### Login shell vs non-login shell

Does it provide you a **login shell**? When a new user logs into your machine — or when we log in from some particular user — then it has its own **environment**.

Remember one thing about any user: **whether it is the root user or anyone at all, they need an environment to run.** Understand? They need an environment, and that environment is defined in your machine.

Whenever a new user in your machine — meaning a new user is created — so whenever a new [user logs in], like what you do at the start, [the] entry — there a login runs, username and password. That we call the **login shell**.

**And what is a non-login shell?** What happened there is that whenever you [switch] — the login shell [is one thing]; the non-login shell is what: it did [this] — that when you switch, in the non-login shell it will prompt for a password to switch into that user, but what happened is that it used the **shell in which you were presently working**.

### `$SHLVL` — shell level

What happens is that if [you want to know] which shell I am working in, for that there is a command. If you have to check your shell level, then for that there is a command: `echo $SHLVL`.

Look, the [value] it is showing you right now — this shell level — this is [one], meaning this is one single shell. If you log in inside this, or [if] it opens one more second shell, then here what is it — its quantity, the number, **increases**; it becomes from `1` to `2` — meaning inside one shell you have opened a second shell.

### Summary of the two

So simply you understood: what is a login shell and a non-login shell?

- **Login shell** is when a new user enters your machine: they put in a login password; after that, what happens is that they have an **environment**, they have **environment variables** which they need in order to run — they log in with those.
- **In a non-login shell**, what you do is: the user account you were working with — when you switch to some other account, then you use it **without the `-` option**, so you are **just acting as** that user; but the environment, the environment variables, the environment being used is that of the **earlier user**.

Again I am repeating: **with only the `su` command, if you switch, what you are doing is acting like that user** — but the whole environment which the earlier user had set up, the environment you were on earlier, you are using that whole thing. Meaning you are not permanently logging into it.

Basically, if you use [`su -`], what does this mean — **you are permanently logging in.** Meaning, like when you switched on the machine, the login screen came, you put in the login username/password, after that you enter with your environment variables — that type of environment, this provides; you log in in that type. So this was the difference between these two.

### The demonstration

And what my brother — someone had asked me the other day in the group: "Sir, why do we get to see it like this?"

Like, now here what is it — I did `su`; I did `su` and simply what did I do — straight, without the dash. Now here what do we do — I put in my password.

Now here [someone] said, "Sir, why does it show like this here?" Because understand this thing: **it is acting**, the `su` command. Here I did not write the user's name. Why didn't I write it? Because **by default, if you don't define it, then by default it considers it the root user.**

So what did it do — this is the root user, **but the environment variables it is using are those of the `kali` user**; it is using the `kali` user's environment variables. And that is why it came here that I am in the home directory of `kali` and not in my [own] home directory, of root.

That is why it is showing you this present working directory here — because here you have used only the normal `su` command.

If what I do here is **exit** — now I directly do:

```bash
su - root
```

I wrote `root`. If I write the full [thing], enter — because now it has **permanently shifted** inside it, into that user account which is the root user. Now what is it — this is its own account, it is using its own environment variables. Now **it is not acting; now it is permanent.**

This thing would be understood — what the `su` command means.

> **Summary:** `su <user>` — you are **acting as** that user, not fully that user. `su - <user>` — you enter **totally as** that user, environment and all.

"Sir, your comments..." — I will take [them] at the end. No, I say 5 minutes; so the doubts you have, [we'll] ask once — the last 5 minutes I will provide to you. Because right now the concept is [flowing] — I would get differentiated a bit, so there will be a problem, because the flow will break.

---

## The `/etc/passwd` file

So now let's talk. I explained to you how to use the `su` command; how you can use [it] — or do it and see, you will come to know. The difference is correct; I showed it in front of you.

`sudo` — simply, if you do `su`, then you are acting as them; you are not fully that user. If with `-` you enter as some user, it means **totally you are entering as that user** — meaning, regarding the environment.

Now I feel I don't need to show you more practically about this. If [I] need to — okay, let me do one thing and show you. I exit, simply I do `ls`; here it is. Now here there is `ls`, `.bash_profile`. Okay, is there something here? A file. Okay okay okay okay okay.

Let me do it again. Leave it — `su`, I do `ls`; here I am not getting to see anything. [Music] I'm not finding that thing; I am trying to show you, because my machine is a bit **modified** — I have made a few changes in it. Okay, anyway, the concept [is clear].

[There are things] to be taught related to that too, so we are going to discuss that too. So come on, then let's continue; we won't waste time.

### Understanding the entry format

**How is a user managed?** How is a user managed? So, like, there is a file — let me try to understand: this whole entry, what is it? Because if you have to do user management, then **it is very, very necessary for you to understand this entry.**

Let me do one thing once — this... okay, then, guess. Yes. Okay.

**Password** — because earlier [the password] used to be [here], but **due to security reasons**, in its place, inside `/etc` a **shadow file** is seen.

After that, we do — its **third entry** that you would be seeing — you get [it]. What does this mean? This is showing you that **this is your user ID**. User ID — every single user has their own unique [ID]. When [it] is a unique ID — whenever a user is created in your machine, its ID is assigned to it accordingly.

Next you get to see one more, `1102` — this is showing its **GID, group ID**; it is representing the group ID.

Next what you get to see — let me [show] here; here the space that appeared, here what happens — right now let me [replace] the space; here it is. Okay.

The entry here, the location entry — [is for] **comments**. What does comment mean: that if you want to keep some tag for this `manish` user, [some note] so that you remember "yes, this is for this purpose" — if you want to give some such comment, then you get to see it inside this.

Next you get to see `/home/manish` — `manish`. If you get to see this, what does this mean, or what does it represent? It represents the **location of the home directory**: what this user's home directory is.

[Then the] location of which **shell** — meaning, in the machine where you work, when you switch into it, which shell it will [give] — this information is here.

These are all the entries, which I have written in detail on this [board]. I hope everyone would be understanding.

### The seven fields of `/etc/passwd`

| # | Field | Meaning |
|---|---|---|
| 1 | username | the user's name |
| 2 | password | now just `x` — the real hash moved to `/etc/shadow` **for security reasons** |
| 3 | **UID** | user ID — unique per user |
| 4 | **GID** | group ID |
| 5 | comment | a descriptive tag for the account |
| 6 | home directory | location of the user's home |
| 7 | shell | which shell they get on login |

---

## `useradd` — creating users

Now keep one thing in mind: whenever you add a user... now this is [what] I've told you. Let me tell you — so I hope... let me [close] this now; let me shut it down.

Now, **normally, how do we add a user?** What I did — first I added a user:

```bash
useradd user1
```

`useradd`, and I wrote `user1`; simply hit enter. Now I added it; I simply wrote it.

Now what will you do — when I do `tail`, and I want to see the last two entries of the `/etc/passwd` file — in this file its entry gets made:

```bash
tail -2 /etc/passwd
```

Enter. Here you get to see: `user1`, password [`x`], `1004` — this is its ID; we did not give a comment in it; this is its home directory; this is its shell — whichever it is; for that, the defined environment variables are [used]; so it assigned it. If you want, you can change it.

### Best practice: specify details explicitly

But what happens — let me advise you one thing: **whenever you add any user, you should mention its full detail information**, as much as you think [necessary].

It is possible that you added it here, and the directory you have — from where by default these things come — there may be something wrong with it, or there may be some problems; so it's possible that because of that some things won't get changed with it — which basically is its **home directory**, its **shell**, some **comment**, its name — all these things.

If, keeping this in mind, you do it modified right from the start — if you add [it] fully — then you will get its benefit nicely, because it's possible that if there is some problem, then [it] will cause a problem.

Like, what do I want to say: I added a user whose name is `user2`; I want to add it. But now what I want to say is — meaning, **modified permission** — I don't want the default one; the one I said earlier, modified — put that permission, [and] after that whatever is left, by default, you add that in it.

**Modify option `-d`** — I want the home directory; which one do I want to give? Simply `/home`, [and] I'll go; inside home, which one — I want to keep `user2` itself. After that **`-c`** — `-c` means I want to give a **comment**; what comment do I want to give? See, this is its home directory; you would be getting to see it here.

```bash
useradd -d /home/user2 -c "comment" -s /bin/bash user2
```

So in this manner — **this is the best way you should do it.**

---

## `/etc/default/useradd` — where the defaults come from

And after that, now what happens is — so this is what I told you: whenever we add any user, automatically the system [does things]. Now I saw that even modified, [but] still a lot of things will come in front of it.

If you want to see **where these default entries came from** — if you want to see this thing, then for that there is a directory. Let me `cat`: inside `/etc` there is a directory named `default`, and inside it there is this [`useradd` file]; inside it those things are defined.

Whenever any new [user] will be added, then by default what things will come onto it:

- Like, [for a] normal user, what is its **default shell** — `/bin/sh` will come, the one that came to us.
- After that, what will its starting be — `100`, whoever gave it. After that 1 2 3 4... [IDs below that are reserved] for the system.
- **Group** — and how its home directory will be stored: look, it will be `/home`, after that its name.
- After that, what is this — **number of days after your password [is] disabled.** Now this is saying that whenever any new user is added, then do you want to fix its password so that after so many days it expires? Here it is written **`-1`** — this will **never expire**.
- Now, **default expiry date**: up to now, what we have — this user we added has no expiry date added; meaning by default there isn't one.
- And there is one more thing here — this thing, **`SKEL`**, the skeleton requirement. I will tell you a bit about this in a little while.

Basically, in a **skel directory**, what things are there — let me just [take] a bit; two concepts along the way. Right now, [about] `skel`, in a small [aside] I will tell you — so it picks up some things from that skel directory.

So all these things, by default, whenever you add a user — it uses all those details from here and after that they get added automatically with this command. Because here there is a **binary**; a program has been [written], and in that program it is written from where you have to take what thing by default. If a modify [option] comes, then first add that, and after that [take] the [rest]. That is what the program means.

I hope everyone would be understanding up to here — what I did and what I was trying to do here.

---

## `usermod` — modifying users

Let me tell you one thing: if you want to modify any user — if you want to modify some user's details — simply, like I do `tail`: what I want is that `/bin/...` — this one, I want to give it the `bash` shell, [and] I want to modify it. So how will you do it?

Simply you will do the command **`usermod`** — `usermod` means you want to do a modification of the user:

```bash
usermod -c "This is my demo" -s /bin/bash user2
```

- **`-c`** means — what comment do you want to give? One, I want to add a comment; what is the comment — "this is my demo".
- For the **shell** — I want to modify it; after that the **user's name** — what is the user's name, `user2`. Simply hit enter.

Now if you see this information with the `tail` command, you will get to see it. Yes — this was `user2`, "this is my demo", bash shell; then this is its home directory; this, its shell, got changed.

So in this manner you can use the `usermod` command — you can make modifications in it.

And what all options you can use with it — for that there is [`--help`]. As you start using it, like that [you'll learn].

---

## `userdel` — deleting users

For that there is the command [`userdel`]. I did `userdel`. Now what do I do — if I `cd` into [the home] directory, here I do `ls`.

Look here, what did I do — **I deleted `user2`; still, here you get to see `user2`'s home directory.** Why? Because [of] what happened — it deleted the user from the system; **the user got deleted from the system, but its home account has still not been deleted; its home directory has still not been deleted.**

If you want to delete its home directory too along with it, then how will you do it?

```bash
userdel -r user1
```

Okay — if you use it, then what will happen: **it will be deleted along with the home directory.**

### ⚠ Security warning about deleting users

Now here, one thing — understand this as a warning from my side; you will get to see this thing in many books too. **You have to keep this in mind whenever you are deleting any user**, especially:

**First point:** whenever you are going to delete any user, **first check their home directory** — whether there is something important in it or not. Whether there is some important thing in it or not. If you feel there is something specifically important, then **transfer it**. If it is useless stuff, if you feel that no problem will happen from deleting it, then what you have to do is delete it, applying `-r`.

### Why it matters — the UID reuse attack

Now, what problem can happen because of this? Further: **without `-r`**, without specifying the option, if you delete any user, then if there is some **sensitive information** in their directory, it **stays there** — because the directory's information is left behind, [and] the user has been deleted.

And remember one thing: **whenever a user is deleted, the ID that was assigned to them, the UID — that becomes free.** But the home directory is still [there]; the home directory is also still created, and in it there is sensitive information.

So here there is a **security point**: this can **lead to sensitive information leakage** and other security [issues].

How does it happen? Whenever you add any new user, the ID that is assigned to them is assigned [as] the **first free ID in the system**. It's possible that when you defined the user, by default [it took it]; and it's possible that the username too seemed almost the same to you.

So it's possible that what the system did is: **the ID that was defined for that deleted user, which got released — it assigned that ID to this [new user].** So the files that were in the [old] user's home directory, the permissions of their files — those will get updated with the permissions of the newly assigned/added [user].

So this simply means that **the sensitive information of [the old user] can be accessed by the newly added user** to whom that ID is being assigned. Here this can be a **security issue**.

**Second:** whenever you can add [a user] — until you define the `-u` option with it, until then you cannot manually assign an ID; by default it takes [one]. So that's why, here, this sensitive information [risk].

### The attack scenario

Now, it's possible that... suppose I am attacking; I [gained access] — I used [some] technique and somehow or other I became a normal user. And I went into [a] user's home directory; there I got to see some entries: "okay, there are users."

And what I [did] is try to **find** — there is a command, `find`, a command — and with that command, [I check] what that user has access to; [I] tried: "in the whole root partition, is there any file lying which has **no owner**, no UID?"

It turned out: "okay, a user was found." So what will it do — [an attacker] can [exploit] adding a new user.

### Two solutions

So here there are two options; according to the situation you have two solutions:

1. **One solution** is: extract its data and delete it.
2. **Second**, manually: **transfer the data.** If you are leaving something like that, or you have to do it, then **change its name completely**, assign it to someone else.

For showing practically — bro, right now I think we don't have that much time, but **I will try my best**: whenever we have time left, I will try to show you the practical. Okay, I will [try].

Because in the capsule course I have to get a lot done for you; [there's] a lot to get done. Do one thing: **first try it yourself**; if you people can't do it, then [tell us] in the [session], after that we can try — what we have to do. Okay, after that we can try.

So now let's talk, let's continue. So you came to know how you have to modify any user, how to delete it, how [to handle] which things inside it, what to keep in mind.

---

## `/etc/skel` — the skeleton directory

Now I talk about — there was talk of a directory; which one is it? **What is this?**

Whenever we create any new user account in our machine, then **a lot of the contents which are inside this directory get copied automatically into your user account's directory.**

Meaning what — when a user will be created, then a **framework** is prepared for them: these things were the requirement, these things should be with them.

Or, what did you do — you are doing the duty of an admin account, administrator, and [at your] LAN extension; and when you don't [go there] completely, then your [organization] said, "this is your user ID; through this too you can work in your machine."

Now the system's policy for using it — you won't go and tell that to everyone; either it will be in your letter, otherwise what happens is that when you log in, there some **news** [message] will come along for [the day]: what you have to do, what you don't have to do.

So where does that thing stay? Where does that thing stay? That thing [stays in] the **skel directory**, and there are some **profile files**; it stays mentioned inside those.

As soon as your account is created, those by default get loaded into your account. Whenever you use that machine [there is] a warning post — all these things come by default from here itself.

So the environment [of a certain type] by default, which is needed to do any particular work, stays **defined inside the skel directory**.

The skel directory — if I do `cd`, `cd /etc/`, and [`skel`]... All these things by default are — what — your home [directory's].

Let me do one thing, let me `cd`. Look, these things which are the bash ones — automatically they have come along with it. Why did they come along with it? **Because these things were mentioned in the skel directory**, so all of them will come into this.

If you don't believe it, then let me do this: in front of you, let me add a user; I keep its name — right now I keep [one] — and simply hit enter.

Now I switch — where am I? Change directory to the home directory. Okay, let's exit; we'll have to look at this. Its password is not mentioned yet.

So right now, what I have — let me do `tail`; I have the `manish` one. [Music] I am doing `sudo su` and `manish`, and inside it. So I will do `pwd` — root is mine. Then `cd` — I go into its [directory]. And [`cd`] to home. Yes, yes, yes, yes — `pwd`. Okay, `/home/kali`. Okay, there's a problem, because [if] you do [the] security [switch], you will get to see it.

Let me exit, and in `kali` let me do `ls`. Look, here too you will get to see that skel directory thing: `.bash_logout`, `.bashrc`, `.profile` — you will get to see it here too.

So these things were inside the [skel] directory. So in this manner we can [do it].

---

## Group Management

Now let me show you: if some group has to be added, how can we do it? Because let's do it today, it will happen in 10 minutes — because if we don't do it today, then unnecessarily we'll have to study again; inside this itself we'll be able to start the topic tomorrow. So shall we do it together? Tell me in the comments — **group management**, local group management, how we do it. It won't take much time. Tell me, tell me.

### Why groups are needed

Come on, look. Now let's talk about group management. Now, look, what happens —

So I would not do that; instead of giving this, what can I do — simply I will say: **I will make a group** of those people, and in that group, however many members there will be, [for] those members I will define permissions on those particular files — [whether] there are five files, six files, or seven. And **that file's group**, or the directory's group — I will add that group into it.

So what will happen from that: the permission of the files that were inside that directory or that project will be given to all those members **at once**. And if I have to add anyone in future, simply I will make [them] a member of that group. And if [I decide] "no, now their work — now there is no need for this" — both [ways], simply I will **remove** that person, that member, from this group.

So all the work will become easy. **Why would I give permission 100 times, and remove the permission 100 times?** That's a big task.

### The two types of group

So for this, in your machine there are **two types of groups**:

1. **Primary group**
2. **Secondary group**

**Which one is the primary group** — [every user] is a member of their own primary group, and that primary group is created **with their own name**.

**A secondary group** is the group we create according to our convenience, and what do we do — we add other members inside it, so that work can be done according to that project.

### The `/etc/group` file

If [you] have to see the information, then what can I do — simply I did `tail`, I did `-5`, and inside `/etc` there is also a **group** file; there is a file, `group`:

```bash
tail -5 /etc/group
```

Look, here the information stays. What is this — this is a group; because the [name] is the same, [it's] the same — **primary group**. What is the group ID? If there are secondary groups, you will get to see them here; here you will get to see the secondary groups.

If I show you `kali`'s — if I do `cat /etc/group`, `kali` — because already it was a member of a lot of groups. Group, after that what do I do — I do `grep`, do `group`, `kali`, in it. And okay, then I hit enter.

Now look at so many things: look, `kali` is a group and all these are its members; this too is a group — look, `scanner` [etc.]. Take out boxes like this.

So in this manner — this is `kali`'s, or [it got] assigned when you were doing the configuration; according to the machine it got added. So basically you get to see the information of the **secondary groups** here, and here you get to see the **primary group**.

### `groups` — which groups am I in?

Let me tell one thing here: **you can add any one user into multiple groups, and those will be called their secondary groups** — of any user. And if you want, you can change their **primary group** too.

If I [want] to see which groups I am a member of — [I am] root, like what I did — then for checking this there is a command:

```bash
groups
```

And hit [enter] — so these are all members of their own group. If I [want to see] `kali`, which is my user — [to see] which groups you are a member of — simply I will do:

```bash
groups kali
```

G-R-O-U-P-S `groups`, and the group's name... the `kali` user — whatever your `kali` user is — that: `kali`, `adm`, `dialout`, `cdrom`, [and so on] — the ones we had seen with the `id` command. [Music] It is a member of this many groups — you will get to see which groups you are a member of.

### `groupadd` — creating a group

If what you have to do is add any group in your machine, how can you do that?

```bash
groupadd UNIX
```

G-R-O-U-P `groupadd` — the command's name — and I wrote the group's name, `UNIX`. `UNIX` — I wrote the group's name in **capitals**.

And if [I want] to see this, then what will I do:

```bash
tail -2 /etc/group
```

`tail -2 /etc/group` — and before `tail`, what do I do — I have to see the last two lines, so hit enter. Look — now `UNIX` is there; this is the group.

Now `UNIX` is indeed a group; whether it has any user or not, [it exists] — but what will come: it **has no members yet**. Okay, so this group has been added; you would have come to know.

### `usermod -aG` — adding a user to a secondary group

If I show this — let me do one thing. If I do `tail`, and what do I do — I [see] here, `UNIX` is not assigned [to anyone], because there's no user by such a name.

Now what I want to do: `sachin2` — the `sachin2` user is appearing on your screen. What I want to do with it — **I want to make it a member of this group**; meaning, what I want to do with `sachin2` is add it to the **secondary group** — I want to add it as a secondary [member]. How will I do it?

For that there is the command **`usermod`** — because you are making a modification in the user, so `usermod`:

```bash
usermod -aG UNIX sachin2
```

- the **`-a`** option
- the **capital `-G`** option

### ⚠ The `-a` flag is mandatory

**Keep one thing in mind here: the `-a` option is mandatory**, whenever you simply want to make one user a member of some group.

Why? If what you want to do is simply [make] a user a member of some group [while keeping the existing ones] — [then you need `-a`]. [Otherwise, if you want] to **remove all the existing groups** — remove them all, delete them; meaning not delete them [entirely], but for this user remove all those groups, and add only this group, [making them] a member of only this — if you want to do that, then simply what will you do: **remove the `-a` option**.

So what will happen: it will **remove all the existing groups** and make them a member of the new group.

Look, what I [did]: with `-G` I wrote `UNIX`, and its name, `sachin`, and I will hit enter. Now what it did — it added the secondary [group]. What it does — [if] it doesn't use the `-a` option, what happens is that **it will override them** with the new group.

So you can do that too. Okay, so you would have come to know how to add a group and how to add [a user] to their secondary group.

### `usermod -g` — changing the primary group

Now if what I want to do is **change someone's primary group**...

Like, what I want to say — I am doing `cat`; not `cat`, I am doing `tail`. `tail`, what did I do, `-5`, and after that I am saying `/etc/passwd`. Hit enter — and the `sachin2` I have, which is its primary group? This ID of its is `1055`.

Now what I want to say is: I want to change its primary group itself. If I want to change its primary group, for that the command will be:

```bash
usermod -g UNIX sachin2
```

`usermod` — I will not use `-G`; **I will use small `g`** for changing the primary group. After that `UNIX`, and its group's name.

Let's see — so its primary group too will have changed. Look, it will come as `105`/`106`. If I want to look over there, [I] can check with `group` — it will have changed.

If I do — your `UNIX`, and the secondary group is `c`... [so] its `UNIX` [is now primary]. So this is [how] you change its primary group.

> **Summary:** `usermod -aG <group> <user>` — **add** a secondary group (keep existing). `usermod -G <group> <user>` — **replace** all secondary groups. `usermod -g <group> <user>` — change the **primary** group.

### `groupmod -n` — renaming a group

But let me tell you one thing: **if you have to make a modification in a group** — for example, I have to change the group's name — how will I do that? For that there is:

```bash
groupmod -n unix UNIX
```

`groupmod`, after that **`-n`** — meaning I want to give it a **new name**, of the group. And, like, as the new name, what do I want to give — I want to give `unix`. And which group's name — `U-N-I-X`.

The new name you will get to see — that will remain. You [do] `tail`; now its name has changed. Its name got changed.

In this manner you can also do modification of any group. If I show you `groupmod --help`, then simply — all these options with which you can use it; the one I used, `new` means new group name. This you know.

### `groupdel` — deleting a group

If you have to delete any group, how will you do it? So there is the **`groupdel`** command; after that, like, the group's name, `unix`. Enter.

Now it said **"cannot remove the group"**. Why?

> **⚠ Keep one thing in mind: whenever you delete any group, that group must not be the primary group of any user.** If it is the primary group of any user, then you cannot delete that group. First you have to change their primary group.

So how will I do it? Okay, `sachin2`; after that I changed it.

Now if I want to delete — sorry bro — now what is this: your group will get deleted, `unix`, [because] it is no longer its primary member. Now here you will not get to see the group named `unix`.

In this manner you can delete any user — but the thing you have to keep in mind is that **it should not be their primary group**; otherwise you will not be able to delete the group.

---

## Recap of today

So this was ours:

- How to add a user
- How to add a group
- How to delete any group
- How to delete any [user]
- How to make [a user] a member, part of another secondary group
- How to change any user's primary group
- And if you delete a group, what problem came in front of you, [and] how you can do it
- How to modify any group, or how to modify any user

These were four or five commands which I told you.

Secondly, if you are deleting a user, then you have to **specially keep `-r` in mind**; and keeping [that] in mind, you also have to keep in mind whether that is sensitive information for you or not. **If there is sensitive information inside it, then first transfer that information** — otherwise you will say "you taught us and [we] directly did the `-r` option", and because of that the [sensitive] data inside got deleted.

All these things — you would have got to learn something in today's class. I hope it became clear to everyone, everyone would have understood. Okay, because there was nothing confusing; it was very straight and forward.

---

## Doubt session

If even then something is not understood, then there are 5 minutes for you; right now there's a 5-minute doubt session, so you can ask right now. Open.

Again, if you people feel that I am teaching you well and [giving] valuable information for you people — please, please, **it's my request, humble request**: if you people want good content from me and want to study well from me, then what you people have to do is **share this**; it should reach the maximum people who need it.

[Especially] those who have absolutely no money, who are running things just from a phone — absolutely, absolutely, people in [that] category who feel that they won't be able to do it. So please, please — in today's time everyone has internet. Please, it's my request, personal request.

Because **my vision, my mission** — my mission is to reach those people who really need me. I want to help them from the heart. Because those people [who have resources] will get help anyway; they'll get help from somewhere — those who know something, or who somewhere have some backup, can do something. **But what about those people who absolutely, absolutely cannot** — those who have nothing at all, no sources at all? And we are thinking of helping them.

So please, our thinking has come [to this]. Look, the more you people spread it, the more you tell people, the more you tell everybody — from this, people will know about us; from this, you people [help] us, because we have taught you. You people tell others. Please, look — it's a good thing, and [it's a] guide thing.

Because let me tell you one thing: when we conduct further classes, on some other topic, then **again and again this thing will be compared** — because I have made your fundamentals [strong], of Linux, because now you are going to need this in every single thing.

And if you haven't learned this properly now — I am telling you, if you do **pen testing** too, then **again and again you will need to come here**, will have to learn. I have seen; those who worked with me — okay, those who did the fundamentals — like, when attacks happen, then the thing is understood: "what is this thing, does this file have this thing, this is there" — all these things stay. So we know that thing. **That's why** — please, simple request. So you people, next, try that it reaches the maximum number of people.

### Q: Explain groups briefly once more

"What is it — explain groups briefly once, give it." A bit — [let me] show, bro, **why the need arose**.

Look, what happens is that if in a company, in an organization, **1000 people are working** — 1000 people are working — out of whom **50 people are working on some project**. And that project is: [it] is being used on your machine; and there, what is it — **to work in that project there are 30 to 40 files** on which they should have access; they have to work [on them].

So what is it — but what is it: there are 40 to 50 people who are all different; all of them need [access]. So **you people tell me**: will I define separate access for those 50 people for those 15 to 20 — or the 35 files that are there? **Every time, give permission on that file for that user?**

**Is it possible in a real scenario? Not possible.** Because doing so is [not] possible — one, you won't be able to monitor all of them, who is doing what; second, it is **time consuming** — nobody has that much time.

So a solution for that was found: **why don't we do one thing — we make a group of the 50 people**, and to that group we give the permissions; we make [those] people members of that group. And the files that there will be, 34–35, like some files which are for working in that project — the permissions needed on those files for those particular 50 members...

**We will make a group of those files** — the group of 50 people. **We can change the group of any file too**; the file's ownership, whichever group it has, we can change that too — `root` and `root` is what you get to see, so we can change that.

What we will do: we will change the group of the [relevant] files, and put in that group's name — the one to whom the permissions have to be given.

So what will happen from this — a **security** [posture] will be maintained; 50 people will remain monitored; and you won't have to give permission to someone on 25 to 35 files every single time.

If a 51st or 52nd person also comes, then simply what will you do — you will make them a member. Tomorrow if you feel that "no, this one member should not remain with us, we [want to] take them out," then you will simply take them out — rather than limiting each individual's access on the file.

**That is the reason to make the group.**

I hope, Ojha ji, it would have become clear to you. Is groups still not clear? Tell me please, tell me in the chat.
