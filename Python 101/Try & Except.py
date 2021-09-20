## try/except blocks are used to respond to the user something when an error occur
## best practice to use except with specific errors


try:
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as  err:
    print(err)
except ValueError:
    input("Invalid input")