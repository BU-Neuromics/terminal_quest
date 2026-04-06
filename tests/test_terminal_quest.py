from unittest.mock import patch

import pytest

from terminal_quest.terminal_quest import rndchr


# --- rndchr ---

@pytest.mark.parametrize("n", [1, 5, 10, 26, 27, 52])
def test_rndchr_correct_length(n):
    result = rndchr(n)
    assert len(result) == n


def test_rndchr_only_letters():
    for _ in range(20):
        assert rndchr(10).isalpha()


def test_rndchr_produces_variety():
    results = {rndchr(6) for _ in range(50)}
    assert len(results) > 1


# --- main() integration ---

def test_main_creates_top_level_structure(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    from terminal_quest.terminal_quest import main
    with patch("terminal_quest.terminal_quest.banner"):
        main()

    assert (tmp_path / "level0").is_dir()
    assert (tmp_path / "level0" / "level0.md").is_file()
    assert (tmp_path / "level0" / "level1").is_dir()
    assert (tmp_path / "level0" / "level1" / "level1.md").is_file()


def test_main_creates_level2_hidden_dir(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    from terminal_quest.terminal_quest import main
    with patch("terminal_quest.terminal_quest.banner"):
        main()

    level1 = tmp_path / "level0" / "level1"
    level2_dirs = [d for d in level1.iterdir() if d.name == ".level2"]
    assert len(level2_dirs) == 1
    assert (level2_dirs[0] / "level2.md").is_file()


def test_main_prints_instructions(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    from terminal_quest.terminal_quest import main
    with patch("terminal_quest.terminal_quest.banner"):
        main()

    out = capsys.readouterr().out
    assert "level0" in out
    assert "cd" in out
    assert "grep" in out
