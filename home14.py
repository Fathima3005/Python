import random
import math

name = input("Enter names of customers (comma-separated) who have placed orders today: ")
participant_list = name.split(",")

new_list = list(set(participant_list))
print("Customers name after removing duplication: ", new_list)

random.shuffle(new_list)
print("Shuffled final list of names: ", new_list)

random_customer = random.sample(new_list, 2)
print("Randomly selected 2 customers: ", random_customer)

for x in random_customer:
    print("The reversed string is: ", x[::-1])

count = len(new_list)
print("The total number of unique participants: ", count)
print("The square root of the number of participants and rounded to the nearest whole number", math.ceil(math.sqrt(count)))


