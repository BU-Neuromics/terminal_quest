import sys

# terminal_quest.py has module-level sys.argv inspection that calls sys.exit()
# when extra arguments are present. Set argv to a single entry before any
# test module imports the package so that code path is never triggered.
sys.argv = ["terminal_quest"]
