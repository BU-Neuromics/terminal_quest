#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='terminal_quest'
      ,version=open('VERSION').read().strip()
      ,description='Cute little puzzle for teaching basic command line usage'
      ,author='Adam Labadorf'
      ,author_email='labadorf@bu.edu'
      ,packages=find_packages()
      ,package_data={'terminal_quest': ['mds/*','mds/.level*']}
      ,install_requires=[
        'future'
        ,'fabulous'
      ]
      ,entry_points={
        'console_scripts': [
          'terminal_quest=terminal_quest:main'
        ]
      }
     )
