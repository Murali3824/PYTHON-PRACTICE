#  5. Polymorphism
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors. 

class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"

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
print(my_tesla.fuel_type())

safari = Car("tata", "safari")
print(safari.fuel_type())
