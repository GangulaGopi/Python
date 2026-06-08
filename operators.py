# operators in python
# Operator Type       	Examples
# Arithmetic Operators	 +, -, *, /
# Assignment Operators	 =, +=, -=
# Comparison Operators	 ==, !=, >
# Logical Operators	     and, or, not
# Bitwise Operators	     &, |
# Membership Operators   in, not in
# Identity Operators	 is, is not
# Arithmetic Operators -it is used to perform mathematical calculations
a=45
b=18
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a//b)
print(a%b)
#Assignment operators-it is used to assign a value to the variable
x=10
print(x)
x+=2
print(x)
x-=2
print(x)
x/=2
print(x)
x//=2
print(x)
x%=2
print(x)
x=20
x*=2
print(x)
# comparison operators -it is used to compare the values
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
# logical operators -it is used between the conditions
a=1
b=0
print(a and b)
print(a or b)
print(not a)
print(not b)
# bitwise operators-it checks with the binary form and returns the answer simply works on binary values
a=5
b=3
print(a&b)
print(a|b)
print(a<<b) #left shit
print(a>>b) # right shift
# membership operators-it checks whether the elements present or not
a=["gopi","praneeth","babu"]
print("gopi" in a)
print("gopi"  not in a)
# Identity -Check whether two variables refer to the same object
a=10
b=10
print(a is b)
print (a is not b)