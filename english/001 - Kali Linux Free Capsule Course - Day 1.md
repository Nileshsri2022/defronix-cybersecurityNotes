# 001 — Kali Linux Free Capsule Course — Day 1

**Source transcript:** `transcripts/001 - Kali Linux Free Capsule Course - Day 1 [ Hindi ].hi-orig.srt`
**Type:** Verbatim English translation of the spoken Hindi/Hinglish session

---

Hi, good evening everyone. This is Sachin, CEO of Defronix Cyber Security Private Limited company, and also the trainer of this capsule course.

So, in the last class — previously — what happened is that we had uploaded a video on our channel: "Installation of Kali Linux." Okay? So you can watch it from there, how you can install Kali Linux inside our machine. It has been shown to you live, in a recorded session. So I hope that you people will go to our Defronix Academy channel and you can get information about it there — and how to install it. Okay?

So today, basically, what I am going to teach you people is the History of Linux. Okay? And the second topic I am going to teach is Data Storage Planning of Linux. Both are very important topics, because before studying anything, it is very, very necessary to know a little of its history. Okay? Until we know about its history, we cannot properly understand why I am studying this thing — and I mean, a little bit of background work is necessary.

After that we will talk about Data Storage Planning. Okay? Why is it necessary to study Data Storage Planning in Linux? Because, look — what do we do? Up to now in Linux, whether someone is a beginner, or someone is advanced, or someone is intermediate — if they have come to the channel, then it is necessary for everyone. Because some people do this: there are a lot of people who know Linux, who know about commands, who know everything, but the thing is that still they don't know about the data storage plan. So we blindly create any file anywhere in Linux, we create any directory anywhere, and after that they don't have any permission there — nothing special is there. Okay? And they start working there.

Now what happens because of that is that permission will not be granted, and what do people do? They call Linux frustration — "we got frustrated, we don't understand why I created a file here and why it is not running." Because actually, Linux has a data storage planning. Okay? Actually, in Linux, which file should we create where — the planning that is there by default inside it — until you know about that, whether you are a Linux admin or whether you are a cyber security engineer, it is necessary for everyone. But until you don't know about it, until you don't know about its data storage planning, until then you will get no benefit, because you will just blindly keep doing it anywhere, shooting in the dark. After that you created a second file, you created a third one — useless memory gets filled up.

So please go through our installation video already. Okay? Because for however many days our capsule course runs, everything will be done quite nicely and practically. So now there will be a bit of practical work in it, so from there, complete the installation process and get going.

Now I am taking you to my whiteboard, I am taking you to the black screen. There I will give you a slightly theoretical part today, because it is a very important part — until you know this, there is no benefit in studying Linux, for any Linux admin, even if you are a cyber security engineer.

So I am taking you to my screen. One minute. Okay, full screen. Okay.

---

## History of Linux

So first of all, we are going to study about the History of Linux. What is the history of Linux? Okay. History of Linux — we are going to study about it. Now let us start right from the beginning: what is the history of Linux? It is a little interesting, so let's study about it. I hope my screen is visible to everyone, and I hope my voice is also clear to everyone. So now let's start.

Look, the beginning happened like this: 1964. Okay, 1964. Inside Bell Laboratory — in '64, inside Bell Laboratory, which is in New Jersey. Okay? At Bell Laboratory, in New Jersey — New Jersey, J-E-R-S-E-Y. Okay? Inside New Jersey, what happened is that a project was running. A project was running inside it, and what was the purpose of this project? The main purpose of this project was that an operating system should be built which is multi-user. Meaning, what does multi-user mean? That multiple users should be able to use that operating system. Okay? Inside one single machine, multiple users should be able to use it. With this purpose, planning was going on to build such an operating system.

Now what happened is that in 1969, this project was withdrawn. This project was withdrawn — meaning it was removed.

Now in this project there were two important people who were part of it, who were members. Okay? Whose names were: one was Dennis — Dennis Ritchie, R-I-T-C-H-I-E, Dennis Ritchie — and Ken Thompson. Ken Thompson sir. Okay? Both sirs were present in it. Okay.

Now they were not satisfied with this thing. They were not satisfied with this thing — that the work we had started was stopped midway. Okay? Now it happens, right — some people do not get satisfaction. So what did they do? They started working on it again. What did they do? They started this project again from the beginning. Although in 1969 the project was withdrawn by Bell Laboratory, but what happened is that these two — Dennis Ritchie and Ken Thompson — started working on it, and finally they created an operating system. Okay? They created an operating system whose name was UNICS. Okay?

UNIX — the name by which we know it. Okay? Actually, what we know, the name by which we know it, that name is UNIX. Okay? That name is UNIX. But actually its name is U-N-I-C-S, UNICS. Okay? This is it. But gradually we started saying it like this — what we called U-N-I-C-S, we turned into U-N-I-X.

Now what was its full form? Its full form was UNIplexed Information and Computing Service — UNIplexed Information and Computing Service. That was its full form.

This was a free operating system. Okay? It was a free OS, plus it was open source. Open source — what does open source mean? That its source code, the code of the operating system, the source code, anybody can review it, anybody can make changes in it according to their requirement, according to their need. Okay. So it is according to our need — we can modify it.

So now let's talk about the next part; let's continue in the same flow. Now in 1975, what happened is that in 1975 another version of it came. Okay? UNIX version V6, which became quite popular in those days.

And at this same time, what happened — around 1975, a lot of companies came into the market who did what? Who took this commercially... this thing that was there — what was it? It was the operating system that had been built by both Dennis Ritchie and Ken Thompson. What did they do? They started making commercial versions of it, around 1970, because the companies also wanted to take benefit. What did they do? They brought versions of UNIX into the market, which we call **flavours of UNIX**. Okay? Flavours of UNIX.

Which flavours of UNIX were present at that time? The first one was, for example, IBM AIX. Okay? After that, the one made by Sun Systems — Sun Solaris. Sun Solaris. After that came Mac OS, by Apple company. After that came HP-UX. Meaning, these were some flavours of UNIX, which those companies made into commercial versions.

Now let's talk — that was a little bit of our History of UNIX. Now the actual thing we are going to talk about is the history of Linux. Okay? Because now a lot of people say that Linux has been derived from UNIX, but the truth is something else — today we are going to talk about that.

Now what had happened is that in 1991 — okay, 1991 — there was a student, Linus Torvalds. Okay? A student named Linus Torvalds. He was doing his studies at university, and he had been given some project, and in that project he had to use some operating system — there was a requirement of an operating system. Now he saw that in the market UNIX had become old, and the paid versions that were available, the commercial versions, they were quite expensive. At that time even $1,000 was a lot, so they were quite expensive. So what did he think? That when every company can make its own UNIX-based operating system, why shouldn't I make one?

So what did he do? He started building his own operating system. Okay? He started building his own operating system, whose name was Linux. Okay? Whose name was Linux — it was derived from his own name. Okay? From the name Linus Torvalds, the Linux operating system, that name was given to it.

Now why am I saying that UNIX did not derive it? Because look, previously, all the companies that made commercial versions — what did they do? They took UNIX and modified its source code a little bit, made changes in it, and released their own versions. But what did he do? In this, what he did was he wrote the entire code of Linux — the source code — from scratch. From the beginning, from scratch, he wrote the whole code. Okay? He did not modify the UNIX code; he wrote the entire code himself for the Linux operating system.

Yes, for understanding purposes he used UNIX — for understanding how it works, how its source code is. But what he did was write the whole source from the beginning. But there is one thing he did: rather than UNIX the most — there is a name — instead of UNIX, what he studied most was Andrew Tanenbaum. He studied Andrew Tanenbaum the most, he studied him the most. Who was he? He was a professor. He was a professor, and he had built an operating system to teach his students. He had built an operating system to teach his students, whose name was **MINIX** — M-I-N-I-X — whose name was MINIX. He had built this.

Now what did Linus Torvalds do? He fully studied this MINIX operating system that Andrew Tanenbaum had built. Okay? He studied that itself, and on that same base, what did he do? He built his own operating system, which he named Linux.

Now a lot of people know... okay, that was the history of our Linux — that Linux was made in 1991 by Linus Torvalds. But the thing is, how it was made — that was a bit of the history.

---

## GNU and the Free Software Movement

Now, a lot of people know that "Linux, we already know about it," but you must also have heard one word: GNU. What is this thing, GNU? Let me tell you about GNU.

Now, 1991 to... now what was happening is that in the interval up to 1995, a movement was going on. Inside this there was a movement whose name was the **Free Software Movement**. Its name was the Free Software Movement.

Now what was the purpose of this movement? At that time, maximum software was paid. Now people have to work, developers have to work, companies have to work. Okay? So you can't pay for everything, right? So what did they do at that time — during this movement, a lot of software was made free. And because a lot of software was made free, the GNU project, the GNU movement that was there — the name was GNU — in it, that is why it is called GNU, because in it a lot of software was made free.

Now the thing is, if we mix them together, then our operating system is formed, which we call the OS. Okay? But what do we do — we start calling Linux itself the OS, but actually the OS is this [GNU + Linux]; Linux is the name of a kernel. Okay?

---

## Flavours of Linux

Now let me tell you, it also has some flavours. Its flavours — okay, flavours of Linux. Which flavours of Linux? Which were the flavours of Linux? Let me tell you.

Now look, what is there — Fedora-based has come. Fedora-based. Okay. One is Debian-based. Debian-based. Okay?

Now what happens — in Fedora-based, for example, RHEL has come: Red Hat Enterprise Linux. CentOS has come. Now these companies also released their own vendor-specific operating systems.

After that, in Debian, we have, in Debian-based: Kali Linux. Okay? Which we are going to study. Parrot OS. Okay? Parrot operating system. After that came Ubuntu. Okay. And many more are left. Now, for example, in "others" I'll say: Arch Linux. Okay? This is also there. Now Mint is also there — there are many like this.

So now all of these are the flavours of Linux.

---

## What is an Operating System?

Now I will talk about what an operating system is, so that those who don't know can find out. What is an OS? One minute — what is an OS? What is this operating system? What is an OS?

It is an interface between the users and the hardware. Users and hardware — between them there is an interface. How? If the user has to get any work done from their hardware — okay, if the user has to use the hardware to get their work done — then what will they need? They will need an OS. Otherwise, if there is no operating system, then for even a small cut-copy-paste, even to move the mouse, they would have to write a lot of lines of code, which is not possible — to do every task. That is why the operating system works as an interface between them.

Now, the OS is also accessed in two ways. The OS is accessed in two ways. One is CLI, which we call the **Command Line Interface** — Command Line Interface. And one is GUI, which we call the **Graphical User Interface** — Graphical User Interface.

Up to now, what do we do? We have been using Windows. Okay? What have we been seeing the most? The graphical user interface. Our example is which one? Windows 10 or 11. What are these? GUI operating systems. Okay?

But when, inside Windows, you use the command prompt, you use CMD, you open CMD — then what happens? What do you get to see there? You get to see a black screen, which we call CLI. If you want, you can use CLI in Windows too, as per your requirement. But our Linux operating system is entirely CLI-based. It is graphical-based too, but you won't enjoy it as much — okay — as much as you enjoy it in Windows. But the thing is, if you use CLI, then you are going to enjoy it very, very greatly, because it is much faster than Windows.

---

## Features of Linux

So now we are going to discuss a little about the Features of Linux. Features of Linux. Features.

Now the first feature is — what? It is **open source**. What open source means, I have already told you — just a minute or two ago I told you that open source means the one whose source code is available. It does not mean that it is freely available; it could be paid and available — but the one whose source code is available.

Now, a lot of you people must be thinking: everybody uses Windows systems. Even we — I am live-streaming, I am also using the Windows operating system; you people are also watching from the Windows operating system. And even 90% of people still use the Windows operating system as their personal PC or whatever. But why do companies use Linux? Instead of Windows, companies use Linux. When [Windows] is so good, everything is user-friendly to use, then why? And why do companies prefer Linux? That's the second question. And the third question: why do companies need a Linux admin then?

So the answer to all this is hidden in this very thing — in open source. What does open source mean? Look, Microsoft made its own operating system, and what did it do? It refused to share its OS code, the operating system code. Now if you have to run Windows, then you need a license from Microsoft. Okay? Because Windows is not free. But what does Linux do? It says: use my operating system, I will also give you the source code, use it however you want, do modifications however you want. But Windows is not like that.

Now you will say, "Sir, there are a lot of us who use pirated ones, we don't need a license." But in a company you cannot use pirated Windows, because if pirated Windows is used — because Windows keeps track of everything, of who is using pirated and who is using genuine — and from that it will track and it will finish off that company, because it will say "you have to use mine only."

Now Windows — the second reason I will tell you, why [companies use Linux] — because Windows is very expensive. Okay? It's very expensive. Anyway, it's paid. [Music] "Use mine however you want to use it, but otherwise I will not provide my source code. Yes, if you want to implement a policy, then yes, I will tell you that you can use this thing like this and like that" — in that you can define a policy, but "I will not give you my source code." Linux says, "I will give mine."

The second reason: it is **secure**. It is secure. Now everybody says it's secure, it's secure, it's secure — how is it secure? Okay, how is it secure?

Look, what happens is that whenever any malware hits, whom does it hit the most? Windows. It hits Linux very little. Because what happens — we all know that whenever any malware, or any hacker, tries to enter inside any machine, they will come through the network. Now in Windows, once it has entered through the network, then what happens — okay, if the antivirus can detect it, fine; if it has used a good evasion technique, then what will it do? It will enter inside your machine and will take full control of your machine.

But in Linux, what is there — OS hardening has been done. And because of OS hardening, what happens is that in whichever domain whatever service is running — okay, and what does domain mean? For example, if you use a web server, then for accessing the web server, whichever files are needed, only those files have been put into it. [In Windows] in your machine, automatically whatever executable file is there, it will be executed in the background and it has taken control of the whole machine. But this is not possible [in Linux], because if it cannot even use the root user's permission, then that means it does not have [the rights] — otherwise it would control everything. But the thing is, in the matter of security it is advanced, because there it does not have permission; it has to run within one domain only.

So this is the main reason: Linux is more secure than Windows. Everything — because even everyone must know that the Android we use is also Linux-based. Okay?

So now let's talk about the third point. Its third point is that it is very easy to update. Easy to update. Update. Easy to update. It is very easy to update.

The fourth point — what is it? It is **lightweight**. Lightweight. What does lightweight mean? That the size of the OS is very small, and it consumes less RAM. When you install any particular... if you install Kali Linux, even if you give it 1 GB RAM, it gives quite better performance than your Windows. If you give Windows 4 GB RAM, even then it runs with hanging; it needs 8 GB, it needs good network connectivity, and only then does Windows run properly.

---

## Windows vs Linux terminology

But what you need to understand now — let me compare and show you a bit. Comparison, in the sense... well, comparison:

- In **Windows**, the main user, the super user, we call him the **Administrator**; and in **Linux** we call him the **root user**. We call him the root user.
- After that, the file: in Windows we call a file a "file"; in Linux too [we call it a file].
- And software — the software that is there inside our Windows, which we call "software" — in Linux we call them **packages**. P-A-C-K-A-G-E. We call them packages.

---

## Data Storage Planning in Linux

Now let me show you how the data storage planning of Linux is. What happens is that whenever we install Linux on our machine, then in Linux you will get to see two types of data. Okay? Two types of data in Linux — which ones?

1. In it you will get **OS-defined data**.
2. Secondly, you get to see **user-defined data**.

Now how is its planning done? How is this data decided, how is it planned? Let me tell you about that. Before that, I will take a small example — I am going to compare with Windows. I am going to compare with Windows, for your Linux... the Windows OS. Okay?

Now what happens is that whenever we install the Windows operating system on our machine, what happens is that by default, what do you get to see in your machine? You get to see a C drive, you get to see a D drive, and an E drive if we have created one — then we get to see an E drive.

Now whenever we open the C drive, what do we get to see in the C drive? A lot of folders, a lot of files, a lot of programs — you get to see them in it by default. Now these folders, files, the programs that you get to see inside the C drive, we call that **OS-defined data**. Okay? We call this OS-defined data.

And the rest that is left — our C drive, D drive — we use this for personal data. Okay? We use it for personal data: you stored your movies, photos, documents, etc. And this we call **user-defined data**. User-defined data means the data that has been defined by the user, that has been created [by the user].

Now look, what is OS-defined data? Whatever gets created by default whenever the operating system is installed inside your machine. Now it is not the case that OS-defined data is created only at the time the operating system is installed — no. This also happens in two ways. Okay? OS-defined data — this is also of two types:

**First:** During installation. Okay? Whenever your operating system is installed, then along with it, whatever files, whatever programs get generated by default in your machine — those are what they are. So in this way your OS-defined data is created.

**Second:** What happens is that once your operating system has been installed — after installation of the OS — after this, what happens is that whenever you install any software, whenever we install any software or application in our machine, then what happens is that along with it there are a lot of programs, there are a lot of its files, and by default they go and get stored inside your C drive. And when they get stored inside the C drive, then this is also a second way [that OS-defined data is created].

So in these two ways your OS-defined data is what you get to see here — in these two ways.

Now, user-defined data. After that I'll do [that one]. Our user-defined data — user-defined data — what always happens is that whenever your operating system is installed, after that whatever files, directories you create, or whatever movies you store, whatever you do — that is created only after that.

---

## Types of Data

Come, let's discuss a bit about this data, let's go a bit into detail.

Now, data — basically what is it? Information. Data could be anything. Okay? That's what data means.

Now let's talk about **types of data**. Let's talk about this: types of data. There are two types of data:
1. One is your **default data**. You get to see default data.
2. The second is your **customized data**. Customized data. Okay?

Now the default data — in a way, what would you call it? OS-defined data. In a way we can call it OS-defined data. Why? Because whenever the operating system was installed, or after the operating system was installed, whichever file, whichever application or software we downloaded and installed — along with that, all the files that got created by default go and get stored inside your C drive, or inside the default data. Okay?

Now after that, customized data — what can I call it? I can also call it user-defined data. Meaning, user-defined data, I'll take it under customized data. I'll take user-defined data under customized data. Because whenever, after the OS installation — meaning once our operating system has been installed — after that, whatever work was done by any user, any file, document, whatever work was done, that comes under your customized data.

---

## The root partition `/`

Now we came to know — basically, what was my motive in telling you about Windows? That whenever we install the Windows operating system, by default in the C drive you get to see a lot of its folders, you get to see a lot of files, by default. This same funda you get to see in Linux too.

But what happens is that in the case of Linux there is no C drive, D drive, E drive. Okay? There is no C drive, D drive. In Linux there is no concept of these drives at all. But what concept does Linux have? I am going to tell you about it.

In Linux, all the data that gets stored, goes and gets stored inside one parent folder. Okay? If you people don't know — in the case of Linux, all of Linux's data... we can call it a parent folder, P-A-R-E-N-T, parent folder. If I show you its symbol, then its symbol is this — do you all see this? Here it is: **`/`**.

This is the one under which all the data, under which all the files — or whatever your OS-defined data is, or whatever is there — so now whether it is OS-defined data or user-defined data, all that data is created underneath this. All data has to be created underneath this — OS-defined data as well as user-defined data. Okay? All of it has to be created under this itself. In this there is no concept of C drive, D drive.

Now what do we call this? The symbol you see — your backward... which we call **forward slash**. We can call it the **root partition**. P-A-R-T-I-T-I-O-N. We can also call it the root partition, or we can also call it the **parent partition** — P-A-R-E-N-T, parent partition. Or we can call it the **parent folder** — parent folder.

But let me tell you one thing, for clarity: what you will most get to see and use is that we will either call it the root partition — okay — or the parent partition. Okay? Because with the other terms you will get confused later on when you are working through the whole course: "what did he say, what is this thing?" — there will be confusion in it. So the better option is that you keep it in mind, remember, that we can call it the root partition.

Now what happens is that whenever you go into Windows, you click on My Computer, then what happens there — your file opens: Local Disk C, D. Now you will get to see a forward slash; you will get to see this forward slash — so understand [that this is the root].

---

## The default directories and where users work

Now let's talk about the fact that inside it there are two types of data. How is it, of which type? Okay, there are two types of data — let's talk about this.

Now before understanding about this, let me tell you a little. Now, keep one thing in mind: whenever our Linux was installed — whenever, one minute — whenever our Linux was installed, what happened in it? By default, around **19 sub-directories** get created. Sub-directories get created. This can be 17 too, it can be 16 too — this depends on the operating system. Okay? 17, 15, 20 — it can be anything, it is not fixed. But I am going with the example that right now our machine has 19 sub-directories, for example. Okay? But by default, it stays around this — 16, 17, 18, 19 — only this many sub-directories get created by default, automatically, whenever your operating system is installed.

Now what are these directories? Now every directory has its own job. Okay? For each directory — the 19 directories that are there — their own rules are defined. Okay? And the entire operating system depends on these same 19 directories. Okay?

Now what is there in it — in this operating system, in these 19 directories it is already set which directory or which folder its configuration files will be saved in, in which its temporary files will be saved, in which its process files will be saved, in which its library files will be saved, and in which its log files will be saved. This is already set in Linux. You don't need to worry about this, because it is already defined; this doesn't change. It is inside these 19 sub-directories already, from before. And on these, you have to work exactly according to the defined permissions.

Now you must be thinking: if I create any file, or what if I created one more folder, or I created one more directory, a sub-directory — will that come within the 19, or separately? That will go beyond the 19; it will start counting as 20, 21, like that.

Now I told you that whenever the operating system was installed, 19 sub-directories were created. Now your next question will be: then where do the users operate from? Where will users operate from in this, because you said that by default 19 directories [come] with the operating system — so where will users operate from?

So let me explain a bit about this, about the 19 directories. What is it? Look, all these 19 directories come inside your root partition. Okay? I took here around 19 default directories. Now out of these, what happens... I am doing it like this for you so that you identify this forward slash, but this doesn't come in your curly bracket.

So out of these, what happens is that around 17 directories — the 17 directories that are there — what does it do with them? The operating system operates them. They are operated by the operating system.

Now the two directories that are left — the example given — the two directories that are left: in these two directories, one directory is the home directory of the super user; we can call it the **home directory of the root user / super user**. And the second one that is left, one directory — okay — this is for your normal users. This is reserved for all of your normal users.

Now, as I told you, one directory will be used for root's home account, and the second directory — in this, however many normal users are created in the machine, 8, 10, 15, all of them will come inside this same directory.

Now here the condition is that one user cannot go into another user's home account and check their data — what the other user has created in their account. Meaning, the straightforward thing to say is that one person cannot go into another person's house and peep at what he is doing in his house. That's the simple meaning. That's the simple meaning of it.

---

## Public place vs Private place

Now let me tell you about creating data. Whenever we create data inside our Linux machine — okay — then we have to keep some things in mind here. These are the very things where mistakes happen. Okay?

Now let me tell you one thing: by default, the root user, or your super user, can create any directory, any files anywhere in the machine, and at any place. Okay? If I write it here — let me write it for you: "By default, our root user can create files and directories on any place." Okay?

Now he can create at any place. That's a simple matter. Now I have used one term here: "place." What does it mean? Okay, this is of two types. It is of two types. The first one is what we will call a **private place** — everyone has one, they have their private place too. The second is a **public place**. Public place.

Now what do private and public mean? Okay, what they mean is: whether you are the root user or whether you are a normal user, the home accounts of both of you come under your private place. Meaning, what — the straightforward statement is that **every user has the default right of data creation in their home directory**. A user, by default, has permission to do anything in their private place — whether they create a file, delete a file, execute a file, anything. Okay? By default. A normal user too.

Now, leaving aside their home directory, leaving aside their home account, all the places that remain, all the places that are left — all of those count as public places. Okay? All of those count as public places. **Except the users' home directory** — leaving the users' home directory aside, the rest are all public places. All of them are your public places.

So I told you that here there are two: public and private. Now some people will say, "Sir, if I am the root user, then does public/private mean anything for me too?" So tell me — the house is yours, you built this house, you only did the partitioning, so you can go anywhere, right? For you there is no public/private, right? Okay. But the thing is, public and private have been defined according to terminology.

If you want to go anywhere — fine, let's say you are an attacker, you are an ethical hacker, no issue — then you can also become root, and you can be a normal user in your own machine. In that sense, whatever you will do... when you will be doing Linux [work], whatever you are doing, then you — or even any Linux admin — inside any organization, what happens is that they don't get root access. Root access is not given at all; they remain a normal user. But we have got into the habit that in our own machine we always work as the root user. **This is a bad thing.** Some day, if some attacker came and got into your machine, then he got in [as root]. Don't become the root user until there is a need; manage with `sudo`. Now what `sudo` is, I will tell you. But the thing is, until there is a need, don't become [root]. Okay? Because there is an issue with your security in this — whatever system security there is.

So now I have told you here the funda of public and private, because the super user can do anything anywhere. Okay? And what can a normal user do? He can do anything only inside his home account. But keep one thing in mind here: this rule is for everyone.

Now apart from that — whether the normal user works in a public place, or the root user works... now root, if he wants, can change it, but the normal user cannot change it. But if you have to create any file in a public place, if you have to create any directory, or if you have to work with any file, then what is it — you will have to work exactly according to the permissions that are already set. Okay? You will have to work exactly according to those in Linux. Okay? Now just — just a minute. Okay. So you will have to work according to that.

So now I have told you public and private. Because that was the biggest thing — the problem that people used to have: whenever we used to work inside our machine, or any cyber security engineer used to work inside their machine, the problem was that they used to create any file anywhere. After creating any file anywhere, after that they used to think, "man, why am I not getting permission here?" Because no beginner, or even intermediate level, knows where inside this we have to work.

When I teach you the file system, after that you will come to know that every directory — the 19 or 17, whatever directories you will have — okay — what happens in which directory of yours; you will enjoy working there.

So this is the concept of storage management. I hope everyone understood what a public place is, what a private place is — all these things. Because if you have understood all these things today, then tomorrow's session — meaning your next scheduled session — when you study in it, or whatever you are going to study after today, okay, whatever work you do in Linux, then you will never have this doubt: "Where do I have to create a file, where should I not, where do I have to do what work, where not." Okay? So this basic storage management — I have told you how storage is managed in Linux.

---

## Demo on the machine

So now let me take you to the machine and show you some things. Machine. Okay? Right now you must be seeing it on our screen — this is our Linux machine. This is our Linux machine, which is called Kali Linux, which is the Kali operating system. Generally it is used by pentesters, it is used by security professionals, and it is the most popular operating system. When you use Kali Linux — okay — Parrot and Kali are what you'll hear about the most, and out of those too you use Kali the most.

This is a basic overview. This is your terminal. Okay? Whenever you work, whatever you work on — this is your terminal, on which you work.

Now let me show you a basic overview. Inside this — let me show the graphical view — there are a lot of applications: more than 600 packages are installed in it by default. So according to every category: Information Gathering, Vulnerability Analysis, Web Application Analysis, Database Assessment, Password Attacks — meaning a lot are there by default, already installed in it, packages. So this is its GUI mode that you must be seeing here. Okay? You will simply click on any one and it will start working. But we will not use the GUI.

Because [the shell] works between the user and your operating system. Okay? Because I told you a small thing about what an OS is, but actually, if you look — if I talk about the architecture — then first of all what do you have? There is the **hardware**. On top of the hardware there is the **kernel**, which we call Linux. On top of that is your **shell**, and on top of that the **users** work.

Now, the user has to get some work done from the hardware, so what does he do? This terminal of yours — which will open now — here it is, this is the terminal, a shell has opened. Okay? So we simply fire a command on it, we write something, and then what does it do? It directly takes it and gives it to your kernel, and the kernel provides it to the hardware — to fire the command on the hardware for whatever output we need, whatever work has to be done. And after that what do we get? We get the output on our screen. From the kernel... the same process again: the kernel gives it to the shell, the shell gives it to the user. This is the simple basic architecture.

Now let me show you one thing — if you [have] the next class... okay, fine.

So for the difference between public and private, since you people are asking, let me tell you. Public and private — look, private: you understand what private is; in your personal life too you maintain privacy, meaning the one in which only you are the owner, you alone are the owner.

Public and private — let me tell you. Look, here it is: whatever your home account is — okay — `/home/user`. But let me show you now: `cd` — I went into your root partition. Now let me show you what this thing is.

Now here you will be seeing one thing — these, the 19 [directories] I am talking about, the 17 or around that I'm talking about; how many can we count? These will be 17, 18. This one that you have is **home**, here it is. Okay? This is your home. And which is this one? This is for all of your normal users, apart from the super users. One is this — **root** — this is root's home account. Okay? This is root's home account. And this is the users' home account.

Apart from these, all the directories or files that you are getting to see on the screen — all of these are public places, and these [two] are private places. This is root's own private place, and these are all the users — okay — all of these are the normal users. Which one is a normal user? The one who is not the admin, the one for whom completely limited permissions are defined — that is the normal user, and all of them are inside this.

And except for these two places, everything else in your Linux is a public place. Meaning, there some permission or other is already defined on every directory. If, apart from your private account, apart from your private place, if you are working, then what is it — you will have to work in public exactly according to the permissions that are there by default. Okay? You cannot tamper with their permissions there.

Now, for example, in your home account — this one, I am highlighting it for you — inside this you can do any work, create any file, create any directory, execute any file or anything, or delete it — you can do it. In this there are no restrictions on you. Other than this, you have restrictions. So this is the difference between public place and private place. Okay?

Private means you can do anything in it. Okay? Other than that — other than your house, all the other houses that are left, okay, whatever is in the neighbourhood — all that is what for you? It is public. Okay? But for you, your private property is this one. Other than that... in private you can do anything.

But tell me one thing. I'll take an example: you live in a society. In a society, what happens — suppose there are 50 houses; out of those 50 houses, one will be your flat, your house. In that house, you are its owner, you are its master; it is your private place. In it, whether you dance, listen to music, do anything. Can you do all these things by going into another house? No — because it is public property, it is a public place.

Now here we are not talking about that public place — like "I won't do anything in my house and I'll go outside and do everything." We are not talking about that here. That is a private place; in your house you can do anything, but you cannot go into another house and do it, because he will consider it trespassing — meaning someone has come to steal in my house. Okay? You will go into someone's house and they'll say okay, "I'm just taking a stroll" — you can come and go, but you cannot do much more, because there the work will happen according to whoever is the owner of the house.

So I hope there won't be a better example than this.

---

## Closing

So now, whatever doubts come to you, be patient with me — meaning, stay with me, and please keep commenting, no issue; we will study, your doubts will be cleared. But let me tell you one thing: whenever I teach, keep your doubt with you but watch my courses completely once. Meaning, today I have taught you [this]; tomorrow I will bring one topic, the next day I will bring a different topic. If after that your present doubts still remain, if I am not able to clear them, then I will definitely clear them for you. But you won't have doubts, because I know how to teach you, and I know where you will have which doubt.

So when we study about the File System Hierarchy — these are the things I will teach in the next class — then here you will come to know what every file and directory means. When you work, public/private will become clear to you in the same way, and as soon as you learn to work inside it, it will become clear to you: "yes, where do I have to go, where do I not have to go."

But there was one concept, a basic concept, that I had to explain to you: what you should do in Linux and what you should not do. If you have understood this — once, repeat and watch the videos when they come up here, it will come tomorrow, okay — so listen once again, revise the concept once again, and it will become clear to you. It is a very basic concept, but very important.

So that's all for today. Bye bye, good night.
