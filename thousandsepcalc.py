#!/usr/bin/python3

"""
This is the "thousandsepcalc" module and it is the main module which
is called from the command line to start the calculator.

TODO
- Ability to scroll up and down the history of expressions.
- Ability to use Ctrl+a, Ctrl+e, left arrow and right arrow to change
  cursor position within the current expression.
- Print result with thousand separator.
"""

import sys

def remove_comma(s):
  """
  This function removes comma characters from the input string.
  """

  return s.replace(',', '')

for line in sys.stdin:
  print("{:,}".format(eval(remove_comma(line))))

