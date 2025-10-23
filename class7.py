grocery_list=["milk","bread","eggs"]

def add_item(item):
    grocery_list.append(item)
add_item("butter")
add_item("juice")    

def remove_last_item():
    if grocery_list:
        grocery_list.pop()  
remove_last_item()

display_item=  lambda item: print("Item:",item)

print("\nCurrent Grocery List:")
for item in grocery_list:
    display_item(item)

def count_characters(items):
    if items == []:
        return 0
    else:
       return len(items[0]) + count_characters(items[1:])


total = count_characters(grocery_list)
print("Total characters in all Items:", total)



