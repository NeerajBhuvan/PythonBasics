# Following are the methods to access package functions/classes/variable
from Python_packages_108_109.HomeShifting_Neeraj.Footwears.shoes import shoes_container

# Method 1
print("\nMethod 1...")
import Python_packages_108_109.HomeShifting_Neeraj.books

#call variable
print(Python_packages_108_109.HomeShifting_Neeraj.books.book_container)

#call function
Python_packages_108_109.HomeShifting_Neeraj.books.display()

#call class
types = Python_packages_108_109.HomeShifting_Neeraj.books.MyBooksType()
types.type1()

# Method 2
print("\nMethod 2...")
from Python_packages_108_109.HomeShifting_Neeraj import books

#call variable
print(books.book_container)

#call function
books.display()

#call class
types = books.MyBooksType()
types.type1()

# Method 3 (To access all data in module)
print("\nMethod 3...")
from Python_packages_108_109.HomeShifting_Neeraj.Footwears.shoes import *

#call variable
print(shoes_container)

#call function
display()

#call class
shoes_types = ShoesBrandType()
shoes_types.type1()
shoes_types.type2()

# Method 4 (To access particular data/function in module)
print("\nMethod 4...")
from Python_packages_108_109.HomeShifting_Neeraj.Cloths import shirts

#call function
display()

# Method 5 (To access all modules in package)
print("\nMethod 5...")
from Python_packages_108_109.HomeShifting_Neeraj.Cloths import *

#call package inside function (declare all functions in __init__.py as (__all__ = ["jeans", "shirts"]))
jeans.display()
