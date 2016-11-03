

shop_list = {"tshirt" : 30, "jeans": 100, "dress" : 50}
values = shop_list.values()
def itemm():
	global shop_list
	global values
	for item, price in shop_list.items():
		if price == max(values):
			print item


ALPHABET = "abcdefghijklmnopqrstuvwxyz" #or import string
#ALPHABET = string.ascii??
def main():
#Ask User for name
	name = raw_input("What's your name?").lower()
	letters  =count_letters(name)
	print letters 
#create a dictionary
def count_letters(name):
	letter_count = {}
#loop through the characters
	for l in name:
		if l in ALPHABET:
			if l in letter_count:
#store letters as keys
				letter_count[l] +=1
#and counts as values
			else:
				letter_count[l] = 1
 	return letter_count

if __name__ == '__main__':
	main()





























