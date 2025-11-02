import os

item = input("Enter the name of a new item: ")
if os.path.exists("items.txt"):
    with open("items.txt", "a") as file:
        file.write(item +"\n")

else:
    with open("items.txt","w") as file:
        file.write(item +"\n")

print("\nFull list of items:")
with open("items.txt", "r") as file:
    items = file.readlines()
    
number = 1
for line in items:
    print(str(number) + ". " + line.strip())
    number = number + 1


