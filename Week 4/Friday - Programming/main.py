#==ACTIVITY 1==
class TV:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.volume = 0
        self.channel = 1

    @staticmethod
    def turn_on():
        print(f"TV is now ON.")

    @staticmethod
    def turn_off():
        print(f"TV is now OFF.")

    def set_volume(self, volume):
        self.volume = volume
        print(f"Volume set to {self.volume}.")

    def change_channel(self, channel):
        self.channel = channel
        print(f"Channel changed to {self.channel}.")
    
    @staticmethod
    def show_brand(brand):
        print(f"TV Brand: {brand}")

def test_tv():
    my_tv = TV("Samsung", 55)
    TV.turn_on()
    my_tv.set_volume(15)
    my_tv.change_channel(5)
    TV.show_brand(my_tv.brand)
    TV.turn_off()

class Employee:
    salary = 50000
    def __init__(self, name, position, id):
        self.name = name
        self.position = position
        self.id = id

    def display_info(self):
        print(f"Employee Name: {self.name}, Position: {self.position}, ID: {self.id}, Salary: {Employee.salary}")

    def make_password(self):
        password = self.name + str(self.id)
        return password

    @classmethod
    def change_salary(cls, new_salary):
        Employee.salary = float(new_salary)
        print(f"Salary changed to {Employee.salary}")

def test_employee():
    emp = Employee("Alice", "Developer", 101)
    emp.display_info()
    Employee.change_salary(60000)
    emp.display_info()
    print(f"Generated Password: {emp.make_password()}")

#==Activity 2==
class Circle():
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)
    
    def __mul__(self, other):
        return Circle(self.radius * other.radius)
    
    def __gt__(self, other):
        return self.radius > other.radius

def test_circle():
    C1 = Circle(3)
    print(f"C1: {C1.radius}")
    C2 = Circle(4)
    print(f"C2: {C2.radius}")
    C3 = C1 * C2
    print(f"Area of Circle with radius {C3.radius}: {C3.area()}")
    if C1 > C2:
        print("C1 is larger than C2")
    else:
        print("C2 is larger than C1")

#==ACTIVITY 3==
class Bird:
    def __init__(self, species):
        self.species = species

class Pigeon(Bird):
    def fly(self):
        print(f"The {self.species} is flying.")
    
    def eat(self):
        print(f"The {self.species} is eating.")

    def run(self):
        print(f"The {self.species} is running.")

class Sparrow(Bird):
    def fly(self):
        print(f"The {self.species} is flapping its wings.")

    def eat(self):
        print(f"The {self.species} is eating food.")

    def run(self):
        print(f"The {self.species} is running fast.")

def test_bird():
    pigeon = Pigeon("Pigeon")
    sparrow = Sparrow("Sparrow")
    for bird in (pigeon, sparrow):
        bird.fly()
        bird.eat()
        bird.run()

class Plane:
    def __init__(self, model, passengers):
        self.model = model
        self.passengers = passengers

    def take_off(self):
        print(f"The {self.model} is taking off.")
    
    def show_passengers(self):
        print(f"The {self.model} has {self.passengers} passengers.")

    def land(self):
        print(f"The {self.model} is landing.")

class FighterJet(Plane):
    def let_passengers_off(self):
        print(f"The {self.passengers} pilot is getting off.")

class Aeroplane(Plane):
    def let_passengers_off(self):
        print(f"The {self.passengers} passengers are getting off.")

def test_plane():
    jet = FighterJet("F-16", 1)
    aero = Aeroplane("Boeing 747", 300)
    for plane in (jet, aero):
        plane.take_off()
        plane.show_passengers()
        plane.land()
        plane.let_passengers_off()

def main():
    test_tv()
    test_employee()
    test_circle()
    test_bird()
    test_plane()

if __name__ == "__main__":
    main()