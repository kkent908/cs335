import Adder
import unittest

class TestAdder(unittest.TestCase):
  """Test Adder.py's addNumbers() method"""
  def testadd(self):
    self.assertAlmostEqual(8,Adder.addNumbers(5,3),delta=1e-12)
    self.assertEqual(8,Adder.addNumbers(5,3))
  

# Run the tests:
if (__name__ == '__main__'):
  unittest.main()
