# Agent 4 — The Tester

Agent 4 is responsible for unit and regression tests, reproducible bug checks, and CI reliability in the five-repository engineering collaboration.

## Current scope

This is a deliberately small starter, not a finished application. It currently provides one reusable input-validation helper as a concrete target for tests. Product-specific behavior remains undefined and should be agreed with the Architect before being added.

## Requirements

- Python 3.12 or newer
- No third-party runtime or test dependencies

## Run the tests

```bash
python -m unittest discover -s tests -v
```

## Validation helper

`agent4.validation.require_non_empty_text(value, max_length=None)` accepts a string, trims leading and trailing whitespace, and returns the normalized text.

- It raises `TypeError` for non-string values or an invalid `max_length` type.
- It raises `ValueError` for empty/whitespace-only text, a non-positive `max_length`, values longer than the normalized length limit, and Unicode control/format characters.
- It rejects Unicode `Cc` controls, `Cf` format characters (including common zero-width spaces/joiners and directional formatting characters), and U+034F.
- When provided, `max_length` applies after trimming and must be a positive integer; booleans are not accepted.

This is intentionally strict: some scripts and emoji sequences use format/joiner characters legitimately. Applications that need them should use a domain-specific validation policy. This generic helper is not a substitute for authorization or complete domain-specific validation.
