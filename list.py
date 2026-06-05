# list : list is data type in python which is used to store multiple values
# it stores different types of data and same type of data also which is also known as heterogeneous data and homogeneous data
#homo means same and hetero means different
#list is a mutable data type
#list has so many inbuilt methods to perform functions easily
# list is specified in a square brackets []
name=["gopi","praneeth","suri"]
print(name)
nums =[1,34,56,78,98]
print(nums)
list=["gopi",18,59.50]
print(list)
# if we need same floating values then we need to use to methods one is format and second one is f-string
# By using these methods we can easily print how many float values as we required
#using format method
list=["gopi",18,59.50]
print("{:.2f}".format(list[2]))
print(f"{list[2]:.2f}")
# append() - it is a method which is used to add the elements in the last
nums.append(45)
print(nums)
name.append("Babu")
print(name)
#pop -it is a method to remove elements from a list
# it removes a element by specifying the index number
# when we not passed anything in the pop then it removes last element
nums.pop()
print(nums)
nums.pop(2)
print(nums)
#remove()-it is also a method to remove a element by specifying a element directly
nums.remove(34)
print(nums)
name.remove("praneeth")
print(name)
# Accessing a list by using index values
print(nums[0])
print(name[2])
print(nums[-1])
print(nums[2])
#insert -it is a method to insert the elements in between the list
nums.insert(2,56)
print(nums)
#extend-it is also a method to add multiple values to a list
nums.extend([23,45,67,89])
print(nums)
#min() - it is used to find out minimum value from a list
x=min(nums)
print(x)

#max()- it is used to find maximum value from a list
y=max(nums)
print(y)
