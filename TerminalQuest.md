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

## Level 3 - ls and globbing

  1. there are a lot of files in this directory, most with random names
  2. there are also a lot of hidden directories with random names
  3. by doing an ls *SECRET files get printed out that reveal the name of the
     correct hidden directory to follow

## Level 4 - looking at files to find the file path to the right answer

  1. there are 30 files in this directory, each that contains another filename
     or a hidden directory name
  2. there is a chain of 5 files that lead to the file with the directory name
     of the next level, all the other files contain random filenames that do not
     exist

## Level 5 - 
