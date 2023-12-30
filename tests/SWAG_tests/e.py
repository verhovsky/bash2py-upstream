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

a=Bash2Py(1)
b=Bash2Py(2)
c=Bash2Py(3)
d=Bash2Py(4)
e=Bash2Py(5)
print(Glob(str(a.val)),Glob(str(b.val)),Glob(str(c.val)),Glob(str(d.val)),Glob(str(e.val)))
