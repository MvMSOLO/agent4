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

`agent4.validation.require_non_empty_text(value)` accepts a string, trims leading and trailing whitespace, and returns the normalized text. It raises `TypeError` for non-string values and `ValueError` for empty or whitespace-only input.

This generic helper is not a substitute for domain-specific validation, authorization, or security controls.
