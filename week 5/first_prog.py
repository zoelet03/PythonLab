number = input("Enter a number: ") #Asks for user input
number = int(number) #User input is an integer
print("The numbered entered was", number)
if (number % 2) == 0: #to detect if even or odd and to print result
	print("That is an even number")
else:
	print("That is an odd number")

if (number % 10) == 0:
	print("This number is also divisible by 10")