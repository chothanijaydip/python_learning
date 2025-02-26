
'''
Task 1
'''

file1 = open("sample.txt",'w')
file1.write("This is a sample text file.\nIt Contains multiple lines.")
file1.close()


try:
    with open("sample.txt",'r') as file:
        print("Reading file content:")
        count = 1
        for line in file:

            print(f"Line {count}:"+line.strip())
            count = 1+count
        file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")


'''
Task 2
'''

try:
    fileContent1 = input("Enter a file content:")
    file1 = open("output.txt",'w')
    writeFile =file1.write(fileContent1)
    if writeFile:
        print("Data successfully written to output.txt.")
    file1.close()
    fileContent2 = input("Enter additional text to append:")
    file1 = open("output.txt",'a')
    appendFile =file1.write(fileContent2)
    if appendFile:
        print("Data successfully appended.")
    file1.close()
    file1 = open("output.txt",'r')
    readFile =file1.read()
    print('Final contents of output.txt')
    print(readFile)
    file1.close()
except FileNotFoundError:
    print("Error: The file 'output.txt' was not found.")
