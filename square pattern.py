# pattern's in python can be printed by using loop's either while or for by using *,alphabets or numbers
# We can print square pattern with two loops ,one loop for rows and another loop for columns
# we can print using by one single loop with the help of string multiplication
# square pattern using two loops
# for i in range(5): # oter loop for flow (rows)
#     for j in range(5): # inner loop for printing stars(columns)
#         print("*",end=" ")
#     print()# for new line

# square pattern in one loop using string multiplication
# for i in range(5):
# #     print("* "*5)
# for i in range(5):
#     for j in range(5):
#          print(i,end=" ")
#     print()
# for i in range(5):
#     for j in range(5):
#          print(j,end=" ")
#     print()
# for i in range(5):
#     print("1 "*5)

# for i in range(5):
#     for j in range(5):
#          print(1,end=" ")
#     print()

# using alphabets
# n=5
# for i in range(65,70):
#     for j in range(5):
#          print(chr(i),end=" ")
#     print()
# n=5
# num=65
# for i in range(n):
#     for j in range(5):
#          print(chr(num),end=" ")
#          num+=1
#     print()
# using numbers
n=5
num=1
for i in range(n):
    for j in range(5):
         print(num,end=" ")
         num+=1
    print()