def that_takes (list1,list2):
    my_set=set(list1)
    for i in list2:
        if i in my_set:
            return True
        return False
    
my_list1=input().split()
my_list2=input().split()
print(that_takes(my_list1,my_list2))