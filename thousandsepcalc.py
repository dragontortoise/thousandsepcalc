#!/usr/bin/python3

"""
This is the "thousandsepcalc" module and it is the main module which
is called from the command line to start the calculator.

TODO
- Ability to scroll up and down the history of expressions.
- Ability to use Ctrl+a, Ctrl+e, left arrow and right arrow to change
  cursor position within the current expression.
"""

import sys

def remove_comma(s):
  """
  This function removes comma characters from the input string.
  """

  return s.replace(',', '')

import argparse

parser = argparse.ArgumentParser(
  description='thousand separator calculator')
parser.add_argument('--nosep', dest='no_sep', const='y',
  default='n', action='store_const', help='omit thousand separator')
args = parser.parse_args()

for line in sys.stdin:
  try:
    result = eval(remove_comma(line))
    if args.no_sep == 'y':
      print("{:.2f}".format(result))
    else:
      print("{:,.2f}".format(result))
  except:
    print("Warning! You enter an incorrect formula.")
    pass

