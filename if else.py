# if else and elif statements
# if -is a conditional statements to cheks the condition and returns true
# elif - it is also used to check with in if condition like 2nd code runs if condition2 is True
#else-it returns true when none of the above conditions are true
# age=int(input("Enter your age:"))
# if age>=18:
#     print("Valid")
# it executes the conditions and returns true when we give a valid input otherwise doesn't give any output
# elif
# age=int(input("Enter your age:"))
# salary=int(input("Enter your salary:"))
# if age<18:
#     print("InValid")
# elif salary>=50000:
#     print("valid")
age = int(input("Enter your age:"))

if age < 18:
    print("Minor")
elif age == 18:
    print("Exactly 18")
else:
    print("Adult")
