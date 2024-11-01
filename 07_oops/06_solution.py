#  6. Class Variables
# Problem: Add a class variable to Car that keeps track of the number of cars created

class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "electric charge"
    
my_tesla = ElectricCar("tesla", "models", "80kWh")
    
# my_car = Car("toyota", "corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())
# print(my_tesla.full_name())
# print(my_tesla.get_brand())
# print(my_tesla.fuel_type())

Car("tata", "safari")
Car("tata","nexon")
# print(safari.fuel_type())
print(Car.total_car)
print(Car.general_description)