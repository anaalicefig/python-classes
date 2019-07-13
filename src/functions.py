# functions
def add(value1, value2):
    return value1 + value2

def mult(value1, value2):
    return value1 * value2

value1 = input("Enter the first value: ")
value2 = input("Enter the second value: ")

add = add(float(value1), float(value2))
mult = mult(float(value1), float(value2))

print("add = ", add)
print("mult = ", mult)