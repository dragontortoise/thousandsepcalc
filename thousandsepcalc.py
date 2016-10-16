#!/usr/bin/python3

"""
This is the "thousandsepcalc" module and it is the main module which
is called from the command line to start the calculator.

AUTHOR: @dragontortoise
Version: 1.0
Date: October 16, 2016 at 10:02 PM ICT

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
  print(eval(remove_comma(line)))

