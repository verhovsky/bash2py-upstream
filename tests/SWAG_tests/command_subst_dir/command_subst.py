#! /usr/bin/env python
from __future__ import print_function
import os,glob
def Glob(value):
  ret = glob.glob(value)
  if len(ret) < 1:
    ret = [ value ]
  return ret

print(Glob(os.popen("date").read().rstrip("\n")))
print(Glob(os.popen("ls -la").read().rstrip("\n")))
