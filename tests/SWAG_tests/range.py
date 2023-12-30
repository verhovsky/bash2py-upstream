#! /usr/bin/env python
from __future__ import print_function
import glob
class Bash2Py(Object):
        #
  __slots__ = ["val"]
        #
  def __init__(self, value=''):
    self.val = value


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

def Glob(value):
  ret = glob.glob(value)
  if len(ret) < 1:
    ret = [ value ]
  return ret

for Make("i").val in [3,4,5,6,7]:
    print(Glob(str(i.val)))
for Make("i").val in [12,14,16,18,20]:
    print(Glob(str(i.val)))
