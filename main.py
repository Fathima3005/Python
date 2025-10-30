#main file of tracker.py

import json
from datetime import datetime
from tracker import travel_record

records = [
    travel_record("Paris" , "Visited the Eiffel Tower" , "20-05-2021"),
    travel_record("Tokyo" , "Loved the sushi and cherry blossom", "02-04-2022"),
    travel_record("New York", "Times square was amazing!", "05-10-2024")
]

for record in records:

    date_object = datetime.strptime(record["date"],("%d-%m-%Y"))
    record ["date"] = date_object.strftime("%B %d, %Y ")

with open("travel_records.json","w") as file:
    json.dump(records,file, indent=4)

print(" Travel records saved successfully to 'travel_records.json'")

with open("travel_records.json", "r") as file:
    data = json.load(file)

print("Travel Records:\n")
for record in data:
    print(f"City:{record['city']}, Comment: {record['comment']}, Date: {record['date']}")
