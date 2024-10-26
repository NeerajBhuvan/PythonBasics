a = 20 #Global scope, check 3
def display1():
    a = 15 + 1 #local scope , check 2 - if a not present it will go to check 3
    def show():
        print(a) #check 1
        # a = 1 UnboundLocalError: cannot access local variable 'a' where it is not associated with a value
    show()

display1()
print(a)

#python don't have block scope other than function
if a > 5:
    c = a + 5
print(c) # c is not blocked, inside a if block

#Lec - 79 Global Keyword
name = "Jenny's"
def display_name():
    global name #refers to global variable
    name = name + " Lectures"

print(name)
display_name()
print(name)