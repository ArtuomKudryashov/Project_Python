from HW.hw_5.bike import Bike
from HW.hw_5.boat import Boat
from HW.hw_5.car import Car
from HW.hw_5.plane import Plane
from HW.hw_5.train import Train

car = Car("Toyota", "Camry", 2022, "Red", "Petrol")
bike = Bike("Trek", "FX", 2021, "Black", "Hardtail")
plane = Plane("Boeing", "747", 2019, "White", 68.4)
boat = Boat("Bayliner", "185", 2020, "Blue", "Fiberglass")
train = Train("Siemens", "Velaro", 2018, "Silver", 10)

car.display_info()
print()
bike.display_info()
print()
plane.display_info()
print()
boat.display_info()
print()
train.display_info()
print()

print("Original")

car1 = Car("Toyota", "Camry", 2022, "Red", "Petrol")
car1.display_info()
print("Change")
car1.set_make("Volkswagen")
car1.set_model("Tiguan")
car1.set_year(2024)
car1.set_color("Grey")
car1.set_engine_type("Petrol")
print()
car1.display_info()
print()
car1.set_year(2000)


car1.display_info()