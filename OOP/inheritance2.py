# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Child class
class Student(Person):
    def __init__(self, name, age, std):
        super().__init__(name, age)   # Call parent constructor
        self.std = std

    def show_student(self):
        print(f"Class: {self.std}")


# Create object
s1 = Student("Sagar", 15, 10)

# Parent class method
s1.show_details()

# Child class method
s1.show_student()