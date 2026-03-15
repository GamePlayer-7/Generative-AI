class Student:
    # constructor
    def __init__(self,name,age,std):
        self.name=name
        self.age=age
        self.std=std

    # __str__() is used to define how an object should look when we print it. 
    # If you want to know memory address then comment this function line.
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Standard: {self.std}"

# create object
Student1=Student("Sham",11,5)
print(Student1)
print(Student1.name)
print(Student1.age)
print(Student1.std)