## the possibility to create arrays within arrays as a grid-like structure
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

## to identify any element within the list 
print(number_grid[0][0])
print(number_grid[2][1])

## nested for loop to go through the entire list/array

for row in number_grid:
    print(row)

for row in number_grid:
    for col in row:
        print(col)


number_grid = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9,
    0
]

for row in number_grid:
    print(row)

