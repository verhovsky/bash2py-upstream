#! /usr/bin/env python
from __future__ import print_function
import sys,os,glob
from stat import *
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

FILE=Bash2Py(Glob(str(sys.argv[1])))
if (os.path.isfile(Str(Glob(str(FILE.val)))) ):
    print(Glob("File "+str(FILE.val)+" exists."))
else:
    print(Glob("File "+str(FILE.val)+" does not exist."))
if ((os.path.exists(Str(Glob(str(FILE.val)))) and S_ISBLK(os.stat(Str(Glob(str(FILE.val)))).st_mode)) ):
    print(Glob("File "+str(FILE.val)+" exists and is a block-special file."))
else:
    print(Glob("Not a block-special file"))
