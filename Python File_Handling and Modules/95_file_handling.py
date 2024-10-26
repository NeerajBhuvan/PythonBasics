# open and create file
# file_1 = open("95_file_handling_file_1", "x") # "x" - used to create a file
from os import write
from pprint import pprint

# Types of file:

# 1) Text Files:

# Types of mode:

# 1) read mode (r)
# file_1 = open("95_file_handling_file_1", "r")
# content = file_1.read()
# print(content)

# 2) write mode (w)
# file_1 = open("95_file_handling_file_1", "w")
# file_1.write("How are you! Neeraj!") #overwrites the existing file data

# 3) read + mode (r+)
# file_1 = open("95_file_handling_file_1", "r+")
# file_1.write("How are you?") #this code will overwrite the existing file data from the beginning
# print(file_1.read()) #so follow the recommended first read then write so file handle will be end of the file data
# #recommended
# print(file_1.read())
# file_1.write("How are you?")

# 4) write + mode (w+)
# file_1 = open("95_file_handling_file_1", "w+")
# file_1.write("How are you, ")
# print(file_1.tell())
# file_1.seek(0)
# print(file_1.tell())
# print(file_1.read())
# print(file_1.tell())
# file_1.write("Neeraj?")
# file_1.seek(0)
# print(file_1.tell())
# print(file_1.read())
# print(file_1.tell())

# 5) append mode (a)
# file_1 = open("95_file_handling_file_1", "a") #append data from end of previously typed data
# file_1.write("How is your sister")

# 6) append + mode (a+)
# file_1 = open("95_file_handling_file_1", "a+")
# file_1.write("How is your mom")
# print(file_1.tell())
# file_1.seek(0)
# print(file_1.tell())
# print(file_1.read())

# 2) Binary Files:

# 1) rb (read-binary)
image_file_1 = open("C:\\Users\\neera\\OneDrive\\Pictures\\profile.jpg", "rb")
# print(image_file_1.read())

# 2) wb (write-binary)
image_file_2 = open("95_file_handling_file_2.jpg", "wb")
for i in image_file_1:
    image_file_2.write(i)



