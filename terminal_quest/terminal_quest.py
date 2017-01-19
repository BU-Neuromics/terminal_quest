from collections import defaultdict
from glob import glob
import random
import os
import shutil
import string
import textwrap
from fabulous.color import bold, yellow, blue
from fabulous import text

import pkg_resources

opj = os.path.join

# clean
try :
  shutil.rmtree('level0')
except Exception,e :
  pass
  #print e
except Error,e :
  pass
  #print e

def copy_md(level,path) :

    level_md = '{}.md'.format(level)

    f = pkg_resources.resource_stream(__name__, opj('mds',level_md))
    desc = f.read()
    size = f.tell()
    open(os.path.join(path,level_md),'w').write(desc)

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

    print
    print text.Text('Terminal',skew=5)
    print text.Text('   Quest',skew=5)
    print
    print bold(yellow('Your personal quest is being created right now, please wait.'))
    print

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
    paths = random.sample(range(0,300),49)
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
    top_suess = suess[:int(len(suess))/2+3]
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

    level9_dir = '.bnattG'
    ##################################################

    ##################################################
    # level 9
    lpath = opj(lpath,level9_dir)
    os.mkdir(lpath)
    create_mds('level9',lpath)

    calvin = """
                                    oooo   ooo
                                   $   $  $   $
                                   \"o  $ $  o\"\"
                                     o  \"   \"ooooo
                                 oo \"\"           o$
                   o            o            oo  \"
                  $$             $o$\"\"$o  ooo$
                  $\"$          o $    \"$  $
        o$o       $ \"$         $ $     $ $
         $$$o     $$ \"$       o$ $     o $o
         \"$ \"\"o   \"$   \"o     $$ \"o     o\"
     $o   $$   \"o  $     \"oo  $\"  $   o$\"
      \"$   $o    \"o$$       \"o$    $o$\" oo$
        \"o \"$o                     \"$o $\"$$
          \"        oo$$$$$$$oo        $oo$$\"\"      o\" o
 \"\"\"\"\"\"\"\"\"      o$$$$$$$$$$$\"$o             o\"\"\"$o$$  o$
       ooo$$$\"o$$$$$$$$$$$$$$ \"$o    o   o$$$o   $ $ o$
    o$$$$$$$$$$$$$$$$$$$$$$$$    \"oo  o      \"\"o  \"$ $
   $$$$$$$$$$$$$$$$$$$$$$$$$$      \"$o   o$$\"\"\"$     \" oo\"\"o
o\"\"\"\"$$$$$$$$$$$$$$$$$$$$$$\"         \"\"$o\"$o          \"   o$
     \"$$$$$$$$\"\"\"\"$\"\"$$$\"\"              \"$oo$\"\"$o     o$\"\"\"
      $$$$$$$\"                           $\"\"\"\"$\"  o\"\"\"\"
       $\"\"\"\"\"$ooooo        ooooo$$$$$$$     o$\" o\"
        $     \"\"\"\" oooo$$$$$$$$$$$$$$\"     $\"  o\"
      oo$   oooo$$$$$$$$$$$\"\"\"\"\"$$$$\"    o$\" o$\"
    \"$ $o$$$$$$$$$$$$$\"\"$     o$$$\"oooo$\"  o\"
      \"o$ \"$$$$$$$$$$$$         $$o$\"$$$   $\"
        \"$  \"\"$$$$$$$$$        o$\"$$$ \"$$o$$
          \"o   \"\"$$$$$$o     o$$$$ \"\"$o \"\"\"$
            \"$o    \"\"$$$$$$o\"  o$$$$oo o$$$$
               \"\"$oo     $$\" \"$$$\"\" ooooooo$
                    \"\"\"\"$\"  o$\"   oo$$$$$\"\"$$
                       $ oo$\"  o$$$$$\"\"  ooo$
                       $o$\"  o$$$$\"  oo$$$$$$$o
                        $$ o$$$\"  o$$$$$$\"\"\"\"\"$o
                         \"o$$\"  o$$$$\"\"  o$$$$$$$o
                           \"$oo$$$$\"  o$$$$$\"\"\" o$o
                             \"$$$\" oo$$$\"\" oo$$$$$$$
                          ooooo$oo$$$\"\" oo$$$$\"\"\"$$\"\"
                         $\"oooo $$$\" o$$$$\"\"      $
                       o$\"o$   $$\"oo$$\"\"       \" o$
                       $ o$$o  $$o$$\"          oo$$
                       $ $$$$  $$$$$$$$$$$$$$$$$$$$
                       $ $$$$  $$$$$$$$$$$$$$$$$$$$\"
                       $ $$$$  $$$$$$$$$$$$$$$$$$$$
                       $ \"\"    \"\"$$$$$$$$$\"\"\"$\"\"\"\"
                       $o         $\"$\"    \" $\"
                        $o       $$  $o    o$
                         \"$o   o$$    \"\"$$$\"
                           \"\"\"\"\"\" """.split('\n')
    linesperbit = 5
    calvinbits = [calvin[_:_+linesperbit] for _ in range(0,len(calvin),linesperbit)]

    secret_ids = random.sample(range(len(calvinbits)),5)
    head_tail_ids = set(range(len(calvinbits))).difference(set(secret_ids))
    head_ids = random.sample(head_tail_ids,3)
    tail_ids = set(head_tail_ids).difference(set(head_ids))

    # do the secret ones
    for cid in secret_ids :
        calvinbit = calvinbits[cid]
        lines = []
        lines.extend([rndchr(60) for _ in range(random.randint(300,1000))])
        lines.extend(['SECRET    '+_ for _ in calvinbit])
        lines.extend([rndchr(60) for _ in range(random.randint(300,1000))])
        fn = rndchr(6)+'.txt'
        open(opj(lpath,fn),'w').write(''.join(_+'\n' for _ in lines))

    # do the heads
    for cid in head_ids :
        calvinbit = calvinbits[cid]
        lines = []
        lines.extend(['          '+_ for _ in calvinbit])
        lines.extend([rndchr(60) for _ in range(random.randint(300,1000))])
        fn = rndchr(6)+'.txt'
        open(opj(lpath,fn),'w').write(''.join(_+'\n' for _ in lines))

    # do the tails
    for cid in tail_ids :
        calvinbit = calvinbits[cid]
        lines = []
        lines.extend([rndchr(60) for _ in range(random.randint(300,1000))])
        lines.extend(['          '+_ for _ in calvinbit])
        fn = rndchr(6)+'.txt'
        open(opj(lpath,fn),'w').write(''.join(_+'\n' for _ in lines))

    ##################################################

    print bold(yellow('Your quest is ready. It begins in the directory'))
    print
    print bold(blue('level0/'))
    print
    print bold(yellow('This quest consists of puzzles that you can solve using '
                 'only the following commands:'))
    print bold('  - cd')
    print bold('  - cat')
    print bold('  - ls')
    print bold('  - man')
    print bold('  - grep')
    print
    print bold(yellow('and redirection (e.g. cat A.txt B.txt > A_and_B.txt)'))
    print
    print bold(yellow('There are ten levels in all.'))
    print bold(yellow('Good luck.'))

if __name__ == '__main__' :

    main()
