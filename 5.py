# Program 5 : program to check if person is eligible to marry or not (male age >=21 and female age>=18)

age = int(input("Enter your Age:"))
gender = input("Enter your Gender (M/F):")

if (age >= 21 and (gender=="M" or gender=="m")):
    print("Person is eligible for marriage.")

elif (age >= 18 and (gender=="F" or gender=="f")):
    print("Person is eligible for marriage.")
    
else:
    print("Person is not eligible for marriage.")