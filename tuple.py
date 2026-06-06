#tuple -it is same as list but it is immutable
#the data cannot be changed
#tuple is created by using ()
#it supports different data types
#there are less built in methods for tuple like index and count
tup=("gopi",22,55.8)
print(tup)
# index-it is a method to get the index number of a element
x=tup.index(22)
print(x)
#count- count is a method to count the number of times the element is appears
y=tup.count("gopi")
print(y)
#
tup=("gopi",22,55.8,"gopi")
y=tup.count("gopi")
print(y)