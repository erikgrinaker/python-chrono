#!/usr/bin/python

from __future__ import absolute_import

import os.path
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tests


class TestSuite(unittest.TestSuite):

    def __init__(self):
        unittest.TestSuite.__init__(self)

        self.addTests(unittest.defaultTestLoader.loadTestsFromModule(tests))


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(TestSuite())
