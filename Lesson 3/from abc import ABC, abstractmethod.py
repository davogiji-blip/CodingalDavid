from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def display(self):
        print(f"Name: {self.name}| Habitat: {self.habitat}")

    @abstractmethod
    def speak(self):
        pass

    class Dog(Animal):
        def __init__(self, name, habitat, breed):
            super().__init__(name, habitat)
            self.breed = breed

        def speak(self):
            print(f"{self.name} the {self.breed} says: Woof! Woof!")

    class Parot(Animal):
        def __init__(self, name, habitat, color):
            super().__init__(name, habitat)
            self.phrase = phrase
        def speak(self):
            print(f"{self.name} the {self.phrase} ! {self.phrase}")
    class Lion(Animal):
        def __init__(self, name, habitat, roar):
            super().__init__(name, habitat)
            self.roar = roar

        def speak(self):
            print(f"{self.name} says: {self.roar}")


    dog = Dog("Buddy", "Domestic", "Golden Retriever")        
    parrot = Parot("Polly", "Jungle")
    lion = Lion("Simba", "Savannah", "Pride Rock")
    for animal in (dog, parrot, lion):
        animal.display()
        animal.speak()
        print()