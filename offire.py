import unittest

class TestTest(unittest.TestCase):
  def test_der(self):
    self.assertEqual(23, 2 + 21)

  def test_un(self):
    self.assertEqual(23, 2 + 21)

if __name__ == '__main__':
    unittest.main()
