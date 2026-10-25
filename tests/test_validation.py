"""Unit tests for the generic input-validation helper."""

import unittest

from agent4.validation import require_non_empty_text


class RequireNonEmptyTextTests(unittest.TestCase):
    def test_trims_leading_and_trailing_whitespace(self) -> None:
        self.assertEqual(require_non_empty_text("  hello  "), "hello")

    def test_preserves_internal_whitespace(self) -> None:
        self.assertEqual(require_non_empty_text("hello   world"), "hello   world")

    def test_accepts_unicode_text(self) -> None:
        self.assertEqual(require_non_empty_text("  salom, 世界  "), "salom, 世界")

    def test_rejects_non_string_values(self) -> None:
        for value in (None, 123, [], b"hello"):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    require_non_empty_text(value)

    def test_rejects_empty_string(self) -> None:
        with self.assertRaises(ValueError):
            require_non_empty_text("")

    def test_rejects_whitespace_only_string(self) -> None:
        for value in (" ", "\t", "\n  \t"):
            with self.subTest(value=repr(value)):
                with self.assertRaises(ValueError):
                    require_non_empty_text(value)


if __name__ == "__main__":
    unittest.main()
