"""Generic input-validation helpers used by the initial test foundation."""

from unicodedata import category


# U+034F is an invisible combining grapheme joiner (category Mn), so it needs
# an explicit check in addition to Unicode control/format categories.
_EXTRA_ZERO_WIDTH_CHARACTERS = frozenset({"\u034f"})


def require_non_empty_text(value: object, max_length: int | None = None) -> str:
    """Return trimmed non-empty text, rejecting invisible control formatting.

    max_length applies to the normalized (trimmed) text. It must be a
    positive integer when provided; booleans are rejected despite being
    int subclasses in Python.

    Raises:
        TypeError: If value is not a string or max_length is not an integer
            or None.
        ValueError: If input contains Unicode control/format characters, is
            empty after trimming, exceeds max_length, or max_length is not
            positive.

    This deliberately strict policy rejects Unicode Cc control and Cf format
    characters (including zero-width spaces/joiners and directional
    formatting controls), plus U+034F. Some legitimate writing systems and
    emoji sequences use format characters; callers should choose a
    domain-specific policy if those characters must be supported.
    """
    if not isinstance(value, str):
        raise TypeError("value must be a string")

    if max_length is not None:
        if isinstance(max_length, bool) or not isinstance(max_length, int):
            raise TypeError("max_length must be a positive integer or None")
        if max_length < 1:
            raise ValueError("max_length must be a positive integer")

    for char in value:
        if category(char) in {"Cc", "Cf"} or char in _EXTRA_ZERO_WIDTH_CHARACTERS:
            raise ValueError(
                "value must not contain control or zero-width formatting characters"
            )

    normalized = value.strip()
    if not normalized:
        raise ValueError("value must not be empty or whitespace")

    if max_length is not None and len(normalized) > max_length:
        raise ValueError(f"value must not exceed {max_length} characters")

    return normalized
