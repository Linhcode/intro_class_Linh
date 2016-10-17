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
		if int(now.day) - int(bday) >= 0:
			print "Yay, I can vote!"
		else: 
			print "Aww, I can not vote."
	else: 
		print "Aww, I can not vote"
else: 
	print "Aww, I can not vote."