
'''
Task 1
'''
def is_number(value):
    return value.strip().isdigit()
a = input("Enter a number :")

if a.strip() == '':
    print("Error: One or both inputs are empty!")
else:
    if is_number(a) :
        if int(a)% 2 == 0:
            print(a," is an even number.")
        else:
            print(a," is an odd number.")
    else:
        print("Error: Invalid input!")

'''
Task 2
'''
totalSum = 0

for num in range(1, 51):
    totalSum += num


print("The sum of numbers from 1 to 50 is:", totalSum)
