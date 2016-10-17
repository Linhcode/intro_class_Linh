from datetime import datetime
now = datetime.now()
bday = raw_input("What is the day of your birthday?")
bmonth = raw_input("What is the month of your birthday?")
byear = raw_input("Which year were you born in?")

# Doesn't work if birthday is 29/2 and current month is Feb of the normal year.
# Doens't work if raw_input is invalid (if people put in negative number,...)
if int(now.year) - int(byear) > 18:
	print "Yay, I can vote!"
elif int(now.year) - int(byear) == 18:
	if int(now.month) - int(bmonth) >0:
		print "Yay, I can vote!"
	elif int(now.month) - int(bmonth) == 0:
		if int(nw.day) - int(bday) >= 0:
			print "Yay, I can vote!"
		else:
			print "Aww, I can not vote."
	else:
		print "Aww, I can not vote"
else:
	print "Aww, I can not vote."

##########################################################
###  this is the start of how I would solve excercise 5
##########################################################

# honestly, I just let the int function throw an error at the user if the value isn't an integer'
bday = int(bday)
bmonth = int(bmonth)
byear = int(byear)

# convert the individual integers to datetime object, this will handle edge cases (ex 2/29/2015)
bdate = datetime(byear, bmonth, bday)

# use the subtraction operator between the two datetime objects, it returns another object called timedelta
timedelta = now - bdate

# name this number
seconds_in_year = ( 365 * 24 * 60 * 60 )

# the timedelta object has a function called total_seconds which returns the total number of seconds between two dates
age = int(timedelta.total_seconds() / seconds_in_year)

if age > 18:
	print "Yay, I can vote!"
else:
	print "Aww, I can not vote"