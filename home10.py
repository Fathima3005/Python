from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self,name,account_year):
        self.name = name
        self.account_year = account_year

    @abstractmethod
    def get_role(self):
        pass

    def account_age(self):
        current_year = 2025
        return current_year - self.account_year
    
class Admin(User):
    def get_role(self):
        return "Admin"
    
    def __str__(self):
        return "Admin User: " + self.name +", Account created in " + str(self.account_year)
        

class Guest(User):
    def get_role(self):
        return "Guest"
    
    def __str__(self):
         return "Guest User: " + self.name +", Account created in " + str(self.account_year)
    
admin1 = Admin("Fathima",2021)
guest1 = Guest("Gowri", 2023)

print("Role:", admin1.get_role())
print("Account Age:", admin1.account_age(),"years")
print(admin1)

print("\n")

print("Role:" , guest1.get_role())
print("Account Age:", guest1.account_age(), "years")
print(guest1)