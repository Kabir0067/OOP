def second_smaller(list1):
    my_list=sorted(list1)
    if len (my_list)<2:
        return False
    return my_list[1]

list1=[1,2,-8,-2,0]
print(second_smaller(list1))