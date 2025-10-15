import random  

price_rice = 45
price_sugar = 40
price_oil = 130

qty_rice = 3
qty_sugar = 2.5
qty_oil = 1.8

total_rice = price_rice * qty_rice
total_sugar = price_sugar * qty_sugar
total_oil = price_oil * qty_oil

print("Rice total (₹):", total_rice)
print("Sugar total (₹):", total_sugar)
print("Oil total (₹):", total_oil)

total_bill = total_rice + total_sugar + total_oil
print("Total bill (₹):", total_bill)

total_int = int(total_bill)   
print("Total bill (integer ₹):", total_int)

total_str = str(total_bill)
print("The total bill amount is ₹" + total_str)

delivery_charge = random.randrange(5, 11) 
final_bill = total_bill + delivery_charge

print("Delivery charge (₹):", delivery_charge)
print("Final bill including delivery charge (₹):", final_bill)
