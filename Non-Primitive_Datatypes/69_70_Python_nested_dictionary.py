import os

student_data = {
    "Ram": {
        "roll_no": 101,
        "age": 20,
        "course": "Python"
    },
    "Mohan": {
        "roll_no": 102,
        "age": 21,
        "course": "Java"
    }
}

# To access nested dictionary
print(student_data)
print(student_data["Ram"]["course"])

# To update nested dictionary
student_data["Ram"]["phone_no"] = [123456, 987642]
print(student_data["Ram"])

# To delete nested dictionary
# del (return nothing)
del student_data["Ram"]["age"]
print(student_data["Ram"])

# pop (return deleted value)
print(student_data["Mohan"].pop("age"))
print(student_data)

# Nesting a list within dictionary
travel_data = {
    "Rajasthan": ["Jaipur", "Udaipur"],
    "TamilNadu": ["Madurai", "Chennai"]
}
print(travel_data["Rajasthan"][0])

# Nesting a dictionary within list
student_data_list = [
    {
    "name": "Ram",
    "roll_no": 101,
    "age": 20,
    "course": "Python"
    },
    {
        "name": "Mohan",
        "roll_no": 102,
        "age": 21,
        "course": "Java"
    }
]

print(student_data_list[1]["name"])
student_data_list[1]["phone_no"] = [123456, 987642]
print(student_data_list)

#Lec-70 add new entry to the list
def add_new_student(name, roll_no, age, course):
    student = {
        "name": name,
        "roll_no": roll_no,
        "age": age,
        "course": course
    }
    student_data_list.append(student)

add_new_student("Shyam", 22, 18, "C++")
print(student_data_list)

os.system('cls')