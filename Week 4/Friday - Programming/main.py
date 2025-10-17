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

def main():
    test_tv()
    test_employee()

if __name__ == "__main__":
    main()