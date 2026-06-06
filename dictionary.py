#dictionary-it is used to store key value pairs
# dictionary -it is also a mutable data type
#it is created by using {}
# keys should be unique
dict={"maths":"40","ps":"45","cs":"56"}
print(dict)
#get -it is a method to get the particular element from the dict ---if the value is not present in the dict it doesn't throws any
# error
x=dict.get("maths")
print(x)
y=dict.get("40")
print(y)
# it throws error
# z=dict[30]
# print(z)
#keys -it returns all keys
a=dict.keys()
print(a)
# values -it returns all values
b=dict.values()
print(b)
# items -it returns both key and value pairs
c=dict.items()
print(c)
