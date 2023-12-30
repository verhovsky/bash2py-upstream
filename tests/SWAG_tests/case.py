#! /usr/bin/env python
from __future__ import print_function
import glob
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

print(Glob("Which fruit do you like most?"))
fruit = Bash2Py(raw_input())

if ( Str(Glob(str(fruit.val))) == 'apple'):
    print(Glob("Mmmmh... I like those!"))
elif ( Str(Glob(str(fruit.val))) == 'banana'):
    print(Glob("Hm, a bit awry, no?"))
elif ( Str(Glob(str(fruit.val))) == 'orange' or Str(Glob(str(fruit.val))) == 'tangerine'):
    print(Glob("Eeeks! I dont like those! Go away!"))
    exit(1)
else:
    print(Glob("Unknown fruit - sure it isn't toxic?"))
