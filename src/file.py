file = open("./files/filetest.txt")
lines = file.readlines()

for line in lines:
    print(line)

file.close()
print("------------")


file2 = open("./files/file2.txt", "w")
file2.write("File 2")

file2.close()

file2 = open("./files/file2.txt")
text = file2.read()
print(text)
file2.close()