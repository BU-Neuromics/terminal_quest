from collections import namedtuple
from glob import glob
import os
import shutil

Level = namedtuple('Level',['name','desc','size'])
level_texts = {}

level_mds = glob('*.md')

for level_md in level_mds :
  f = open(level_md)
  desc = f.read()
  size = f.tell()
  level_texts[level_md] = Level(
    level_md
    ,desc
    ,size
  )

print level_texts

level_dirs = [
  'level0'
  ,'level1'
  ,'.level2'
  ,str(level_texts['level2.md'].size)
]
level_paths = [os.path.join(*level_dirs[:_]) for _ in range(1,len(level_dirs)+1)]

# clean
try :
  shutil.rmtree(level_dirs[0])
except Exception,e :
  print e

if __name__ == '__main__' :

  path_iter = iter(level_paths)
  
  # initial
  p = next(path_iter)
  os.mkdir(p)

  # level 0
  p = next(path_iter)
  os.mkdir(p)

  # level 1
  p = next(path_iter)
  os.mkdir(p)

  # level 2
  p = next(path_iter)
  os.mkdir(p)

  # level 3
  p = next(path_iter)
  os.mkdir(p)
