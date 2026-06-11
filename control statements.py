# control statements - in python there are three control statements to control the flow of loop execution
# break,continue,pass
# break- it breaks the entire loop based on given condition
# continue - it doesn't execute the particular specified condition based iteration and continue the flow
# pass - it does nothing ,it is used in the block to Leave it for now
# i=1
# while i<=5:
#     print("gopi",i)
#     if i==4:
#         break
#     i+=1
# i=1
# while i<=5:
#
#     if i==4:
#         i+=1
#         continue
#
#     print("gopi",i)
#     i+=1

# using for loop
# for i in range(1,10):
#     if i==5:
#         break #it breaks the loops and stops the execution
#     print(i)
# for i in range(1,10):
#     if i==5:
#         continue # it skips the particular i==5 statement and continue the loop execution
#     print(i)

# for i in range(1,10):
#     if i==5:
#         pass # it does nothing
#     print(i)
# for i in range(1,10):
#     if i%2==0:
#         continue
#     print(i)
for i in range(1,10):
    if i%2==1:
        continue
    print(i)