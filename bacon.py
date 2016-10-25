def eat():
	print "EAT IT!"

def warrior():
	print "Bacon will turn you into a true warrior!"

def main():
	print "Should you eat that bacon?"
	angels = raw_input("Do you want to feel like angels are frolicking on your taste buds?" "\n" + "1 - Yes" + "\n" + "2 - No" + "\n" + "3 - I'm afraid" + "\n")

	if int(angels) == 1:
		eat()
	elif int(angels) == 2:
		print "You've clearly never tasted bacon"
		eat()
	elif int(angels) == 3:
		choice = raw_input("Are you a coward?").lower()
		if choice == "I am not".lower():
			eat()
		elif choice == "yes":
			warrior()
if __name__ == '__main__':
   	main()

