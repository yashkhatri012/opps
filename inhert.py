class Animal:

    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound." )

animal= Animal("Generic animal")
animal.speak()

class Dog(Animal):

    def speak(self):
        print(f"{self.name} barks.")

dog=Dog("Buddy")
dog.speak()