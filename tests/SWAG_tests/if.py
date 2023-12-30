#! /usr/bin/env python
from __future__ import print_function
import sys,glob
class Bash2Py(Object):
        #
  __slots__ = ["val"]
        #
  def __init__(self, value=''):
    self.val = value


def Glob(value):
  ret = glob.glob(value)
  if l(ret) < 1:
    ret = [ value ]
  return ret

# This script prints a message about your weight if you give it your
# weight in kilos and height in centimeters.
weight=Bash2Py(Glob(str(sys.argv[1])))
height=Bash2Py(Glob(str(sys.argv[2])))
idealweight=Bash2Py(Glob("$["+str(height.val)+" - 110]"))
if (int(Glob(str(weight.val))) <= int(Glob(str(idealweight.val))) ):
    print(Glob("You should eat a bit more fat."))
else:
    print(Glob("You should eat a bit more fruit."))
