# 1) Adding multiple sets at same time
# method 1(names) - supports multiple sets at same time other than Symmetric Difference
# method 2(operator) - all four supports multiple sets at same time

# 2) Adding different datatypes
# method 1(names) - all four supports different datatypes
# method 2(operator) - all four does not supports different datatypes

unionSet1 = {'Neeraj', 'Anu', 'Varsha'}
unionSet2 = {'Meera', 'Dhanum', 'Anu'}
unionSet3 = {'Neeraj', 'Atsara'}

# union
print("union Operation...")
# method1
print(unionSet1.union(unionSet2))
print(unionSet1.union(unionSet2, unionSet3))  # can add multiple sets at a same time
print(unionSet1.union(('Neeraj',
                       'Murali')))  # tuple - can add different datatype operands to this set method by first converting into set and do union operation

# method2
print("union Operation using operator(|) ...")
print(unionSet1 | unionSet2)
print(unionSet1 | unionSet2 | unionSet3)  # can add multiple sets at a same time
# print(unionSet1 | ('Neeraj', 'Murali')) #tuple - cannot add different datatype operands to this set method
# #TypeError: unsupported operand type(s) for |: 'set' and 'tuple'

# union_update
print("union Operation updation ...")
unionSet3.update(unionSet2, unionSet1)
print(unionSet3)  # it will remove duplicate elements comparing both sets and merge it
unionSet2.update(['Anu', 'Lakshmi'])  # different datatype operands also possible
print(unionSet2)
unionSet1 |= unionSet2
print(unionSet1)

# intersection
print("\nintersection Operation...")
interSet1 = {'Neeraj', 'Anu', 'Varsha'}
interSet2 = {'Meera', 'Dhanum', 'Anu'}
interSet3 = {'Neeraj', 'Atsara'}

# method1
print(interSet1.intersection(interSet2))
print(interSet1.intersection(interSet2, interSet3))  # can add multiple sets at a same time
print(interSet1.intersection(('Neeraj',
                              'Murali')))  # tuple - can add different datatype operands to this set method by first converting into set and do intersection operation

# method2
print("intersection Operation using operator(&) ...")
print(interSet1 & interSet2)
print(interSet1 & interSet2 & interSet3)  # can add multiple sets at a same time
# print(unionSet1 & ('Neeraj', 'Murali')) #tuple - cannot add different datatype operands to this set method
# #TypeError: unsupported operand type(s) for &: 'set' and 'tuple'

# intersection_update
print("intersection Operation updation ...")
interSet3.intersection_update(interSet2)
print(interSet3)  # it will print duplicate elements comparing both sets
interSet2.intersection_update(['Anu', 'Lakshmi'])  # different datatype operands also possible
print(interSet2)
interSet1 &= interSet2
print(interSet1)

# difference
print("\nDifference Operation...")
differSet1 = {'Neeraj', 'Anu', 'Varsha'}
differSet2 = {'Meera', 'Dhanum', 'Anu'}
differSet3 = {'Neeraj', 'Atsara'}

# method1
print(differSet1.difference(differSet2))
print(differSet1.difference(differSet2, differSet3))  # can add multiple sets at a same time
print(differSet1.difference(('Neeraj',
                             'Murali')))  # tuple - can add different datatype operands to this set method by first converting into set and do difference operation

# method2
print("difference Operation using operator(-) ...")
print(differSet1 - differSet2)
print(differSet1 - differSet2 - differSet3)  # can add multiple sets at a same time
# print(differSet1 - ('Neeraj', 'Murali')) #tuple - cannot add different datatype operands to this set method
# #TypeError: unsupported operand type(s) for -: 'set' and 'tuple'

# difference_update
print("difference Operation updation ...")
differSet1.difference_update(differSet2)
print(differSet1)  # it will compare both sets and print non-difference items from set1
differSet2.difference_update(['Anu', 'Lakshmi'])  # different datatype operands also possible
print(differSet2)
differSet1 -= differSet2
print(differSet1)

# Symmetric_difference
print("\nSymmetric Difference Operation...")
symtDifferSet1 = {'Neeraj', 'Anu', 'Varsha'}
symtDifferSet2 = {'Meera', 'Dhanum', 'Anu'}
symtDifferSet3 = {'Neeraj', 'Atsara'}

# method1
print(symtDifferSet1.symmetric_difference(symtDifferSet2))
# print(symtDifferSet1.symmetric_difference(symtDifferSet2, symtDifferSet3)) #cannot add multiple sets at a same time in this
# TypeError: set.symmetric_difference() takes exactly one argument (2 given)
print(symtDifferSet1.symmetric_difference(('Neeraj',
                                           'Murali')))  # tuple - can add different datatype operands to this set method by first converting into set and do symmetric_difference operation

# method2
print("Symmetric Difference Operation using operator(^) ...")
print(symtDifferSet1 ^ symtDifferSet2)
print(
    symtDifferSet1 ^ symtDifferSet2 ^ symtDifferSet3)  # can add multiple sets at a same time in this method (in normal method it's not possible)
# print(symtDifferSet1 ^ ('Neeraj', 'Murali')) #tuple - cannot add different datatype operands to this set method
# #TypeError: unsupported operand type(s) for ^: 'set' and 'tuple'

# Symmetric_difference_update
print("Symmetric difference Operation updation ...")
symtDifferSet1.symmetric_difference_update(symtDifferSet2)
print(symtDifferSet1)  # it will compare both sets and print non-difference items both sets
symtDifferSet2.symmetric_difference_update(['Anu', 'Lakshmi'])  # different datatype operands also possible
print(symtDifferSet2)
symtDifferSet1 ^= symtDifferSet2
print(symtDifferSet1)

# disjoint_set (if all elements are different, then return True)
print("Disjoint_Set...")
disjointSet1 = {'Neeraj', 'Anu', 'Varsha'}
disjointSet2 = {'Meera', 'Dhanum', 'Anu'}

print(disjointSet1.isdisjoint(disjointSet2))
print(disjointSet2.isdisjoint(['Bhuvi', 'Vishnu']))

# there is no operator for disjoint

# subset_set (if all elements are same, then return True - if set1 contains all the elements in set2)
print("subset_Set...")
subsetSet1 = {'Neeraj', 'Varsha'}
subsetSet2 = {'Neeraj', 'Varsha', 'Atsara', 'Vishnu'}

# method1
print(subsetSet1.issubset(subsetSet2))
print(subsetSet2.issubset(['Neeraj', 'Vishnu', 'Varsha', 'Atsara', 'Darshana']))

# method2
print(subsetSet1 <= subsetSet2)
print(subsetSet2 <= subsetSet1)  # because all the values in set2 not present in set1

# super_set (if all elements are same, then return - if set2 contains all the elements in set1(reverse of subset))
print("Super_Set...")
superSet1 = {'Neeraj', 'Varsha'}
superSet2 = {'Neeraj', 'Varsha', 'Atsara', 'Vishnu'}

# method1
print(superSet1.issuperset(superSet2))
print(superSet2.issuperset(['Neeraj', 'Vishnu', 'Varsha', 'Atsara', 'Darshana']))

# method2
print(superSet1 >= superSet2)  # because all the values in set1 not present in set2
print(superSet2 >= superSet1)

# del and clear comparison
superSet1.clear()  # remove only the items in set
print(superSet1)

del superSet2  # remove the complete variable itself
# print(superSet2) #NameError: name 'superSet2' is not defined. Did you mean: 'superSet1'?


# ReCall
set1 = {'Neeraj', 'Anu', 'Varsha'}
set2 = {'Meera', 'Dhanum', 'Anu'}

# print(set1.union(set2)) # or print(set1 | set2) # {'Anu', 'Meera', 'Neeraj', 'Dhanum', 'Varsha'}
# set1.update(set2); print(set1)# or set1 |= set2; print(set1) # {'Anu', 'Meera', 'Neeraj', 'Dhanum', 'Varsha'}

# print(set1.intersection(set2)) # or print(set1 & set2) # {'Anu'}
#set1.intersection_update(set2); print(set1)  # or set1 &= set2; print(set1) # {'Anu'}

# print(set1.difference(set2)) # or print(set1 - set2) # {'Neeraj', 'Varsha'}
# set1.difference_update(set2); print(set1)  # or set1 -= set2; print(set1) # {'Neeraj', 'Varsha'}

# print(set1.symmetric_difference(set2)) # or print(set1 ^ set2) # {'Neeraj', 'Dhanum', 'Varsha', 'Meera'}
# set1.symmetric_difference_update(set2); print(set1)  # or set1 ^= set2; print(set1) # {'Neeraj', 'Dhanum', 'Varsha', 'Meera'}

set12 = {'Meera', 'Dhanum', 'Anu', 'Neeraj', 'Varsha'}

print(set1.isdisjoint(set2)) #False

print(set1.issubset(set12)) #True
print(set1 <= set2) #False

print(set1.issuperset(set12)) #False
print(set12 >= set2) #True
