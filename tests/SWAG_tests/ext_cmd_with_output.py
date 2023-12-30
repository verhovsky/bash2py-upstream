#! /usr/bin/env python
from __future__ import print_function
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

R=Bash2Py(Glob(os.popen("cat /etc/redhat-release").read().rstrip("\n")))
secretNumber=Bash2Py(Glob(str(( ((os.popen("date +%N").read().rstrip("\n") / 1000) % 100) +1 ))))
guess=Bash2Py(-1)
while (Str(Glob(str(guess.val))) != Str(Glob(str(secretNumber.val)))):
    print(Glob("I am thinking of a number between 1 and 100. Enter your guess:"),end="")
    guess = Bash2Py(raw_input())
    if (Str(Glob(str(guess.val))) == Str(Glob()) ):
        print(Glob("Please enter a number."))
    elif (Str(Glob(str(guess.val))) == Str(Glob(str(secretNumber.val))) ):
        print(Glob("\aYes! "+str(guess.val)+" is the correct answer!"))
    elif (int(Glob(str(secretNumber.val))) > int(Glob(str(guess.val))) ):
        print(Glob("The secret number is larger than your guess. Try again."))
    else:
        print(Glob("The secret number is smaller than your guess. Try again."))
