class Vehicle:
    color="Black"
    def __init__(self, name, max_speed, mileage):
        self._name = name
        self._max_speed = max_speed
        self._mileage = mileage
        
class Buss(Vehicle):
    pass

class Car(Vehicle):
    pass

my_buss=Buss("Volvo",180,12)
my_buss.color="Orange_Yelow"
print("-"*65)
print(f"Color: {my_buss.color}, Name: {my_buss._name}, Spead: {my_buss._max_speed}, Mileage: {my_buss._mileage}")

print("-"*65)
my_car=Car("Meacedes-Benz GLE 63", 360,50)
print(f"Color: {my_car.color}, Name: {my_car._name}, Spead: {my_car._max_speed}, Mileage: {my_car._mileage}")
print("-"*65)
