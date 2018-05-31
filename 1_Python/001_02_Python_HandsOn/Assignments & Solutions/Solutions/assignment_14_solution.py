list = []
while True:
    val = raw_input('Enter a number: ')
    if val == 'done':
        break
    try:
        val = int(val)
        list = list + [val]
    except:
        print "Invalid input"
        continue
    
print "Maximum is:",max(list)
print "Minimum is:",min(list)
