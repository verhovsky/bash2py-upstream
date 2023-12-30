#! /usr/bin/env python
import sys,os,subprocess,glob
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

SUBDIR=Bash2Py(Glob("ijdavis"))
os.environ['SUBDIR'] = SUBDIR
_rc0 = _rcr1, _rcw1 = os.pipe()
if os.fork():
    os.close(_rcw1)
    os.dup2(_rcr1, 0)
    subprocess.call([Str(Glob("grep")),Str(Glob("SUBDIR"))],shell=True)
else:
    os.close(_rcr1)
    os.dup2(_rcw1, 1)
    subprocess.call([Str(Glob(os.path.expanduser("~+"/+"b+"i+"n+"/+"a+"r+"g+"s)))],shell=True)
    sys.exit(0)

