class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_details(self):
         print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self,name,age,employee_id):
      Person.__init__(self,name,age)
      self.employee_id = employee_id

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}")

class PartTime(Person):
    def __init__(self,name,age,working_hours):
       Person.__init__(self,name,age)
       self.working_hours = working_hours

    def show_details(self):
        print(f"Name : {self.name}, Age: {self.age}, Working Hours: {self.working_hours}")
    
class Consultant(Employee,PartTime):
    def __init__(self,name,age,employee_id,working_hours,project_name):
        Employee.__init__(self,name,age,employee_id)
        PartTime.__init__(self,name,age,working_hours)
        self.project_name = project_name

    def show_details(self):
        print(f"Name: {self.name},Age:{self.age},Employee ID:{self.employee_id},Working Hours:{self.working_hours},Project Name:{self.project_name}")

person = Person("Fathima",22)
employee = Employee("Alisha", 22,"E101" )
part_time = PartTime("Gowri",25, 3.5)
consultant = Consultant("Nandana",23,"E202",7.0,"Web Development")

person.show_details()
employee.show_details()
part_time.show_details()
consultant.show_details()