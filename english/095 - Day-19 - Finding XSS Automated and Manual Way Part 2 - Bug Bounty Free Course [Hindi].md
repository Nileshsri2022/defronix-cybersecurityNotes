# Day-19 — Finding XSS Manually and with Automation, Part 2 — English Translation

*Translated from: `095 - Day-19 - Finding XSS Automated and Manual Way Part 2 - Bug Bounty Free Course [Hindi].hi-orig.srt`*

---

Part 2 turns the XSS model into a repeatable authorized workflow. Map inputs from URLs, forms, JSON bodies, headers, and client-side routes. Insert a unique non-executable marker and use Burp to locate every reflection. Determine parser context before changing syntax.

Manual testing is primary because it reveals transformations, encoding, filters, DOM behavior, authentication, and business impact. Compare raw response with the browser DOM and review JavaScript sources/sinks. Change one element at a time and keep requests reproducible in Repeater.

Automated scanners such as Dalfox, XSStrike, Burp Scanner, or Nuclei can triage large approved URL sets, but they create false positives and may send many payloads. Read tool behavior, restrict scope, lower concurrency/rate, exclude destructive endpoints, and manually verify every result. Do not feed archive output directly into scanners without scope and method review.

Filter bypass should mean understanding an incomplete defense—not spraying obfuscated payloads at production. Encoding layers, browser parsing, server normalization, and WAF behavior can differ. A WAF block is not proof that the underlying application is safe.

Report the exact source, sink/context, request, response or DOM evidence, trigger steps, user interaction, affected role, CSP/browser conditions, and harmless impact demonstration. Remediation must match the sink: contextual encoding, safe APIs, vetted sanitization, and architectural removal of string-to-code behavior.

<!-- DONE-095 -->
