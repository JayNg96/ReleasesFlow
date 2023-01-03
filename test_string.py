import pytest
from helloworld import helloworld


def test_testOne():
  result = helloworld()
  assert result == "Hello Worlda!"


test_testOne()
