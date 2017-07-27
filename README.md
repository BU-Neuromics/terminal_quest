# Introduction

`terminal-quest` is a [gamified](https://en.wikipedia.org/wiki/Gamification) introduction to basic command line navigation and file manipulation skills. It is implemented in the python programming language but requires no programming other than entering commands on a command line. 

`terminal-quest` is a series of puzzles that can be solved with only the commands **cd**, **ls**, **man**, **cat**, **head**, **tail**, **grep**, file globbing (`*` character), and output redirection (`>` character).

![terminal_quest.png](terminal_quest.png)

## Installation and Use ##

### pypi ###

You can install `terminal-quest` using `pip`:

```
pip install terminal-quest
```

### Anaconda ###

An alternative way to install `terminal-quest` is by using [anaconda](https://anaconda.org). After installing anaconda, open a terminal and run:

```
conda create -n terminal-quest -c bubhub python=3.5 terminal-quest
```

This will create a new conda environment called *terminal-quest* and install this software and the needed dependencies into it. To create your own terminal quest, run:

```
source activate terminal-quest
terminal_quest
```

Note that the executable is `terminal_quest` not `terminal-quest`! The second command will display a festive and colorful splash message while it creates your own personal quest and provides some instructions and hints on how to start. **NB:** the anaconda method only currently works on linux systems.

### Manual Installation ###

If you do not have access to anaconda, you may also install this package manually. You can either clone this repo to your local machine with:

```
git clone https://bitbucket.org/bubioinformaticshub/terminal_quest.git
```

or simply download the most recent stable version from [the downloads page](https://bitbucket.org/bubioinformaticshub/terminal_quest/downloads/?tab=tags).

Once downloaded (and expanded, if downloaded as an archive), open a terminal and run from within the source directory:

```
python setup.py install
terminal_quest
```

### Dependencies ###

This package uses the following non-standard python packages:

* [future](https://pypi.python.org/pypi/future)
* [fabulous](https://pypi.python.org/pypi/fabulous)
* [pillow](https://python-pillow.org/)
