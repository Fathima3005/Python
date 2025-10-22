attendance=[18,20,19,15,21]

for x in attendance:
   if x>= 20:
    print("Full")
   else:
    print("Not Full")

count=0
for x in attendance:
  if x>= 20:
    count=count+1
print("Days the class was full:",count)

total_attendance= sum(attendance)
print("Total attendance over 5 days:",total_attendance)

