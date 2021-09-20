#[] = store list of values within the variable
#Any kind of data can be stored
#index = starts from 0
#if [-1] = access the last element of the list
#if[1:] = access the element at the position 1 and the subsequent elements
#if[1:3] = access the element at the position 1 until the position 3

friends = ["Kevin", "Jim", "Rebeca"]
print(friends)
print(friends[0])

## functions to use in lists in python
##.extend() = apend a list to another
##.apend() = apend another element to the end of the list
##.insert(index, item) = apend the element to the respective index position
##.remove = to remove the element inside the list
##.clear() = to clear the entire list
##.pop() = removes the last element of the list
##.index("value") = indicates the index position of the element in the list
##.count(value) = counts how many times the element repeats in the list
##.sort() = sort down the list in ascending order
##.reverse() = reverse the order of the list
##.copy() = copy the list

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = [ "Kevin", "Karen", "Kim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
print(friends)
friends.apend("Creed")
print(friends)
friends.insert(1,"Kelly")
print(friends)

friend2 = friends.copy()


