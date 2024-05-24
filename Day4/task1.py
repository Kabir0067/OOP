class Vehicle:
    def __init__(self,name,max_spead,mileage):
        self._name=name
        self._max_spead=max_spead
        self._mileage=mileage
    
    def show_info(self):
        return f"Vehicle Name: {self._name}, Spead {self._max_spead}, Mileage {self._mileage}"
        
class Buss(Vehicle):
    pass


buss1=Buss("School Volvo", 180, 12)
print(buss1.show_info())

