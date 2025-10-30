#main program of tripdata.py

from tripdata import trip_details
import datetime
import json

trips = [
    trip_details("India", "10-02-2025", "discovering the beauty of India"),
    trip_details("Italy", "15-03-2025", "exploring the historic sites of Italy"),
    trip_details("Japan", "20-04-2025", "experiencing the culture of Japan")
]

for x in trips:
    d = datetime.datetime.strptime(x["date"], "%d-%m-%Y").date()
    x["date"] = d.strftime("%B %d, %Y")

json_trip_details = json.dumps(trips, indent=4)
print(json_trip_details)