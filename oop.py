class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"The {self.name} says woof!")

dog = Dog("Bulldog")
dog.bark()