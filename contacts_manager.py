#import contact
#or
from classes import Contact, print_attributes



def main():
	contact_list = []
	while(True):
		print "Type done to stop"
		add = raw_input("Add more contact?").lower()
		if add == "done":
				print_attributes(contact_list)
				break
		else:
			first_name = raw_input("What is your first name?")
			last_name = raw_input("What is your last name?")
			mobile_number = raw_input("What is your mobile number?")
			email = raw_input("What is your email?")
			new_contact = Contact(first_name, last_name, email,mobile_number)
			
			contact_list.append(new_contact)
			for contact in contact_list:

				print_attributes(contact_list)

if __name__ == '__main__':
	main()


