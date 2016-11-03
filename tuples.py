def check_prime(num):
	if num <= 1:
		print "This is not a prime number"
	else: 
		for i in range(2,num):
			if num%i == 0:
				print "Divisible by", i
				return "This is not a prime number"		
		return "This is a prime number"
#The print command will not end the function.  It will continue evaluating after the print command. 


print check_prime(9)


