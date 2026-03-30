from __future__ import annotations

import shutil
import sys


CSI = "\033["
RESET = "\033[0m"


def _supports_ansi() -> bool:
    return sys.stdout.isatty()


def _wrap_ansi(text: str, code: str) -> str:
    if not _supports_ansi():
        return text
    return f"{CSI}{code}m{text}{RESET}"


def bold(text: str) -> str:
    return _wrap_ansi(text, "1")


def yellow(text: str) -> str:
    return _wrap_ansi(text, "33")


def blue(text: str) -> str:
    return _wrap_ansi(text, "34")


def green(text: str) -> str:
    return _wrap_ansi(text, "32")


def bg256(color: str, text: str) -> str:
    if not _supports_ansi():
        return text
    color = color.lstrip("#")
    if len(color) != 6:
        return text
    red = int(color[0:2], 16)
    green = int(color[2:4], 16)
    blue = int(color[4:6], 16)
    return f"{CSI}48;2;{red};{green};{blue}m{text}{RESET}"


class TerminalInfo:
    def __init__(self) -> None:
        size = shutil.get_terminal_size(fallback=(80, 24))
        self.width = size.columns
        self.height = size.lines


class Text:
    def __init__(self, value: str, skew: int = 0, shadow: bool = False, color: str | None = None) -> None:
        del shadow, color
        self.value = value
        self.skew = max(0, skew)

    def __str__(self) -> str:
        indent = " " * min(self.skew, 8)
        return f"{indent}{self.value}"
