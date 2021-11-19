# Wodneful sample program
#steps
#1. ask age, convert and stage
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