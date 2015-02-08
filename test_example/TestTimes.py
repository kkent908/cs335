import Times
import unittest

class TestTimes(unittest.TestCase):
  """Test Times.py's addNumbers() method"""
  def testmultiply(self):
    self.assertAlmostEqual(15,Times.multiply(5,3),delta=1e-12)
    self.assertEqual(15,Times.multiply(5,3))
  

# Run the tests:
if (__name__ == '__main__'):
  unittest.main()
