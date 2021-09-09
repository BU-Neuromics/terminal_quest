from __future__ import division
from __future__ import print_function
from builtins import zip
from builtins import str
from builtins import range
import getpass
import hashlib
from past.utils import old_div
from collections import defaultdict
from glob import glob
import random
import os
import shutil
import string
import sys
import textwrap
from fabulous.color import bold, yellow, blue
from fabulous import text

from .pizzazz import fini

import pkg_resources

opj = os.path.join

# the final level gives the user a code based on their username
user = getpass.getuser()
user_code = hashlib.sha1(user.encode()).hexdigest()[:10]

if len(sys.argv) > 1 :
    if sys.argv[1] == 'thosetastycodez' :
        print(user_code)
    elif sys.argv[1] == user_code :
        fini()
    else :
        print(bold("This is not the code you're looking for."))
        print(bold("Try again, or get to the last level first."))
    sys.exit(0)

# clean
try :
  shutil.rmtree('level0')
except Exception as e :
  pass
  #print e
except Error as e :
  pass
  #print e

def copy_md(level,path) :

    level_md = '{}.md'.format(level)

    f = pkg_resources.resource_stream(__name__, opj('mds',level_md))
    desc = f.read()
    size = f.tell()
    open(os.path.join(path,level_md),'w').write(desc.decode('utf-8'))

    return level_md,desc,size

def create_mds(level,path) :
    copy_md(level,path)
    copy_md('.'+level+'_hint',path)

def rndchr(n) :
    if n > len(string.ascii_letters) :
        rnd = [random.sample(string.ascii_letters,1)[0] for _ in range(n)]
    else :
        rnd = random.sample(string.ascii_letters,n)
    return ''.join(rnd)

def main() :

    print()
    print(text.Text('Terminal',skew=5))
    print(text.Text('   Quest',skew=5))
    print()
    print(bold(yellow('Your personal quest is being created right now, please wait.')))
    print()

    ##################################################
    # level 0
    lpath = 'level0'
    os.mkdir(lpath)
    create_mds('level0',lpath)
    ##################################################

    ##################################################
    # level 1
    lpath = opj(lpath,'level1')
    os.mkdir(lpath)
    create_mds('level1',lpath)
    ##################################################

    ##################################################
    # level 2
    lpath = opj(lpath,'.level2')
    os.mkdir(lpath)

    level2_md, level2_desc, level2_size = copy_md('level2',lpath)
    copy_md('.level2_hint',lpath)

    # create 49 directories named as random numbers between 0-300
    paths = random.sample(list(range(0,300)),49)
    while level2_size in paths :
      paths.remove(level2_size)
      paths.append(random.randint(0,300))
    paths = [str(_) for _ in paths]
    for path in paths:
      os.mkdir(os.path.join(lpath,path))
      # put a decoy md file in each path
      open(opj(lpath,path,'level3.md'),'w').write("# this is not the level you're looking for")
      open(opj(lpath,path,'.level3_hint.md'),'w').write("# this is not the level you're looking for")
    ##################################################

    ##################################################
    # level 3
    lpath = opj(lpath,str(level2_size))
    os.mkdir(lpath)
    create_mds('level3',lpath)

    # create a bunch of random dot directories
    for _ in range(100) :
      rnd_dir = '.'+rndchr(6)
      os.mkdir(opj(lpath,rnd_dir))
      open(opj(lpath,rnd_dir,'level4.md'),'w').write(
        "# other directories might have what you seek, but not this one"
      )
      open(opj(lpath,rnd_dir,'.level4_hint.md'),'w').write(
        "# other directories might have what you seek, but not this one"
      )
      open(opj(lpath,rnd_dir,'you-won.md'),'w').write(
        "just kidding, no you didn't, but you did find a SECRET"
      )

    # use the last random directory as the real one
    real_fns = [rndchr(6).upper()+'_{}_SECRET' for _ in range(len(rnd_dir))]
    real_fns.sort()
    real_fns = [_1.format(_2) for _1, _2 in zip(real_fns,rnd_dir)]

    # create a bunch of files with the pattern [A-Z]{6}_[a-z]_[A-Z]{6}
    fake_fns = [rndchr(6).upper()+'_x_'+rndchr(6).upper() for _ in range(1000)]
    for fn in real_fns+fake_fns :
      open(opj(lpath,fn),'w')
    ##################################################

    ##################################################
    # level 4
    lpath = opj(lpath,rnd_dir)
    # this directory was already created in the previous step
    create_mds('level4',lpath)

    level5_dir = '.'+rndchr(6)
    true_file_path = [rndchr(6)+'.txt' for _ in range(5)]

    # create the file chain
    open(opj(lpath,'init.txt'),'w').write(true_file_path[0]+'\n')
    for src,tgt in zip(true_file_path[:-1],true_file_path[1:]) :
        open(opj(lpath,src),'w').write(tgt+'\n')
    open(opj(lpath,true_file_path[-1]),'w').write(level5_dir+'\n')

    # create a bunch of other files that contain random filenames
    # or hidden directory names
    for _ in range(24) :
        fn = rndchr(6)+'.txt'
        if random.random() > 0.5 :
            txt = rndchr(6)+'.txt'
        else :
            txt = '.'+rndchr(6)
        open(opj(lpath,fn),'w').write(txt+'\n')

    # create a bunch of random hidden directories
    for _ in range(999) :
        rnd_dir = '.'+rndchr(6)
        os.mkdir(opj(lpath,rnd_dir))
        open(opj(lpath,rnd_dir,'level5.md'),'w').write(
          "# guessing? I *guess* no one's coming?"
        )
        open(opj(lpath,rnd_dir,'.level5_hint.md'),'w').write(
          "# guessing? I *guess* no one's coming?"
        )
        open(opj(lpath,rnd_dir,'you-won-again.md'),'w').write(
          "nope, just kidding again, but again you did find a SECRET"
        )

    ##################################################

    ##################################################
    # level 5
    lpath = opj(lpath,level5_dir)
    os.mkdir(lpath)
    create_mds('level5',lpath)

    # write out each line to a different file
    level6_dir = '.vrkalp'
    code = [
         r"                     _              _         "
        ,r"                    | |            | |        "
        ,r"     __   __  _ __  | | __   __ _  | |  _ __  "
        ,r"     \ \ / / | '__| | |/ /  / _` | | | | '_ \ "
        ,r"  _   \ V /  | |    |   <  | (_| | | | | |_) |"
        ,r" (_)   \_/   |_|    |_|\_\  \__,_| |_| | .__/ "
        ,r"                                       | |    "
        ,r"                                       |_|    "
    ]
    code = random.sample(code,len(code))
    for fn,line in zip(string.ascii_uppercase,code) :
        open(opj(lpath,fn+'.txt'),'w').write(line+'\n')

    # create a bunch of random hidden directories
    for _ in range(999) :
        rnd_dir = '.'+rndchr(6)
        os.mkdir(opj(lpath,rnd_dir))
        open(opj(lpath,rnd_dir,'level6.md'),'w').write(
          "# Informed decision-making comes from a long tradition of guessing and then blaming others for inadequate results. - Scott Adams"
        )
        open(opj(lpath,rnd_dir,'.level6_hint.md'),'w').write(
          "# Informed decision-making comes from a long tradition of guessing and then blaming others for inadequate results. - Scott Adams"
        )
        open(opj(lpath,rnd_dir,'ding-ding-ding-ding.md'),'w').write(
          "that's the sound of you winning...or just guessing at where the SECRET s are..."
        )

    ##################################################

    ##################################################
    # level 6
    lpath = opj(lpath,level6_dir)
    os.mkdir(lpath)
    create_mds('level6',lpath)

    level7_dir = '.'+rndchr(6)
    quotes = [
        ("I think it's much more interesting to live not knowing than to have answers which might be wrong.","Richard Feynman")
       ,("Look deep into nature, and then you will understand everything better.","Albert Einstein")
       ,("We are drowning in information, while starving for wisdom. The world henceforth will be run by synthesizers, people able to put together the right information at the right time, think critically about it, and make important choices wisely.","E. O. Wilson")
       ,("The world is full of magical things patiently waiting for our wits to grow sharper.","Bertrand Russell")
       ,("For me, it is far better to grasp the Universe as it really is than to persist in delusion, however satisfying and reassuring.","Carl Sagan")
       ,("Science has a simple faith, which transcends utility. It is the faith that it is the privilege of man to learn to understand, and that this is his mission.","Vannevar Bush")
    ]
    
    lines = []
    for quote,author in quotes :
        lines.extend([rndchr(60) for _ in range(random.randint(1000,1500))])
        lines.append('SECRET')
        for tw in textwrap.wrap(quote,40) :
            lines.append('SECRET    '+tw)
        lines.append('SECRET     - '+author)
    lines.extend([rndchr(60) for _ in range(random.randint(1000,1500))])
    lines.append('SECRET    '+level7_dir)
    lines.extend([rndchr(60) for _ in range(random.randint(1000,1500))])
    open(opj(lpath,'pearls.txt'),'w').write(''.join([_+'\n' for _ in lines]))

    # create a bunch of random hidden directories
    for _ in range(999) :
        rnd_dir = '.'+rndchr(6)
        os.mkdir(opj(lpath,rnd_dir))
        open(opj(lpath,rnd_dir,'level6.md'),'w').write(
          "# by now, you should know this strategy doesn't work"
        )
        open(opj(lpath,rnd_dir,'.level6_hint.md'),'w').write(
          "# by now, you should know this strategy doesn't work"
        )
        open(opj(lpath,rnd_dir,'is-this-getting-old-yet.md'),'w').write(
          "there's no SECRET to this, guessing doesn't work"
        )

    ##################################################

    ##################################################
    # level 7
    lpath = opj(lpath,level7_dir)
    os.mkdir(lpath)
    create_mds('level7',lpath)

    snake = r"""
                    /^\/^\
                  _|__| O |
         \/     /~     \_/ \
          \____|__________/  \
                 \_______      \
                         `\     \                 \
                           |     |                  \
                          /      /                    \
                         /     /                       \\
                       /      /                         \ \
                      /     /                            \  \
                    /     /             _----_            \   \
                   /     /           _-~      ~-_         |   |
                  (      (        _-~    _--_    ~-_     _/   |
                   \      ~-____-~    _-~    ~-_    ~-_-~    /
                     ~-_           _-~          ~-_       _-~   - jurcy -
                        ~--______-~                ~-___-~""".split('\n')

    linesperbit = 4
    snakebits = [snake[_:_+linesperbit] for _ in range(0,len(snake),linesperbit)]
    for fn,snakebit in zip(string.ascii_uppercase,snakebits[::-1]) :
        lines = []
        lines.extend([rndchr(60) for _ in range(random.randint(1000,1500))])
        lines.extend(['SECRET'+_ for _ in snakebit])
        lines.extend([rndchr(60) for _ in range(random.randint(300,1000))])
        open(opj(lpath,fn+'.txt'),'w').write(''.join(_+'\n' for _ in lines))

    for _ in range(999) :
        rnd_dir = '.'+rndchr(6)
        os.mkdir(opj(lpath,rnd_dir))
        open(opj(lpath,rnd_dir,'level7.md'),'w').write(
          "# I've got a lovely bunch of coconuts, diddle dee dee"
        )
        open(opj(lpath,rnd_dir,'.level7_hint.md'),'w').write(
          "# I've got a lovely bunch of coconuts, diddle dee dee"
        )
        open(opj(lpath,rnd_dir,'on-a-scale-of-1-to-10.md'),'w').write(
          "YOU are a SECRET 11"
        )

    level8_dir = '.python'
    ##################################################

    ##################################################
    # level 8
    lpath = opj(lpath,level8_dir)
    os.mkdir(lpath)
    create_mds('level8',lpath)

    suess = r"""

        .;''-.
      .' |    `._
     /`  ;       `'.
   .'     \         \
  ,'\|    `|         |
  | -'_     \ `'.__,J
 ;'   `.     `'.__.'
 |      `"-.___ ,'
 '-,           /
 |.-`-.______-|
 }      __.--'L
 ;   _,-  _.-"`\         ___
 `7-;"   '  _,,--._  ,-'`__ `.
  |/      ,'-     .7'.-"--.7 |        _.-'
  ;     ,'      .' .'  .-. \/       .'
   ;   /       / .'.-     ` |__   .'        I like
    \ |      .' /  |    \_)-   `'/   _.-'`` nonsense . It
     _,.--../ .'     \_) '`_      \'`   wakes up the b rain cells.
   '`f-'``'.`\;;'    ''`  '-`      |    Fantasy is a n ecessary ingredient
      \`.__. ;;;,   )              / in living; it's a way of looking
       `-._,|;;;,, /\            ,'  at life through t he wrong end of a
        / /<_;;;;'   `-._    _,-'                    t elescope.
       | '- /;;;;;,      `t'` \.     - Theodor Seuss G eisel
       `'-'`_.|,';;;,      '._/|     
       ,_.-'  \ |;;;;;    `-._/
             / `;\ |;;;,  `"     
           .'     `'`\;;, /
          '           ;;;'|
              .--.    ;.:`\    _.--,
             |    `'./;' _ '_.'     |
              \_     `"7f `)       /
              |`   _.-'`t-'`"-.,__.'
              `'-'`/;;  | |   \ mx
                  ;;;  ,' |    `
                      /   ' """.split('\n')
    top_suess = suess[:old_div(len(suess),2)+3]
    lines = [rndchr(60) for _ in range(random.randint(1000,1500))]
    open(opj(lpath,'fox.txt'),'w').write(''.join(_+'\n' for _ in top_suess+lines))

    tail_suess = suess[len(top_suess):]
    lines = [rndchr(60) for _ in range(random.randint(1000,1500))]
    open(opj(lpath,'sox.txt'),'w').write(''.join(_+'\n' for _ in lines+tail_suess))

    for _ in range(999) :
        rnd_dir = '.'+rndchr(6)
        os.mkdir(opj(lpath,rnd_dir))
        open(opj(lpath,rnd_dir,'level7.md'),'w').write(
          "# I do not like them, Sam I am, I do not like bad guesses and spam"
        )
        open(opj(lpath,rnd_dir,'.level7_hint.md'),'w').write(
          "# I do not like them, Sam I am, I do not like bad guesses and spam"
        )
        open(opj(lpath,rnd_dir,'stars-on-thars.md'),'w').write(
          "but of course all the sneeches have SECRET s in their breeches"
        )

    level9_dir = '.bnattG'
    ##################################################

    ##################################################
    # level 9
    lpath = opj(lpath,level9_dir)
    os.mkdir(lpath)
    create_mds('level9',lpath)

    scroll = """
         __________________
    ()==(                 (@==()
         '_________________'|
           |     your       |
           |    secret      |
           |     code       |
           |      is:       |
           |        {a}       |
           |        {b}       |
           |        {c}       |
           |        {d}       |
           |        {e}       |
           |        {f}       |
           |        {g}       |
           |        {h}       |
           |        {i}       |
           |        {j}       |
           |                |
           |      run       |
           | terminal_quest |
           |   again with   |
           |  this code as  |
           |    its only    |
           |    argument    |
           |   and prosper  |
         __)________________|
    ()==(                 (@==()
         '----------------'
                              PjP
    """.format(**{i:c for i,c in zip('abcdefghij',user_code)}).split('\n')

    # add the line number to the beginning of each line to make it easier
    for i in range(len(scroll)) :
      scroll[i] = '{0:02d}: {1}'.format(i,scroll[i])

    linesperbit = 5
    scrollbits = [scroll[_:_+linesperbit] for _ in range(0,len(scroll),linesperbit)]

    num_secret = int(len(scrollbits)/2)
    secret_ids = random.sample(list(range(len(scrollbits))),num_secret)
    head_tail_ids = set(range(len(scrollbits))).difference(set(secret_ids))

    num_heads = int(num_secret/2)
    head_ids = random.sample(head_tail_ids,num_heads)

    tail_ids = set(head_tail_ids).difference(set(head_ids))

    # do the secret ones
    for cid in secret_ids :
        scrollbit = scrollbits[cid]
        lines = []
        lines.extend([rndchr(60) for _ in range(random.randint(300,1000))])
        lines.extend(['SECRET    '+_ for _ in scrollbit])
        lines.extend([rndchr(60) for _ in range(random.randint(300,1000))])
        fn = rndchr(6)+'.txt'
        open(opj(lpath,fn),'w').write(''.join(_+'\n' for _ in lines))

    # do the heads
    for cid in head_ids :
        scrollbit = scrollbits[cid]
        lines = []
        lines.extend(['          '+_ for _ in scrollbit])
        lines.extend([rndchr(60) for _ in range(random.randint(300,1000))])
        fn = rndchr(6)+'.txt'
        open(opj(lpath,fn),'w').write(''.join(_+'\n' for _ in lines))

    # do the tails
    for cid in tail_ids :
        scrollbit = scrollbits[cid]
        lines = []
        lines.extend([rndchr(60) for _ in range(random.randint(300,1000))])
        lines.extend(['          '+_ for _ in scrollbit])
        fn = rndchr(6)+'.txt'
        open(opj(lpath,fn),'w').write(''.join(_+'\n' for _ in lines))

    # diminish satisfaction for those who think they are clever and use grep -R SECRET
    open(opj(lpath,'.listen.md'),'w').write("ok, so if you figured out how to use grep -R SECRET and skip right to the end, that's great, but do you *really* feel satisfied?")

    ##################################################

    print(bold(yellow('Your quest is ready. It begins in the directory')))
    print()
    print(bold(blue('level0/')))
    print()
    print(bold(yellow('This quest consists of puzzles that you can solve using '
                 'only the following commands:')))
    print(bold('  - cd')+' - change the current directory')
    print(bold('  - cat')+' - print a file or files to the screen')
    print(bold('  - head')+' - print just the first lines of a file or files to the screen')
    print(bold('  - tail')+' - print just the last lines of a file or files to the screen')
    print(bold('  - ls')+' - list the file names or file information')
    print(bold('  - man')+' - when given another command as its argument, display usage information about the command, e.g. man ls')
    print(bold('  - grep')+' - search for the text in the second argument in the filename passed as the third argument')
    print()
    print(bold(yellow('the glob character "*" (e.g. ls *.txt),')))
    print(bold(yellow('and the redirection character ">" (e.g. cat A.txt B.txt > A_and_B.txt)')))
    print()
    print(bold(yellow('There are ten levels in all.')))
    print(bold(yellow('Good luck.')))

if __name__ == '__main__' :

    main()
