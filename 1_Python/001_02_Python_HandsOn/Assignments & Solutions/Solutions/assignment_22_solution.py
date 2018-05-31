def myfunc(*args):
	list_of_evens=list()
	for num in args:
		if str(num).isdigit():
			if num%2==0:
				list_of_evens.append(num)
		else:
			return False
	return list_of_evens
	
#Note that this program has a limitation of negative digits as the string.isnumeric() attribute is not applicable in python 2.7