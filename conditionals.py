from datetime import datetime
now = datetime.now()
today = '%s/%s/%s' %(now.month, now.day, now.year)
bday = raw_input("What is the day of your birthday?")
bmonth = raw_input("What is the month of your birthday?")
byear = raw_input("What is the year of your birthday?")
age = int(now.year) - int(byear)
if int(now.year) - int(byear) >= 0 and int(now.month) - int(bmonth) >=0 and int(now.day) - int(bday) >= 0:
	print age 
if int(now.year) - int(byear) >= 0 and int(now.month) - int(bmonth) >=0 and int(now.day) - int(bday) < 0:
	print  age - 1
if int(now.year) - int(byear) >= 0 and int(now.month) - int(bmonth) < 0:
	print age - 1
if int(now.year) - int(byear) < 0:
	print "Invalid"
# Doesn't work if birthday is 29/2 and current month is Feb of the normal year.
