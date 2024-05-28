def chek_whether(tpl,elm):
    if elm in tpl:
        return f"Chek whether a charter {elm} exits whith in tupl"
    return False

my_tupl=("w","3","e","r","s","o","u","r",'c',"e")
elm=input()
print(chek_whether(my_tupl,elm))