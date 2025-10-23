print("=========week 4 =====")
class Bird(object):
    message1 = "Global variable of Bird class"

    def fly(self):
        message ="The Bird is flying" #local variable
        return message

sparrow = Bird()
print(sparrow.message1)
#print(sparrow.message)# failed

class Aircraft(object):

    def __init__(self, name, model, capacity, engine, speed):
        self.name = name
        self.model = model
        self.capacity = capacity
        self.speed  = speed
        self.engine = engine
    
    def fly(self):
        print("The created aircraft can fly")

    def info(self):
        print("========INFO===")
        print("Make {} and the model is {}".format(self.name, self.model))
        print("The created aircraft has {} passengers ".format(self.capacity))
        print("Engine type {} and maximum speed {}".format(self.engine, self.speed))

a = Aircraft("F16", "BCX", 2, "C112", 1000)
print("From the fighter jet class")
a.fly()
a.info()

class CivilianAircraft(Aircraft):

    def fly(self):
        print("This aircraft does not fly in stealth mode")

    def passengers(self):
        print("There are more seats in civillian aircraft")
    
    def runwayLength(self, length):
        print("=======RUNWAY INFO=====")
        print("The runway length for  {}  {}  is {}".format(self.name, self.model, length))
    
b = CivilianAircraft("Boeing", "B334", 800, "Rolls Royce", 656)
b.runwayLength(7250)
b.fly()
b.passengers()
print(b.name, b.model, b.capacity)

class Fighterjet(Aircraft):

    def __init__(self, name, model, capacity, engine, speed, wings):
        super().__init__(name, model, capacity, engine, speed)
        self.wings = wings

    def runwayLength(self, length):
        print("=======RUNWAY INFO=====")
        print("The runway length for  {}  {}  is {}".format(self.name, self.model, length))

print("======F32_INFO========")
F32 = Fighterjet("USD", "F32",2, 350, 5000, 2)
F32.fly()
F32.info()
F32.runwayLength(2250)

class Machine(object):

    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def display(self):
        print("The created machine is ",self.name , "with id",self.id)

class Robot(Machine):

    def __init__(self, name, id, job, location):
        Machine.__init__(self, name, id)
        self.job = job
        self.location = location

    def display(self):
        print("The created machine is ",self.name , "with id",self.id)
        print("The job description is ",self.job, "with location",self.location)

roboCop = Robot("Rcop", 1, "police", "Leeds")
roboCop.display()
#print(help(Aircraft))


class Radio(object):

    def __init__(self, make, model, channel):
        self.make = make 
        self.model =model 
        self.channel = channel

    def tuneChannel(self):
        print("Tuning to BBC")

class Camera(object):

    def __init__(self,name, lens, pixels):
        self.name = name
        self.lens = lens
        self.pixels = pixels
    
    def snap(self):
        print("Snapping method")

class CellPhone(Radio, Camera):

    def __init__(self, make, model, channel,name, lens, pixels, year):
        Radio.__init__(self,make, model, channel)
        Camera.__init__(self,name, lens, pixels)
        self.year = year


phone = CellPhone("Iphone", "S2340", 88, "Canon", "D5000", 4320, 2025)

phone.tuneChannel()
phone.snap()   