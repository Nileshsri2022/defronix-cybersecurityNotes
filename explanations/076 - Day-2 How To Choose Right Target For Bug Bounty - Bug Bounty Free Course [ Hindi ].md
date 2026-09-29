# Choosing a suitable bug-bounty target — Explained

## Lesson map

Day 2 argues that target selection is a technical skill. Beginners often pick the most famous program, repeat the same obvious tests as thousands of researchers, receive duplicates or `Not Applicable` decisions, and lose motivation. Duplicates are normal, but thoughtful selection can reduce avoidable competition and align effort with existing skills.

## Compare programs systematically

The instructor compares two hypothetical targets. One has thousands of active researchers, narrow scope, and slow triage; another has fewer researchers, broad scope, and quicker responses. The second may look preferable, but there is no universal winner: if the first program's technology and allowed vulnerability classes match your strongest skill, it may still be the better choice.

Evaluate at least:

- **Scope size and clarity:** number and variety of permitted web, API, mobile, and wildcard assets.
- **Your skills:** technologies and vulnerability classes you can test competently.
- **Competition and program age:** popular mature assets are more heavily tested; new assets and newly launched programs may offer fresher surface.
- **Response/triage history:** how actively reports are handled and how clearly decisions are explained.
- **Rewards:** eligible severities, ranges, exceptions, and whether the program is paid or VDP-only.
- **Policy constraints:** forbidden automation, denial-of-service, social engineering, account access, data handling, and disclosure restrictions.
- **Product fit:** whether you can create accounts, understand workflows, and test without harming real users.

## Understanding scope

Using a platform program page, the instructor points out the `Scope and rewards` section. Scope is the exact set of assets on which testing is authorized, often with asset-specific eligibility and severity rules. A company name is not scope. Related domains, third-party services, acquired brands, and IP addresses remain out of scope unless listed. Conversely, a wildcard may include many subdomains but still have exclusions.

Check scope again before every test and before reporting because programs change. Save evidence of the policy version you relied on. When ownership or authorization is ambiguous, ask the program rather than assuming.

## A practical selection method

Shortlist several programs, score them against scope, skill fit, competition, response quality, and reward expectations, then spend a fixed trial period understanding one product deeply. Build a program-specific attack-surface map instead of firing a generic scanner at every target. Track previous tests and disclosed reports so that each session explores something new.

A good first target is not necessarily the one with the highest maximum bounty. It is the program where permission is clear, the product is accessible, the scope offers enough depth, and the researcher can apply a well-understood technique safely and produce a strong report.

## Review checklist

- Work only on assets explicitly included in an authorized lab or program scope.
- Explain the purpose and risk of each step rather than copying commands blindly.
- Test success, failure, and invalid-input paths.
- Record observations and preserve enough evidence for reproducible notes.

<!-- DONE-076 -->
