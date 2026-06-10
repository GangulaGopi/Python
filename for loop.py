# for loop - it doesnt required  any condition
# it automatically increases i value itself
# it specially works with sequence data types
x=["Gopi",18,59.50]
for i in x:
    print(i)
# we can use list in the same for loop without any extra variable
for i in ["Gopi",18,59.50]:
    print(i)
# there is a range function we can use with for loop
# range is a function it has start ,end and step count
# for i in range(1,10): # it prints upto 9 becuase last one is excluded in range
#     print(i)
# for i in range(10): # when we give only one argument then it take it as end
#     print(i)
for i in range(10,-1): # when we give like this it doesn't provide output  becuase of reverse indexing we need to specify start,end and step count
    print(i)
for i in range(10,1,-1):
    print(i)
