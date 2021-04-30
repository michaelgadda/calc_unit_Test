from calc import calculator as calc 

class Test_time:	
	
	def test_calc(self): 
		assert calc.addition(3, 5) == 8
		assert calc.subtraction(3, 5 ) == -2 
		assert calc.multiplication(3,5) == 15
		assert calc.divide(3,5) == (3/5)



