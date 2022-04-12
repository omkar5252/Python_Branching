# verify userid and password with captcha

import random
userid = input("Enter userid:")
password = input("Enter password:")

# Userid and password correct than generate 4 digit number (captcha)
if (userid == "omkar_dorugade" and password == "12345"):
    number = random.randrange(1111,9999)
    print("captcha generated:",number)

    digit = int(input("\nEnter captcha here:"))     # Entered captcha here and login
    if (number == digit):
        print("sucessfully login")
    else:
        print("wrong captcha")
else:
    print("\nChecked your userid and password.")

