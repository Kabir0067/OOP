class Dog:
    def __init__(self,name,breed,age):
        self._name=name
        self._breed=breed
        self._age=age
        self._tricks=[]
    
    def bark(self):
        return f"{self._name}  Woof Woof"
    
    def add_tricks(self,trick):
        self._tricks.append(trick)
    
    def dog_information(self):
        print('_'*25)
        print(f"Name --> {self._name}")
        print(f"Breed --> {self._breed}")
        print(f"Age --> {self._age}")
        print(f"Tricks --> {",".join(self._tricks)}")
        print('_'*25)

dog1 = Dog("Rembo", "Petbul", 5)
dog1.add_tricks("Smart")
dog1.add_tricks("Warrior")
dog1.add_tricks("sit")
dog1.dog_information()






