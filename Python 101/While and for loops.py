## while specify a condition that will be run repeatedly until the false condition
## while loops always checks the condition prior to running the loop

i = 1
while i  <= 10:
    print(i)
    i += 1

print("Done with loop")

## for variable 'in' collection to look over:
## the defined variable will change each iteration of the loop

for letter in "Giraffe academy":
    print(letter)

## the loop will print each letter individualy for the defined variable
## letter will correspond to the first, than the second, than ... each iteration

friends = ["Jim", "Karen", "Jorge"]
for name in friends:
    print(name)

for index in range(10):
    print(index)
## range() = will count up to the design value, but without it
## in the above example, index will correspond to 0,1,2,...,9 for each iteration
for index in range(3,10):
    print(index)

## an example of for loop to loop through an array

for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("Begin iteration!")
    elif index == 4:
        print("Iteration complete!")