
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


def convert_score_to_letter(score):
	if score >=90:
		print score "is an A"
	elif score >=80:
		print score "is a B"
	elif score >=70:
		print score "is a C"
	elif score >=60:
		print score "is a D"
	else:
		print "You failed!"
def file_to_list()
	with open("class_grades.txt") as my_file: 
		grade_list = my_file.readlines()
	return grade_list
def main():
	grade_list = file_to_list()
	for grade in grade_list:
		convert_score_to_letter(int(grade.strip()))
if __name__ == '__main__':
	main()













