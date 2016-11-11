
#this function will let us write the content that we add into the dictionary to a file
def write_to_file():
	rand_dict ={"stuff":"in there"}
	my_file = open(‘name.txt’,‘w’)
	my_file.write(str(rand_dict))
	my_file.close()

# #this function will read that file
def read_from_file():
	my_file = open(‘name.txt’, ‘r’)
	rand_dict = eval(my_file.read())
	my_file.close()
	return rand_dict

# write_to_file()
# print read_from_file()













