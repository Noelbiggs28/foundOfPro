import unittest
from multiply import multiply_3_numbers

class TestMultipy(unittest.TestCase):

    def test_01(self):
        result = multiply_3_numbers(2,3,4)
        self.assertEqual(result, 24)

    def test_02(self):
         result = multiply_3_numbers(2,3,4)
         self.assertNotEqual(result, 22)

    def test_03(self):
        result = multiply_3_numbers(0, -1, 1)
        self.assertEqual(result, 0)     

    def test_04(self):
         result = multiply_3_numbers(-9, -1, -2)
         self.assertEqual(result, -18)
    
    def test_05(self):
         result = multiply_3_numbers(1.5, 3.0, 4.0)
         self.assertAlmostEqual(result, 18.0, 4)

if __name__ == '__main__':
        unittest.main()
