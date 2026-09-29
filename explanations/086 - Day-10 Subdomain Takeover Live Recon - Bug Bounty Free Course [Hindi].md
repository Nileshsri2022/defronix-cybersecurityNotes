# Day-10 Subdomain Takeover Live Recon — Explained

## Purpose of this lesson

Subdomain takeover is a **lifecycle and ownership failure** across two control planes:

1. the organization's DNS zone;
2. a third-party provider's resource namespace.

A scanner sees symptoms. A researcher must prove that the two control planes are disconnected in an exploitable way.

The canonical condition is:

```text
in-scope DNS name
  + dangling delegation/alias
  + externally claimable provider resource
  + ability to bind/serve the original hostname
  = potential subdomain takeover
```

Remove any term and the conclusion may be false.

---

# 1. DNS background

## CNAME

```dns
help.example.com. 300 IN CNAME tenant.vendor.example.
```

A resolver follows the alias to find address records for `tenant.vendor.example`. The browser still normally sends:

```http
Host: help.example.com
```

and validates TLS for `help.example.com`. The provider routes the request based on that hostname/custom-domain binding.

## Other record types

Takeover-like conditions are not limited to CNAME. Cloud resources can be referenced through:

- A/AAAA records to released addresses;
- NS delegation to abandoned DNS zones/services;
- MX or service-specific records;
- platform-specific alias/ANAME behavior;
- CDN and storage endpoints.

The validation model differs by record type. A dangling CNAME is the common teaching example, not the complete universe.

## DNS commands

Focused lookup:

```bash
dig +noall +answer help.example.com CNAME
dig +short help.example.com CNAME
```

Trace the chain manually:

```bash
dig help.example.com
dig tenant.vendor.example A
dig tenant.vendor.example AAAA
```

Check authoritative nameservers when cache/staleness matters:

```bash
dig example.com NS +short
dig @authoritative-ns help.example.com CNAME
```

`NXDOMAIN` means the queried name does not exist in DNS. `NOERROR` with no answer can mean an empty non-terminal or absence of that record type. `SERVFAIL` indicates resolution failure, often DNSSEC or upstream trouble. These are not interchangeable.

---

# 2. CNAME is not HTTP redirection

| DNS alias | HTTP redirect |
|---|---|
| resolver follows before connection | server responds after connection |
| address bar can remain original host | browser navigates to `Location` URL |
| provider receives original Host/SNI | next request targets redirect host |
| configured in DNS | configured in HTTP application/server |

Misunderstanding this distinction leads to weak takeover analysis. The vulnerability depends on where DNS sends traffic and how the provider assigns the original hostname.

---

# 3. Resource lifecycle failure

A safe decommissioning workflow should coordinate:

```text
application owners
DNS owners
cloud/SaaS account owners
security inventory
```

The common failure is organizational:

1. Team creates a vendor tenant/site/bucket.
2. DNS team points `sub.example.com` to it.
3. Months later, app team deletes the tenant.
4. DNS record has no tracked owner or dependency.
5. Namespace becomes available to another account.

This is why remediation is not merely “delete this CNAME.” Organizations need asset ownership and decommissioning controls.

---

# 4. Claimability versus dangling state

## Dangling but not claimable

A provider may return “resource not found” while preventing anyone else from claiming it because:

- the custom domain remains reserved to the original account;
- DNS TXT verification is mandatory;
- certificate/domain ownership must be proven;
- deleted names enter permanent or timed quarantine;
- the endpoint type is no longer offered;
- the namespace is account-specific rather than global.

This is a broken service configuration, but not necessarily a takeover.

## Claimable but not bindable

An attacker may recreate a similarly named provider project but still be unable to bind `help.example.com`. Serving only from `attacker.vendor.example` does not control the organization's hostname.

## Bindable and exploitable

A genuine takeover normally requires that requests for the original subdomain reach researcher-controlled content and pass the provider's routing requirements. TLS behavior also matters: if HTTPS cannot be served, impact may be reduced but not automatically absent.

---

# 5. Provider fingerprints

A fingerprint is a recognizable response associated with an unconfigured resource, such as a distinctive phrase, header, status, or DNS target.

A high-confidence fingerprint should include multiple signals:

```text
DNS target suffix matches provider
+ HTTP status/body/header matches known orphan state
+ resource identifier absent/unregistered
+ current provider behavior permits claim
```

One body string is weak because CDNs, proxies, translated errors, and custom pages change content.

The community `can-i-take-over-xyz` project is useful for provider research, but entries can become stale. Review its latest commits/issues and the provider's current verification documentation.

---

# 6. Authorized manual triage workflow

## Step 1: constrain input to scope

Maintain a reviewed file containing only approved names:

```text
in-scope-subdomains.txt
```

Do not feed raw certificate-transparency output directly into scanners. A discovered hostname can belong to a vendor or excluded asset.

## Step 2: obtain DNS chain

```bash
while IFS= read -r host; do
    printf '\n## %s\n' "$host"
    dig +noall +answer "$host" CNAME
 done < in-scope-subdomains.txt
```

Also resolve target records and preserve timestamps.

## Step 3: inspect HTTP and TLS gently

```bash
curl -sS -D headers.txt -o body.html \
  --max-time 15 "https://$host/"
```

Do not disable certificate checks by default. Certificate errors are evidence and may indicate the service cannot currently provision the hostname.

Record:

- status;
- redirect chain;
- server/provider headers;
- body fingerprint;
- certificate names/issuer;
- final URL.

## Step 4: map to provider

Confirm the DNS suffix and error against current provider documentation/fingerprint data.

## Step 5: determine policy

Read the bug-bounty brief for:

- whether subdomain takeover is eligible;
- whether resource claiming is allowed;
- whether third-party interaction is allowed;
- required proof format;
- cleanup instructions.

## Step 6: minimal proof

Prefer non-invasive evidence. Claim only if explicitly allowed. Do not collect visitor traffic, credentials, analytics, or cookies.

---

# 7. Tooling without blind trust

## Subzy-style scanners

Takeover scanners automate:

- DNS resolution;
- provider classification;
- HTTP requests;
- fingerprint matching.

They do not reliably prove:

- scope;
- legal authorization;
- current namespace claimability;
- custom-domain binding;
- realistic impact.

Run current help because flags change:

```bash
subzy --help
subzy run --targets in-scope-subdomains.txt
```

Treat output states separately:

| Output | Meaning |
|---|---|
| vulnerable/candidate | manually investigate |
| not vulnerable | no known fingerprint; not proof of safety |
| timeout/error | inconclusive |
| unknown provider | manual DNS/provider research required |

## Nuclei

List relevant templates before execution:

```bash
nuclei -tl -tags takeover
```

Inspect templates. Then use low rate and concurrency against the validated list:

```bash
nuclei -l in-scope-subdomains.txt \
  -tags takeover \
  -rl 5 \
  -c 2 \
  -o takeover-candidates.txt
```

Pin/log tool and template versions for reproducibility. Template updates can change results between runs.

## Deprecated tools

An abandoned scanner can create both false negatives and false positives due to obsolete fingerprints. It may also carry vulnerable dependencies. Maintenance status is part of tool selection.

---

# 8. Common false positives

## Ordinary 404

A 404 means the requested web resource was not found, not that a cloud namespace can be claimed.

## Temporarily unhealthy service

Deployment, maintenance, access policy, or origin outage can resemble an orphan state.

## Private tenant

The resource may exist but require authentication or network access.

## Protected custom domain

The provider may require a TXT challenge, account ownership, or pre-verified domain.

## Stale data

DNS caches, historical datasets, and scanners can show records already removed at the authoritative source.

## Wildcard DNS

A domain may resolve every arbitrary label to one error service. Test random labels and compare.

## CDN/WAF normalization

A fronting layer may replace origin errors with generic pages that match a scanner signature.

## Out-of-scope third party

A CNAME target can be vendor-owned. Testing/claiming that vendor resource may be unauthorized even though the alias begins under the company domain.

---

# 9. Impact analysis without exaggeration

A precise report distinguishes demonstrated control from hypothetical escalation.

## Direct impact

- trusted-host content control;
- brand impersonation;
- malicious downloads/links;
- content injection at old bookmarked URLs.

## Conditional impact

Cookies are exposed only if their scope and attributes permit it. OAuth risk exists only if the exact subdomain/URL is trusted as a redirect. CORS risk exists only if origin policy trusts it. CSP bypass exists only if the subdomain is an allowed source and relevant content can be served.

State these as confirmed only after authorized configuration evidence. Otherwise label them potential and explain prerequisites.

---

# 10. Safe report structure

```markdown
Title: Dangling CNAME permits takeover of help.example.com

Asset: help.example.com (in scope)

Summary:
The subdomain aliases an unclaimed vendor resource. Current vendor behavior
permits an authorized account to bind the hostname.

DNS evidence:
help.example.com CNAME tenant.vendor.example

Provider fingerprint:
<status, response phrase, headers, timestamp>

Reproduction:
1. Resolve CNAME...
2. Visit URL...
3. Observe provider orphan response...
4. [If explicitly permitted] bind test resource...
5. Observe neutral proof page...

Impact:
<demonstrated control and validated trust relationships>

Cleanup:
<resource removed/retained for remediation coordination>

Remediation:
Remove the stale record or restore and verify the intended resource.
```

Redact account IDs, secrets, and unrelated data.

---

# 11. Remediation engineering

## Immediate

- remove/disable dangling DNS;
- restore the legitimate provider resource if service is needed;
- coordinate any researcher-created proof resource;
- inspect logs and certificates for prior abuse;
- review trust relationships involving the subdomain.

## Preventive

- maintain DNS records as code with owners and review;
- link DNS entries to cloud-resource inventory;
- require decommissioning tickets to remove DNS before resource release;
- continuously resolve third-party aliases and alert on orphan fingerprints;
- use provider domain-verification controls;
- reserve important provider namespaces where appropriate;
- narrowly scope cookies, CORS, CSP, OAuth redirects, and allowlists;
- review wildcard DNS and wildcard trust rules.

## Monitoring

Detection should combine authoritative DNS inventory with active validation. Avoid automatically claiming resources as a monitoring method.

---

# 12. Special cases

## NS takeover

Dangling nameserver delegation can provide control over records beneath a delegated zone and may have broader impact than one web host. Validation is more complex and potentially disruptive; escalate carefully under policy.

## Expired domains

If a CNAME target is under an expired registrable domain, registering that domain may control many aliases. Domain registration creates cost and legal implications and should never be done without explicit permission.

## Cloud IP reuse

An A record pointing to a released cloud IP can become risky if another tenant receives the same IP. Proving intentional reallocation is less deterministic than claiming a named SaaS resource and may affect unrelated tenants.

---

# Command/reference card

```bash
# DNS
 dig +short sub.example.com CNAME
 dig +noall +answer sub.example.com
 dig sub.example.com +trace
 nslookup sub.example.com

# HTTP/TLS observation
 curl -sS -I --max-time 15 https://sub.example.com/
 curl -sS -D headers.txt -o body.html https://sub.example.com/

# Scanner discovery (verify current syntax)
 subzy --help
 nuclei -tl -tags takeover
 nuclei -l in-scope.txt -tags takeover -rl 5 -c 2
```

Never interpret command output without considering scope, authoritative DNS, provider status, and current claimability.

---

# Review questions

1. Why is a dangling CNAME not sufficient proof of takeover?
2. What is the difference between a CNAME and an HTTP redirect?
3. Which provider-side behavior makes an orphaned resource claimable?
4. Why can an unclaimed-resource fingerprint become stale?
5. What evidence can prove the issue without claiming a resource?
6. Why is a generic 404 a weak signal?
7. How do cookie attributes affect takeover impact?
8. What should a decommissioning workflow remove first?
9. Why must scanner errors remain “inconclusive” rather than “safe”?
10. Which control planes must an organization inventory together?

<!-- DONE-086 -->
