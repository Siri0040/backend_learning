
'''
def sum_all(*args):
    try:
        return sum(int(i) for i in args)
    except:
        return False
'''
		
def myfunc(*args):
	for num in args:
		if num.isdigit():
				return sum(int(i) for i in args)
		else:
			return False
