# Problem 4 : Input 5 subject marks from user and display grade.

m = int(input("Enter your Maths marks:"))
s = int(input("Enter your Science marks:"))
h = int(input("Enter your History marks:"))
g = int(input("Enter your Geography marks:"))
ma = int(input("Enter your Marathi marks:"))

marks_obtain = m + s + h + g + ma
total_marks = 500                               # Assume marks per sub=100 so,5 sub=500 marks

percentage = marks_obtain/total_marks * 100

if (percentage >= 60):                                           # above 60% = First class
    print(percentage,"%","Student is getting First Class.")

elif (percentage >= 45):                                         # (45% to 60%) = Second class
    print(percentage,"%","Student is getting Second Class.")

elif (percentage >= 35):                                         # (35% to 45%) = Just pass                                    
    print(percentage,"%","Student is just Pass.")

else:                                                            # Less than 35% = Failed
    print(percentage,"%","Student is Failed.")

