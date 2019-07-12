firstName = input("What is your first name? ")
lastName = input("What is your last name? ")
fullName = firstName.strip() + " " + lastName.strip()

print("Welcome " + fullName.lower() + "!") 

lengthName = len(fullName) - 1

print("Your name have", lengthName,  "characters")

firstLetter = firstName[0]

print("The first letter of your name is " + firstLetter.upper())

myName = fullName.split(" ")

print(myName)


searchTerm = input("Search a word: ")
searchResult = fullName.lower().find(searchTerm.lower())

if searchResult == -1:
    print("Word Not Found")
else:
    print("result: " + fullName[searchResult:])