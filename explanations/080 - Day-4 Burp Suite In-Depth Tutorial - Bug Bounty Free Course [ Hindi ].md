# Burp Suite — proxy, CA certificate, and interception — Explained

## Lesson reconstruction

Day 4 introduces Burp Suite as an intercepting HTTP proxy. Normally a browser sends requests directly to a server. After proxy configuration, browser traffic passes through Burp, allowing an authorized tester to inspect, pause, modify, forward, or drop messages in both directions. Burp is not a VPN and does not create permission to test a site.

Community Edition supports the core manual workflow, while some automated features and Intruder speed are limited compared with Professional. Understanding raw requests and responses is more valuable than depending on automation.

Burp's default listener is commonly `127.0.0.1:8080`. Loopback means local applications only. Confirm the listener under Proxy settings, then configure a dedicated Firefox lab profile to use that host and port for HTTP and HTTPS. Keep personal browsing and accounts outside this profile.

HTTPS requires certificate trust. Burp terminates the browser-side TLS connection and presents dynamically generated site certificates signed by Burp's local CA. Export the CA from Burp or obtain it from Burp's helper page, import it into the dedicated browser's certificate authorities, and trust it only for website identification in this lab. Remove it when finished. A CA private key is powerful and must not be shared.

Under **Proxy → Intercept**, turn interception on and request an authorized lab page. Burp displays method, URL, headers, cookies, and body. **Forward** releases the message; a page usually causes many requests, so several forwards may follow. **Drop** cancels the selected request. Turn interception off for normal proxied browsing; HTTP history still records traffic.

The editor permits controlled changes before forwarding. This reveals that browser-side fields are not security boundaries: the server must validate authorization and input itself. Send a copy to Repeater for careful one-variable-at-a-time experiments rather than repeatedly editing live traffic.

The instructor closes by asking students to practise setup and explore Burp's tabs only against local vulnerable applications. Scope discipline matters because a browser also loads third-party assets.

## Engineering and safety notes

Limit Burp project scope and logging to authorized hosts. Redact cookies, tokens, passwords, and personal data from screenshots. Prefer a temporary browser profile or Burp's embedded browser. If HTTPS fails, inspect proxy settings, listener status, certificate import location, hostname/time, and HSTS rather than disabling verification globally.

## Verification checklist

- Reproduce the workflow only in an isolated lab or explicitly authorized scope.
- Validate inputs, quote paths and variables, and test failure behavior.
- Preserve source, date, command, and minimal evidence for every observation.
- Distinguish a lead from a verified finding; do not overstate impact.
- Remove secrets and personal data from notes before sharing.

## Review questions

1. What prerequisite or authorization boundary controls this workflow?
2. Which output justifies the next action, and which output is only a lead?
3. How can false positives or stale data appear?
4. What is the safest failure/cleanup behavior?
5. How would a defender prevent or detect the weakness discussed?

<!-- DONE-080 -->
