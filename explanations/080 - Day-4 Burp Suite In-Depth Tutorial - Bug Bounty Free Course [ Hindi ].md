# Burp Suite proxy setup and request interception — Explained

## Lesson map

Day 4 introduces Burp Suite as an intercepting HTTP proxy. The instructor explains the client–proxy–server model, configures Firefox, installs Burp's local CA certificate for the lab browser, and captures requests.

## What Burp does

Normally a browser sends HTTP requests directly to a server and receives responses. With Burp configured as the browser's proxy, both directions pass through Burp. A tester can inspect messages, pause them, modify permitted test data, forward them, or drop them. Burp is not a VPN, and merely routing traffic through it does not make unauthorized testing legal.

Community Edition supports the core manual workflow; some automated features and Intruder speed are limited compared with Professional. Learning raw requests and responses is more important than edition-specific automation.

## Listener and browser configuration

Burp's default proxy listener is commonly `127.0.0.1:8080`. The loopback address means only software on the same machine can reach it. Confirm the listener is running under Proxy settings, then configure the dedicated Firefox lab profile to use that host and port for HTTP and HTTPS. Do not proxy everyday browsing or accounts through an experimental setup.

For HTTPS inspection, Burp dynamically presents certificates signed by its own local CA. Export Burp's CA certificate or obtain it through Burp's local helper page, then import it into the dedicated browser's certificate authorities and trust it only for website identification in this lab profile. Protect the CA private key and remove trust when the lab is retired. Certificate warnings should be investigated, not bypassed indiscriminately.

## Intercept workflow

Under **Proxy → Intercept**, switch interception on, then request a lab page. Burp pauses the outbound request and displays method, URL, headers, cookies, and body. **Forward** releases the current message; several forwards may be required because one page loads many resources. **Drop** cancels the selected request. Switch interception off when passive browsing is desired; HTTP history can still record proxied traffic.

The request editor allows controlled changes before forwarding, making client-side assumptions visible. Always stay within scope and avoid modifying destructive or real-user operations. The tutorial's central model is simple: browser is the client, Burp is the controlled intermediary, server remains the destination.

## Next practice

Use an intentionally vulnerable local application to identify a request, send copies to analysis tools such as Repeater, vary one input at a time, compare responses, and document the result. Keep target scope narrow so unrelated traffic is not collected.

## Review checklist

- Use only isolated training systems or assets covered by explicit authorization.
- Download tools and images from trustworthy sources and verify them where possible.
- Record configuration, expected behavior, and rollback steps.
- Keep personal data and everyday accounts outside the security lab.

<!-- DONE-080 -->
