#==ACTIVITY 1==
class Animal:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs
    
    def walk(self):
        print("All animals can walk.")

class Dog(Animal):
    def __init__(self, name, legs, eyes):
        super().__init__(name, legs)
        self.eyes = eyes

def test_dog():
    dog = Dog("Buddy", 4, 2)
    print(f"Dog's Name: {dog.name}")
    print(f"Number of Legs: {dog.legs}")
    print(f"Number of Eyes: {dog.eyes}")
    dog.walk()

def main():
    test_dog()
    
if __name__ == "__main__":
    main()