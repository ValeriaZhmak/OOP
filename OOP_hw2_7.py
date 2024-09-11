# Базовий клас
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self) -> str:
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"

# Автомобіль
class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def __str__(self) -> str:
        return f"{super().__str__()}, Number of doors: {self.num_doors}"

# Велосипед
class Bicycle(Vehicle):
    def __init__(self, brand, model, year, bicycle_type):
        super().__init__(brand, model, year)
        self.bicycle_type = bicycle_type 

    def __str__(self) -> str:
        return f"{super().__str__()}, Type: {self.bicycle_type}"

# Човен
class Boat(Vehicle):
    def __init__(self, brand, model, year, boat_type):
        super().__init__(brand, model, year)
        self.boat_type = boat_type 

    def __str__(self) -> str:
        return f"{super().__str__()}, Boat type: {self.boat_type}"


car = Car("Toyota", "Corolla", 2020, 4)
bicycle = Bicycle("Giant", "Escape 3", 2019, "Road")
boat = Boat("Yamaha", "242X", 2021, "Motor")


print(car)
print(bicycle)
print(boat)
