shopping_lists = {"Target" : []}

def menu():
	print "0 - Main Menu" 
	print "1 - Show all lists"
	print "2 - Show a specific list."
	print "3 - Add a new shopping list."
	print "4 - Add an item to a shopping list."
	print "5 - Remove an item from a shopping list."
	print "6 - Remove a list by nickname."
	print "7 - Exit when you are done."
	print "Your current shopping lists:"
	print shopping_lists
#menu1
def show_list():
	print shopping_lists

#menu2
def spec_list(list_you_want):
	if list_you_want in shopping_lists:
		print shopping_lists[list_you_want]
	else:
		print list_you_want + " is not in the shopping lists"

#menu3
def add_list(new_list):
	shopping_lists[new_list] = []
	print shopping_lists

#menu4
def add_item(which_list, item_add):
	#need to global shopping_lists in so that python knows which list
	the_list = shopping_lists[which_list]
	if item_add in the_list:
		print "item has been added"
	else:
		the_list.append(item_add)
		the_list.sort()
		print the_list
		print shopping_lists

#menu5
def remove_item(which_list, item_remove):
	the_list = shopping_lists[which_list]
	if item_remove in the_list:
		the_list.remove(item_remove)
		the_list.sort()
		print the_list
		print shopping_lists
	else:
		print item_remove + " is not in the list"

#menu6
def remove_list(which_list):
	if which_list in shopping_lists:
		del shopping_lists[which_list]
		print shopping_lists
	else:
		print which_list + " is not in the shopping lists"


def main():
	while(True):
		menu()
		choice = int(raw_input("Where would you like to start?"))
		if choice == 0:
			menu()
		elif choice == 1:
			show_list()
		elif choice == 2:
			list_you_want = raw_input("Which list would you like to see?")
			spec_list(list_you_want)
		elif choice == 3:
			new_list = raw_input("Which list would you like to add?")
			add_list(new_list)
		elif choice == 4:
			which_list = raw_input("Which list would you like to modify?")
			item_add = raw_input("Which item would you like to add?")
			add_item(which_list, item_add)
		elif choice == 5:
			which_list = raw_input("Which list would you like to modify?")
			item_remove= raw_input("Which item would you like to remove?")
			remove_item(which_list, item_remove)
		elif choice == 6:
			which_list = raw_input("Which list would you like to remove?")
			remove_list(which_list)
		else:
			break


if __name__ == '__main__':
	main()




















