# `terminal_quest` #

`terminal_quest` is a [gamified](https://en.wikipedia.org/wiki/Gamification) introduction to basic command line navigation and file manipulation skills. It is implemented in the python programming language but requires no programming other than entering commands on a posix-compliant operating system command line interface.

`terminal_quest` is a series of puzzles that can be solved with only the commands **cd**, **ls**, **man**, **cat**, **head**, **tail**, file globbing (`*` character), and output redirection (`>` character).

![terminal_quest.png](https://bitbucket.org/repo/goGkbA/images/153806769-terminal_quest.png)

## Installation and Use ##

The easiest way to install `terminal_quest` is by using [anaconda](https://anaconda.org). After installing anaconda, open a terminal and run:

```
conda create -n terminal-quest -c bubhub python=3.5 terminal-quest
```

This will create a new conda environment called *terminal-quest* and install this software and the needed dependencies into it. To create your own terminal quest, run:

```
source activate terminal-quest
terminal_quest
```

The second command will display a festive and colorful splash message while it creates your own personal quest and provides some instructions and hints on how to start.