from itertools import product, cycle
import random
import sys
import termios
from time import sleep

import pyfiglet

from .compat import TerminalInfo, bg256, bold, green

try:
    _terminal_fd = sys.stdin.fileno()
    _flags = termios.tcgetattr(_terminal_fd) if sys.stdin.isatty() else None
except (AttributeError, OSError, termios.error):
    _terminal_fd = None
    _flags = None

term = TerminalInfo()

def set_echo_and_icanon(flag) :
    if _flags is None or _terminal_fd is None:
        return
    if flag :
        new = _flags.copy()
        new[3] = new[3] | termios.ECHO | termios.ICANON
    else :
        new = _flags.copy()
        new[3] = new[3] & ~termios.ECHO & ~termios.ICANON
    termios.tcsetattr(_terminal_fd, termios.TCSANOW, new)
    pass

def write(o) :
    sys.stdout.write(str(o))
    sys.stdout.flush()

def move(x,y) :
    write('\033[{};{}H'.format(y,x))

def up(n) :
    write('\033[{}A'.format(n))

hex_chars = '0123456789ABCDEF'
def random_color() :
    return '#{}'.format(''.join(random.choices(hex_chars,k=6)))

def rect(x1,y1,x2,y2,color) :

    term = TerminalInfo()

    positions = list(
            product(
                range(max(0,x1),min(x2,term.width)),
                range(max(0,y1),min(y2,term.height))
            )
    )
    for x,y in positions :
        move(x,y)
        write(bg256(color,' '))

def type_text(text,speed=0.03) :
    variance = 1
    for c in str(text) :
        write(c)
        jitter_speed = speed*((1-variance/2)+random.random()*variance)**2
        sleep(jitter_speed)

def type_texts(texts,speed=0.03,delay=1):
    for text in texts :
        sleep(delay)
        type_text(text,speed=speed)
        if texts.index(text) != len(texts)-1 :
            write(' ')
    sleep(delay)

# Taglines shown under the banner — add more here whenever inspiration strikes
TAGLINES = [
    "the black screen is a feature, not a bug.",
    "your mouse is on vacation. it'll be fine.",
    "click nothing. type everything.",
    "the cursor is blinking encouragingly.",
    "you're basically a hacker now.",
    "no icons were harmed in the making of this terminal.",
    "boldly going where no mouse has gone before.",
    "this is not the end. unless you type 'exit'.",
    "every great journey begins with a single keystroke.",
    "warning: may cause uncontrollable typing.",
    "you can't accidentally close a tab here.",
    "where there's a terminal, there's a way.",
]

def banner():
    art = pyfiglet.figlet_format("terminal quest", font="slant")
    write(bold(art))
    tagline = random.choice(TAGLINES)
    write(f"  {tagline}\n\n")

def dazzle() :

    term = TerminalInfo()

    positions = list(product(range(term.width),range(term.height)))
    random.shuffle(positions)
    for x,y in positions :
        move(x,y)
        write(bg256(random_color(),' '))
        sleep(0.001)

def clear() :
    write('\033[2J')

def fini():

    clear()

    move(0,0)
    sleep(3)
    type_text(green("oh hey"),speed=0.1)
    sleep(3)
    type_text(green("\n\nyou did it"),speed=0.1)
    sleep(3)
    type_text(green("\n\nthat was fun"),speed=0.08)
    sleep(3)
    type_text(green("\n\nthanks for playing"),speed=0.08)
    sleep(3)
    type_text(green("\n\nand as your reward"),speed=0.08)
    sleep(3)
    type_text(green("\n\nprepare yourself to be........."),speed=0.08)
    sleep(3)
    type_text(green("\n\nDAZZLED"),speed=0.01)
    sleep(1)

    if _flags is not None:
        set_echo_and_icanon(0)
        try :
            dazzle()
        finally :
            set_echo_and_icanon(1)
            banner()
            sleep(10)
            move(0,term.height)

    print(bold('if you enjoyed terminal quest, why not try the sequel: terminal temple?'))
    print(bold('https://bitbucket.org/bucab/terminal_temple'))
    print(bold('it almost certainly could be as good!'))
