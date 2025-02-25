import math
'''
Task 1
'''
def is_number(value):
    return value.strip().isdigit()
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = input("Enter a number :")
if number.strip() == '':
    print("Error: One or both inputs are empty!")
else:
    if is_number(number) :
        result = factorial(int(number))
        print(f"Factorial of {number} is: {result}")
    else:
        print("Error: Invalid input!")



'''
Task 2
'''
num = float(input("Enter a number: "))
sqrt_num = math.sqrt(num)
log_num = math.log(num)
sin_num = math.sin(num)

print(f"Square root : {sqrt_num}")
print(f"Logarithm: {log_num}")
print(f"Sine: {sin_num}")
