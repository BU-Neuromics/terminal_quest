# Terminal Quest

This tutorial puzzle will help students get comfortable with a number of
common command line tools while searching for files nested in a directory
structure. The levels are as follows:

## Level 0 - ls, cat, and cd

  1. list the contents of the directory
  2. cd to the only directory available, proceeding to level 1

## Level 1 - man, ls -a

  1. type `man ls`, which gives usage information
  2. one of the options in the man page describes how to list hidden,
     or dot files, use it to list all the contents of the directory
  3. there is a hidden directory named .level2

## Level 2 - ls -l

  1. there are about fifty directories in .level2 that are different numbers
  2. one of the options in the man page describes how to list files in
     long format, which prints out the file size of each file among other infos
  3. the file size of the level file is the correct directory to change to
  4. all of the other directories have a fake level3 file in them, and they all
     are actually hard links to the same directory that leads nowhere

## Level 3 - 
