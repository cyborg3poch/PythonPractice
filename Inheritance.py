class Animal:

    def __init__(self):
        self.age = 3

    def eat(self):
        print("eat")


class Mammal(Animal):

    def __init__(self):
        # calling the animal class constructor explicitly  so that it have access to age
        super().__init__()
        self.weight = 5

    def move(self):
        print("move")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
print(m.age)
print(m.weight)
print(isinstance(m, Animal))
print(isinstance(m, object))
print(issubclass(Mammal, Animal))
