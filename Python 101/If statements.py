## if statement allow the program to respond accordingly to the condition determined
## the indentation is assigned to the true condition
## one way to work with more than one variable in if statements - 'or', 'and' keyword
## or - the if statement will be true if one or all the conditions are true
## and - the statement will be true if all the conditions are true
## else if - 'elif' it checks to check another condition prior to the else/'false' outcome
## not(variable) = negate the variable assumption

is_male = True

if is_male:
    print("You are a male")
else:
    print("You are not a male")

is_male = False

if is_male:
    print("You are a male")
else:
    print("you are not a male")

is_tall = True
is_male = True

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male or tall")

is_tall = True
is_male = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male, but tall")
else:
    print("You are either not male or tall or both")

