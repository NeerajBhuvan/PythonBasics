# def title_case(word):
#     word_array = word.split(" ")
#     altered_words = []
#     for words in word_array:
#         # chars = list(words)
#         # chars[0] = chars[0].upper()
#         # altered_words.append("".join(chars))
#         altered_words.append(words.title())
#     return " ".join(altered_words)


# input_words = input("Enter the words separated by space to convert into title case: ")
# print(title_case(input_words))

# str_value = "hello neeraj bhuvan how are you"
# print(str_value.title())

import statistics


def add(a, b):
    print(f"The sum of {a} and {b} is {a + b}") # no return statement so it's Implicit

add(5, 5) # Implicitly returns None

# multiple return statements
def format_names(first_name, last_name):
    if first_name is not None and first_name.isalpha() and last_name is not None and last_name.isalpha():
       formated_first_name = first_name.title()
       formatted_last_name = last_name.title()
       return formated_first_name + " " + formatted_last_name # has return statement so it's Explicit
    else:
        return "Invalid Input"

first_name_input = input("Enter the first name: ")
last_name_input = input("Enter the last name: ")
print(format_names(first_name_input,last_name_input)) # Explicitly returns
# get_names = input("Enter the first and last name separated by comma(,): ")
# words = get_names.split(",")
# print(format_names(words[0], words[1]))


# multiple output in single return
def mean_medium_mode(list_Value):
    mean_result = statistics.mean(list_Value)
    median_result = statistics.median(list_Value)
    mode_result = statistics.mode(list_Value)
    return mean_result, median_result, mode_result #(5.5, 5.5, 2)

# output = mean_medium_mode([2,3,4,5,6,7,8,9])
a,b,c = mean_medium_mode([2,3,4,5,6,7,8,9])
print(f"Mean is {a} \nMedian is {b} \nMode is {c}")



