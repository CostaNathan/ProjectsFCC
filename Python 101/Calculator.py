#when getting an input from a user, by default it become a string 
#to convert strings to num = 'int' - works with only hole number
#to convert string to num with decimal = 'float' - works with hole and decimal numbers

num1 = input("Enter a number: ")
num2 = input("Enter an integer: ")
result = float(num1) + int(num2)

print(result)