# Problem 6 : calculate tkt_ammount with respect to age

age1=int(input("Enter age of first person: "))
age2=int(input("Enter age of second person: "))
age3=int(input("Enter age of third person: "))
age4=int(input("Enter age of fourth person: "))
age5=int(input("Enter age of fifth person: "))

tkt_price = float(input("\nEnter ticket price:Rs."))
total_amount = 0

# First person to pay
if (age1 <= 12):
    amt1 =tkt_price - (tkt_price * 0.3) 
elif (age1 >= 59):
    amt1 =tkt_price - (tkt_price * 0.5)
else:
    amt1 = tkt_price

# Second person to pay
if (age2 <= 12):
    amt2 =tkt_price - (tkt_price * 0.3)
elif (age2 >= 59):
    amt2 =tkt_price - (tkt_price * 0.5)
else:
    amt2 = tkt_price

# Third person to pay
if (age3 <= 12):
    amt3 =tkt_price - (tkt_price * 0.3)
elif (age3 >= 59):
    amt3 =tkt_price - (tkt_price * 0.5)
else:
    amt3 = tkt_price

# Fourth person to pay
if (age4 <= 12):
    amt4 =tkt_price - (tkt_price * 0.3)
elif (age4 >= 59):
    amt4 =tkt_price - (tkt_price * 0.5)
else:
    amt4 = tkt_price

# Fifth person to pay
if (age5 <= 12):
    amt5 = tkt_price - (tkt_price * 0.3)
elif (age5 >= 59):
    amt5 = tkt_price - (tkt_price * 0.5)
else:
    amt5 = tkt_price

total_amount = total_amount + amt1 + amt2 + amt3 + amt4 + amt5
print("\nTotal amount of ticket to travel for all of them:Rs.",total_amount)