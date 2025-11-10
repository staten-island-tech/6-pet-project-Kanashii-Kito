# Lesson: Using Classes with Inheritance in Python

## Introduction to Inheritance
**Inheritance** is a fundamental concept in object-oriented programming that allows a class (child class) to inherit properties and behaviors from another class (parent class). This promotes code reusability and hierarchical structuring of classes.

### Defining a Parent Class
A **parent class** (also known as a base or super class) provides common attributes and methods that other classes can inherit.

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def display_info(self):
        return f"User: {self.name}, Email: {self.email}"
```

### Creating Child Classes
A **child class** (also known as a derived or subclass) inherits from the parent class. It can also extend or override its behavior.

#### Student Class
```python
class Student(User):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)  # Call the parent class constructor
        self.student_id = student_id
    
    def display_info(self):
        return f"Student: {self.name}, Email: {self.email}, Student ID: {self.student_id}"
```

#### Teacher Class
```python
class Teacher(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject
    
    def display_info(self):
        return f"Teacher: {self.name}, Email: {self.email}, Subject: {self.subject}"
```

#### Administrator Class
```python
class Administrator(User):
    def __init__(self, name, email, role):
        super().__init__(name, email)
        self.role = role
    
    def display_info(self):
        return f"Administrator: {self.name}, Email: {self.email}, Role: {self.role}"
```

### Instantiating and Using the Child Classes
```python
student = Student("Alice", "alice@example.com", "S12345")
teacher = Teacher("Mr. Smith", "smith@example.com", "Mathematics")
administrator = Administrator("Ms. Johnson", "johnson@example.com", "Principal")

print(student.display_info())  # Output: Student: Alice, Email: alice@example.com, Student ID: S12345
print(teacher.display_info())  # Output: Teacher: Mr. Smith, Email: smith@example.com, Subject: Mathematics
print(administrator.display_info())  # Output: Administrator: Ms. Johnson, Email: johnson@example.com, Role: Principal
```

---

## Overriding Parent Class Methods
A child class can **override** methods from the parent class to provide specialized behavior.

For example, let's modify the `Administrator` class to include an additional action:

```python
class Administrator(User):
    def __init__(self, name, email, role):
        super().__init__(name, email)
        self.role = role
    
    def display_info(self):
        return f"Administrator: {self.name}, Email: {self.email}, Role: {self.role}"
    
    def manage_system(self):
        return f"{self.name} ({self.role}) is managing the system."
```

### Using the Overridden Method
```python
admin = Administrator("Ms. Johnson", "johnson@example.com", "Principal")
print(admin.manage_system())  # Output: Ms. Johnson (Principal) is managing the system.
```

---

## Using `super()` to Extend Parent Methods
Instead of completely overriding a method, we can extend its behavior using `super()`.

```python
class Teacher(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject
    
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Subject: {self.subject}"
```

### Using the Extended Method
```python
my_teacher = Teacher("Mr. Brown", "brown@example.com", "Science")
print(my_teacher.display_info())  # Output: User: Mr. Brown, Email: brown@example.com, Subject: Science
```

---

## Key Takeaways
1. **Inheritance** allows a child class to reuse and extend a parent class’s behavior.
2. **`super()`** is used to call methods from the parent class.
3. **Method overriding** enables modifying parent class methods in a child class.
4. **Extending methods** using `super()` allows the original behavior to be retained while adding new functionality.
5. **Hierarchical structuring** using inheritance improves code organization and reduces redundancy.

This lesson provides a foundation for using inheritance in Python to create efficient, modular, and maintainable code.

