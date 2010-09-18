#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
from pepseq.core import __version__

setup(name='pepseq',
      version=__version__,
      description='A peptide sequencing application',
      long_description=open('README.md').read(),
      author='Jon Bernard',
      author_email='jbernard@tuxion.com',
      url='http://github.com/jbernard/pepseq',
      scripts=['bin/pepseq'],
      packages=['pepseq'],
      license='GPL-3')
