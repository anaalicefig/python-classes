myList = ["Mary", "John", "Mike", "Alice"]

myList.append("Mark")

for l in myList:
    print(l)

searchTerm = input("search something on the list: ")

if searchTerm in myList:
    print("Found")
else:
    print("Not found")

del myList[2]

for l in myList:
    print(l)

print("-----------")

array = [1,5,2,4,3]

array.sort(reverse=True)

print(array)
