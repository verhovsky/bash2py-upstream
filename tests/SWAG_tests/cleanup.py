#! /usr/bin/env python
from __future__ import print_function
import os,subprocess,glob
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

# Cleanup
# Run as root, of course.
os.chdir(Str(Glob("/var/log")))
_rc0 = subprocess.call(Str(Glob("cat")) + " " + Str(Glob("/dev/null")),shell=True,stdout=file(Str(Glob("messages")),'wb'))
> messages
_rc0 = subprocess.call(Str(Glob("cat")) + " " + Str(Glob("/dev/null")),shell=True,stdout=file(Str(Glob("wtmp")),'wb'))
> wtmp
print(Glob("Log files cleaned up."))
