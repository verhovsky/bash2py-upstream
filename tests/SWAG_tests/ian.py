#! /usr/bin/env python
import os,glob
class Bash2Py(Object):
        #
  __slots__ = ["val"]
        #
  def __init__(self, value=''):
    self.val = value


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

x=Bash2Py(Glob(os.popen("ls -la").read().rstrip("\n")))
eval(Str(Glob("ls -la")))
eval(Str(Glob(os.popen("prowler a.xml 1 2").read().rstrip("\n"))))
