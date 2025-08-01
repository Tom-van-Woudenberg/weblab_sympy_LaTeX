import unittest
from solution import *
from weblabTestRunner import TestRunner

class TestSuite(unittest.TestCase):
  
# TESTS START HERE
  def test_one(self):
    assert sym.simplify(V_AC- (C1 - q*x)) == 0, "Equation for V_AC not valid"
  
  def test_two(self):
    assert sym.simplify(M_AC - (C2 + C1 * x + q*x**2/2)) == 0, "Equation for M_AC not valid (or the test is wrong)"
  
# TESTS END HERE

if __name__ == "__main__":
  unittest.main(testRunner=TestRunner)
