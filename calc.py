class calculator():
	def addition(a, b): 
		try: 
			number_check = float(a)
			number_check_b = float(b)
		except: 
			return "Not a number, please try again!"

		sum = a+b 
		
		return sum 

	def subtraction(a, b):
		try: 
			number_check = float(a)
			number_check_b = float(b)
		except: 
			return "Not a number, please try again!"

		sum = a - b

		return sum

	def multiplication(a, b): 
		try: 
			number_check = float(a)
			number_check_b = float(b)

		except: 
			return "Not a number, please try again!"
		product = a * b 

		return product

	def divide(a, b):
		try: 
			
			number_check = float(a)
			number_check_b = float(b)
		
		except: 
			
			string1 = "Not a number, please try again!"
			return string1
		
		try: 
			
			quotient = a/b 
		
		except ZeroDivisionError: 
			
			string2 = "You can not divide by 0!"
		
			return string2

			
		return quotient




