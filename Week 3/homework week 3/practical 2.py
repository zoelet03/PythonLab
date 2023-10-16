
import sys

passcheck = input("Enter a password to check: ")

checking=set(passcheck)

passlength = len(passcheck)

points=0

symbols = {'!','$','%','^','&','*','(',')','-','_','=','+'}
qwerty = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]




if passlength <8 or passlength >12:
    print("ERROR. Password must be between 8-12  characters long")


else:

    for i in qwerty:

        if i in passcheck:  #If entered password is in the form of 'QWERTY': subtract 15 points.
            points-=15
            print("your password contain form of 'QWERTY' , Don't use weak password.")
            print(points)
            sys.exit()




