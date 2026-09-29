# Explained — 052 — Day 8: Nmap Port Scanning — the Scan-Type Toolbox

**Source:** Defronix Network Security Day-8 (Ayush Pathak) — the "port scanning: basic → advanced" lecture promised at the end of Day-7. Stops mid-curriculum (he had to ship the upload); the tail continues in Day-9 (055).
**Why it matters:** Day-7 found *who is alive*; Day-8 begins *what is running on them*. Every scan type below is the same conversation in a different accent — send a packet, classify the reply (or the silence). The types differ in **who may run them** (root vs. not), **how loud they are**, and **what they can see through firewalls and loggers**. Choosing the right accent is the real skill.

---

## 1) Ground truth — what a "port state" even is

- **open** — a service is listening there (Lecture-4 chain: IP → port → socket → bind() → LISTEN). On port 80 it *usually* means a web server waits for clients.
- **closed** — nothing listens; the kernel itself answers any connection attempt with a RST (TCP) or ICMP error (UDP). Connection fails.

nmap, however, must express *its own uncertainty* and reports **six states**:

| State | Meaning |
|---|---|
| `open` | something accepts connections |
| `closed` | reachable, nothing listening |
| `filtered` | nmap **cannot determine open/closed** — probes dropped (firewall, packet loss) |
| `unfiltered` | port **is reachable** (it answered *something*) but nmap still can't decide open vs closed — typical of ACK scans |
| `open|filtered` | open or filtered — can't tell (typical of UDP & flagless scans) |
| `closed|filtered` | closed or filtered — can't tell |

Room answers: states exist in **6** forms (four primitive + two combo); the state you're *interested* in is **`open`** — but a `filtered` result is an *instruction*, not a failure: switch scan method and try again (that's the whole reason the advanced half of this lecture exists).

---

## 2) TCP flags refresher (the vocabulary every scan type speaks)

The TCP header carries 6 control bits — a flag is "set" when its bit = **1**:

- **SYN** — start a connection (*synchronize* sequence numbers)
- **ACK** — "I acknowledge receipt of what you sent"
- **FIN** — "I'm done — close gracefully"
- **RST** — hard reset: tear it down / nothing here / stop
- **PSH** — push buffered data up to the application now
- **URG** — urgent data: process this ahead of the regular queue

The **3-way handshake** = SYN → SYN/ACK → ACK, then data transfer. Every scan type below is defined by *which of these bits it sets* and *what answers it classifies*.

---

## 3) `-sT` — TCP Connect scan (the polite doorbell)

nmap asks the OS to do a **normal, complete connection** — full 3-way handshake, then disconnect.

```
you ──SYN──▶ box ──SYN/ACK──▶ you ──ACK──▶ …connected! ⇒ OPEN
you ──SYN──▶ box ──RST/ACK──▶             ⇒ CLOSED (it refused mid-greeting)
```

- **Who can run it:** anyone — it's nmap's **default for non-privileged users** (THM: "if you are not a privileged user, -sT is the only possible option"). No packet crafting; the kernel's `connect()` does everything.
- **Cost:** slowest and loudest — a *complete* connection is exactly what application logs, firewalls, and IDS record.

## 4) `-sS` — SYN / "half-open" / stealth scan (the knock-and-run)

```
you ──SYN──▶ box ──SYN/ACK──▶ you ──RST──▶  ⇒ OPEN  (we learn, then tear it down)
you ──SYN──▶ box ──RST/ACK──▶              ⇒ CLOSED
```

The trick: after learning the port is open, you send **RST instead of the final ACK** — the connection *never completes*. Rationale from the lecture: **logging systems that count only established connections never register it**. (Modern IDS *do* see SYN floods — "stealth" is relative to old-school loggers, as the lecturer's wording allows.) **Requires root** — you're crafting raw SYNs, not asking the OS to connect. It is the **default when you are root**, which is why `sudo nmap …` and `nmap …` can behave differently from the same shell.

## 5) `-sU` — UDP scan (the one where silence ≈ yes)

UDP has no handshake and no delivery guarantee:

```
you ──UDP──▶ open port   →  usually SILENCE          ⇒ open (or open|filtered)
you ──UDP──▶ closed port →  ICMP port-unreachable    ⇒ closed
```

- The logic inverts intuition: **no answer is the good news** ("it's stateless — nobody cares whether your packet arrived"); a closed port is the one that *replies* — via **ICMP Type 3 (destination unreachable)**, code 3 = port unreachable — the same ICMP lessons from Day-7 recycled.
- Why it feels slow: to rank silence as "open," nmap waits out timeouts and retransmits. That's the wait he sits through on camera.
- Same lesson as Lecture 4: **open UDP ports are quiet; closed ones complain** — count on the complainers.

---

## 6) Choosing what & how fast — the flag shelf

| Flag | Meaning |
|---|---|
| `-p22,80,443` | comma list of ports |
| `-p1-1023` | range |
| `-p-` | **all 65,535** ports (`-p1-65535` twin) |
| `-F` | **fast mode** — the ~100 most common ports only |
| `--top-ports N` | the N most common ports (nmap ships frequency stats) |
| `--min-rate N` / `--max-rate N` | send at least/at most N packets per second |
| `--min-parallelism` / `--max-parallelism` | probe-group sizing knobs (skip for now) |

The house rule from Day-7: never blindly sweep 65,535 UDP ports first — triage with `-F` or `--top-ports 100`, then widen deliberately.

---

## 7) The flagless family: `-sN`, `-sF`, `-sX` (the weird-doorbell scans)

RFC 793 says a packet that doesn't look like any phase of a conversation must be **answered with RST if the port is closed, and ignored if open** — giving all three scans the SAME result table:

| scan | flags set | open port | closed port | can't tell (filtered) |
|---|---|---|---|---|
| **NULL `-sN`** | **none — 0 flags** | silence | **RST** | silence… ambiguous |
| **FIN `-sF`** | FIN | silence | RST | " |
| **Xmas `-sX`** | **FIN+PSH+URG (3 flags)** — lit up "like a Christmas tree" | silence | RST | " |

Room quiz answers embedded in the lecture: flags set in NULL = **0**; in Xmas = **3**.

**The question HE asks for you** — *"if all three behave identically, why do three exist?"* — and answers: because **firewalls have opinions about packets**. Some middleboxes drop only SYN-less oddity; some drop everything weird *regardless of port state* (his "certain systems drop these packets regardless"). Running `-sN`, `-sF`, `-sX` and **comparing which probes got answers** profiles the firewall's rule set — their real job is **middlebox detection and evasion**, not better port truth. Caveat he reads off the room: on **modern networks this technique is unreliable-ish** — treat it as reconnaissance about the defenses, not as a port list.

---

## 8) `-sA` (ACK) and `-sW` (Window) — mapping the firewall itself

- **`-sA` ACK scan:** send a bare ACK — a packet that belongs to *no* connection. Any live TCP stack must reply **RST** to it (RFC-mandated). So: RST back ⇒ the port is **`unfiltered`** (reachable — no stateful filter ate it); silence/ICMP-error ⇒ **`filtered`**. It deliberately **cannot** say open-vs-closed; its whole point is *"is a firewall in between, and which way does it filter?"* — his classroom framing: "dono dekhne ko se lag rahe hain — antar hai: kya aane pe kya samajhna hai, port ke state ka nahi, firewall ka hisaab."
- **`-sW` Window scan:** ACK-scan twin that additionally reads the **TCP Window size field** in the returning RST — on some stacks, open ports answer with a non-zero window, closed with zero — squeezing open/closed hints out of the same probe. "Almost same — ek extra cheez."
- His demo on the room's target: 443/HTTPS type results come back **unfiltered/unverifiable** — he opens `http://` in the browser to sanity-check, and answers the room's question ("is it really open to us?") with **No**. Meta-lesson: these scans serve **rule-checking**, and you verify with the actual client (browser/curl), not by faith in scan labels.
- Both are root-only (raw packets) and — his words — **"not the scans you start with"**; they're second-stage instruments.

---

## 9) `--scanflags` — roll your own

`nmap --scanflags SYN,FIN 10.10.x.x` sets an *arbitrary combination* of bits. His demo: set **SYN alone** → you have re-implemented `-sS` by hand. No convention, no defaults — you set the flags, you send the packet, you classify the response yourself. Why teach it: it proves the scan types are just presets on one dial, and it is the primitive for probing filters that anticipate *known* scans.

---

## 10) Spoofing (`-S`) and decoys (`-D`) — hiding who knocked

- **IP spoofing `-S <addr>`:** forge the SOURCE IP on your probes ("pretend we are someone else"). The target then believes *that* host scanned it; an **idle/throwaway box** makes the perfect alibi. **The catch that makes this half-useless by itself:** all replies go to the *spoofed* address — **you see nothing unless you can sniff the network where the replies land**. (That traffic-capture machinery is booked for a later lecture; conceptually it's the zombie/idle-scan family.) Without the sniffing leg, spoofed scans are reconnaissance-by-sacrifice: you hide, but you're blind.
- **Decoys `-D decoy1,decoy2,ME,…`:** keep your real IP in the source list but bury it among **3+ fake ones** (`RND` generates randoms). Target logs then show several simultaneous "scanners" and can't tell which one is real. He tripped over the diagram direction and corrected himself on camera — the decoy layout is the one to remember: *"multiple hosts ke beech apne aapko hide"* — your machine becomes one line among many in the IDS alarm list. On your own LAN you can similarly play with **MAC addresses**.
- Room quiz mechanics: "make the scan appear to come from IP X" → **`-S X`**; "add decoys" → **`-D …`**. Both need matchable reachability (same route/segment) to be believable — and, as with spoofing, you only learn results for the probes sourced from **your** address among the decoys.

---

## 11) The decision flow (what to reach for, when)

```
Am I root?
 ├─ no  → -sT connect scan (your only option) — accept the noise
 └─ yes → -sS half-open SYN scan (default) — fastest, quiet-ish

UDP services of interest (DNS/53, SNMP/161, DHCP)?  →  -sU -p53,161... (slow — be specific)

Getting all-filtered on TCP?
 ├─ map the wall:      -sA  (unfiltered vs filtered — firewall present? stateful?)
 ├─ squeeze window:    -sW  (window-size hint on the RSTs)
 ├─ probe its biases:  -sN / -sF / -sX  (which odd packets get through?)
 └─ then hand-craft:   --scanflags …     (dial past its rule set)

Suspicious IDS / need cover?
 ├─ -D RND:5,ME  → stay visible but smeared across decoys
 └─ -S <idle-ip> → frame someone quiet (only useful if you can SNIFF the replies)

Speed?  -F | --top-ports 100 | --min-rate 1000 (lab), gentler on real networks
Always: results of filtered/open|filtered = instructions to try another scan — not answers
```

---

## 12) Pitfalls & exam-worthy details

- **Defaults differ by privilege**: same command, different scan — `nmap host` as user = `-sT`; as root = `-sS`. Triple the surprise when people diff their outputs.
- **"-sS is stealth" is a legacy claim** — modern IDS signatures watch half-open SYN patterns; the feature is *log-thinness*, not invisibility.
- **UDP silence is not proof of open** — hence `open|filtered` labels; confirm with a real client (dig, snmpwalk, the app).
- **`filtered` ≠ `closed`** — the single most common beginner misread. Filtered means *unanswered*, i.e., **someone exists and chose silence**.
- **RST proves a live stack**, even from a closed port — the Day-7 host-discovery principle, now working at port granularity.
- **NULL-scan logic relies on RFC 793 compliance** — Windows stacks famously don't comply (answer RST to everything ⇒ ports all look closed). Cross-check with a second scan family before believing a flagless result.
- **Spoof without sniff = blind** — the lecture's mandatory caveat ("is machine pe sniffing zaruri hai — warna scan bekar").
- **Scan speed flags (`-T0..5` family exists upstream too)** — his lab demos run fast; production patience (-T2/-T3) is the professional default — clipping rates avoids melting SOHO routers/SOC alarms.

---

## 13) 20-second cheat card

```
states: open · closed · filtered · unfiltered · open|filtered · closed|filtered
flags : SYN=start ACK=ack FIN=finish RST=reset PSH=push URG=priority   (bit=1 means SET)

-sT  full handshake        non-root default · noisy/complete · open=connect ok, closed=RST here
-sS  SYN then RST          root default    · "half-open", skips connection logs
-sU  no reply=open · ICMP port-unreachable=closed   (stateless! slow)
ports: -p22,80 · -p1-1023 · -p- (65535) · -F fast100 · --top-ports N
speed: --min-rate/--max-rate · (timing -T0..5)

flagless (open=SILENCE, closed=RST — all identical results, different packet shapes):
  -sN none(0 flags)   -sF FIN(1)   -sX FIN+PSH+URG(3)   → use: firewall profiling/evasion
-sA  ACK probe → RST = unfiltered (reachable), silence = filtered  → maps the firewall
-sW  same as -sA + reads RST Window size for open/closed hint
--scanflags SYN,URG,FIN  → build any preset yourself

hide:  -D ip,ip,ME decoys (real one lost in the crowd)
       -S ip  spoof source; replies go AWAY — only useful if you sniff their network
```

---

**Where Day-9 (055) picks up:** the lecture was cut short for shipping — remaining advanced material (IDS/firewall evasion techniques, fragmentation, the idle/zombie scan and its sniffing dependency, timing templates) is announced as "nothing skipped, next video finishes it." Day-7+8 together now cover the recon arc: discover hosts → scan ports → read the defenses.
