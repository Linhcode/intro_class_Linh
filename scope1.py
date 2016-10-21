tip_amount = 0
total_bill = 0
split_amount = 0

def calculate_bill(original_bill_amount, tip_perecntage = 18, split_number = 1):
	global tip_amount
	global total_bill
	global split_amount
	tip_amount = original_bill_amount * tip_perecntage/100
	total_bill = original_bill_amount + tip_amount
	split_amount = total_bill / split_number
	return tip_amount, total_bill, split_amount
	
print calculate_bill(100.0, tip_perecntage = 25, split_number = 3)



