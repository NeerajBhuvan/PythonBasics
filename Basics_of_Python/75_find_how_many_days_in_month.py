def find_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year_input, month_input):
    month_day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month_input == 2 and find_leap_year(year_input):
        days = month_day_list[1] + 1
    elif 1 <= month_input <= 12:
        days = month_day_list[month_input - 1]
    else:
        return "Invalid Input!"

    return f"Totally there are {days} days in a {month_input} month of year {year_input}"

get_year = int(input("Enter the year: "))
month = int(input("Enter the month in number(1 to 12): "))
output = days_in_month(get_year, month)
print(output)



