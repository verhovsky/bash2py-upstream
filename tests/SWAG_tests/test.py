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

SCORE=Bash2Py(0)
if ((SCORE.val < 1) ):
    print(Glob("true"))
else:
    print(Glob("false"))
