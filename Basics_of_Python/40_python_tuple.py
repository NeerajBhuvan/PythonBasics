tuple_syntax = ()
# print(tuple_syntax[0])
print(type(tuple_syntax))

tuple1 = (10,11,-43,2,10,22) # allow duplicates
tuple2 = (71,)
print(tuple1)
print((type(tuple2)))

#access tuple values
print(tuple1[1])
print(tuple1[-2])
print(tuple1[1:4]) #slicing is possible
print(tuple1[::3])

# tuples are immutable
# tuple1[2] = 10
# print(tuple1) #TypeError: 'tuple' object does not support item assignment

#length method
print(len(tuple1))

#Nested tuple
tuple3 = (tuple1, tuple2)
print(tuple3)
print(len(tuple3))
print(tuple3[1][0])

#concatenate tuple
tuple4 = tuple1 + tuple2
print(tuple4)

#max and min
print(min(tuple4))
print(max(tuple4))

#count
print(tuple1.count(10))

#fetch index
print(tuple1.index(10)) #search right to left and print first identified value leave a duplicate value

#convert list into tuple
list1 = [15,20,25,30]
print(tuple(list1))

#multiple a tuple
print(tuple2 * 5) #(71, 71, 71, 71, 71)



