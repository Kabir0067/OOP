class FlyingMachine:
    def __init__(self, max_altitude):
        self.max_altitude = max_altitude

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Drone(Vehicle, FlyingMachine):
    def __init__(self, make, model, max_altitude):
        super().__init__(make, model)
        FlyingMachine.__init__(self, max_altitude)

drone = Drone("BMW", "X7", 5000)
print(f"Drone: Make = {drone.make}, Model = {drone.model}, Max Altitude = {drone.max_altitude} feet")