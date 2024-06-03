class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)  
        self.battery_size = battery_size

    def display_info(self):
        print(f"""
        Electro Motor
_____________________________________
Marka --> ({self.make})
Model --> ({self.model})
Year --> ({self.year})
Battery size --> ({self.battery_size} KWH)   
_____________________________________           
""")
        
car1=Car("Merceds Benz","GLE 6.3",2023)
print(f"""
Marka --> ({car1.make})
Model --> ({car1.model})
Year --> ({car1.year})  
    """)  


eltr_car = ElectricCar("Tesla", "Elon Musk", 2024, 10000)
eltr_car.display_info()
