"""Generic input-validation helpers used by the initial test foundation."""


def require_non_empty_text(value: object) -> str:
    """Return normalized non-empty text.

    Raises:
        TypeError: If value is not a string.
        ValueError: If value is empty or contains only whitespace.
    """
    if not isinstance(value, str):
        raise TypeError("value must be a string")

    normalized = value.strip()
    if not normalized:
        raise ValueError("value must not be empty or whitespace")

    return normalized
