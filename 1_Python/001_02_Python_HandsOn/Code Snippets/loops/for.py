lower = 10
upper = 20
print("Prime numbers between",lower,"and",upper,"are:")
for num in range(lower,upper + 1):
	for i in range(2,num):
		if (num % i) == 0:
			break
		else:
			print '%d is a prime number \n' %(num),
			break