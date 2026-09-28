# 022 — Day 7 — OSINT Free Live Training Capsule Course

**Source transcript:** `transcripts/022 - Day-7 OSINT Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Topics:** Twitter OSINT — technical method · Advanced Twitter search operators ("tricks" 1–9) · Wildcards · Date ranges · Filters · Logic operators · Location search
**Type:** Verbatim English translation of the spoken Hindi/Hinglish session

> **Note on this transcript:** the captions are heavily garbled in places (`ओपन 100 से इंटेलिजेंस`/`टेलिजेंस` = "open-source intelligence", `रेडिसन मेथड` = "traditional method", `स्लिक्स`/`स्ट्रीक्स`/`तार` = the **`*` (star/wildcard)** trick, `लिस्ट` = the date-scoped search operator as the instructor pronounces it (cf. Twitter's `since:`/`until:` family), `थर्मो`/`धर्म` = "Sharma", `ट्विन टी ब्लू आई एन जी`/`ट्विनिंग` = (typing) "filter:", `परिस्को पी` = **Periscope** (live-video filter), `दास`/`हिफिन` = "dash/hyphen (`-`)", `साइंस` = **`since:`**, `अंटील` = **`until:`**, `नियर`/`विदीन` = **`near:` / `within:`**, `सीपीयू` = CPO/CFO (C-suite), `एसिडिटी` = "activity"). The intended operator has been restored where unambiguous. Passages where the captions collapse entirely are summarised in [square brackets].

---

[Music] Hello everyone, good evening friends. Confirm once — can everyone hear my voice or not? Okay, thank you.

So once again, welcome all of you to our YouTube channel. Everyone knows what we studied in the last class, and the topic that is running — **[Twitter] open-source intelligence** — today we continue it. You all know what OSINT is and how to perform it. I had told you that we are performing OSINT on **Twitter**, because Twitter is one of the most famous platforms, and that there are two methods:

- the **technical method** — which we can also call the *hackers' method*, and
- the **non-technical method** — which we also call the *traditional method*.

In the last class we learned the **traditional method** — how we do information gathering with its help. If some people have come directly today: **please, after today's class, go and watch yesterday's class too** — only on that basis will you get real interest. Because until you use the non-technical method, you will not feel comfortable using the technical method — you won't have information about your target. If you can first perform the non-technical/traditional method like an actor [with a hacking mindset], then you will perform your technical method very well, in an excellent way.

So today we talk about how, with the help of the **technical method**, we perform our Twitter OSINT. It's practical — give me a minute — *"I will take my notes and open my machine."*

---

## Recap: what we gathered yesterday (target: Paytm)

You all know our target in the last class was **Paytm**, and we did some information gathering about it. (If any of you gathered more information than me, tell me in the chat — otherwise let it be 🙂.) What we found live:

- Paytm's username: **@Paytm**
- Founder: **Vijay Shekhar Sharma** — also a CEO of the Paytm company — his ID is **@vijayshekhar**
- The **CPO/CFO** of Paytm [and other executives]
- Other domains/handles: **Paytm Care, Paytm Money, Paytm Payments Bank, Paytm Business** — their Twitter IDs: **@PaytmCare, @PaytmMoney, @PaytmBank, @PaytmBusiness**
- Even **Paytm Money's CEO — Varun Sridhar** — we could extract information about him too.

(*"Bro, could we have taken any target for practice?"* — yes, you could take any target for practice.)

And we had tried **individual targeting** — our individual target was **@vijayshekhar** — and I told you: **don't leave anything; notice every single thing.** For example, look — this is maybe a July 16 post about live streaming, someone commented *"my Paytm bank account has been blocked"* — all these things you have to notice. You can see which latest posts he has performed… So that was all the information; we couldn't yet link much with anyone else.

Now tell me one thing: in **"Vijay Shekhar Sharma" — what is the surname?** What could the surname be? Tell me. [Sharma.] With that, let's start.

---

## Trick #1 — The `*` (star / wildcard)

The first trick of the technical method of information gathering on Twitter — we call it the **star** trick. You have already read about what `*` means — everyone already knows: **anything**. When I taught you [dorking] earlier, I told you what star means — and it is part of programming languages, so it's used everywhere; every programming language uses it; that's why it is quite powerful.

How is it used? For example: our target was **Vijay Shekhar** — V-I-J-A-Y S-H-E-K-H-A-R — and after it I put a **`*`**. What I want: **all the Twitter handles under the name "Vijay Shekhar"** — the front part must be "Vijay Shekhar", after that it can be anything — and it will show all such Twitter handles in the results. Now look, here you can see: *Vijay Shekhar Sharma… Vijay Shekhar Gupta… [a] BJP [account]… Srinivas…* — Vijay Shekhar this, Vijay Shekhar that — you keep seeing them.

### Why this is powerful: finding FAMILY MEMBERS

How can this be powerful in our case? We did information gathering and found who is the CEO, the CPO… but we also want **relatives** — friends — and we will NOT stop at this step of information gathering. We will try to find his **relatives, family members, native relatives — brother, wife, sister, whatever** information we can get.

Why? Everyone knows that the CEO/CIO of this company will be quite **aware** about cyber security — he'll know about it. **But what about your dear family members?** Family members won't be [aware], right? And even if he told them, nobody follows it that much.

Now — if you have the target's username and his **surname**, you all know: every family member, relative — even people in the surrounding area where you live — creates IDs with that surname. His **wife, brother, sister, father** — if they operate a Twitter handle, if they even use Twitter at all, they will surely have used the **surname at the end**.

So on this basis we start our analysis: **`* Sharma`** — star = anything, but at the end it must be **Sharma** (S-H-A-R-M-A). I run it — and whoever has the surname Sharma, it shows them all in the results: anything in front, but "Sharma" at the end. Look: *Anushka Sharma… Kapil Sharma… Rohit Sharma… Dr. Dinesh [Sharma]…* — so much information. Now, you don't know which of them [is a relative], so **you will have to open every profile you suspect and check** — whether they are a relative, mother, father… (a lot of it is Rohit-Sharma-related 🙂; look — "editor-in-[chief]… chairman, India TV" — okay).

So this is your trick: using one `*` you can guess/enumerate their family members. Right now we can't guess much, because we don't have a large amount of information — with the traditional method I only gathered **0.1%** of the information in the last class. Guessing the family members [from so little] is the tricky part.

> **A note on format:** I will only *show you the tricks* — if I performed full information gathering on all of Twitter, it would take me one–two months. That I am not going to perform; I'll show each trick with an example. **This was Trick #1.**

---

## Trick #2 — Date-scoped search (month / year)

Now trick number two. Look — I'll take every trick through a specific example rather than just naming it. Suppose you did information gathering with the traditional method, and you have an idea — you know that the one you've targeted (a company or a username) **tweeted/posted something, or mentioned something, in a specific MONTH or a specific YEAR** — they attended something, liked something, tweeted about some event. You got that idea from your gathering, or you saw it in the news somewhere.

Then you can search on the basis of that **specific month / specific year**. But for that you must already have the idea: *"yes — what I'm about to search, at this time there was some mention of it; some event happened around it."* With this trick you should have the **keywords/hashtags** at hand; if you don't have a username, you can dig out the username on their basis.

**Syntax:** the [date-scope] keyword, then a **colon**, then **without space** we specify either the **month** or the **year** we want.

**Example:** I have the keyword **Paytm** (also the full pattern @Paytm). I scope it to **March… 2022**: now [it should show] the tweets from 2022 in which the @Paytm username was used — whoever mentioned it in their tweet. Look — no such post is visible here… in **Latest**, just this — "Paytm entertainment…" Fine, let me remove the **@**… now something shows — latest post, "Paytm Mall"… no — meaning it wasn't used in March of that [range]. Now I change the month — for example **January**… J-A-N-U-A-R-Y… let's make it 23… **In this way you can scope your search by year and by month.**

(The reason results didn't pour in quickly is that we haven't done enough specific information gathering — in the last class we only had one hour. If I brought pre-gathered intel it would look [magical] — *"this is not good for you, and not good for a teacher."*)

This trick can prove very helpful, because [with it] you can go to the posts/comments **during a specific period of time**, and there you get **more accurate results instead of random results**.

---

## Trick #3 — Hashtags

Trick number three: the **hashtag**. Hashtags exist on almost every social media platform — Facebook, Instagram, Twitter, LinkedIn. People use hashtags to mention things, to talk on a specific topic, on an event, on a hot issue — to talk to each other, to make each other aware. And **for hackers, hashtags prove very important** — they provide a lot of information.

While doing your information gathering, some hashtags will surely have come in front of you which you kept in your notebook/notes. On the basis of that specific hashtag you can gather more information.

**Example:** while I was gathering information on the CEO — Vijay Shekhar Sharma — suppose I saw some tweets showing he has **interest in some football match / football team** — he retweets football-related things and uses **#football**. Now, how do I **confirm** that interest? If that particular person — your target — really has interest in that thing, he'll be tweeting it **regularly** (because it's his interest, he likes it, or at least he tweets something now and then). So on the basis of the hashtag search you can **re-confirm/verify**: on that particular hashtag's posts, how many did he post, like, comment? From that you get the idea: *"okay — he has interest in this thing."*

Let me take the example (I have no prior idea about this): **#football** — now, only on the basis of the particular hashtag #football, all the posts get shown here. I go to **Top** — you see "big fight" [match threads] — whatever information — if you read the retweets, the comments, the likes, you can get information from here: **does your target really hold interest in this thing, or had he just done it randomly once?** In this way you can extract information on the basis of hashtags too.

And you can **combine** tricks: for example, hashtag + the date scope together — [#hashtag] scoped to **April 2022** — enter — and like this, one minute… you see how it works. [Music]

---

## Trick #4 — `from:` / `to:` — checking communication between two users

Our trick number four. What is it? You have the **target's username**, and you have the **target's friend's username** — two things. Now I want to see: **have these two communicated with each other through tweets or not?** I want to confirm this. There's a trick for that too — and it can be very helpful in information gathering, because on the basis of this technique you can even find out **which specific topic they were talking about** — which may later help you create a hacking scenario or help in further information gathering.

**How:**

- **`from:username1 to:username2`** — lists out all the tweets from username1 to username2 — whatever communication happened between them through tweets.
- You can also reverse it: **`from:username2 to:username1`**.
- Another way: **`from:* to:username1`** — meaning *all* tweets, by anyone, that were made **to** username1.
- Or simply **`from:username1`** — list out ALL of username1's tweets/posts.
- And you can add a **keyword**: `from:username1` + the keyword **Paytm** — meaning: show all of username1's tweets, but only the ones in which the keyword *Paytm* [appears].

**Practical:** `from:@vijayshekhar` — look, ALL the posts made by him: *"…our professional [work]… lens focus on the world… in the middle of the song… pain and sadness to every railway employee and leader who is grieving…"* — see, he tweeted on June 5 about an incident [a rail tragedy]. And there are lots and lots of tweets here — all posted by him, only his. Quite a lot of information — this could be [useful] for us… look, "fellow engineers…" — in this way you can use it.

(Again: I will only show you the trick, because performing every single thing would be time-consuming and we'd stay on one topic for many days. You need the **reading capability** for this.)

One more use: inside `to:` you can add **any username** — [show everything] tweeted *to* them. For example I use **Paytm** here: *"…10 years before, Paytm had…"* — see, some information — October… November '22 — like that. Let me open this one: *"…43 international banks' fintech school instructor and the published author of 'The Digital Banking Revolution'… no, it's the third…"* — okay. Next… *"4 days… flying…"* — someone here may even relate — could be a relative, could be not — look, "founder… grand…" — previously… So I can check: **has there ever been a tweet between these two?** I'll try to find that out… and — it happens — a *"thanks, thanks"* reply he made… meaning — *"arre yaar, I opened it right here"* — okay: **Gurgaon** — we have information nearby [a person mentioning Gurgaon]. 

---

## Trick #5 — `filter:` — images / videos / live (Periscope)

Now trick five — your **filtration trick**. Why is filtering necessary? In all the information gathering you've done so far, **unwanted stuff keeps coming again and again** — you don't want it in front of you, you can't focus. With the filter you can minimise that and focus more. (Just a second… okay, sorry for the disturbance.)

What can we filter on?

- **only images** — `filter:images`
- **only videos** — `filter:videos`
- **live [video]** — `filter:periscope`
- combined with any particular **username** or **keyword**.

You know that photos and videos carry a lot of information — basically people post with photos or videos; the chances of a plain small text-only post are low, and people communicate their views on top of those [media posts]. So the useless information that was coming in front of us — now we filter it.

**Practical:** I take this same username as the example — copy — [username] + `filter:images` — now watch: **everything in my output will contain an image.** Look… okay — you see images — and you must scroll down and look at each one — okay, a profile is appearing — "living of the…" — fine. Now to **videos**: `filter:videos` — and you'll see only video-related [posts]. In this way you can gather information. (I randomly targeted a member of the Paytm company here just to demonstrate — *"I am sorry… for that — I'm not revealing anyone here."*) And with **`filter:periscope`** you can check the live [broadcasts] — whether they commented [on live videos] or not.

That was your filtration-related trick.

---

## Trick #6 — Logic operators: `AND` / `OR`

You all know — in every programming language you've read, in logic — which two words do you hear? [AND and OR.] Trick number six. I won't over-explain; example:

- **`@user1 AND @user2`** — means: I want in my results **all the posts where BOTH have been tagged/mentioned** — both usernames used in the same post. Both must be there. If only one is present, it won't come.
- **`@user1 OR @user2`** — you'll get **three types** of information: posts where user1 and user2 are both there, or only user1 is in the post, or only user2.

**Practical:** I take @[vijayshekhar] — and the second one from the Twitter account we were on — paste — now look, where both are: *"Replying to…"* — he replied — *"…not rip[ping] bhai — Paytm, to attract customers we don't want your cashback, we need only service like WeChat for customers in China"* — oh my god, okay — *"congrats to you, meet you on the [stairs/chairs]…"* — like this you can take out what they [said] between themselves. Your results will show even more — **information gathering is YOUR work; my work today is only to tell you the tricks.** (You have to do it — not me 🙂 — that's why this is training.) With logic you can also use **keywords** — compare two keywords — anything.

---

## Trick #7 — `near:` / `within:` — location-based search

The next trick is also very important. If, during information gathering, you succeeded in finding out **where your target lives** — his nearby area — then on that basis you can gather even more with Twitter: **tweets from that specific area**, to confirm things. This helps a lot — with this trick you can find out even his **neighbours**, his family members, and the other people around him.

Think about it: a famous person may have left his village/town some time ago, **but the family members are still there** — or in the family there's someone attached to his work who stayed back. Family members' security doesn't get taken care of. And family members — to show off, to tell people — will have told some special neighbour: *"my boy does this, this whole company is his…"*. Now the neighbour has the information — and don't you think the neighbour will start [engaging]? On every tweet he'll comment, to get noticed, to say *"I'm from your village, I'm so-and-so"* — the "insider village talk" thing — a successful person from his area — sometimes they'll even try tweeting at each other. **All that information becomes the [entry] steps for an attacker.** This type of information gets served up, because in that area…

Look — if I check his profile: where is he, where does he live… his profile information says, for example, **India**. Now you'll see lots and lots of posts. Let me put **near:"India"** — well, "India is very big, bhaiya" 🙂 — for India it's used for different distances: if it's a foreign company you're targeting and [the person] is from India or from a specific place, you can analyse on the basis of that place. Let me narrow it… last one month… "they are not available"… — look, some information: **Kapil Chopra** [a profile] — this information could be quite helpful for us… look — a tweet here — *"laughing your heart out — Hyderabad"* — copy… And earlier we had found the one who had mentioned **Gurgaon** in a post — he mentioned a **specific place** inside India.

So now I have an idea: **near Gurgaon**. I have a username, I have a hashtag, and I know this hashtag came out of a particular post from your target company. So you use **`near:`** and **`within:`** — `near:Gurgaon` — you mention the Gurgaon area, and then you set a **perimeter, a circle**: **`within:5km`** — within 5 kilometres of Gurgaon — a whole area.

**Illustration with the map:** here — Google Maps — suppose someone mentioned **New Delhi**. New Delhi is my target [area], so I say: within a **5 km range of New Delhi**, show me all the tweets for this particular username / this particular hashtag. This is the **range-specific** [search] — with it you can dig much deeper.

**Who will you find there? Common sense:** either their **customers** (nobody bothers tweeting at someone for no reason), which also helps you **confirm the location**; or their **friends — close friends — partners — relatives** may be found right there. There are good chances in information gathering. That's the magic of `near:` / `within:`.

---

## Trick #8 — Exclusion with `-` (hyphen)

Sometimes there are keywords, people's names, or accounts you do NOT want to see — you want your results **focused and accurate**, without the unwanted stuff that keeps re-appearing. How do you **exclude**? (We've done 7 tricks — an hour has passed — come on, you can work a little 🙂.)

**The dash/hyphen (`-`)**:

- **`@username -keyword`** — e.g. `@vijayshekhar -Paytm`: *"show all the posts/tweets of this username, but EXCLUDE wherever the keyword 'Paytm' appears."* (I tell the search bar: on the basis of the Vijay Shekhar username, find the results, but exclude wherever the **word** Paytm is seen — "but big brother has used it everywhere," 🙂 — yes — no, it's working, it's working.)
- **`@username -@Paytm`** — now with the **@**, it is not excluding the *keyword* — it is excluding the **@Paytm username** (mentions). **Understand the difference between the two:** without @, it excluded wherever the word "Paytm" appeared; with @, it automatically excludes the posts where the @Paytm username appears.
- And if you want to search a **specific keyword** for that username but skip something else, you can give the keyword first and exclude the rest — e.g. start with the keyword, then the username, then minus-terms. (I don't have a [prepared] keyword right now, that's why I can't show it — but you can also make it that specific.) — *"Okay, I will try my best, Ojha-ji, I'll try to repeat it for you."*

**Rule:** with the hyphen — and with all the filters you use — **no space** after the operator.

---

## Trick #9 — `since:` / `until:` — exact date ranges

Now trick number nine — the **date-range** trick. Suppose during information gathering you suspected that your target, **previously, in some date range, on some dates**, mentioned something — talked about something, tweeted on something — and you have an **estimated idea around which date** they tweeted that post. Maybe some topic/issue was running, or **they launched something** and talked to their partners through tweets, or a customer talked, a partner talked — some information may be sitting there. (This is more precise than the [month/year] trick from earlier — there you scope by month/year; here you go **exactly**.)

**Syntax:**

- **`since:`** + the **full date** — e.g. `since:2018-…` → it shows all posts **from 2018 up to now**. Look — "OBP… the proof says…" — you'll see a lot — even photos (we already have his photos).
- Add **`until:`** for the end of the range: e.g. **`since:2018-01-20 until:2019-01-01`** — *"I want to see from 20 January 2018 until 1 January 2019."* And there they are — the December 2018 posts — **only that one year's posts** — you can find them for any target.

**A find while demoing:** in the replies — look — *"@… do you have a connection with Vijay Shekhar?"* — they're chatting. Meaning: what can you get here? That **during that time period they were talking — they were friends** — and maybe at present [they've fallen out]. That can be a very good thing for us — we can take benefit of it: since he was a friend earlier, **he will have very good knowledge and information about [the target]** — so we can target *him* too, and make him help our information gathering — using our **manipulation techniques, our social engineering**, by talking to him — because he became a target too, right? First a friend, now not a friend. 🙂 In this way we can gather even more information about a particular target.

---

## Time check & revision

I think [the rest] will take time — we should proceed tomorrow; it's 7:20 already and tricks are still left. We'll continue in this very topic next class. So let me give you a **revision** of everything:

1. **Trick #1 — `*` (star = anything):** you have a target's full username and surname; family members may be unaware and keep the surname in their profiles. Search `* Surname` to enumerate possible relatives — brothers, wife, children — even if the target himself, being aware, removed his surname.
2. **Trick #2 — date-scoped search (month/year):** you have intel that in a specific month of a specific year they tweeted on some event/issue — confirm whether they really did, and find the event and who else engaged.
3. **Trick #3 — hashtags (`#`):** confirm interests. *Combined example (tricks 2+3):* your target loves watching cricket in the stadium and used to upload nice pics with **#cricket + location**; then his company's cyber-security engineers explained "sir, you're exposed, people can target you," and he stopped posting selfies with live location — **but you found an old post from some year/month** — combining the date trick with the hashtag reaches that specific information, so you confirm: *okay — the target loves cricket, still goes, but stopped posting live location due to security awareness.*
4. **Trick #4 — `from:X to:Y`:** you linked someone as a friend/partner (other company), an investor, or a high-profile employee (a CEO won't be friends with a random customer, but with a high-profile employee — possibly, via recommendations). Now **confirm they actually chat**: `from:@vijayshekhar to:@friend` shows any tweets/replies between them — then reverse it. Bonus: in their communication you may find a **hot issue** — some project, some policy — extremely useful; note it down, because later, when you perform exploitation, this feeds a much bigger hacking scenario.
5. **Trick #5 — `filter:`** — until now usernames/hashtags returned videos + images + live all mixed; the output was scattered. `filter:images`, then `filter:videos`, then `filter:periscope` (live) — **narrow down** the unwanted. *"These tricks only hackers have — a normal person doesn't know them and has no use for narrowing down; but for us, we won't leave even the smallest thing. When we do OSINT on a target we spend 10–15 days — for a big target, day and night for months — gathering and linking. That's why the tricks must exist: only then can we get accurate information."*
6. **Trick #6 — logic (`AND`/`OR`):** like in Linux — the more you combine, the better the output. `AND` = both usernames mentioned in the same post ⇒ **there is definitely some relation between them** — some leaked info that proves a relationship and helps you link. `OR` = three scenarios: both in a post, or only user1, or only user2.
7. **Trick #7 — `near:`/`within:`:** the target exposed a location. "India" is huge — but someone specific mentioned **Gurgaon**; `near:Gurgaon within:5km` with your username/hashtag ⇒ customers (location confirmation) and friends/partners/relatives concentrated in that circle.
8. **Trick #8 — exclusion (`-`):** repeatedly-appearing irrelevant keywords/hashtags/usernames — exclude with the hyphen (`-keyword`, `-@username`) — remember **no space**.
9. **Trick #9 — `since:`/`until:`:** you have intel that around a certain date/year they tweeted/worked on something — partners/colleagues/employees may be in that window; find it all on a date-range basis.

Using each of these tricks you can extract different information — quite interesting information. **Yes or no — tell me!** Then we end the class and continue tomorrow.

Okay, let's end today's session… otherwise [the next session] will be the day after — if there's a session tomorrow you'll get the information in the group, whether your session is tomorrow or not. Okay — bye!
