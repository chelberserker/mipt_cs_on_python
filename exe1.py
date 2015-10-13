import unittest
import lib
import math

class LibTest(unittest.TestCase):
	def test_even(self):
		self.assertEqual(lib.even(2), True)
		self.assertEqual(lib.even(16), True)
		self.assertEqual(lib.even(32), True)
		self.assertEqual(lib.even(98), True)
		self.assertEqual(lib.even(1), False)
		self.assertEqual(lib.even(15), False)
		self.assertEqual(lib.even(-11), False)
		self.assertEqual(lib.even(0), True)
	def test_even_two(self):
		self.assertEqual(lib.even(-2), True)
	def test_factorial(self):
		self.assertEqual(lib.factorial(0),1)
		self.assertEqual(lib.factorial(1),1)
		self.assertEqual(lib.factorial(5),120)
	def test_factorial_negative(self):
		self.assertEqual(lib.factorial(-5),1)
	def test_palindrome(self):
		self.assertEqual(lib.palindrome('iii'), True)
		self.assertEqual(lib.palindorme('Pop'), False)
		self.assertEqual(lib.palindrome('dmcp'), False)
		self.assertEqual(lib.palindrome('123321'),True)
	def test_palindrome_two(self):
		self.assertEqual(lib.palindrome('ahaha'), True)
	def test_prime(self):
		self.assertEqual(lib.prime(5), True)
		self.assertEqual(lib.prime(11), True)
		self.assertEqual(lib.prime(13), True)
		self.assertEqual(lib.prime(1), True)
		self.assertEqual(lib.prime(4), False)
		self.assertEqual(lib.prime(-11), True)
		self.assertEqual(lib.prime(-12), False)
		self.assertEqual(lib.prime(0), False)
	def test_sin(self):
		self.assertEqual(lib.sin(6), math.sin(6))
		self.assertEqual(lib.sin(-math.pi/2), -1)
		self.assertEqual(lib.sin(0), 0)
		self.assertEqual(lib.sin(math.pi), 0)
		self.assertEqual(lib.sin(-math.pi/4), -1/(2**0.5))
	def test_sqrt(self):
		self.assertEqual(lib.sqrt(9), 3)
		self.assertEqual(lib.sqrt(0), 0)
		self.assertEqual(lib.sqrt(121), 11)
	def test_sqrt_negative(self):
		self.assertEqual(lib.sqrt(-5), 0)
		
		
		

unittest.main(verbosity=2)
