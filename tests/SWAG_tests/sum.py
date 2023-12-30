#! /usr/bin/env python
from __future__ import print_function
import glob
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

SUM=Bash2Py(3)
SUM1=Bash2Py(1)
SUM2=Bash2Py(Glob("$["+str(SUM.val)+"+"+str(SUM1.val)+"]"))
print(Glob(str(SUM2.val)))
