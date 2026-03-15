class Student:
    def __init__(self,name,age,std):
        self.name=name
        self.age=age
        self.std=std

    def Blue(self):
        print(f"{self.name} belongs to Blue House.")

    def Green(self):
        print(f"{self.name} belongs to Green House.")

    def Red(self):
        print(f"{self.name} belongs to Red House.")

    def Yellow(self):
        print(f"{self.name} belongs to Yellow House.")

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Standard: {self.std}"
    
Student1=Student("Sham", 11, 5)
Student1.Blue()
print(Student1)