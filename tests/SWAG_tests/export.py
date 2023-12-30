#! /usr/bin/env python
import os,glob
def Str(value):
  if isinstance(value, list):
    return " ".join(value)
  if isinstance(value, basestring):
    return value
  return str(value)

def Glob(value):
  ret = glob.glob(value)
  if len(ret) < 1:
    ret = [ value ]
  return ret

os.environ['x'] = Str(Glob("hello"))
os.environ['y'] = Str(Glob("goodbye"))
