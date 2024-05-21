from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self._name = name
        self._country = country
        self._date_of_birth = datetime.strptime(date_of_birth, "%Y %m %d").date()

    def calculate_age(self):
        today = datetime.today().date()
        age = today.year - self._date_of_birth.year
        return age


my_person = Person("Kabir", "Tojik", "2004 08 16")
print("_"*25)                                         
print(f'Nomash --> {my_person._name}         |')
print(f'Milatsh --> {my_person._country}        |')
print(f"{my_person.calculate_age()} sola meboshad         |")
print("_"*25)