#!/usr/bin/env python
# Copyright 2018 gogobook. All Rights Reserved.
#
# Licensed under the MIT License (the "License");


import codecs
import sys
import unittest

from setuptools import setup, Command
import pip_update

class RunTests(Command):
  user_options = []

  def initialize_options(self):
    pass

  def finalize_options(self):
    pass

  def run(self):
    loader = unittest.TestLoader()
    tests = loader.discover('.',pattern='*_test.py', top_level_dir='.')
    runner = unittest.TextTestRunner()
    results = runner.run(tests)
    sys.exit(0 if results.wasSuccessful() else 1)


with codecs.open('README.md', 'r', 'utf-8') as fd:
  setup(
      name='pip-update',
      version=pip_update.__version__,
      description='A current and update package list of environment extractor.',
      long_description=fd.read(),
      url='https://github.com/gogobook/python-env-upgradable-packages-extractor',
      license='MIT License',
      author='gogobook',
      maintainer='gogobook',
      maintainer_email='o968041428@google.com',
      packages=['pip_update', ],
      classifiers=[
          'Development Status :: 1 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
      ],
      keywords='upgradable packages extractor',
      entry_points={
          'console_scripts': ['pip-update = pip_update:run_main'],
      },
      cmdclass={
          'test': RunTests,
      },
)