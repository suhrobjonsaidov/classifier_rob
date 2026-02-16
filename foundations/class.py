# define a class - it's like a cookiecutter - BLUEPRINT
class Dog:

    # __init__ runs automatically when you create an instance - it sets ups the data this object needs
    def __init__(self, name, breed):
        #self = "this specific breed" - when the my_dog.bark() runs self is my_dog
        self.name = name # store name of THIS dog
        self.breed = breed #store breed on THIS dog

    def bark(self):
        print(f"{self.name} says woof")

# creating instances
my_dog = Dog("rex", "german shepherd") # __init__ runs here
other_dog = Dog("Luna", "husky") # __init__ runs here again


my_dog.bark()
other_dog.bark()

