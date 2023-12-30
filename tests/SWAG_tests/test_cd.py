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

os.chdir(Str(Glob("/home")))
os.chdir(os.path.expanduser('~'))
os.chdir(Str(Glob("/home/hello")))
