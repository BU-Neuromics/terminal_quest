#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='terminal-quest'
      ,url='https://bitbucket.org/bubioinformaticshub/terminal_quest/overview'
      ,version=open('VERSION').read().strip()
      ,description='Cute little puzzle for teaching basic command line usage'
      ,author='Adam Labadorf'
      ,author_email='labadorf@bu.edu'
      ,license='MIT'
      ,packages=find_packages()
      ,package_data={'terminal_quest': ['mds/*','mds/.level*']}
      ,python_requires='>=2.6, >=3'
      ,install_requires=[
        'future'
        ,'fabulous'
        ,'pillow'
      ]
      ,entry_points={
        'console_scripts': [
          'terminal_quest=terminal_quest:main'
        ]
      }
      ,classifiers=[
          # How mature is this project? Common values are
          #   3 - Alpha
          #   4 - Beta
          #   5 - Production/Stable
          'Development Status :: 5 - Production/Stable',

          # Indicate who your project is intended for
          'Intended Audience :: Education',
          'Topic :: Education',

          # Pick your license as you wish (should match "license" above)
          'License :: OSI Approved :: MIT License',

          # Specify the Python versions you support here. In particular, ensure
          # that you indicate whether you support Python 2, Python 3 or both.
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
      ]
     )
