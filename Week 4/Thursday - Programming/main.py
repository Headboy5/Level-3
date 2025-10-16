# ==ACTIVITY 1==

# Class: Smartphone

# Attributes
# brand
# battery_level
# storage_capacity

# Methods
# take_photo()
# make_call()
# install_app()


# Class: Candle

# Attributes
# color
# scent
# burn_time

# Methods
# light()
# extinguish()
# melt()


# Class: Backpack

# Attributes
# size
# color
# weight_capacity

# Methods
# open()
# close()
# add_item()

#==ACTIVITY 2==
class Human:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        if isinstance(weight, str):
            if "kg" in weight:
                self.weight = float(weight.split()[0])
            elif "lbs" in weight:
                self.weight = float(weight.split()[0]) * 0.453592
            else:
                self.weight = float(weight)
        elif isinstance(weight, (int, float)):
            self.weight = float(weight)
        else:
            self.weight = 0

    def eat(self, food, weightgain=0):
        self.weight += weightgain
        if weightgain > 0:
            return f"{self.name} is eating {food} and gained {weightgain} kgs."
        return f"{self.name} is eating {food}."

    def sleep(self, hours):
        return f"{self.name} is sleeping for {hours} hours."

    def exercise(self, activity, weightloss=0):
        self.weight -= weightloss
        if weightloss > 0:
            return f"{self.name} is exercising by {activity} and lost {weightloss} kgs."
        return f"{self.name} is exercising by {activity}."

person = Human("Alice", 30, "5'6\"", "80.3 kg")
print(person.eat("pasta" , 2))
print(person.sleep(8))
print(person.exercise("running", 1.5))
print(f"Name: {person.name}, Age: {person.age}, Height: {person.height}, Weight: {person.weight} kg")

class Bird:
    def __init__(self, species, color, wing_span):
        self.species = species
        self.color = color
        self.wing_span = wing_span
        self.has_nest = False

    def fly(self):
        return f"The {self.color} {self.species} is flying."

    def sing(self):
        return f"The {self.color} {self.species} is singing."

    def build_nest(self):
        self.has_nest = True
        return f"The {self.color} {self.species} is building a nest."
    
parrot = Bird("parrot", "green", "25 cm")
print(parrot.fly())
print(parrot.sing())
print(parrot.build_nest())
print(f"Species: {parrot.species}, Color: {parrot.color}, Wing Span: {parrot.wing_span}, Has Nest: {parrot.has_nest}")