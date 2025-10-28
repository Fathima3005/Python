class Account:
    def __init__(self,name,balance):
         self._name = name
         self._balance = balance

    def __add__(self,other):
         name = self._name + " & " + other._name
         balance = self._balance + other._balance
         return Account(name,balance)
    
    def show_details(self):
         print(f"Account Holder:", self._name)
         print(f"Balance:", self._balance)


class SavingsAccount(Account):
     def calculate_interest(self):
          return self._balance * 0.05
     
class CurrentAccount(Account):
     def calculate_interest(self):
          return self._balance * 0.02
     
savings_acc = SavingsAccount("Ravi", 10000)
current_acc = CurrentAccount("Anjali", 15000)

print("--- Savings Account ---")
savings_acc.show_details()
print("Interest: ₹", savings_acc.calculate_interest())
print()

print("---- Current Account ----")
current_acc.show_details()
print("Interest: ₹", current_acc.calculate_interest())
print()

total_balance = savings_acc + current_acc

print("---- Total Balance ----")
total_balance.show_details()
