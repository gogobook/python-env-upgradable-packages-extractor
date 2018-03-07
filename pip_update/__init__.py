from __future__ import print_function

import argparse
import os
import sys
from .pip_update import extract, CMD
__version__ = '0.4.1'

def main(argv):
  """Main program.
  Arguments:
    argv: command-line arguments, such as sys.argv (including the program name
      in argv[0]).
  Returns:
    0 if there were no changes, non-zero otherwise.
  """
  parser = argparse.ArgumentParser(description='A current and update package list of environment extractor.')
  parser.add_argument(
      '-v',
      '--version',
      action='store_true',
      help='show version number and exit')

  args = parser.parse_args(argv[1:])

  if args.version:
    print('pip-update {}'.format(__version__))
    return 0

  print("Getting upgradable information, it will take few seconds.")
  extract(CMD)
  print('Done!')


def run_main():  # pylint: disable=invalid-name
  try:
    sys.exit(main(sys.argv))
  except:
    pass


if __name__ == '__main__':
  run_main()