class Staff:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary
        
    def __str__(self):
        return f"Rolle --> {self.role}, Department --> {self.department}, Salary --> {self.salary}$"

class Techer(Staff):
    pass

teac=Techer("Mualimi zabon","Pedagogiya",5000)
print(teac.__str__())
