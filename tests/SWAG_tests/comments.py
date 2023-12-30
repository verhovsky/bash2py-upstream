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
  if len(ret) < 1:
    ret = [ value ]
  return ret

#A comment
x=Bash2Py(1)
#Another
y=Bash2Py(2)
#Final
print(Glob(str(x.val)+"+"+str(y.val)))
