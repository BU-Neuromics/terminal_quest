from collections import defaultdict
from glob import glob
import random
import os
import shutil
import string

# clean
try :
  shutil.rmtree('level0')
except Exception,e :
  print e

def copy_md(level,path) :

    level_md = '{}.md'.format(level)

    if not os.path.exists(level_md) :
      open(level_md,'w')

    f = open(level_md)
    desc = f.read()
    size = f.tell()
    open(os.path.join(path,level_md),'w').write(desc)

    return level_md,desc,size

def create_mds(level,path) :
    copy_md(level,path)
    copy_md('.'+level+'_hint',path)

opj = os.path.join

def rndchr(n) :
    return ''.join(random.sample(string.ascii_letters,n))

if __name__ == '__main__' :

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
      rnd_dir = '.'+rndchr(5)
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
    open(opj(lpath,'start.txt'),'w').write(true_file_path[0])
    for src,tgt in zip(true_file_path[:-2],true_file_path[1:-1]) :
        open(opj(lpath,src),'w').write(tgt)
    open(opj(lpath,true_file_path[-1]),'w').write(level5_dir)

    # create a bunch of other files that contain random filenames
    for _ in range(25) :
        fn = rndchr(6)+'.txt'
        open(opj(lpath,fn),'w').write(rndchr(6)+'.txt')

    # create a bunch of random hidden directories
    for _ in range(1000) :
        rnd_dir = '.'+rndchr(6)
        os.mkdir(opj(lpath,rnd_dir))
    ##################################################

