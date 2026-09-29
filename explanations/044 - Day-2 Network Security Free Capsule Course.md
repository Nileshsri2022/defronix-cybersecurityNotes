# 044 — Day-2 Network Security Free Capsule Course — Explanation

## What this class covers

Day-2 of the Network Security capsule (trainer **Ayush Pathak**) taught live inside typed-out **TryHackMe rooms** ('Intro: Networking' rooms). The session opens with topology flaw demos, then follows the day's real payload: **IP addressing → subnetting basics → ARP (how LAN delivery really works) → DHCP (who assigns IPs) → the OSI 7-layer model → the TCP/IP 4-layer model**.

## 1. Topology failures (animated, on-screen labs)

- **Ring:** every device chained into a loop — **one cut anywhere and the whole ring dies** (the scissor-cut demo).
- **Bus:** one backbone cable for everyone — **overload the backbone with spam packets and the whole network stalls**.
- **Star:** everyone through a central box (switch/router) — resilient to one edge device dying, but **kill the central device and the entire network dies** (scissors-on-router demo).

## 2. Subnetting basics (the story form)

- 32-bit IPv4 = four octets (8 bits each), each octet 0–255 (00000000↔11111111).
- Per network, three special roles: **network address · gateway · broadcast**; a /24 leaves ~254 usable host addresses.
- **/24 = first 3 octets are the network part**; **/16 = first 2**, with borrowed bits creating sub-networks (the "departments — accounting/HR/finance" story = why classless addressing exists: one big network chopped into employee-group subnets).
- Key lesson: **"are these two IPs on the same network?" cannot be answered without the prefix/mask** — `192.168.29.x` and `192.168.30.x` are apart under **/24** but together under **/16**.
- **Subnet mask** = the network bits written as 1s: `255.255.255.0` ≡ `/24`. **CIDR** = counting how many host bits got lifted into the network side.
- Windows demo: `ipconfig` shows IP (192.168.29.x / 255.255.255.0) and **default gateway** = where packets for other networks go.

## 3. ARP — the day's核心 payload

**Inside a LAN, delivery runs on MAC addresses, not IP.**

- Every device keeps an **ARP table** (IP ↔ MAC mappings).
- Flow: host broadcasts an **ARP request** ("who has 192.168.29.13? tell me — here's my MAC") → everyone whose IP doesn't match **ignores** it → the owner **ARP-replies** with its MAC → requester **stores it in the ARP table** → all further packets to that IP actually go to that MAC.
- **Switch:** keeps a **MAC → physical-port** table; switches work purely on MAC, no IP.
- **Router:** needed only for network-to-network traffic (the NAT boundary); inside your own network the router's IP role doesn't matter — ARP/MAC does.

## 4. DHCP — who gives me my address?

**Dynamic Host Configuration Protocol.** Four-packet dance:

1. **DISCOVER** — client broadcast: "anyone here who can give me an IP?"
2. **OFFER** — server (at home, the router doubles as the DHCP server): "take 192.168.1.210"
3. **REQUEST** — client: "OK, I'd like that one"
4. **ACK** — server: final confirmation, the address is yours

`ipconfig` also shows **Lease Obtained / Lease Expires** — the visible form of Day-1's **dynamic-vs-static** talks: dynamic IPs renew/expiry, static is paid/stable.

## 5. OSI seven-layer model

A **model** (not a physical thing) of how data moves down-and-up between devices:

| # | Layer | Job |
|---|---|---|
| 7 | **Application** | user-facing software/GUIs — browser, email client, file server |
| 6 | **Presentation** | data in one standard form/translation |
| 5 | **Session** | keeps the session; big data chopped into small **packets** |
| 4 | **Transport** | **TCP vs UDP**; how transmission happens (see below) |
| 3 | **Network** | routing — shortest/most-available path; logical IP addressing; router |
| 2 | **Data Link** | MAC handling — the "joining" work inside a LAN |
| 1 | **Physical** | electrical signals, cables, binary |

Going **down = encapsulation** (each layer wraps headers on), going **up = de-encapsulation** (headers stripped till the application gets plain data).

### Transport deep-dive (TCP vs UDP)

- **TCP** — connection-oriented; **three-way handshake**: `SYN → SYN+ACK (seq+1) → ACK`, then data flows; **FIN flag** to finish; lost packets get **re-sent** → slower but reliable → email etc.
- **UDP** — no connection, fire-and-forget; whatever arrives, arrives → **fast** → live streams/stadium broadcasts where a lost frame doesn't matter.

## 6. TCP/IP model (the condensed real one)

Four layers real machines use: **Application** (with its friends) · **Transport** · **Internet** (= OSI's Network) · **Network Interface** (= OSI's Data Link + Physical).

## 7. Class norms & next

- Interior-labs (TryHackMe "Intro: Networking" follow-along) lectures continue to be **support-driven**: share task screenshots (nominate/tag optional but recommended) → the more support, the further the capsule extends.
- Next class: **packets & frames in depth + practicals**.

## Study pointers

- **Be able to draw ARP and DHCP from memory** — both are four-step flows and the two most-asked "how does a LAN actually work" questions.
- Practice the same-network question: given two IPs + a prefix, answer; then flip the prefix and re-answer.
- Memorise the OSI layers top-to-bottom with one job each, and the **SYN → SYN+ACK → ACK** handshake sequence with the +1 rule.
- Remember where each addressing lives: **LAN ⇒ MAC/ARP; switch ⇒ port table; router/Internet ⇒ IP/NAT**.
