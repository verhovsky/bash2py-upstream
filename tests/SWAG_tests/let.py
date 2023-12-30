#! /usr/bin/env python
from __future__ import print_function
import glob
class Bash2Py(Object):
        #
  __slots__ = ["val"]
        #
  def __init__(self, value=''):
    self.val = value
        #
  def plus(self, value):
    self.val += value
    return self.val
        #
  def idivide(self, value):
    self.val //= value
    return self.val


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

# int-or-string.sh
a=Bash2Py(2334)
# Integer.
_rc0= not Make("a").plus(1)
_rc0 = Bash2Py(_rc0)
print(Glob("a = "+str(a.val)+" "))
# a = 2335
print()
# Integer, still.
b=Bash2Py(Glob(str(a.val/23/BB)))
# Substitute "BB" for "23".
# This transforms $b into a string.
print(Glob("b = "+str(b.val)))
# b = BB35
b=0

# Declaring it an integer doesn't help.
print(Glob("b = "+str(b.val)))
# b = BB35
_rc0= not Make("b").plus(1)
_rc0 = Bash2Py(_rc0)
# BB35 + 1
print(Glob("b = "+str(b.val)))
# b = 1
print()
# Bash sets the "integer value" of a string to 0.
c=Bash2Py(Glob("BB34"))
print(Glob("c = "+str(c.val)))
# c = BB34
d=Bash2Py(Glob(str(c.val/BB/23)))
# Substitute "23" for "BB".
# This makes $d an integer.
print(Glob("d = "+str(d.val)))
# d = 2334
_rc0= not Make("d").plus(1)
_rc0 = Bash2Py(_rc0)
# 2334 + 1
print(Glob("d = "+str(d.val)))
# d = 2335
print()
# What about null variables?
e=Bash2Py(Glob())
# ... Or e="" ... Or e=
print(Glob("e = "+str(e.val)))
# e =
_rc0= not Make("e").plus(1)
_rc0 = Bash2Py(_rc0)
# Arithmetic operations allowed on a null variable?
print(Glob("e = "+str(e.val)))
# e = 1
print()
# Null variable transformed into an integer.
# What about undeclared variables?
print(Glob("f = "+str(f.val)))
# f =
_rc0= not Make("f").plus(1)
_rc0 = Bash2Py(_rc0)
# Arithmetic operations allowed?
print(Glob("f = "+str(f.val)))
# f = 1
print()
# Undeclared variable transformed into an integer.
#
# However ...
_rc0= not Make("f").idivide(undecl_var.val)
_rc0 = Bash2Py(_rc0)
# Divide by zero?
#   let: f /= : syntax error: operand expected (error token is " ")
# Syntax error! Variable $undecl_var is not set to zero here!
#
# But still ...
_rc0= not Make("f").idivide(0)
_rc0 = Bash2Py(_rc0)
#   let: f /= 0: division by 0 (error token is "0")
# Expected behavior.
#  Bash (usually) sets the "integer value" of null to zero
#+ when performing an arithmetic operation.
#  But, don't try this at home, folks!
#  It's undocumented and probably non-portable behavior.
# Conclusion: Variables in Bash are untyped,
#+ with all attendant consequences.
exit(int(Glob(str(_rc0))))
