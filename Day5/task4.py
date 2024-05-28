my_tupl=('i','n','d','e','x', " ", 't','u','p','l','e')
elm=input()
if elm in my_tupl:
    print(f'My element ({elm}) in ({my_tupl.index(elm)})  index a tuple')
else:
    print(False)