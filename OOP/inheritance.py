class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")


# Child class inheriting from Animal
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof Woof!")


# Create object of child class
dog1 = Dog("Tommy")

# Access parent class method
dog1.speak()

# Access child class method
dog1.bark()