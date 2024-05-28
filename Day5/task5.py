tuple1=(1,2,3,4)
tuple2=(3,5,2,1)
tuple3=(2,2,3,1)

sum_of_tuples=[]

for i in zip(tuple1,tuple2,tuple3):
    sum_of_tuples.append(sum(i))
print(tuple(sum_of_tuples))

