# XSS Part 2 — Manual and Automated Discovery Explained

## Manual sequence

1. Inventory inputs and rendering locations.
2. Send unique inert marker.
3. Locate it in response and live DOM.
4. Identify HTML/attribute/JS/URL context.
5. Observe encoding and transformations.
6. Create minimum harmless context-specific proof.
7. Retest from a clean victim session if authorized.

## Automation controls

Use a validated URL file, fixed rate, authenticated test account where allowed, and output logs. Disable blind callbacks unless the program permits them. Treat “found” as a candidate until browser reproduction.

## False positives/negatives

Reflection without execution is not XSS. Conversely, DOM execution may not appear in raw responses. Headless browsers, CSP, authentication, single-page routing, and asynchronous rendering affect tools.

## Reporting quality

Include raw and decoded values, exact context, screenshots plus textual requests, and impact prerequisites. Avoid generic severity claims such as “cookie theft” when cookies are HttpOnly or no sensitive session exists.

## Review questions

1. Why start with an inert marker?
2. Why compare response source and DOM?
3. What limits automated scanners?
4. Why can a WAF hide rather than fix XSS?
5. What makes an XSS reproduction complete?

<!-- DONE-095 -->
