# In python when we want to use math functions then we have to import the required module into the environment shell
# for perform math functions we need to import math
# we can use some built in methods without importing math module
# round,abs,pow
a=110.6
print(round(a))
b=-55
print(abs(b))
print(pow(3,2))

# x=math.sqrt(5) throws an error
# print(x)
# Basic math functions
import math
print(math.sqrt(5))  # to find out the square root of a number we need to use sqrt function
print(math.pow(2,3)) # to find out the power of a number it expects two arguments
print(math.factorial(5)) # it gives the factorial value of a given number
print(math.fabs(-6)) # it gives the absolute value
# Rounding and ceiling or floor
print(math.floor(5.258467932)) # it gives the round down value
print(math.ceil(6.235688974332))# it gives the round up value
print(math.trunc(6.9))# it gives the number before decimal