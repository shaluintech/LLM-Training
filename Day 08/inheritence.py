class Animal:
    def __init__(self,name):
        self.name = name

    def speak (self):
        return "...."
class Dog(Animal):
    def speak(self):
        return"Woof!"

class cat (Animal):
    def speak(self):
        return "meow"
        

rex = Dog("Rex")
print    