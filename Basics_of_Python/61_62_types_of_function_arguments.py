# 1) default arguments:
def default_employee(name, roll_no, company="Wipro", dept="NMS"):  # company and dept are default arguments
    print(
        f"Default Arguments - {name} worked in {company} and his roll number is {roll_no} and his department is {dept}")

default_employee("Neeraj", 40086242, dept="IBSF")  # modify default argument dept and it will override a default definition value

# 2) positional arguments:
def positional_employee(name, roll_no, salary):
    print(f"Positional Arguments - I'm {name}, My roll number is {roll_no} and my salary is Rs.{salary}/_")

positional_employee("Neeraj", 40086242, 19500)  # should be same ordered/positioned as in definition
# positional_employee("19500", "Neeraj", 40086242) #else it will collapse like this

# 3) keyword arguments:
def keyword_employee(name, roll_no, salary, experience):
    print(f"Keyword Arguments - I'm {name} and I have {experience} years of experience, My roll number is {roll_no} and my salary is Rs.{salary}/_")

keyword_employee(roll_no=40086242, name="Neeraj", experience=2.8, salary=19500) # order can be changed but keywords should be same as definition

# Combined arguments:
def combined_employee(name, roll_no, salary, place, experience = 2.0):
    print(f"combined Arguments - I'm {name} from {place} and I have {experience} years of experience, My roll number is {roll_no} and my salary is Rs.{salary}/_")

combined_employee("Neeraj", 40086242, experience=2.8, salary=19500, place="Madurai")

# Lec_62
# 4) arbitrary arguments:

# 4.1) arbitrary positional arguments(*args):
def multiple_numbers(*numbers):
    print(numbers)  #first covert it into a tuple(immutable), so that parameter can't be modified
    result = 1
    for num in numbers:
        result *= num
    print(f"Multiplication of given number is {result}")

multiple_numbers(1,2,3,4,5,6,7,8,9)

# 4.2) arbitrary keyword arguments(**kwargs):
def employee_data(**info):
    print(info) #first covert it into a dictionary(immutable), so that parameter can't be modified
    for key,value in info.items():
        print(key, value)

employee_data(name="Neeraj", age=23, salary=19500)

# 4.3) combined arbitrary arguments(*args, **kwargs):
# Always position arguments should define first followed by keyword arguments
def employee_combined_data(*args, **kwargs):

    #arbitrary positional
    print("Positional Values...")
    for i in args:
        print(i)

    # arbitrary keyword
    print("keyword Values...")
    for key,value in kwargs.items():
        print(f"{key}: {value}")

employee_combined_data(1, 2, 3, name="Neeraj", age=23, salary=19500)


