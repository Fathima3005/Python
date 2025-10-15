import random

apple= 15.5
orange= 20
grape= 10.25
total_volume= apple+orange+grape
print(total_volume)

total_int=int(total_volume)
print(total_int)

total_str=str(total_volume)
print(total_str)
print(type(total_str))

bonusVolume = random.randrange(5, 10)
total_volume = total_volume + bonusVolume
print("Bonus volume:", bonusVolume)
print("Final total volume after adding bonus:", total_volume)

