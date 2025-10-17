from typing import Optional, List

class Player:
    def __init__(self, name: str):
        self.name = name
        self.properties: List["Property"] = []

    def add_property(self, prop: "Property"):
        self.properties.append(prop)
        prop.owner = self

    def count_properties_of_type(self, cls):
        return sum(1 for p in self.properties if isinstance(p, cls))

    def __repr__(self):
        return f"Player({self.name})"


class Property:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price
        self.owner: Optional[Player] = None

    def rent(self, **kwargs) -> int:
        """Polymorphic method: subclasses implement their own rent logic."""
        raise NotImplementedError

    def owner_name(self):
        return self.owner.name if self.owner else "Bank"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"


class Street(Property):
    # Street rent depends on how many houses (0..4) or hotel (houses=5).
    HOUSE_MULTIPLIER = {0: 1, 1: 5, 2: 15, 3: 45, 4: 125, 5: 400}

    def __init__(self, name: str, price: int, base_rent: int, houses: int = 0):
        super().__init__(name, price)
        self.base_rent = base_rent
        self.houses = houses  # 0..5 (5 representing a hotel)

    def rent(self, **kwargs) -> int:
        mult = self.HOUSE_MULTIPLIER.get(self.houses, 1)
        return self.base_rent * mult


class Utility(Property):
    # Utility rent: dice_roll * 4 if owner has 1 utility, *10 if owner has both
    def rent(self, **kwargs) -> int:
        dice_roll = kwargs.get("dice_roll", 0)
        if not self.owner:
            return 0
        owned = self.owner.count_properties_of_type(Utility)
        multiplier = 10 if owned >= 2 else 4
        return dice_roll * multiplier


class Railroad(Property):
    # Railroad rents: 25, 50, 100, 200 depending on how many railroads the owner has
    BASE = 25

    def rent(self, **kwargs) -> int:
        if not self.owner:
            return 0
        owned = self.owner.count_properties_of_type(Railroad)
        return self.BASE * (2 ** (owned - 1))


if __name__ == "__main__":
    # Setup players
    alice = Player("Alice")
    bob = Player("Bob")

    # Create properties
    boardwalk = Street("Boardwalk", price=400, base_rent=50, houses=1)
    park_place = Street("Park Place", price=350, base_rent=35, houses=0)
    electric = Utility("Electric Company", price=150)
    water = Utility("Water Works", price=150)
    reading = Railroad("Reading Railroad", price=200)
    penn = Railroad("Pennsylvania Railroad", price=200)

    # Assign ownership
    alice.add_property(boardwalk)
    alice.add_property(electric)
    alice.add_property(reading)

    bob.add_property(park_place)
    bob.add_property(water)
    bob.add_property(penn)
    bob.add_property(Railroad("B. & O. Railroad", price=200))  # bob owns 2 railroads now

    # Polymorphic rent calculation: same method call on different subclasses
    properties = [boardwalk, park_place, electric, water, reading, penn]

    print("Rent values when a player lands on each property (dice roll = 8):\n")
    for p in properties:
        rent_amount = p.rent(dice_roll=8)  # utilities will use dice_roll; streets ignore it
        print(f"{p.name:25} | Owner: {p.owner_name():6} | Rent: ${rent_amount}")