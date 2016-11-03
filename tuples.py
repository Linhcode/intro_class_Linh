def check_prime(num):
	if num <= 1:
		print "This is not a prime number"
	else: 
		for i in range(2,num):
			if num%i == 0:
				print "Divisible by", i
				print "This is not a prime number"		
		return "This is a prime number"


def prime(num):
	if num <=1:
		return False
	else: 
		for i in range(2,num):
			if num % i == 0:
				return False
		return True
		print "This is a prime number" 

print check_prime(11)


