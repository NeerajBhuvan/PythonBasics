set1 = {1, 4, "Neeraj", 21.1, 10} #unordered
print(set1)
print(type(set1))

#duplicates are ignored
set2 = {1, 5, 10, 5, True} # last 5 and True will be ignored
print(set2)
print(len(set2)) #3 (because it counts after duplication)

#access item using index and modifying items in sets are not allowed
# set2[1] = 11 #TypeError: 'set' object does not support item assignment
# print(set2[2]) #TypeError: 'set' object is not subscriptable

# create empty set
set3 = {} #it's a syntax to create dictionary
print(type(set3)) #<class 'dict'>
set3 = set()
print(set3)
print(type(set3))

#update
set3 = {1, 10, 22, "Neeraj"} #updation of complete set is possible, we can't modify items in set
# set3[1] = 11 #TypeError: 'set' object does not support item assignment

#add()
set3.add(28)
set3.add((12,44,5)) # allow tuple to update because it is immutable
# set3.add([2,5,6])  # don't allow list to update because it is mutable. TypeError: unhashable type: 'list'
print(set3)

#remove
set3.remove("Neeraj")
# set3.remove(13) #if we try to remove a item, which is not in set (Error: KeyError: 13)
print(set3)

#discard
set3.discard(22)
set3.discard(13) #if we try to discard a item, which is not in set it won't throw any error
set3.discard((12,44,5))
print(set3)

#pop()
set3.pop() #remove any one random element in a list
print(set3)

#clear
set3.clear() #remove all element in a list
print(set3) #set()

#pop-error (if set is empty if we try to pop it will throw error)
# set3.pop() # KeyError: 'pop from an empty set'
# print(set3)











