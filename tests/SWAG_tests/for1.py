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

for Make("var").val in Glob("1")+Glob("2")+Glob("3")+Glob("4")+Glob("5"):
    print(Glob(str(var.val)),Glob("chimpanzee..."))
print(Glob("DONE!"))
