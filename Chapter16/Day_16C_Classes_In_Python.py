# Write your code below this line 👇

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):   # public getter method
        return self.__balance


acc = BankAccount("Alice", 1000)

print(acc.owner)        # ✅ works
# print(acc.__balance)  # ❌ AttributeError

print(acc.get_balance())  # ✅ 1000
acc.deposit(500)
print(acc.get_balance())  # ✅ 1500
