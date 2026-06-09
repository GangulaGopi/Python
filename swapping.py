# swapping two numbers or variables
# In python there is a special in built method is there to swap two numbers simply
a=9
b=10
print(a)
print(b)
a,b=b,a # this is the logic to swap two numbers easily by rotating the values
print(a)
print(b)
# there are some more methods like xor and formula based operations to perform swapping
a=9
b=10
a=a^b #xor operator
b=a^b
a=a^b
print(a)
print(b)
# using third variable
a = 9
b = 10

temp = a
a = b
b = temp

print(a)
print(b)
