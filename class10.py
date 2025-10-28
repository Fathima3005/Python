class User:
    def __init__(self,name,joining_year):
        self.name = name
        self.joining_year = joining_year

    def account_age(self):
        current_year = 2025
        return current_year - self.joining_year
    

class Customer(User):
    def get_role(self):
        return "Customer"
    
    def __str__(self):
        return "Name: " + self.name + ", Role: " + self.get_role() + ", Account Age: " + str(self.account_age()) + "years"

class Vendor(User):
    def get_role(self):
        return "Vendor"
    
    def __str__(self):
        return "Name:" + self.name + ", Role: " + self.get_role() + ", Account Age: " + str(self.account_age()) + "years"

customer1 = Customer("Anjana",2025) 
vendor1 = Vendor("Ajeena",2020)


print(customer1)
print(vendor1)