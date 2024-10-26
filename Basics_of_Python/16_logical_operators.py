a, b = 5, 6
c = True

#and
print("AND")
print(a <= 5 and c)
print(b == 6 and a < 4)
print(a < 4 and b == 6)
print(a > 10 and not c )

#or
print("OR")
print(a <= 5 or c)
print(a > 4 or b < 6)
print(a < 4 or b == 6)
print (a < 4 or not c)

#not (reverse)
print("NOT")
print(not a != 5)
print(not c)