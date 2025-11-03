import os

count = int(input("Enter the number of students wanted to add: ") )

if os.path.exists("students.txt"): 
    with open("students.txt", "r") as f:
        for x in f:
            print(x.strip())
    mode = "a"
else:
    print("No item in existing file")
    mode = "w"
with open("student.txt", mode) as f:
    for i in range(count):
        student = input("Enter the name of student: ")
        f.write(student + "\n")
print("Updated list:")
with open("student.txt", "r") as f:
    for x in f:
        print(x.strip())
