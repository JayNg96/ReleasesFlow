import pytest
from helloworld import helloworld


def test_testOne():
  result = helloworld()
  assert result == "Hello World!"


test_testOne()