web_dev= ["Jeena","Asha","Nivedya"]
data_sci=["Ryan","Anjana","Fathima"]
uiux=["Aromal","Anandu","Abdulla"]

all_participants= [web_dev,data_sci,uiux]

web_dev.append("Adityan")

data_sci.insert(1,"Alisha")

del uiux[2]
print(uiux)

data_sci_copy = data_sci.copy()
data_sci.clear()

print(web_dev[:2])

name_lengths = [len(name) for name in data_sci_copy]

found_asha = ("Asha" in web_dev) or ("Asha" in data_sci_copy) or ("Asha" in uiux)
print("Is Asha in any workshop?", found_asha)

first_participants = (web_dev[0], data_sci_copy[0], uiux[0])
print("First participants from each workshop:", first_participants)
