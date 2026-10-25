# Contributing

Thanks for contributing to Agent 4.

## Scope and coordination

- Keep changes focused and tied to a concrete correctness, testing, or CI need.
- Coordinate new language, framework, dependency, or broad architecture decisions with the Architect in [agent1](https://github.com/MvMSOLO/agent1). The initial stack proposal is tracked in [Issue #1](https://github.com/MvMSOLO/agent1/issues/1).
- Do not invent product requirements while the application scope is undecided.

## Tests

Use the standard-library `unittest` suite unless the team agrees to another test framework.

Run:

```bash
python -m unittest discover -s tests -v
```

Add regression tests for confirmed bugs and cover relevant valid input, invalid input, and failure paths. Do not claim checks passed unless they were actually run.

## Pull requests and commits

- Use focused changes with clear explanations.
- Prefer Conventional Commit prefixes such as `feat:`, `fix:`, `test:`, `docs:`, and `chore:`.
- Explain behavior changes, tests run, and any checks that could not be performed.
- Keep documentation consistent with the implementation.
