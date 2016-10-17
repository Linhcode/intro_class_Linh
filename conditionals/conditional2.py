if (8%2 == 0) and (9%2 == 0):
	print "Both numbers are even"
elif (8%2 == 0) and (9%2 == 1):
	print "8 is even and 9 is odd"
elif (8%2 == 1) and (9%2 == 0):
	print "8 is even and 9 is odd"
else: 
	print "Both numbers are odd"
favorite_color = str.lower(raw_input("What is your favorite color?"))
if favorite_color == "blue" or favorite_color =="yellow" or favorite_color == "red":
	print "My favorite color is primary color"
else:
	print "My favorite color is secondary color!" 
