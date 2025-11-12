# class Calculator():
#     def add(x, y):
#         print(x + y)
#         return x + y

#     def add_many(numbers):
#         print(sum(numbers))
#         return sum(numbers)

#     def subtract(numbers):
#         return numbers

# Calculator.add(5, 6)


# class Hero:
#     def __init__(self, name, money, inventory):
#         self.name = name
#         self.money = money
#         self.inventory = inventory

#     def buy(self, item):
#         self.inventory.append(item)
#         print(self.inventory)


# Jillian = Hero("Jillian", 150, ["Potion"])
# Jillian.buy({"title": "Sword", "atk": 34})
# print(Jillian.__dict__)

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance  # double underscore means "private"

#     def deposit(self, amount):
#         self.__balance += amount

#     def show_balance(self):
#         print(f"{self.owner} has ${self.__balance}")






class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)


Jerry = Hero("Jerry", 0, ["#BlameJerry"])
Jerry.buy({"title": "Broom", "atk": -1})
print(Jerry.__dict__)



class Jerry2:
    def __init__(self, Jerry, idiot):
        self.owner = Jerry
        self.idiotPercent = idiot  # double underscore means "private"

    def idiot(self, amount):
        self.__idiotPercent += amount

    def show_idiot(self):
        print(f"{self.owner} has %{self._idiot}")