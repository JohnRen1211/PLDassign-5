# Program for rounding numbers given value.
# The program will ask value then evaluate it.
# The program used import for library function.  
# Type import math in program.
# The chain process of successful input.
import math
# define a function for round_up
def round_up (n, decimals =0):
    multiplier = 10 ** decimals
    return math.ceil (n * multiplier) / multiplier

print("Welcome to the system can you input grade given? Type 1 for yes and 2 for no command.")
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

given_grade = float(input("Input grade number: ")) 
equivalent_grade = round_up(given_grade)
print(f"Rounded grade: {equivalent_grade}")

if (equivalent_grade >96.4) or (equivalent_grade ==100):
    print("Grade: 1")
elif (equivalent_grade >93.4) or (equivalent_grade ==96):
    print("Grade: 1.25")
elif (equivalent_grade >90.4) or (equivalent_grade ==93):
    print("Grade: 1.50")
elif (equivalent_grade >87.4) or (equivalent_grade ==90):
    print("Grade: 1.75")
elif (equivalent_grade >84.4) or (equivalent_grade ==87):
    print("Grade: 2.0")
elif (equivalent_grade >81.4) or (equivalent_grade ==84):
    print("Grade: 2.25")
elif (equivalent_grade >78.4) or (equivalent_grade ==81):
    print("Grade: 2.5")
elif (equivalent_grade >75.4) or (equivalent_grade ==78):
    print("Grade: 2.75")
elif equivalent_grade ==75:
    print("Grade: 3.0")
elif (equivalent_grade >64.4) or (equivalent_grade ==74):
    print("Grade: 5.0")

if (equivalent_grade >93) or (equivalent_grade ==100):
    print("Description: Excellent")
elif (equivalent_grade >87) or (equivalent_grade ==93):
    print("Description: very Good")
elif (equivalent_grade >81) or (equivalent_grade ==87):
    print("Description: Good")
elif (equivalent_grade >75) or (equivalent_grade ==81):
    print("Description: Satisfactory")
elif (equivalent_grade ==75):
    print("Description: Passing")
elif (equivalent_grade >64) or (equivalent_grade ==74):
    print("Description: Failure")

print("System successfully processed the information. ")










