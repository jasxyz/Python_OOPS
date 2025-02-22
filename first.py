class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1
    
    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    def gen_desc():
        return "Cars are means of transport !"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


ElectricCar("Tesla", "Model S", "85kWH")

my_car = Car("Jeep", "Compass")

# print(my_car.gen_desc())
print(Car.gen_desc())

# my_car = Car("Jeep", "Compass")
# print(my_car.full_name())