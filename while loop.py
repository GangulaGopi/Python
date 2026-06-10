# looping statements - while,for
# while - A while loop in Python is used to repeat a block of code as long as a condition is True.
# i=1
# while i<=5:
#     print(i)
#     i+=1
# # to print all the numbers in the same line we need to use end="" (end delimiter)
# i=1
# while i<=5:
#     print(i,end=" ")
#     i+=1
# nested while loop -loop with in a loop
import sys;
i=1
while i<=5:
    print("gopi",end=" ")
    j=1
    while j<=5: # when there is two loops then inner loop executes first and then outer loop
        print("babu",end=" ")
        j+=1

    i+=1
    print() # it prints the output of one iteration


