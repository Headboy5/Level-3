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
class CircleMaths():
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)
    
    def __mul__(self, other):
        return CircleMaths(self.radius * other.radius)
    
    def __gt__(self, other):
        return self.radius > other.radius

def test_circle():
    C1 = CircleMaths(3)
    print(f"C1: {C1.radius}")
    C2 = CircleMaths(4)
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

#==EXTENSION==
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The engine of the {self.year} {self.make} {self.model} is starting.")

    def stop_engine(self):
        print(f"The engine of the {self.year} {self.make} {self.model} is stopping.")
    
    def display_info(self):
        print(f"Car Info: {self.year} {self.make} {self.model}")

def test_car():
    car = Car("Toyota", "Camry", 2020)
    car.start_engine()
    car.display_info()
    car.stop_engine()

class Greeter:
    @staticmethod
    def greet(name):
        print(f"Hello, {name}!")

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def subtract(a, b):
        return a - b

def test_calculator():
    print(f"Addition: {Calculator.add(5, 3)}")
    print(f"Subtraction: {Calculator.subtract(5, 3)}")

class Animal:
    @staticmethod
    def speak(sound = "I make a sound"):
        print(f"{sound}")

class Dog(Animal):
    @staticmethod
    def speak():
        print("Woof!")

def test_animal():
    Animal.speak()
    Dog.speak()

class SalesEmployee(Employee):
    def __init__(self, name, position, id, sales_made):
        super().__init__(name, position, id)
        self.sales_made = sales_made

    def display_info(self):
        super().display_info()
        print(f"Sales Made: {self.sales_made}")

def test_sales_employee():
    sales_emp = SalesEmployee("Bob", "Salesperson", 102, 150)
    sales_emp.display_info()

class Shape:
    def __init__(self, colour):
        self.colour = colour
        
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

def test_shape():
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    for shape in (circle, rectangle):
        print(f"Area: {shape.area()}")

class BankAccount:
    def __init__(self, account_number, balance=0):
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited {amount}. New balance is {self._balance}.")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance is {self._balance}.")
        else:
            print("Insufficient funds.")
    def get_balance(self):
        return self._balance

def test_bank_account():
    account = BankAccount("123456")
    account.deposit(1000)
    account.withdraw(500)
    print(f"Account Balance: {account.get_balance()}")

class Person:
    def __init__(self, name = "John", age = 30):
        self._name = name
        self._age = age
    def get_name(self):
        return self._name
    def get_age(self):
        return self._age
    def set_name(self, name):
        self._name = name
    def set_age(self, age):
        self._age = age

def test_person():
    person = Person()
    print(f"Name: {person.get_name()}, Age: {person.get_age()}")
    person.set_name("Alice")
    person.set_age(25)
    print(f"Updated Name: {person.get_name()}, Updated Age: {person.get_age()}")

def main():
    test_tv()
    test_employee()
    test_circle()
    test_bird()
    test_plane()
    test_car()
    Greeter.greet("Alice")
    test_calculator()
    test_animal()
    test_sales_employee()
    test_shape()
    test_bank_account()

if __name__ == "__main__":
    main()