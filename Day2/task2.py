class Name:
    def __init__(self,fname,lname):
        self._fname=fname
        self._lname=lname
        
    def f_name_l_name(self):
        return f'{self._fname[0].upper()}.{self._lname[0].upper()}'
    
    
my_name=Name("Kabir", "Gafurov")
print("_"*18)
print(my_name._fname)
print(my_name._lname)
print(my_name.f_name_l_name())
print("_"*18)
