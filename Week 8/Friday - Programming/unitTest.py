import unittest
from secondActivity import uppercase_input, add_two_numbers, division, multiplication, lowercase_input

class TestSecondActivity(unittest.TestCase):
    def test_uppercase_input(self):
        self.assertEqual(uppercase_input("hello"), "HELLO")
        self.assertEqual(uppercase_input("World"), "WORLD")
        self.assertEqual(uppercase_input("123abc"), "123ABC")

    def test_add_two_numbers(self):
        self.assertEqual(add_two_numbers(2, 3), 5)
        self.assertEqual(add_two_numbers(-1, 1), 0)
        self.assertEqual(add_two_numbers(0, 0), 0)
        self.assertAlmostEqual(add_two_numbers(2.5, 3.1), 5.6)
    
    def test_division(self):
        self.assertEqual(division(6, 3), 2)
        self.assertEqual(division(-6, 3), -2)
        self.assertAlmostEqual(division(5, 2), 2.5)
        with self.assertRaises(ZeroDivisionError):
            division(5, 0)
    
    def test_multiplication(self):
        self.assertEqual(multiplication(2, 3), 6)
        self.assertEqual(multiplication(-1, 1), -1)
        self.assertEqual(multiplication(0, 100), 0)
        self.assertAlmostEqual(multiplication(2.5, 4), 10.0)
    
    def test_lowercase_input(self):
        self.assertEqual(lowercase_input("HELLO"), "hello")
        self.assertEqual(lowercase_input("World"), "world")
        self.assertEqual(lowercase_input("123ABC"), "123abc")

    def test_equality(self):
        self.assertTrue(5 == 5)
        self.assertFalse(5 == 3)
        self.assertTrue("test" == "test")
        self.assertFalse("Test" == "test")

if __name__ == '__main__':
    unittest.main()