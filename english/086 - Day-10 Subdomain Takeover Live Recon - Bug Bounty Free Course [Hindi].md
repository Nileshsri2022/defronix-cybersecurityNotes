# Day-10 Subdomain Takeover Live Recon — Bug Bounty Free Course [Hindi] — English Translation

*Translated from: `086 - Day-10 Subdomain Takeover Live Recon - Bug Bounty Free Course [Hindi].hi-orig.srt`*
*Style: detailed edited translation. Repeated live-chat checks, promotions, and rolling-caption duplication are consolidated. Technical corrections and safety notes are marked [TN].*

---

## Opening and recap

Hello everyone. Please confirm that the audio and video are clear. Welcome to Day 10 of the Bug Bounty course. I hope you revised the sessions through Day 9. If something remains unclear, note the question for the doubt session.

Today's class is highly practical. We are studying a vulnerability that can appear during everyday reconnaissance: **subdomain takeover**. After finding subdomains, this is one of the conditions you may check—only where the bug-bounty program permits it.

Do not begin with a tool. First understand the concept, because a scanner can report false positives. If you understand DNS and the cloud service involved, you can decide whether a finding is genuine.

# 1. What is subdomain takeover?

Suppose a company owns:

```text
example.com
```

It creates a subdomain:

```text
help.example.com
```

The company does not necessarily host the help application on its own server. It may use a third-party platform such as GitHub Pages, Amazon S3, Heroku, Shopify, Tumblr, a help-desk provider, or another cloud/SaaS service.

The company wants visitors to open `help.example.com` while the content is actually served by the third-party platform. DNS makes this association possible.

A **subdomain takeover** can occur when:

1. the company's DNS still points its subdomain to a third-party resource;
2. the company deletes or abandons that third-party resource;
3. the DNS record is not removed;
4. the third-party provider allows another account to claim a resource with the same expected identifier/custom domain.

The remaining DNS record is called **dangling DNS**. If an authorized researcher can legitimately register the missing provider-side resource and bind the company's subdomain, content under that trusted subdomain may come under the researcher's control.

[TN: Dangling DNS alone is not always exploitable. The provider must also allow the unclaimed resource/custom-domain binding, and current ownership-verification controls may prevent it.]

# 2. CNAME records and third-party hosting

A **CNAME** means canonical name. It maps one DNS name to another DNS name without directly assigning an IP address.

Conceptual example:

```dns
help.example.com.  CNAME  company-help.github.io.
```

When a user visits `help.example.com`, DNS resolution follows the CNAME to `company-help.github.io`. The browser still requests the original hostname, and the provider uses that hostname to decide which customer's content to serve.

This is not merely an HTTP redirect. A redirect tells a browser to navigate to a different URL. A CNAME is DNS-level aliasing: it changes how the name resolves, while the user can continue seeing the company's subdomain.

The instructor demonstrates DNS management through a hosting provider/Cloudflare-style interface. The organization creates a CNAME for its help subdomain and points it at the hostname assigned by the third-party service.

Useful lookup commands include:

```bash
dig help.example.com CNAME
```

For broader DNS information:

```bash
dig help.example.com ANY
```

or:

```bash
nslookup help.example.com
```

[TN: `ANY` queries are often restricted or incomplete and should not be treated as a complete DNS inventory. Query record types explicitly. `dig +short CNAME name` is convenient for focused output.]

# 3. Normal lifecycle versus vulnerable lifecycle

## Normal state

```text
help.example.com
        |
        | CNAME
        v
company-help.provider.example
        |
        v
active company-controlled resource
```

The company owns both the DNS configuration and the provider-side project. Requests reach the intended content.

## Decommissioning mistake

Years later, the company stops using the help service. It deletes the provider project but forgets the CNAME:

```text
help.example.com
        |
        | stale CNAME remains
        v
company-help.provider.example
        |
        v
resource no longer exists
```

The subdomain may now display a provider-specific error such as “page not found,” “no such app,” “repository not found,” or “bucket does not exist.” That error is only a clue.

## Potential takeover

If the provider lets a different account recreate or claim the missing resource and attach `help.example.com`, requests may start serving that account's content.

The vulnerability exists because the trusted organization's DNS delegates control to a resource it no longer owns.

# 4. Security impact

The impact is not limited to displaying a defacement page. A compromised trusted subdomain may be abused for:

- phishing under an organization's domain;
- hosting malicious or misleading content;
- abusing user trust and brand reputation;
- receiving traffic from old links or documentation;
- interacting with cookies that were incorrectly scoped to a parent domain;
- bypassing weak allowlists that trust all company subdomains;
- influencing OAuth redirect or CORS configurations if those systems trust the subdomain;
- distributing files from a name users expect to be legitimate.

Impact depends on application design. A takeover does not automatically expose parent-domain cookies because cookie `Domain`, `Path`, `Secure`, `HttpOnly`, and `SameSite` attributes matter. It also does not automatically bypass same-origin restrictions for a different sibling or parent origin.

# 5. Safe proof of control

The instructor demonstrates the idea of creating a provider-side project, uploading an `index.html`, and binding a custom domain so a message appears through the affected subdomain.

A minimal proof page might contain only a researcher identifier and a neutral statement:

```html
<!doctype html>
<html lang="en">
  <meta charset="utf-8">
  <title>Authorized security validation</title>
  <p>Controlled by researcher-name for authorized validation.</p>
</html>
```

However, do this **only** when the program explicitly permits claiming the abandoned resource. Many programs ask researchers not to claim third-party resources because it can disrupt service or create legal/financial consequences.

Safer evidence may include:

- DNS output showing the dangling CNAME;
- the provider's distinctive unclaimed-resource error;
- documentation proving the resource identifier is unregistered;
- a non-invasive validation method approved by the program.

Never upload scripts, collect credentials, set cookies, impersonate the organization, or leave the resource active longer than necessary. Coordinate cleanup with the program.

# 6. GitHub Pages conceptual demonstration

The class uses GitHub as an easy-to-understand example:

1. A company hosts a project through GitHub Pages.
2. GitHub provides a name such as `project.github.io`.
3. The company points its subdomain to that name through CNAME.
4. The repository/site is later removed.
5. The CNAME remains.
6. Another account attempts to create the corresponding Pages resource and associate the custom domain.

The instructor creates a repository, adds an HTML file, and discusses the custom-domain/Pages settings.

[TN: Modern GitHub Pages has domain-verification and anti-takeover protections. Recreating a repository with a similar name does not necessarily permit binding another party's verified domain. Provider behavior changes over time, which is why current documentation and an authorized test are essential.]

# 7. Amazon S3 conceptual demonstration

The class also explains an S3-style static-site scenario. A company may point a subdomain to an S3 website endpoint. If the bucket is deleted but DNS remains, another party may try to create a bucket with the expected globally unique name in the appropriate region and serve an `index.html`.

The demonstration covers:

- creating a bucket;
- selecting a region;
- static website hosting;
- uploading `index.html`;
- content type such as `text/html`;
- access policy/public website configuration;
- mapping through DNS.

[TN: S3 security behavior, account-level public-access blocks, region-specific endpoints, bucket naming, ownership controls, and provider protections change. Never weaken an unrelated account's security or create a bucket for someone else's domain outside explicit authorization. A bucket creation attempt can itself seize a namespace and affect traffic.]

# 8. Which providers are vulnerable?

Not every dangling CNAME can be taken over. Some services:

- require DNS TXT verification before custom-domain binding;
- reserve previously used names;
- prevent cross-account re-registration;
- return an error but do not allow another customer to claim the resource;
- have fixed the takeover class entirely.

The instructor refers to the community-maintained **Can I Take Over XYZ?** project, which records provider fingerprints and whether takeover has historically been possible.

Examples shown in the session include services marked vulnerable, not vulnerable, or changed over time. The status must be treated as a starting point, not permanent truth. Check:

1. current provider documentation;
2. the project's latest entry and issues;
3. the exact error fingerprint;
4. whether domain ownership verification is required;
5. the bug-bounty program's rules.

A tool's “vulnerable” label is not a final report.

# 9. Manual investigation workflow

Before automation, the instructor recommends having a list of discovered in-scope subdomains.

For each candidate:

```bash
dig +short CNAME sub.example.com
```

Then inspect resolution and HTTP behavior:

```bash
dig sub.example.com
curl -I https://sub.example.com/
```

Questions to answer:

- Does the subdomain have a CNAME or other provider-linked record?
- Does the target record resolve?
- Which provider owns the target namespace?
- Does HTTP/TLS return a recognizable unclaimed-resource fingerprint?
- Is the provider currently claimable?
- Does the program permit takeover validation?
- Could this be a false positive caused by a private service, temporary outage, access control, or stale scanner signature?

Do not conclude “takeover” solely because the site returns 404. Ordinary applications return 404 every day.

# 10. Automated scanning with Subzy

The class demonstrates a subdomain-takeover scanner such as **Subzy**. After installing the tool from its maintained source, provide a file containing in-scope subdomains.

Conceptual usage:

```bash
subzy run --targets subdomains.txt
```

Exact flags depend on the installed version, so read:

```bash
subzy --help
```

The tool resolves names, identifies providers/fingerprints, and labels candidates. During the live scan, many entries are reported `not vulnerable`; some candidates appear vulnerable. The instructor manually checks them against provider status and discovers false positives—for example, a provider listed as not vulnerable.

This is the correct lesson: automation narrows a list; it does not replace verification.

The scan may also show connection and HTTP errors. Those errors mean the tool could not complete a check, not that the target is safe or vulnerable. Record them separately for careful review.

# 11. Other tools and maintenance status

The session mentions older takeover tools, including **SubOver**, and warns that discontinued projects may have stale fingerprints and no security updates. A tool being popular in an old tutorial does not make it reliable today.

When choosing a tool, check:

- latest release/commit date;
- open issues;
- fingerprint source and update frequency;
- supported DNS record/provider types;
- false-positive handling;
- whether installation instructions still match current dependencies.

Do not run abandoned binaries with unnecessary privileges.

# 12. Nuclei takeover templates

The instructor then introduces **Nuclei**, a template-driven scanner. Nuclei templates cover many categories; takeover templates encode provider-specific response fingerprints.

The template repository contains areas for HTTP, DNS, files, fuzzing, and takeover checks. Depending on the current Nuclei/template version, paths and tags may differ.

A conceptually safe command against a validated in-scope list is:

```bash
nuclei -l subdomains.txt -tags takeover
```

or a specific template/directory selected from the installed `nuclei-templates` tree. Always inspect current help and template metadata first:

```bash
nuclei -h
nuclei -tl -tags takeover
```

Update templates from the official ProjectDiscovery source and review what a template sends. Use controlled rate and concurrency:

```bash
nuclei -l subdomains.txt -tags takeover -rl 5 -c 2
```

The class explains hidden directories in Linux and where template files may be installed under a user's home/config/template path. File locations vary by version; do not assume one hard-coded path.

# 13. False positives

The live demonstration finds candidates that appear vulnerable, but manual checking shows why a report cannot be submitted immediately.

Common false-positive causes include:

- generic 404 text matching a provider fingerprint;
- provider status changed after tool signatures were written;
- active resource temporarily unavailable;
- private/authenticated tenant rather than abandoned tenant;
- custom domain reserved or already verified;
- DNS wildcard behavior;
- redirects to an unrelated error page;
- stale DNS resolver/cache results;
- CDN/WAF rewriting the response;
- the target is out of scope or belongs to a third party.

Validation should combine DNS chain, provider identity, current claimability, HTTP/TLS evidence, and program authorization.

# 14. Reporting and remediation

A report should include:

- affected in-scope subdomain;
- complete DNS chain and record type;
- third-party provider/resource involved;
- exact unclaimed-resource fingerprint;
- safe evidence of claimability/control, if permitted;
- realistic impact for this domain's trust relationships;
- timestamps and commands;
- cleanup status;
- remediation.

Recommended remediation:

1. Remove the stale DNS record immediately, or restore the intended resource.
2. Verify ownership before re-enabling the mapping.
3. Inventory all third-party DNS dependencies.
4. Make service decommissioning remove DNS and cloud resources in the correct order.
5. Monitor DNS for targets that no longer resolve or return provider-specific orphan errors.
6. Use provider domain-verification features.
7. Avoid broadly scoping cookies, CORS, OAuth redirects, or allowlists to every subdomain.

The safest decommissioning order is generally to remove/disable DNS delegation before releasing the provider namespace, allowing caches to expire as appropriate.

# Closing

Subdomain takeover is simple to describe but easy to misreport. The essential chain is:

```text
company subdomain
→ DNS points to third-party service
→ company deletes service resource
→ DNS remains
→ provider permits resource re-claim
→ another account can serve content on trusted subdomain
```

Start with DNS fundamentals. Use scanners only to identify candidates. Confirm the provider's current behavior, expect false positives, remain inside scope, and use the least invasive evidence the program accepts.

<!-- DONE-086 -->
