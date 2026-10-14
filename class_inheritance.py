class Animal:

    kind = "abstract"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        print("abstract noise")

class Dog(Animal):

    kind = 'canine'

    def sound(self):
         print("bark!")