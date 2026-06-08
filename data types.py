# data types in python are two types such as primitive data types and non-primitive data types also known as mutable and immutable\
# Mutable -it means the data is allowed to change for updates and adding after creation
# list,set,dictionary and bytearray are mutable data types
# Immutable _ the data cannot be changed after creation
# String,int,bool,tuple,frozenset and bytes
#Numeric data types- int,float,complex
a=19
print(type(a))
b=12.5
print(type(b))
c=9+1j
print(type(c))
# Sequence data types- list,tuple,range
l=[10,20,340,567,89]
print(type(l))
t=(10,20,340,567,89)
print(type(t))
r=range(10)
print(r)
print(type(r))
# text data type -string
st=("gopi")
print(type(st))
#bool -returns true or false
x=10
y=20
print(x>y)
print(type(y>x))
# set ,dictionary
set={"gopi",10,"babu"}
print(type(set))
dict={"key":"gopi","age":"22"}
print(type(dict))