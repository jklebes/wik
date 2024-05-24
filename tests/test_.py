import unittest
import pytest

class MyTest(unittest.TestCase):
    def test_method1(self):
        assert ('a'=='a')

    def test_method2(self):
        assert (False)  # fail for demo purposes
