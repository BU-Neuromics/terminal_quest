from unittest.mock import patch

import pytest

from terminal_quest.pizzazz import TAGLINES, banner, random_color, type_text


# --- random_color ---

def test_random_color_format():
    color = random_color()
    assert color.startswith("#")
    assert len(color) == 7
    int(color[1:], 16)  # raises ValueError if not valid hex


def test_random_color_produces_variety():
    colors = {random_color() for _ in range(30)}
    assert len(colors) > 1


# --- TAGLINES ---

def test_taglines_is_nonempty_list_of_strings():
    assert isinstance(TAGLINES, list)
    assert len(TAGLINES) > 0
    for tagline in TAGLINES:
        assert isinstance(tagline, str)
        assert len(tagline) > 0


# --- banner ---

def test_banner_outputs_pyfiglet_art(capsys):
    with patch("terminal_quest.compat._supports_ansi", return_value=False):
        banner()
    out = capsys.readouterr().out
    # pyfiglet art is multi-line and substantially longer than the plain words
    assert len(out) > 50


def test_banner_includes_tagline(capsys):
    fixed_tagline = TAGLINES[0]
    with patch("terminal_quest.compat._supports_ansi", return_value=False):
        with patch("terminal_quest.pizzazz.random") as mock_random:
            mock_random.choice.return_value = fixed_tagline
            banner()
    out = capsys.readouterr().out
    assert fixed_tagline in out


def test_banner_tagline_chosen_from_list():
    chosen = []
    with patch("terminal_quest.compat._supports_ansi", return_value=False):
        with patch("terminal_quest.pizzazz.random") as mock_random:
            mock_random.choice.side_effect = lambda lst: lst[0]
            banner()
            args, _ = mock_random.choice.call_args
            assert args[0] is TAGLINES


# --- type_text ---

def test_type_text_outputs_each_character(capsys):
    with patch("terminal_quest.pizzazz.sleep"):
        type_text("hi!", speed=0)
    assert capsys.readouterr().out == "hi!"


def test_type_text_calls_sleep_per_character():
    with patch("terminal_quest.pizzazz.sleep") as mock_sleep:
        type_text("abc", speed=0.01)
    assert mock_sleep.call_count == 3
