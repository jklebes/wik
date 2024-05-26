#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from io import StringIO
import pytest
from wik import info

class FetchTest(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_getSummary(self, mock_stdout):
        info.getSummary("Linux")
        result=mock_stdout.getvalue()
        self.assertTrue("Linux" in result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_Lahore(self, mock_stdout):
        info.getSummary("Lahore")
        result=mock_stdout.getvalue()
        self.assertTrue(result is not None)
        self.assertTrue("Lahore" in result)
        self.assertTrue("Pakistan" in result)


