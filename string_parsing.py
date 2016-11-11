

my_name = "linh"
list(my_name)
"1,2,3,4,5".split(",")

str = "One fish two fish red fish blue fish"
str.split("fish")


grocery_string = "item:apples,quantity:4,price:1.50\n"

def calculate_bill(grocery_string): 
	list1 = grocery_string.split(",")
	list_q = list1[1].split(":")
	quantity = float(list_q[1])
	list_p = list1[2].split(":")
	price = float(list_p[1])
	return quantity * price

# print calculate_bill(grocery_string) 

items = ["item:apples,quantity:4,price:1.50\n",
        "item:pears,quantity:5,price:2.00\n",
        "item:cereal,quantity:1,price:4.49\n"]
#calculate the bill of each item in the list above
for group in items:
	print calculate_bill(group)


#Below is a list of menu items and prices. 
#Write a function that takes this list and returns a dictionary with t
#he name of the food as the key and the price as the value. 
#Make sure the price is a float, not a string!

menu_list = ["food:hotdog,price:5.50","food:burger,price:9.50",
"food:fries,price:4.00","food:shake,price:5.00"]

food_dict = {}

def make_dict():
	while(True):
		for group in menu_list:
			group1 = group.split(",")
			food = group1[0].split(":")
			food_price = group1[1].split(":")
			name = food[1]
			price = float(food_price[1])
			food_dict[name] = price
		return food_dict
print make_dict()




