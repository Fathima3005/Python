frontend_students={"Gouri","Alisha","Nandana","Anjana"}
backend_students={"Arun","Alisha","Darshan","Nithin"}

backend_students.add("Fathima")
print(backend_students)

frontend_students.remove("Anjana")
print(frontend_students)

both_courses=frontend_students & backend_students
print("Students in both courses",both_courses)

only_backend= backend_students - frontend_students
print("Students enrolled only in backend",only_backend)

unique_students= frontend_students| backend_students
print("Total number of unique students",len(unique_students))

course={
    "Frontend": len(frontend_students),
    "Backend" : len(backend_students)
}
print(course)

for x,y in course.items():
    print("Print each course name with the number of students:",x,y)

new_dictionary={
    "Fullstack": course["Frontend"] + course["Backend"]
}
print("Updated course dictionary:", new_dictionary)



