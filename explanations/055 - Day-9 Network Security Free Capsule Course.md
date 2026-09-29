# Explained — 055 — Day 9: Network Security (Firewall Evasion, Practically + Nmap's Brain)

**Source:** Defronix Network Security Day-9 (Ayush Pathak). Structure: a *deliberate re-run* of the firewall-evasion room with live Wireshark proof, then the last rooms of the TryHackMe module: **version detection, OS fingerprinting, the Nmap Scripting Engine, and output formats.**
**Why the repeat matters:** evasion concepts taught abstractly on Day-8 get **seen on the wire** today — and two genuinely new professional rules drop out: **decoys must be live hosts**, and **IPID-based scanning has a full attack-geometry behind it.** The second half upgrades nmap from "port-finder" to "service/OS profiler with a scriptable brain."

---

## 0) Series context

The TryHackMe *Network Security* module is 3–4 rooms deep; Day-9 closes the **"Nmap Advanced Scanning"** room (evasion techniques) and starts the *Nmap proper* room's tail (service version detection / OS detection / NSE / output). He says it plainly — *"pehle envelope/letter-drama and advanced methods bata diye the; lekin PRACTICAL dikhana zaroori lagta hai"* — hence the re-run. Telegram is the doubt channel; the day ends with "post aayegi — uske peechhe COMMENT karo" (post-centric, like the NetSec capsule's usual rhythm).

---

## 1) Spoofing (`-S`) — the letter model, fixed in your head

One more telling of the story, because it is *the* model: **A** posts a letter to **DC** but writes **XC** in the sender field. DC reads "XC wrote this" and mails the reply **to XC** — not to A. Packets work identically:

```
attacker ──SYN (src = fake-IP)──▶ target ──SYN/ACK──▶ fake-IP   (the real attacker: silence)
```

From the target's logs and firewalls, **the fake box scanned it**. The attacker learns nothing locally… **unless they are sniffing the network segment where the replies land.** That dependency — how to sniff — is repeatedly deferred ("aage waali cheez"), and it is the single honest reason spoofing is a "sometimes tool": **great for blame-shifting, blind for data collection.** Day-8s `-S <ip>` flag syntax stands.

## 2) Decoys (`-D`) — live on the wire, plus THE hygiene rule

The Wireshark demo that makes it real: start capture, then

```
nmap -D <decoy-ip1>,<decoy-ip2>,ME <target-ip>
```

On the wire: **three SYN packets to port 80, three different source IPs** — only one is his; the other two are **decoys**. The target (and its IDS) sees three simultaneous scanners from three sources and replies to all three. **It cannot tell which one is the real operator** when it later checks logs.

### The school-yard analogy (his own, which is why it sticks)

> One kid's name surfaces in a classroom fight → *that kid gets suspended*. The report says **"the whole group did it"** → *unity activated — nobody can be punished*. Confusion reigns. That's exactly how the target reads a decoy scan.

### ⭐ The rule that separates "hidden" from "caught"

> **"Random IPs de doge to PAKDE JAAYENGE."** Decoys must be **live, reachable hosts that look like the real thing.**

The defender's counter-math: take the logged source IPs, ping/sweep them, and ask "which of these even **exist/actionable** on my network?" A fabricated dead address unmasks *you* precisely because it's implausible ("ye mera network hi nahi hai" moment). His operational training:

1. **Scan your own network first** (`nmap -sn 192.168.x.0/24` style) to enumerate **live hosts**.
2. Pick 2–5 of them as decoys (same subnet flavour, plausible roles), ending the list with your real address: `-D live1,live2,live3,ME`.
3. The traffic crowd is now *legitimate-looking* — "jo live ho toalready, reachable bhi ho — detection mushkil ho jaayega."

The principle generalises: `-S` spoofing's throwaway box and `-sI`'s zombie are the same species of choice — **always borrowed, never invented**.

## 3) Fragmentation — `-f` and `-ff`

Some packet filters operate on *whole* packets: reassemble-less, cheap signature-matching on a single buffer. nmap counters by **slicing each probe into tiny IP fragments** the filter can't parse but the destination reassembles normally:

- **`-f`** — fragments carrying **8 bytes** of data (multiples of 8)
- **`-ff`** — fragments carrying **16 bytes** ("double-F")

Wireshark verdict in the demo: one probe on port 80 appears as a *train of small fragments* instead of a single TCP segment — the "data" is visibly **split into parts**. Room quiz mechanics embedded in the lecture: **payload 64 bytes with 16-byte fragments → 64/16 = 4 fragments** — answer **FOUR**.

When to use: slipping past naive stateless filters/IDS that don't defragment. When not: modern appliances reassemble before inspecting, so `-f`mostly buys you *slower* scans, not invisibility. He frames it as just one more doorway in a hallway full of them — *"aur nahi bhi — doosre device ke naam pe kar lo, chhote part mein kar lo, extra cheez add karke kar lo — ek hi cheez itne tareeqon se."*

## 4) The idle (zombie) scan — the full IPID geometry, finally

The advanced scan Day-8 only teased. Its fuel is a quaint IPv4 header field: **IPID**, a per-sender counter that (classically) **increments by one for every IP packet the machine transmits**. It therefore leaks *how many packets a host sent between two observations* — and a machine can be made to "vote" on your behalf.

**Cast:** you (`A`), the **target**, and the **zombie** — a host that is **completely idle**: issuing *no* packets of its own. (His refrain: "ekdum shaant baitha — na request na response — bahut hi rare.")

**The play:**

```
Step 1  A probes the zombie directly (e.g. SYN/ACK prods) and NOTES its IPID → X
Step 2  A sends the target a SYN, but forged:  source-IP = ZOMBIE
          ├─ target port CLOSED │ target sends RST → zombie.Zombie never asked → IGNORES it.
          │                      zombie sends ZERO packets → IPID stays  X (+1 from step 1 = X+1)
          └─ target port OPEN   │ target sends SYN/ACK → zombie.Confused, zombie replies RST →
                                  zombie sent ONE packet → its IPID      X+1 already, (+1) → X+2
Step 3  A probes the zombie again and NOTES the IPID.

Verdict:  IPID_now − X = 1  ⇒ port CLOSED      (only your two probes moved the counter)
          IPID_now − X = 2  ⇒ port OPEN        (the zombie's involuntary RST moved it once more)
```

**What this buys:** the target's logs never see your real address; the scan is laundered through an innocent bystander; and — the neat part — **"filtered" doesn't defeat it in the usual way**: Day-8's lesson maps here as *closed ≡ filtered*, both reading difference-1. Only an *open* port writes a +1 onto the zombie.

**Why it's a museum piece (his honesty):**

- Finding a truly idle machine is **"bahut rare"** — any background chatter tickles its IPID by unknown amounts and your ±1/±2 arithmetic collapses.
- Any filtering mid-path mimics "closed."
- Modern stacks randomise IPIDs per protocol, breaking the trick everywhere except old/embedded gear.

He teaches it regardless — *"samajhna zaroori hai ki aisa bhi ho sakta hai — out-of-box sochna seekhna"* — because the geometry (borrow a silent third party, read side-channel counters) underpins real-world covert-channel logic. Command: **`-sI <zombie-ip> <target-ip>`**, followed (as all these) by the reason-verdict ordering below.

## 5) `--reason` — attach the evidence to the verdict

One flag, huge didactic value:

```
nmap --reason <target>
```

Now each line answers *"kyun?"* — `open` **because** received SYN-ACK; `up` **because** received ARP response; `closed` **because** received RST… His framing: every claim comes packaged with its witness - "ek-ek cheez ke saamne aapko — uska REASON kya hai" — so confusion resolves into Google-able specifics, and new scan types stop looking magical (Day-8's flagless scans, Day-9's zombie, all become "which packet told nmap that?").

## 6) Service & version detection — `-sV` and its intensities

Open-port lists tell you *which door*; this next flag asks **who's behind the door and what version they're running** ("22 agar khula hai — kaunsa ssh chal raha hai — bahut saare aate hain").

```
nmap -sV <target>
```

Mechanism, per his bridge-back to Day-6: exactly what `telnet ip 80` + banner-reading did by hand — nmap **completes a real connection** ("3-way handshake karega hi karega" — hence it *can't* be fully stealthy) and parses banners/probe-responses against a signature DB to name **service + version + host detail**.

**Tuning knobs:**

| Flag | Effect |
|---|---|
| `--version-intensity 0-9` | how hard to probe: 0 = banner-sniff only, 9 = try every probe |
| `--version-light` | = intensity 2 — fast, catches the loud ones |
| `--version-all` | = intensity 9 — slow + noisy, maximal certainty |

Room Q (whose detail fogs in ASR): with `--version-light`, one service went *undetected* — lesson: light mode trades coverage for speed; bump intensity on anything that responds "unknown." His pragmatic addenda: use it to *present* results credibly; after that, Google versions → CVEs (the recon-to-exploit bridge).

## 7) OS detection — `-O` (letter O, not zero — his emphasis)

```
nmap -O <target>
```

Same way humans guess a stranger's accent, nmap ships a **fingerprint database** of TCP/IP-stack quirks (window sizes, options, TTL defaults, DF behaviour…) and, from a handful of crafted exchanges, **matches or *guesses* the operating system** ("fingerprinting se — ya ek guess laga sakta"). Live result in class: it fingerprints the local machine and reports a guess with details. Practical ceiling: depends on what filtered/idle behaviors were visible, so guesses blend with certainty words; also flag `--osscan-guess` exists upstream for "try harder" (not shown — keep for self-study).

## 8) NSE — the Nmap Scripting Engine

The upgrade from "scanner" to "platform":

- Written in **Lua** ("script ka language"); *you can write your own* too.
- Every nmap ships hundreds of ready scripts, sorted into **categories** (auth, brute, default, discovery, vuln, …), located at **`/usr/share/nmap/scripts/`** (he literally browses there).
- They hook the scan pipeline: NSE scripts run *during/around port scanning* and squeeze out **extra information automatically** (http titles, robots.txt content, SSL details, auth banners…).

**The two daily-driver flags:**

```bash
nmap -sC <target>                      # run everything in the DEFAULT category
nmap --script=<name> <target>          # run exactly this script
nmap --script-help                     # (upstream; what his "dek / description" browse = docs)
```

He demonstrates by pulling the **`http-robots.txt`** script's nmap.org page (Entries/Example/…): the takeaway is *read the script's own doc*, then fire it by name. `-sC` vs `--script=`: category-wide defaults vs surgeon's scalpel — you'll want the latter once targets stop being lab boxes.

## 9) Output formats — because scanning is a pipeline step

nmap writes results in multiple shapes simultaneously; his syllabus names three-plus (the ASR-swallowed one noted):

| Flag | Format | Why you reach for it |
|---|---|---|
| `-oN <file>` | **normal** — same text you see | human reading, attaching to reports |
| `-oG <file>` | **grepable** | awk/grep/cut pipelines (his "personal form mein data" = scripting ingestion — JSON-like parsing was probably his intent) |
| `-oX <file>` | **XML** | machine-exchange; **convertible into a styled HTML report** (the room has you open/download a rendered page) |
| `-oA <base>` | **all three at once** | the default habit on engagements (his final "as dena hai" line almost certainly = `-oA`) |

His shrug at the end is the pros'shrug: *"do-teen tareeqa try kar lo — jaisa chahen, vaisa."* On real engagements, `-oA target_$(date …)` is the reflex.

## 10) The whole fortress-bypass toolbox in one view (post-Day-9)

```
VISIBILITY ladder (who does the target think is knocking?):
  plain scan ──▶ -Pn (dodge its discovery rules) ──▶ -D live-host decoys,ME (group blame)
              ──▶ -S fake-ip (blame a stranger; needs SNIFFING to see answers)
              ──▶ -sI zombie (blame the sleeping: IPID side-channel — fragile, rare)

FILTER-shape ladder (how the packet looks in transit):
  -sS half-open ──▶ -sN/-sF/-sX odd-flag probes ──▶ --scanflags custom ──▶ -f/-ff fragment it ──▶ --source-port / -D painting (later rooms' extras)

MEASUREMENT polish (what you carry away):  --reason · -sV (--version-intensity|-light|-all) · -O · -sC/--script · -oN/-oG/-oX/-oA
```

## 11) Pitfalls & perma-details

- **Decoys of the dead expose the living.** The single biggest beginner mistake in evasion — random `-D` values flag you faster than no decoys at all. Sweep, pick live ones, then hide.
- **Spoofing without sniffing is a one-way blindfold** — restated today with the letter. Don't mistake "they can't see me" for "I can see results."
- **Fragments only trouble *lazy* middleboxes** — assume your audience reassembles.
- **IPID-scan dependencies:** idle zombie + slow-changing IPID + path without filters. Any one missing ⇒ garbage. That is why it is *taught but rarely fired*.
- **`-sV` inherently completes connections** — no half-open veil; pace and volume accordingly on watched networks.
- **`-O` = capital letter O** — his explicit warning.
- **NSE scripts are code running against real hosts** — some brute-forcy/vulny ones are as loud as an alarm; know the script before `-sC` on 10,000 hosts.
- **Keep every scan's **`-oA`** for your own diffing** — recon over weeks is meaningless without stored baselines.
- **Housekeeping today:** app's launched (review it), posts carry the real Q&A, screenshots of room tasks get posted/tagged (the "community is the classroom" model holds).

## 12) Cheat card

```
EVADE (advanced nmap room):
  -S <ip>      spoof source — blame fake box; REPLIES GO TO IT ⇒ you must be sniffing
  -D i1,i2,ME  decoys — 3 SYNs seen, mine buried in them; DECOYS MUST BE LIVE/reachable
               (scan own range first, pick real hosts; random = caught)
  -f / -ff     fragment packets: 8-byte chunks / 16-byte chunks (64B @16B = 4 fragments — room answer)
  -sI zombie target  idle-scan: IPID arithmetic ⇒ final-X: 1=closed, 2=open
               zombie must be TRULY idle ("bahut rare") — taught for the geometry

FINGERPRINT:
  -sV                         service+version via full connect (banner logic, telnet-style)
      --version-intensity 0-9 · --version-light · --version-all      (light misses some!)
  -O                          OS fingerprint guess (O, not zero) — stack quirks DB match
  --reason                    every verdict ships with its received-packet evidence

NSE (lua scripts @ /usr/share/nmap/scripts/, categorised):
  -sC               all DEFAULT-category scripts with the scan (auth/banners/etc. bonus info)
  --script=http-robots.txt    one script by name (docs on nmap.org: entries/example/usage)
  write-your-own in Lua

OUT:
  -oN normal · -oG grepable (pipeline food) · -oX XML (→ HTML report) · -oA all at once
```

**Series position:** the NetSec capsule now spans basics → discovery → port-scan toolset → evasion → profiling/NSE/output; the room closes with "next lecture" pending — the remaining TryHackMe rooms (protocols/firewalls/VPN-shaped topics in this module's tail) or a new segment, per the capsule's traffic. Either way, the reconnaissance arc is now *complete end-to-end* — and Bash (053/054) is queued to automate exactly this toolset in later chapters.
