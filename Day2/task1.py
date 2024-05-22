import random

class Employee:
    def __init__(self, first_name, last_name):
        self.fullname = first_name + " " + last_name
        self.rand = random.randrange(99)
        self.email = (first_name + last_name + str(self.rand) + "@gmail.com")

emp1 = Employee("Gafurov", "Kabir")

print(emp1.fullname) 
print(emp1.email)