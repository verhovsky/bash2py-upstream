#! /usr/bin/env python
from __future__ import print_function
import subprocess,glob
class Bash2Py(Object):
        #
  __slots__ = ["val"]
        #
  def __init__(self, value=''):
    self.val = value
        #
  def postinc(self, inc=1):
    tmp = self.val
    self.val += inc
    return tmp


def GetVariable(name, local=locals()):
  if name in local:
    return local[name]
  if name in globals():
    return globals()[name]
  return None

def Make(name, local=locals()):
  ret = GetVariable(name, local)
  if ret is None:
    ret = Bash2Py(0)
    globals()[name] = ret
  return ret

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

count=Bash2Py(1)
done=Bash2Py(0)
while (int(Glob(str(count.val))) <= 9):
    subprocess.call([Str(Glob("sleep")),Str(Glob("1"))],shell=True)
    Make("count").postinc()
    if (Str(Glob(str(count.val))) == Str(Glob("5")) ):
        continue
    print(Glob(str(count.val)))
print(Glob("Finished"))
