str1 = "hello World"
str2 = "a1pha num3ric"
str3 = "123456"

print "\n"
print str1.capitalize()
print "str1.count('o', 1, len(str1)):\t", str1.count('o', 1, len(str1)),"\n"
print "isalpha(str1):\t", str1.isalpha()
print "isdigit(str3):\t", str3.isdigit()
print "isalnum(str2):\t", str2.isalnum()
print "split(str2):\t", str2.split()
print "str1.replace('o', str3):\t", str1.replace('o', str3)