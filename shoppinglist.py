
shoppinglist = []
def updated_list():
	global shoppinglist
	shoppinglist.sort()
	print shoppinglist
	
def add_item():
	global shoppinglist
	item = raw_input("What do you want to add into your list?").lower()
	if item in shoppinglist:
		print "Item has already been added. Please add something else!"
	else:
		shoppinglist.append(item)
		print shoppinglist
		updated_list()

def remove_item(): 
	global shoppinglist
	item = raw_input("Which item would you like to remove?").lower()
	if item in shoppinglist:
		shoppinglist.remove(item)
		print shoppinglist
		updated_list()
	else: 
		print item + " is not in the list"
		updated_list()


def menu():
	print "0 - Main Menu"
	print "1 - Show current list."
	print "2 - Add an item to your shopping list."
	

def main():	
	while(True):
		menu()
		option = int(raw_input("Which option would you like to choose?"))
		if option == 2:
			global shoppinglist
			print "Type exit to exit"
			item = raw_input("What do you want to add into your list?").lower()
			if (item == "exit"):
				break
			elif item in shoppinglist:
				print "Item has already been added. Please add something else!"
			else:
				shoppinglist.append(item)
				print shoppinglist
				updated_list()
			
		elif (option == 1):
			updated_list()
		else:
			print "This is your updated shopping list"
			updated_list()
	print "This is your updated shopping list"
	updated_list()

if __name__ == '__main__':
    	main()






