# The steps to do.
#1 Ask for 3 numbers value.
#2 Show the lowest value showing the highest is optional.
# Using list,min,max,raise commands for the program.

print("Welcome to the system can you input 3 numbers? Type 1 for yes and 2 for no command.")
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
  
number1 = float(input("num#1: "))
number2 = float(input("num#2: "))
number3 = float(input("num#3: "))

if number1 <= number2 and number3:
    print(f"The number#1 value {number1} is the lowest number.")
elif number2 <= number1 and number3:
    print(f"The number#2 value {number2} is the lowest number.")
elif number3 <= number1 and number2:
    print(f" The number#3 value {number3} is lowest number.")



if (number1 >= number2) and (number1 >= number3):
    print(f"The number#1 value {number1} is the highest number.")
elif (number2 >= number1) and (number2 >=number3):
    print(f"The number#2 value {number2} is the highest number.")
elif (number3 >= number1) and (number3 >=number2):
    print(f"The number#3 value {number3} is the highest number.")

print("The lowest value is: ")
print(min([number1, number2, number3]))
print("The highest value is: ")
print(max([number1, number2, number3]))



