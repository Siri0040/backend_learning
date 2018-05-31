hours = raw_input("Enter Hours:")
rate = raw_input("Enter Rate:")
try:
    f_hours = float(hours)
    f_rate = float(rate)
except:
    print "Error, please enter numeric input"
    quit()

if f_hours > 40:
    regulr = f_rate*f_hours
    over_time_pay = (f_hours-40.0)*(f_rate*0.5)
    pay = regulr + over_time_pay
else:
    pay = f_hours * f_rate
print "Pay:", pay
