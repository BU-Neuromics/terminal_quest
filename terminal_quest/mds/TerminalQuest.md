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
  3. by doing an `ls *SECRET` files get printed out that reveal the name of the
     correct hidden directory to follow

## Level 4 - looking at files to find the file path to the right answer

  1. there are 30 files in this directory, each that contains another filename
     or a hidden directory name
  2. there is a chain of 5 files that lead to the file with the directory name
     of the next level, all the other files contain random filenames that do not
     exist
  3. the chain starts with init.txt

## Level 5 - cat files together to print an ascii art message

  1. an ascii art version of the secret directory (.vrkalp) is split one per line
     across 9 files
  2. use cat to order the files correctly to read the directory name

## Level 6 - grep lines out of a bunch of a file to find secret messages

  1. `pearls.txt` contains mostly garbage text, but some lines start with SECRET
  2. grepping out these lines contains interesting science-y quotes, and the last
     line contains the directory to the next level

## Level 7 - grep lines out of a bunch of files using redirects and cat them together

  1. an ascii art python is split among five different text files that have random
     text lines, the art lines all start with SECRET
  2. the art lines are sequential within each file, but are in reverse order wrt
     the alphabetical sorting of the files
  3. the directory to level 8 is .python

## Level 8 - head and tail

  1. the top and bottom half of a Dr. Suess ascii art and quote is split between
     two files, fox.txt and sox.txt, respectively
  2. taking the appropriate number of head lines of fox.txt and concatenating
     with the appropriate number of tail lines of sox.txt reveals the full picture,
     quote, and a column of characters that points you to the last level

## Level 9 - putting it all together

  1. an ascii art of Calvin from Calvin and Hobbes jumping with sunglasses on is
     spread across multiple files, some with lines starting with SECRET, and others
     as the head or tail
  2. students should copy and paste this completed picture into blackboard
