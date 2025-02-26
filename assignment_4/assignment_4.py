
'''
Task 1
'''

file1 = open("sample.txt",'w')
file1.write("This is a sample text file.\nIt Contains multiple lines.")
file1.close()


try:
    with open("sample.txt",'r') as file:
        print("Reading file content:")
        count = 1;
        for line in file:

            print(f"Line {count}:"+line.strip())
            count = 1+count
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")


'''
Task 2
'''
