#! /usr/bin/env python
import subprocess,glob
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

_rc0 = subprocess.call([Str(Glob("***ABC***"))],shell=True)
_rc0 = subprocess.call([Str(Glob("***ABC***"))],shell=True)
