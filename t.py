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






# class Hero:
#     def __init__(self, name, money, inventory):
#         self.name = name
#         self.money = money
#         self.inventory = inventory

#     def buy(self, item):
#         self.inventory.append(item)
#         print(self.inventory)


# Jerry = Hero("Jerry", 0, ["#BlameJerry"])
# Jerry.buy({"title": "Broom", "atk": -1})
# print(Jerry.__dict__)

    








# class Pet:
#     def __init__(self, name, happiness):
#         self.name = name
#         self.__happiness = happiness  # private attribute

#     def play(self, amount):
#         """Increase happiness by a given amount."""
#         if amount > 0:
#             self.__happiness += amount

#     def show_happiness(self):
#         print(f"{self.name} has a happiness level of {self.__happiness}")

# dog = Pet("Buddy", 50)
# dog.play(20)
# dog.show_happiness()





# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email

#     def display_info(self):
#         return f"User: {self.name}, Email: {self.email}"


class Student(User):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)  # Call the parent class constructor
        self.student_id = student_id
    
    def display_info(self):
        return f"Student: {self.name}, Email: {self.email}, Student ID: {self.student_id}"
    
class Teacher(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject
    
    def display_info(self):
        return f"Teacher: {self.name}, Email: {self.email}, Subject: {self.subject}"

class Administrator(User):
    def __init__(self, name, email, role):
        super().__init__(name, email)
        self.role = role
    
    def display_info(self):
        return f"Administrator: {self.name}, Email: {self.email}, Role: {self.role}"


student = Student("Alice", "alice@example.com", "S12345")
teacher = Teacher("Mr. Smith", "smith@example.com", "Mathematics")
administrator = Administrator("Ms. Johnson", "johnson@example.com", "Principal")

print(student.display_info())  # Output: Student: Alice, Email: alice@example.com, Student ID: S12345
print(teacher.display_info())  # Output: Teacher: Mr. Smith, Email: smith@example.com, Subject: Mathematics
print(administrator.display_info())  # Output: Administrator: Ms. Johnson, Email: johnson@example.com, Role: Principal


class Administrator(User):
    def __init__(self, name, email, role):
        super().__init__(name, email)
        self.role = role
    
    def display_info(self):
        return f"Administrator: {self.name}, Email: {self.email}, Role: {self.role}"
    
    def manage_system(self):
        return f"{self.name} ({self.role}) is managing the system."

admin = Administrator("Ms. Johnson", "johnson@example.com", "Principal")
print(admin.manage_system())  # Output: Ms. Johnson (Principal) is managing the system.


class Teacher(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject
    
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Subject: {self.subject}"

my_teacher = Teacher("Mr. Brown", "brown@example.com", "Science")
print(my_teacher.display_info())  # Output: User: Mr. Brown, Email: brown@example.com, Subject: Science
