def main():
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
        def __init__(self, species, color, wing_span, age=0):
            self.species = species
            self.color = color
            self.wing_span = wing_span
            self.age = age
            self.has_nest = False

        def fly(self):
            return f"The {self.color} {self.species} is flying."

        def sing(self):
            return f"The {self.color} {self.species} is singing."

        def build_nest(self):
            self.has_nest = True
            return f"The {self.color} {self.species} is building a nest."

    robin = Bird("robin", "red", "30 cm")
    print(robin.fly())
    print(robin.sing())
    print(robin.build_nest())
    print(f"Species: {robin.species}, Color: {robin.color}, Wing Span: {robin.wing_span}, Has Nest: {robin.has_nest}")

    #==ACTIVITY 3==
    class Car:
        def __init__(self, make, model, year, mileage=0, passengers=0):
            self.make = make
            self.model = model
            self.year = year
            self.mileage = mileage
            self.passengers = passengers

        def drive(self, distance):
            self.mileage += distance
            return f"The {self.year} {self.make} {self.model} drove {distance} km."

        def service(self):
            return f"The {self.year} {self.make} {self.model} is being serviced."

        def display_info(self):
            return f"Car Info: {self.year} {self.make} {self.model}, Mileage: {self.mileage} km."

        def get_passenger_count(self):
            # print(f"The {self.year} {self.make} {self.model} has {self.passengers} passengers.")
            return self.passengers
        
        def get_model(self):
            return self.model

    my_car = Car("Toyota", "Camry", 2020, passengers=4)
    print(f"Passenger Count: {my_car.get_passenger_count()}")
    print(f"Model: {my_car.get_model()}")

    class Parrot(Bird):
        def __init__(self, species, color, wing_span, Name, vocabulary=None):
            super().__init__(species, color, wing_span)
            if vocabulary is None:
                self.vocabulary = []
            else:
                self.vocabulary = vocabulary
            self.name = Name

        def learn_word(self, word):
            self.vocabulary.append(word)
            return f"The {self.color} {self.species} learned the word '{word}'."

        def speak(self):
            if self.vocabulary:
                return f"The {self.color} {self.species} says: " + ", ".join(self.vocabulary)
            return f"The {self.color} {self.species} has nothing to say."
        
        def get_name(self):
            return self.name
        def get_age(self):
            return self.age
        
    polly = Parrot("parrot", "green", "25 cm", "Polly")
    print(polly.get_name())
    print(polly.get_age())



if __name__ == "__main__":
    main()