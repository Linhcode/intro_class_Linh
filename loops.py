def newlist():
	for num in range(10,-1,-1):
		if num == 0:
			print "Blastoff"
		else:
			print num

'''for num in range (1,21):
	if num ==13:
		print "hello"
	else:
		print num

fruits = ["apples", "oranges", "bananas"]
for item in fruits:
	print item
for item in range(len(fruits)):
	print item+1, fruits[item]'''


def sum_num(num):
	total = num  #total included num/ Total not included num: total = 0
	for num in range(num):
		total = total+1
	return total
	

def sum_num2(num):
	total = num
	if num < 0:
		for num in range(num,0):
			total = total + (-1)
	else:
		for num in range(0,num):
			total = total + 1
	return total
print sum_num2(3)



