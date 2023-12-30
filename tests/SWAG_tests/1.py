#! /usr/bin/env python
from __future__ import print_function
import glob
def Glob(value):
  ret = glob.glob(value)
  if len(ret) < 1:
    ret = [ value ]
  return ret

print(Glob("a"+str((1 + 2))+"b"))
