def cal_tip(bill_amount, tip_p):
	return bill_amount * tip_p

def Total_Bill(bill_amount, tip_p):
	tip = cal_tip(bill_amount, tip_p)
	return tip + bill_amount

def Split(bill_amount, tip_p, people):
	Total_amount = Total_Bill(bill_amount, tip_p)
	return Total_amount/ people



def main():
	print "1 - calculate tip"
	print "2 - split the bill"
	clients_choice = raw_input("What would you like?")
	if clients_choice == "1":
		bill_amount = float(raw_input("What is the original bill amount?"))
		tip_p = float(raw_input("What is the tip percentage?"))
		print cal_tip(bill_amount, tip_p)
		print Total_Bill(bill_amount, tip_p)
		split = str.lower(raw_input("Would you like to split the bill?"))
		if split == "yes":
			people = int(raw_input("How many poeple are there?"))
			print "The split for each is " + str(Split(bill_amount, tip_p, people))
	else: 
		bill_amount = float(raw_input("What is the original bill amount?"))
		people = int(raw_input("How many poeple are there?"))
		tip_p = float(raw_input("What is the tip percentage?"))
		print "The split for each is " + str(Split(bill_amount, tip_p, people))

if __name__ == '__main__':
    	main()



