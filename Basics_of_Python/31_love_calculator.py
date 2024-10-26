firstPerson = input("Enter the first person name: ").replace(" ","")
secondPerson = input("Enter the second person name: ").replace(" ","")
names = (firstPerson + secondPerson).lower()

t = names.count('t')
r = names.count('r')
u = names.count('u')
e = names.count('e')

true = t + r + u + e

l = names.count('l')
o = names.count('o')
v = names.count('v')

love = l + o + v + e

lovePercent = int(str(true) + str(love))
if lovePercent < 10 or lovePercent > 90:
    print(f"Your love score is {lovePercent}. You go together like coke and mentos")
elif lovePercent <= 40 or lovePercent <= 50:
    print(f"Your love score is {lovePercent}. You are alright to be together!")
else:
 print(f"Your love score is {lovePercent}")
