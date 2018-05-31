class Details(object);
	name = "John"
	@classmethod
	def print_name(cls, name);
		print name
		
	@classmethod
	def print_even_numbers(cls, new_var, n=5):
		for i in range(n):
			if i%2 == 0:
				print i, "is even"
				
#TODO: Include print_odd_numbers
