# Explanation — 048 — Day 4: Network Security (Free Capsule Course)

**Source:** `transcripts/048 - Day-4 Network Security Free Capsule Course [Hindi].hi-orig.srt`
**Translation:** `english/048 - Day-4 Network Security Free Capsule Course.md`
**Level:** Beginner networking, Day 4 (trainer **Ayush Pathak**) — the promised *"better third way"* for port forwarding (**portmap.io + OpenVPN**, full hands-on walkthrough) plus the bridge into the exploitation half of the series (**Metasploitable 2** install, Kali-side OpenVPN, apache2/python file-serving, Zenmap).

---

## 1. The problem being solved (pick up from Day-3)

Day-3 left two port-forwarding options, each broken for real use:

| Option | Why it fails |
|---|---|
| **Router-based forwarding** | needs the router to expose the feature (his didn't) **and** a **static public IP** — home IPs are **dynamic**, so any IP you hand out "changes after some time" |
| **ngrok** (free tier) | tunnel dies on a timer, **URL changes every restart**, chokes under load |

**Requirement stated formally:** a **static link** you can give anyone — works from anywhere in the world **while your system is on**, dies when your system is off, and **the link itself never changes**. The motivating use case he names explicitly: **reverse shells need a fixed callback address** — a payload must know where to call home even across reboots and reconnects.

## 2. The solution recipe — portmap.io + OpenVPN (full walkthrough)

1. **Register on portmap.io** — with a **real email**. Hard-earned warning: temporary/fake emails (or misuse) get the account **silently BLOCKED** — the site doesn't tell you; you just see a dead "ban" sign and nothing connects. He burned a whole morning on this.
2. **Activate the account** via the emailed link → log in.
3. **Configuration → Create New Configuration**: type = **OpenVPN**, protocol = **TCP** (per your service) → **Download** the generated **.ovpn** file.
4. **Install OpenVPN GUI** (Windows 64-bit build).
5. **Run your local service** — he starts **XAMPP** so a web server listens on **port 80** (verified: `localhost` shows the "hello" page).
6. **In portmap, create the mapping entry:** external (assigned) port → **your machine's port 80**.
7. **Connect the tunnel:** OpenVPN GUI has no main window — **right-click the system-tray icon → Import File → select the .ovpn → right-click → Connect → icon goes green**; the portmap box shows the tick/green on refresh.
8. **Windows-side gotchas:** he disables the **Defender firewalls** (domain/private/public) via the "network security" settings, and notes the Wi-Fi **public/private profile** choice can block things.
9. **Copy the generated link → Enter → his locally-hosted website opens from the public internet.**

**The payoff (stated precisely):** the link survives **system restarts, VPN disconnect/reconnect, everything** — it only stops when (a) the machine is off, or (b) he **manually deletes the mapping entry** in portmap. Machine off → link down; machine back on → **same link serves again**. And it's **free**. (Rule repeated: it's a mapping, not website-only — **any** local service can be exposed this way.)

## 3. VPN basics, second pass (the "two-minute think" question)

He pauses the video: *"When you imported that .ovpn file — what did you actually DO?"* Answer through the TryHackMe diagram:

- Two grey **private networks** each sit on the internet but can't realistically act as one.
- The **blue network (the VPN) is a THIRD, separate network** — a device from each LAN joins it, and those members **act as if they're on a single LAN** — being in India vs Pakistan vs anywhere in Asia makes no difference.
- This is precisely why the TryHackMe / certification-lab experience feels like **"sitting inside a company's internal network"**: you're not port-forwarding *into* them — you've **joined their network**.

Side theory from the same module walkthrough: **switches come in Layer-2 and Layer-3 flavours**; **VLAN (Virtual LAN)** = one physical switch's ports split into fully separate virtual networks (VLAN-1 vs VLAN-2 — mutually blind, yet sharing one switch and one router above it); the *Network Simulator* room animates a switch flooding *"where is computer-3?"*, the TCP SYN exchange, and the final data flow — recommended to re-run slowed-down.

## 4. The pivot — exploitation needs a legal target (Metasploitable 2)

Fundamentals module = done. Next: enumeration → exploitation. Since **you can't attack arbitrary systems**, the series standardises on a **deliberately-vulnerable VM**:

- **Download Metasploitable 2** (~865 MB; he aliases it as "table-2").
- Install exactly like the Kali VMware image: extract → in VMware **New/File → Import** the VM → Start. Default login shown on-screen (classic `msfadmin`-style) — mostly it just needs to *run*; you'll be attacking it from your system.
- **Standing instruction: finish this setup before the next class** — "we're going to do quite a lot of work" against it (service enumeration, exploitation), with extra material added beyond the track where he deems fit.

## 5. Kali-side toolbox (demoed because the next phase lives in labs)

- **OpenVPN on Linux:** `sudo openvpn --config file.ovpn` → a new **tun0** interface appears (check with `ipconfig`/`ip a`; it vanishes on disconnect — his instant ch proof). **The reverse-shell rule:** when working inside such a lab/VPN, your callback IP is **the tun0 address the VPN assigned you** — *not* your router's private IP, *not* your public IP.
- **apache2:** `service apache2 start` — drop site files in **`/var/www/html`** and it's serving.
- **Windows quick-share:** `python3 -m http.server` → instant HTTP server bound to **any interface on port 8000** (browser must include `:8000` since 80/443 are the defaults) — his go-to for small file transfers.
- **Zenmap:** the GUI face of nmap on Windows — type only the **target**, it builds the command and renders results live (demo: scanning his own 192.168.x.x network). Reassures: full **scanning techniques** will be re-done properly later.

## 6. Logistics & close

- All tasks (including backlog from earlier lectures) must be **completed and shared** — that's his fuel to keep extending the series; doubts → comments (no registration needed anywhere to ask).
- Long lecture is deliberate — "everything will happen; you'll have no trouble."
- Coincided with **Teachers' Day** (Sept 5) — wishes exchanged at the end.
- Next: the remaining fundamentals-adjacent rooms wrap, then the slide toward scanning/enumeration against the Metasploitable target begins.

## 7. Study pointers

1. Recite the **static-vs-dynamic** argument: why does a reverse shell die with (a) dynamic home IP, (b) ngrok free links, and survive with portmap+OpenVPN?
2. Redraw the **blue-network-3** diagram from memory; answer his pause question in one line: *importing an .ovpn = joining the remote network as if local*.
3. Hands-on before next class: Metasploitable 2 imported and booted; on Kali — `sudo openvpn --config …` → confirm **tun0**, `service apache2 start`, and `python3 -m http.server` from a folder with one test file (open `http://<ip>:8000` from another machine/VM).
4. Keep the **callback-IP rule** taped to the monitor: *in a lab/VPN, LHOST = your tun0 IP.*
