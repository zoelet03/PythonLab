
import sys

passcheck = input("Enter a password to check: ")

checking=set(passcheck)

passlength = len(passcheck)

points=0

symbols = {'!','$','%','^','&','*','(',')','-','_','=','+'}
qwerty = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]


bad_passwords = ['password', 'letmein', 'sesame', 'justinbieiber']

if passcheck := bad_passwords:
    print("Your password cannot be commonly used")


    if passlength <8 or passlength >12:
        print("ERROR. Password must be between 8-12  characters long")


else:


    for i in qwerty:

        if i in passcheck:
            points-=15
            print("your password contain form of 'QWERTY' , Don't use weak password.")
            print(points)
            sys.exit()




