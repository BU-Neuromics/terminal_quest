from unittest.mock import patch

import pytest

from terminal_quest.compat import (
    Text,
    TerminalInfo,
    _supports_ansi,
    _wrap_ansi,
    bg256,
    blue,
    bold,
    green,
    yellow,
)


# --- _supports_ansi / _wrap_ansi ---

def test_supports_ansi_non_tty():
    with patch("sys.stdout") as mock_stdout:
        mock_stdout.isatty.return_value = False
        assert _supports_ansi() is False


def test_supports_ansi_tty():
    with patch("sys.stdout") as mock_stdout:
        mock_stdout.isatty.return_value = True
        assert _supports_ansi() is True


def test_wrap_ansi_no_tty():
    with patch("terminal_quest.compat._supports_ansi", return_value=False):
        assert _wrap_ansi("hello", "1") == "hello"


def test_wrap_ansi_with_tty():
    with patch("terminal_quest.compat._supports_ansi", return_value=True):
        result = _wrap_ansi("hello", "1")
        assert "\033[1m" in result
        assert "hello" in result
        assert "\033[0m" in result


# --- color helpers ---

@pytest.mark.parametrize("fn,code", [
    (bold,   "1"),
    (yellow, "33"),
    (blue,   "34"),
    (green,  "32"),
])
def test_color_with_tty(fn, code):
    with patch("terminal_quest.compat._supports_ansi", return_value=True):
        result = fn("text")
        assert f"\033[{code}m" in result
        assert "text" in result
        assert "\033[0m" in result


@pytest.mark.parametrize("fn", [bold, yellow, blue, green])
def test_color_no_tty_passthrough(fn):
    with patch("terminal_quest.compat._supports_ansi", return_value=False):
        assert fn("text") == "text"


# --- bg256 ---

def test_bg256_valid_with_hash():
    with patch("terminal_quest.compat._supports_ansi", return_value=True):
        result = bg256("#ff0000", "hi")
        assert "48;2;255;0;0" in result
        assert "hi" in result


def test_bg256_valid_no_hash():
    with patch("terminal_quest.compat._supports_ansi", return_value=True):
        result = bg256("00ff00", "hi")
        assert "48;2;0;255;0" in result


def test_bg256_invalid_length():
    with patch("terminal_quest.compat._supports_ansi", return_value=True):
        assert bg256("#abc", "text") == "text"


def test_bg256_no_tty():
    with patch("terminal_quest.compat._supports_ansi", return_value=False):
        assert bg256("#ff0000", "text") == "text"


# --- TerminalInfo ---

def test_terminal_info_has_dimensions():
    info = TerminalInfo()
    assert isinstance(info.width, int)
    assert isinstance(info.height, int)
    assert info.width > 0
    assert info.height > 0


# --- Text ---

def test_text_no_skew():
    assert str(Text("hello")) == "hello"


def test_text_with_skew():
    result = str(Text("hello", skew=4))
    assert result == "    hello"


def test_text_skew_capped_at_8():
    result = str(Text("hello", skew=100))
    assert result == "        hello"


def test_text_negative_skew_treated_as_zero():
    result = str(Text("hello", skew=-5))
    assert result == "hello"


def test_text_shadow_and_color_ignored():
    # shadow and color parameters are accepted but have no effect
    result = str(Text("hello", skew=2, shadow=True, color="#ff0000"))
    assert result == "  hello"
