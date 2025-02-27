# Student Marks and List Manipulation in Python

## Task 1: Student Marks Lookup
This program allows users to input a student's name and retrieve their marks from a predefined list. If the student is not found, an appropriate error message is displayed.

### Functionality:
- Takes user input for a student's name.
- Searches for the student in a predefined list of dictionaries.
- Displays the student's marks if found.
- Provides an error message if the name is empty or the student is not found.

### Code:
```python
student = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 78},
    {"name": "Charlie", "marks": 92},
    {"name": "David", "marks": 88},
    {"name": "Eve", "marks": 76}
]

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
```

## Task 2: List Manipulation
This program performs basic list operations on a list of numbers from 1 to 10.

### Functionality:
- Creates a list containing numbers from 1 to 10.
- Extracts the first five elements of the list.
- Reverses the extracted elements and prints them.

### Code:
```python
oList = list(range(1, 11))
print("Original list: ", oList)
print("Extracts first five elements: ", oList[0:5])
print("Reverses extracted elements: ", list(reversed(oList[0:5])))
```

## How to Run the Code
1. Copy and paste the Python scripts into a Python environment.
2. Run the script and follow the prompts.
3. For Task 1, enter a student's name to see their marks.
4. For Task 2, the list operations will be printed automatically.

## Notes
- Ensure you have Python installed.
- The script is case-insensitive when searching for student names.
- The script handles empty input for student names with an error message.

