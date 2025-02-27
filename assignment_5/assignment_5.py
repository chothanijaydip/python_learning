'''
Task 1
'''

student = [ {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 78},
    {"name": "Charlie", "marks": 92},
    {"name": "David", "marks": 88},
    {"name": "Eve", "marks": 76}]
studentName = input("Enter the student's name: ")
if studentName.strip() == '':
    print("Error: One or both inputs are empty!")
else:
    for student in student:
        if student["name"].lower() == studentName.lower():
            print(f"{student['name']}'s marks: {student['marks']}")
            break
    else:
        print("Student not found.")

'''
Task 2
'''

oList =list( range(1,11))
print("Original list: ", oList)
print("Extracts first five elements: ", oList[0:5])
print("Reverses extracted elements: ", list(reversed(oList[0:5])))

