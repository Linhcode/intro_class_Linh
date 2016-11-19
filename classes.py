class Contact(object):
	def __init__(self, first_name, last_name, email = "None", mobile_phone = "None"): #always has "self", and required attributes
		#optional attributes can be set equal to "None", if don't put them up here,
		#put : self.email = '' , self.mobile_phone=''

		self.first_name = first_name
		self.last_name = last_name
		self.mobile_phone = mobile_phone  
		self.email = email

	def send_text(self, message):
		if self.mobile_phone == '':
			print "Number does not exist"
		else:
			print "To %s - %s" % (self.mobile_phone, message)

contact_list = []

Kath = Contact("Katherine", "Chandler") #adding info into cLass Contact, must fill the required attributes
Kath.mobile_phone = '87645689' #adding optional attribute
Linh = Contact("Linh", "Erickson", "linherickson@gmail.com")
Linh.mobile_phone = '93468789'
contact_list.append(Linh)
contact_list.append(Kath)

def print_attributes(test_list):
	for contact in test_list:
		print contact.first_name
		print contact.last_name
		print contact.mobile_phone
		print contact.email
 
def main():
	print_attributes(contact_list)
	for contact in contact_list:  
		contact.send_text("Hiiii")  #this is how to call a method in class. Can replace "contact" by anything
		#"name", "item",...

if __name__ == '__main__':
	main()






