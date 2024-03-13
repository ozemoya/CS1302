
import math

class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

class Car:
    def __init__(self, car_name, location, cost_per_mile):
        self.car_name = car_name
        self.location = location
        self.cost_per_mile = cost_per_mile

    def __str__(self):
        return f"[{self.car_name}, {self.location}, {self.cost_per_mile}]"

    def move_to(self, new_x, new_y):
        self.location = Location(new_x, new_y)

class Passenger:
    def __init__(self, passenger_name, location):
        self.passenger_name = passenger_name
        self.location = location

    def __str__(self):
        return f"[{self.passenger_name}, {self.location}]"

    def move_to(self, new_x, new_y):
        self.location = Location(new_x, new_y)

class RideSharingApp:
    def __init__(self):
        self.cars = []
        self.passengers = []

    def add_car(self, car):
        self.cars.append(car)

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def remove_car(self, car):
        self.cars.remove(car)

    def remove_passenger(self, passenger):
        self.passengers.remove(passenger)

    def find_cheapest_car(self):
        if not self.cars:
            return "No cars available"
        cheapest_car = min(self.cars, key=lambda car: car.cost_per_mile)
        return str(cheapest_car)

    def find_nearest_car(self, passenger):
        if not self.cars:
            return "No cars available"
        nearest_car = min(self.cars, key=lambda car: self._calculate_distance(car.location, passenger.location))
        return str(nearest_car)

    def _calculate_distance(self, location1, location2):
        return ((location1.x - location2.x) ** 2 + (location1.y - location2.y) ** 2) ** 0.5

# Test code provided in hw1.py
print('---------------------Object creation------------------')
location1 = Location(2,1)
location2 = Location(-4,1)
car1 = Car('car1', location1, 0.61)
car2 = Car('car2', location2, 0.50)
print('Car object 1 created:',car1)
print('Car object 2 created:', car2)

location3 = Location(-2,3)
location4 = Location(0,0)
passenger1 = Passenger('passenger1', location3)
passenger2 = Passenger('passenger2', location4)
print('Passenger object 1 created:', passenger1)
print('Passenger object 2 created:', passenger2)
