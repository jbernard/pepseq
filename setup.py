#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pepseq
from distutils.core import setup

setup(name='pepseq',
      version=pepseq.__version__,
      description='A peptide sequencing application',
      long_description=open('README.md').read(),
      author='Jon Bernard',
      author_email='jbernard@tuxion.com',
      url='http://github.com/jbernard/pepseq',
      scripts=['bin/pepseq'],
      packages=['pepseq'],
      license='GPL-3')
