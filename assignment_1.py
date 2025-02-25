
'''
Task 1
'''
def is_number(value):
    return value.strip().isdigit()
a = input("Enter the first Number :")
b = input("Enter the second Number :")

if a.strip() == '' or b.strip() == '':
    print("Error: One or both inputs are empty!")
if is_number(a) and is_number(b):
    print("Addition:", int(a) + int(b))
    print("subtraction:", int(a) - int(b))
    print("Multiplication:", int(a) * int(b))
    print("Division:", int(a) / int(b))

'''
Task 2
'''

first = input("Enter the first name : ")
last = input("Enter the last name : ")

if a.strip() == '' or b.strip() == '':
    print("Error: One or both inputs are empty!")
else:
    print("Hello,",first,last+"!"," Welcome to the Python program.")
