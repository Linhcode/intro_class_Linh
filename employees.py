Employee = {}
Employee["name"] = "Pullo"
Employee["age"] = 30
Employee["height"] = float(raw_input("What is your height?"))
Employee["age"] = 25

print Employee

if "name" in Employee: 
	print "'name': " + Employee["name"] 
else: 
	print "It doesn't exist"


if 26 in Employee: 
	print " 26: " + Employee[26] 
else: 
	print "It doesn't exist"


for key in Employee:
	print key

for key, value in Employee.items():
	print key, value

print Employee.keys()
print Employee.items()