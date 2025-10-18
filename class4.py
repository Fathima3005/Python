fruits=["apple","banana","orange"]
vegetables=["carrot","beetroot","tomato"]
beverages=["juice","soda","water"]

fruits.append("grapes")

vegetables.insert(1,"cabbage")

del beverages[2]
print(beverages)

inventory=[fruits,vegetables,beverages]

print(fruits[:2])

print(vegetables[:-1])

fruits_lengths=[len(item) for item in fruits]
print(fruits_lengths)

if "water" in beverages:
    print("Yes,'water' is in the beverages ")
else:
    print("No,'water'is not in the beverages")

first_items = (fruits[0], vegetables[0], beverages[0])
print("Tuple of first items", first_items)    


