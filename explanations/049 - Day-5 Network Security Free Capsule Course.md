# Network Security Day 5 — Active/Passive Recon, WHOIS, DNS, Shodan aur Wayback (Hinglish Explanation)

**Source transcript:** `transcripts/049 - Day-5 Network Security Free Capsule Course [ Hindi ].hi-orig.srt`
**Trainer in transcript:** Ayush Pathak
**Builds on:** Network Days 1–4 — addressing, VPN lab, ports and Metasploitable setup
**Continues:** Day 6 browser/ping/traceroute/Telnet/Netcat diagnostics
**Note:** Ye exact matching Hindi transcript ko context ke saath samajh kar likha gaya hai. Recon tools ko passive/public or explicitly authorized scope mein use karo; Shodan/DNS data ko exploit permission mat samjho.

---

## 1. Reconnaissance kya hai?

Attack/security assessment ka information-gathering phase reconnaissance hai:

- target/domain inventory,
- public IP/DNS,
- subdomains,
- historical pages,
- exposed services/devices,
- organizational clues.

### Active vs passive

| Type | Interaction | Example |
|---|---|---|
| Passive | Target infrastructure ko directly request nahi/low direct interaction | WHOIS, public search, Wayback, Shodan index |
| Active | Target/DNS/service ko query/probe | DNS queries, ping, port scan |

Passive less noisy but not risk-free; data stale/inaccurate. Active requires authorization, rate limit and scope.

---

## 2. WHOIS

WHOIS/RDAP domain-registration information provide kar sakta hai:

- registrar,
- creation/expiry dates,
- nameservers,
- registrant details if public/not privacy-protected.

Privacy services/redaction common. WHOIS email/phone historical/stale ho sakta; person identity proof nahi.

Defensive use:

```text
domain -> registrar/date/nameservers -> asset ownership hypothesis
```

Use official RDAP/registrar sources where possible. Contact data copy/share minimize.

---

## 3. DNS tools: `dig` and `nslookup`

DNS hostname ko IP/services records se map karta hai.

```bash
dig example.test A
dig example.test MX
dig example.test NS
dig example.test TXT
nslookup example.test
```

Records:

- A/AAAA: address,
- MX: mail servers,
- NS: authoritative nameservers,
- CNAME: alias,
- TXT: verification/policy text.

Subdomain discovery/zone transfer attempts active and authorization-sensitive. DNS data public hone par bhi no exploitation/no brute-force.

### 3.1 DNS troubleshooting

Different resolvers/cache/TTL ki wajah se results vary:

```bash
dig @1.1.1.1 example.test
```

Public resolver use policy/organization rules ke according. Sensitive internal names public query services mein paste mat karo.

---

## 4. DNSDumpster

Transcript DNSDumpster.com ko visual/public DNS discovery tool ke roop mein mention karta hai:

- subdomains,
- DNS records,
- IP relationships,
- host/network diagram.

Results leads hain; ownership and freshness verify karo. Tool terms/rate limits follow. Organization ke authorized domain par asset inventory ke liye use; random third-party domain nahi.

---

## 5. Shodan

Shodan internet-wide indexed service/banner data provide kar sakta hai. Search concepts:

- domain/IP,
- hostname,
- port,
- product/banner,
- organization/location filters.

Shodan result ka meaning:

```text
indexed observation at capture time
```

It is not permission, live proof or vulnerability proof. Banner old/false, IP reused, NAT/CDN/shared hosting ho sakta.

Defensive workflow:

1. Own authorized domain/IP range identify.
2. Shodan result capture timestamp/source.
3. Asset owner/port verify safely.
4. Exposure remediate—patch, close port, auth, firewall.
5. Recheck after change.

Credentials or exposed service par login/test nahi.

---

## 6. Tool overflow: recon ecosystem

Transcript additional tools/categories name-drops karta hai—search engines, subdomain/DNS tools, archive and public intelligence services. Tool list ya memorization se zyada methodology important:

```text
Question -> source/tool -> observation -> corroboration -> report
```

Different tools inconsistent output de sakte hain. Query/timezone/source note karo.

---

## 7. Wayback Machine

`archive.org/web` historical web snapshots preserve kar sakta hai:

- old pages,
- retired contact pages,
- previous JavaScript/assets,
- historical subdomains/branding,
- old public docs.

Useful for defensive exposure review, but archive copy:

- incomplete,
- stale,
- missing assets,
- cached sensitive content
ho sakti.

Historical secret milne par use nahi; current owner/security contact ko report and rotate/revoke recommend.

---

## 8. Recon report template

```markdown
Target: authorized domain/IP
Scope and authorization:
Tool/source:
Query/date/time:
Observation:
Freshness/limitations:
Independent verification:
Risk:
Recommended remediation:
```

Recon report mein:

- full personal contact data redact,
- no passwords/tokens,
- no exploit payload,
- screenshots only necessary,
- source links and timestamps.

---

## 9. Common mistakes aur safety points

1. Passive result ko current truth samajhna.
2. WHOIS privacy-redacted data ko infer/harass karna.
3. DNS query ko authorization bypass samajhna.
4. DNSDumpster result se every subdomain active assume.
5. Shodan banner ko vulnerability proof.
6. Shared/CDN IP ko organization ownership proof.
7. Wayback old secret ko use karna.
8. Active scan without scope.
9. Public recon data se login/brute force.
10. Source/timestamp/freshness record na karna.

---

## 10. Day 5 self-check questions

1. Active aur passive reconnaissance compare karo.
2. WHOIS/RDAP se kya data mil sakta hai aur limitation kya?
3. `dig A/MX/NS/TXT` records ka role kya?
4. DNSDumpster result ko verify kaise karoge?
5. Shodan indexed banner ko authorization kyu nahi samjha ja sakta?
6. Wayback defensive use-case do.
7. Historical secret milne par proper response kya?
8. Recon report mein timestamp/freshness kyu important?
9. CDN/shared IP attribution risk kya hai?
10. Passive reconnaissance kab active interaction ban sakta hai?

---

## 11. Continuity

Day 5 ne external/public recon ka toolkit diya. Day 6 browser, ICMP/ping, traceroute, Telnet and Netcat se network path/service behavior manually observe karega.
