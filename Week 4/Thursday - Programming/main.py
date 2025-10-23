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

#==ACTIVITY 2==
class Screensize:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def showScreensize(self):
        print(f"Width: {self.width}, Height: {self.height}")

class Display:
    def __init__(self, pixel_density, colour):
        self.pixel_density = pixel_density
        self.colour = colour
    
    def showDisplay(self):
        print(f"Pixel Density: {self.pixel_density}, Colour: {self.colour}")

class TV(Screensize, Display):
    def __init__(self, width, height, pixel_density, colour):
        Screensize.__init__(self, width, height)
        Display.__init__(self, pixel_density, colour)
    
    def displayInfo(self):
        print("This is a child class of screensize and display.")

def test_tv():
    tv = TV(1920, 1080, 300, "Black")
    tv.showScreensize()
    tv.showDisplay()
    tv.displayInfo()

def main():
    test_dog()
    test_tv()

if __name__ == "__main__":
    main()