#!/usr/bin/env python

from pathlib import Path

from setuptools import setup, find_packages

ROOT = Path(__file__).parent

version = (ROOT / 'VERSION').read_text(encoding='utf-8').strip()
long_description = (ROOT / 'README.md').read_text(encoding='utf-8')

setup(name='terminal-quest'
      ,url='https://github.com/BU-Neuromics/terminal_quest'
      ,version=version
      ,description='Cute little puzzle for teaching basic command line usage'
      ,long_description=long_description
      ,long_description_content_type="text/markdown"
      ,author='Adam Labadorf'
      ,author_email='labadorf@bu.edu'
      ,license='MIT'
      ,packages=find_packages()
      ,package_data={'terminal_quest': ['mds/*','mds/.level*']}
      ,python_requires='>=3.9'
      ,install_requires=[]
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
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'Programming Language :: Python :: 3.12',
          'Programming Language :: Python :: 3.13',
          'Programming Language :: Python :: 3.14',
      ]
     )
