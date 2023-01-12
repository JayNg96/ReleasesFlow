import pytest
import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from helloworld import helloworld

def test_testOne():
  result = helloworld()
  assert result == "Hello World!"


test_testOne()
