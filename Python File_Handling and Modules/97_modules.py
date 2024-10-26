# print(help("modules")) #to check available built_in modules

# Built_in module

# import math
# print(math.pi)

# user_defined module

# normal import:
# import user_defined_module
# print(user_defined_module.a)

# normal import in shortform:
# import user_defined_module as udm
# print(udm.a)

# import specific variable/function from module:
# from user_defined_module import calculator
# calculator(10,5)

# import specific variable/function from module in shortform:
# from user_defined_module import calculator as cal
# cal(10,5)

# import multiple specific variable/function from module in shortform:
# from user_defined_module import calculator as cal, a
# cal(10,5)
# print(a)

# import all variable/function from module using *:
# from user_defined_module import *
# calculator(10,5)
# print(a)

# override module value issue:
# from user_defined_module import *
# calculator(10,5)
# a = 15
# print(a) # it overrides the module value to avoid use normal import

# override module value issue fix case:
import user_defined_module
a = 15
print(a)
print(user_defined_module.a)