# Base Class
class Animal:
    def speak(self):
        return "Sound of the animal."
    
# Derived Class
class Dog:
    def speak(Self):
        return "Woof!"
    
# Derived Class
class Cat:
    def speak(Self):
        return "Meow!"
    
# Function that shows polymorphism
def animal_speak(animal):
    print(animal.speak())
    
dog=Dog()
cat=Cat()
print(dog.speak())
print(cat.speak())
animal_speak(dog)