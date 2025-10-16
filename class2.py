header= """The Shop,
Bookstore
Customer Receipt."""
print(header)

item1 = "Book Title: {}\t- ₹{}".format("Python Basics", 450)
item2 = "Book Title: {}\t- ₹{}".format("Data Science Intro", 600)

total = 450 + 600
total_line = "Total Amount:\t₹{}".format(total)

thank_you = "\n---------------------------\n\tTHANK YOU FOR SHOPPING WITH US!"

receipt = header + "\n" + item1 + "\n" + item2 + "\n" + total_line + thank_you

print(receipt.upper())
