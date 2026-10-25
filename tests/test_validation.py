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
        with self.assertRaisesRegex(ValueError, "empty or whitespace"):
            require_non_empty_text("")

    def test_rejects_whitespace_only_string(self) -> None:
        for value in (" ", "\u00a0"):
            with self.subTest(value=repr(value)):
                with self.assertRaisesRegex(ValueError, "empty or whitespace"):
                    require_non_empty_text(value)

    def test_rejects_control_characters(self) -> None:
        for value in ("\x00", "\x1f", "\x7f", "\x85", "\nhello", "hello\r"):
            with self.subTest(value=repr(value)):
                with self.assertRaisesRegex(ValueError, "control or zero-width"):
                    require_non_empty_text(value)

    def test_rejects_zero_width_and_format_characters(self) -> None:
        for invisible in ("\u200b", "\u200c", "\u200d", "\u2060", "\ufeff", "\u034f"):
            with self.subTest(codepoint=f"U+{ord(invisible):04X}"):
                with self.assertRaisesRegex(ValueError, "control or zero-width"):
                    require_non_empty_text(f"safe{invisible}text")

    def test_max_length_accepts_exact_limit_after_trimming(self) -> None:
        self.assertEqual(require_non_empty_text("  abc  ", max_length=3), "abc")

    def test_max_length_rejects_value_over_limit(self) -> None:
        with self.assertRaisesRegex(ValueError, "must not exceed 3 characters"):
            require_non_empty_text("abcd", max_length=3)

    def test_max_length_is_optional(self) -> None:
        value = "x" * 300
        self.assertEqual(require_non_empty_text(value), value)
        self.assertEqual(require_non_empty_text(value, max_length=None), value)

    def test_max_length_rejects_non_integer_values(self) -> None:
        for max_length in (True, False, 3.5, "3"):
            with self.subTest(max_length=repr(max_length)):
                with self.assertRaisesRegex(TypeError, "max_length"):
                    require_non_empty_text("text", max_length=max_length)

    def test_max_length_rejects_zero_and_negative_values(self) -> None:
        for max_length in (0, -1):
            with self.subTest(max_length=max_length):
                with self.assertRaisesRegex(ValueError, "positive integer"):
                    require_non_empty_text("text", max_length=max_length)


if __name__ == "__main__":
    unittest.main()
