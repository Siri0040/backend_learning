score = raw_input("Enter Score: ")
score = float(score)
if score >= 0.0 and score <= 1.0:
    if score >= 0.9:
        print "A"
        quit()
    elif score >= 0.8:
        print "B"
        quit()
    elif score >= 0.7:
        print "C"
        quit()
    elif score >= 0.6:
        print "D"
        quit()
    else:
        print "F"
        quit()
else:
    print "Please enter proper score"
