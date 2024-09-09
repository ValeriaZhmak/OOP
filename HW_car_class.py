
class Car:
    def __init__(self, make: str, model: str, year: int, price: float):
        self.make = make   
        self.model = model 
        self.year = year   
        self.price = price  


    def get_info(self):
        return f"{self.year} {self.make} {self.model} - ${self.price}"

class CarDealership:
    def __init__(self):
        self.cars_for_sale = []  

    
    def add_car(self, car: Car):
        self.cars_for_sale.append(car)
        print(f"{car.get_info()} додано до автосалону.")

    
    def sell_car(self, car: Car):
        if car in self.cars_for_sale:
            self.cars_for_sale.remove(car)
            print(f"Автомобіль {car.get_info()} було продано.")
        else:
            print(f"Автомобіль {car.get_info()} не знайдено в автосалоні.")

    
    def show_inventory(self):
        if self.cars_for_sale:
            print("Автомобілі, доступні для продажу:")
            for car in self.cars_for_sale:
                print(f"- {car.get_info()}")
        else:
            print("Наразі в автосалоні немає автомобілів.")

car1 = Car("Toyota", "Camry", 2020, 24000)
car2 = Car("Honda", "Civic", 2018, 18000)
car3 = Car("Ford", "Mustang", 2021, 36000)
dealership = CarDealership()
dealership.add_car(car1)
dealership.add_car(car2)
dealership.add_car(car3)
dealership.show_inventory()
dealership.sell_car(car2)
dealership.show_inventory()
