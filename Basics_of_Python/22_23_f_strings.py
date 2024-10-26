name = "Neeraj"
age = 23
height = 1.81

print(f"My name is {name}. I am {age} years old. My height is {height} meters")

#Lec-23 Calculate age till 90 years
givenAge = int(input("Enter your age: "))

yearsLeft = 90 - givenAge
monthsLeft = yearsLeft * 12
weeksLeft = yearsLeft * 52
daysLeft = yearsLeft * 365

print(f"As per your age untill 90 years, you have {daysLeft} days, {weeksLeft} weeks, {monthsLeft} months and {yearsLeft} years left")
