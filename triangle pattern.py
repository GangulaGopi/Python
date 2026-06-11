# Triangle patterns
# Right angle triangle
# Reverse right angle  triangle
# Number triangle
# Increasing number pattern triangle
# pyramid triangle
# Reverse pyramid

# Right angled triangle pattern
# for i in range(5):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(5):
#     for j in range(i+1):
#         print("*",end=" ")
# #     print()
# for i in range(5):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(1,6):
#     print("* "*i)

# Reverse triangle
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(5,0,-1):
#     print("* "*i)
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# #number pattern
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# increasing number pattern
# n=4
# num=1
#
# for i in range(1,n+1):
#
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num+=1
#
#     print()
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
# alphabets triangle
# n=5
# ch=65
# for i in range(1,n+1):
#     for j in range(i):
#         print(chr(ch),end=" ")
#         ch+=1
#     print()
#
# n=5
# ch=65
# for i in range(1,n+1):
#     for j in range(i):
#         print(chr(ch),end=" ")
#         ch+=1
#     print()

#  Pyramid Pattern
n=5

for i in range(1,n+1):

    print(" "*(n-i),end="")

    for j in range(i):
        print("* ",end="")

    print()