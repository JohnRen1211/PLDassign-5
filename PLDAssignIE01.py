# The if else application
#steps
#1. ask age, convert and stage.
#2. Show response in condition.

print("Welcome to the system can you input age? Type 1 for yes and 2 for no command.")
answer= int(input("Response: "))
command1 = 1
command2 = 2
if answer == command2:
    print("Okay, then rest.")
    raise SystemExit
elif answer <= -1:
    print("Input the right command.")
    raise SystemExit
elif answer == command1:
    print("Continue to the survey")
elif answer >= command2:
    print("Input the right command.")
    raise SystemExit

age = int(input("Age: "))
#2. test 0-12
if age > -1 and age <= 12:
    print("Kid")
#3. test 12-17
elif age >= 13 and age <= 17:
    print("Teen") 
#4. test 18
elif age==18:
    print("Debut")
#5. test >= 19
else:
    print("Adult age")

print("System successfully processed the information.")