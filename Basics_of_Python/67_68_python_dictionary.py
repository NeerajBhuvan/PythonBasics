# 1) 3 ways to create a dictionary
phone_no = {
    'Neeraj': 1234,
    'Varsha': 3456,
    'Anu': 6789
}

# phone_no = dict({
#     'Neeraj': 1234,
#     'Varsha': 3456,
#     'Anu': 6789
# })

# phone_no = dict([
#     ('Neeraj', 1234),
#     ('Varsha', 3456),
#     ('Anu', 6789)
# ])
print(phone_no)
print(type(phone_no))

# copy dictionary
phone_no2 = phone_no.copy() #it will create a new reference and store it
print(id(phone_no2))
print(id(phone_no))

# 2) To update items in dictionary
phone_no['Balamani'] = 5478
print(phone_no)
print(phone_no2)

# 3) To modify values in dictionary
phone_no['Neeraj'] = {
    'Work': 5555,
    'Home': 6666
}
print(phone_no)

# 4) To Access values in dictionary
print(phone_no['Balamani'])

# Nested Dictionary
print(phone_no['Neeraj']['Home'])

# get method
print(phone_no.get('Anu'))
print(phone_no.get('anu')) #None

# access only keys in dictionary
print(phone_no.keys())

# access only values in dictionary
print(phone_no.values())

# access all items in dictionary (return as list with items in tuple)
print(phone_no.items())

# access keys/values/items in loop
for i in phone_no:
    print(i) #keys
    print(phone_no[i]) #values

for i in phone_no.items():
    print(i) #items

for key,value in phone_no.items():
    print(key) #keys
    print(value) #values

# 5) To delete items in dictionary
# del
del phone_no['Balamani']
print(phone_no)

# pop()
print(phone_no.pop('Anu'))
print(phone_no['Neeraj'].pop('Work')) #Nested pop
print(phone_no)

#popitem() - remove last item in a dictionary
print(phone_no.popitem())
print(phone_no)

# clear()
print(phone_no.clear())
print(phone_no)

# Lec = 68 Program to convert marks into grades
student_marks = {
    "Jenny": 92,
    "Harry": 78,
    "Dimpy": 56,
    "Rahul": 41,
    "Aniket": 99,
    "Prem": 34
}
print(student_marks)
student_grades = {}
for student in student_marks:
    mark = student_marks[student]
    if mark >= 90: 
        student_grades[student] = 'A+'
    elif mark > 80:
        student_grades[student] = 'A'
    elif mark > 70:
        student_grades[student] = 'B+'
    elif mark > 60:
        student_grades[student] = 'B'
    elif mark > 50:
        student_grades[student] = 'C'
    elif mark > 40:
        student_grades[student] = 'D'
    else:
        student_grades[student] = 'F'
print(student_grades)