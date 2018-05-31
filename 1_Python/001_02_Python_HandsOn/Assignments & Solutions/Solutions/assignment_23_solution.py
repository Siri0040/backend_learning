def myfunc(string):
	string2=[]
	for i in range(0,len(string)):
		if i%2==0:
			string2.append(string[i].lower())
		elif i%2==1:
			string2.append(string[i].upper())
		else:
			string2.append(string[i])
	return ''.join(string2)
