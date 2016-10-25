
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

def main():
	add_item()
	add_item()
	add_item()
	add_item()
	remove_item()


if __name__ == '__main__':
    	main()




