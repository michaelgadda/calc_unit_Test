import unittest as ut 
from calc import calculator as calc

class test_calc(ut.TestCase): 

	def test_addition(self): 
		#OK tests
		self.assertEqual(calc.addition(10,5), 15 )
		self.assertEqual(calc.addition("st", 10), "Not a number, please try again!")
		#Not Equal Tests
		self.assertNotEqual(calc.addition(1,1), 3 )
		self.assertNotEqual(calc.addition(500,2), 600000)


	def test_subtraction(self): 
		#OK tests
		self.assertEqual(calc.subtraction(10,5), 5 )
		self.assertEqual(calc.subtraction("st", 10), "Not a number, please try again!")
		#Not Equal Tests 
		self.assertNotEqual(calc.subtraction(10,5), 15)
		self.assertNotEqual(calc.subtraction(10,200000), 41)


	def test_multiplication(self): 
		#OK tests
		self.assertEqual(calc.multiplication(10,5), 50 )
		self.assertEqual(calc.multiplication("st", 10), "Not a number, please try again!")
		#Not Equal Tests
		self.assertNotEqual(calc.multiplication(10,5), 500)
		self.assertNotEqual(calc.multiplication(1,1), 2)
		#A failed Test
		self.assertEqual(calc.multiplication(10,5), 16 )

	def test_division(self): 
		#OK tests
		self.assertEqual(calc.divide(10,5), 2 )
		self.assertEqual(calc.divide("st", 10), "Not a number, please try again!")
		self.assertEqual(calc.divide(10, 0), "You can not divide by 0!")
		#Not Equal Tests
		self.assertNotEqual(calc.divide(10,-5), 2 )
		self.assertNotEqual(calc.divide(-5,-5), -1 )


if __name__ == '__main__': 
	ut.main()


#In order to run use python -m unittest -v calc_unit_test.py