class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self._name = name
        self._max_speed = max_speed
        self._mileage = mileage
        
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self._name} is {capacity} passengers"
    
    
class Bus(Vehicle):
    pass

bus1 = Bus("bus", 180, 12)
print(bus1.seating_capacity(50))