
                                    #FILE HANDLING PGMS...

# Program 1
'''
file = open("student.txt", "w")
name = input("Enter name: ")
roll = input("Enter roll number: ")
branch = input("Enter branch: ")
semester = input("Enter semester: ")
file.write("Name: " + name + "\n")
file.write("Roll No: " + roll + "\n")
file.write("Branch: " + branch + "\n")
file.write("Semester: " + semester + "\n")
file.close()
print("Data written successfully")
'''

# Program 2
'''
file = open("student.txt", "r")
content = file.read()
print(content)
file.close()
'''


# Program 3
'''
file = open("student.txt", "a")
file.write("College: DYPCET\n")
file.write("City: Kolhapur\n")
file.close()
print("Data appended successfully")
'''


# Program 4
'''
file = open("student.txt", "r")
for line in file:
    print(line, end="")
file.close()
'''


# Program 5
'''
file = open("student.txt", "r")
line_list = file.readlines()
print("Total line_list:", len(line_list))   
file.close()
'''


# Program 6
'''
f = open("student.txt", "r")
data = f.read()
words = data.split()
print("Total words:", len(words))
f.close()
'''



# Program 7
'''
file = open("student.txt", "r")
content = file.read()
print("Total characters:", len(content))
file.close()
'''


# Program 8
'''
file = open("student.txt", "r")
line_list = file.readlines()
for line in reversed(line_list):
    print(line, end="")
file.close()
'''


# Program 9
'''
file = open("student.txt", "r")
content = file.read().lower()
vowels = 0
consonants = 0
for ch in content:
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1
print("Vowels:", vowels)
print("Consonants:", consonants)
file.close()
'''


# Program 10
'''
file = open("student.txt", "r")
content = file.read()
alphabets = 0
digits = 0
spaces = 0
special = 0
for ch in content:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1
print("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)
file.close()
'''


# Program 11
'''
file = open("student.txt", "r")
word_list = file.read().split()
longest = max(word_list, key=len)
print("Longest word:", longest)
file.close()
'''


# Program 12
'''
file = open("student.txt", "r")
word_list = file.read().lower().split()
total_count = {}
for word in word_list:
    if word in total_count:
        total_count[word] += 1
    else:
        total_count[word] = 1
print("Word frequency:", total_count)
file.close()
'''


# Program 13
'''
file = open("student.txt", "r")
word = input("Enter word to search: ")
total_count = 0
line_no = 0
for line in file:
    line_no += 1
    for w in line.split():
        if w == word:
            total_count += 1
            print("Found on line:", line_no)
print("Total occurrences:", total_count)
file.close()
'''


# Program 14
'''
file =open("student.txt", "r")
content = file.read()
old = input("Enter word to replace: ")
new = input("Enter new word: ")
content = content.replace(old, new)
file.close()
file = open("student.txt", "w")
file.write(content)
file.close()
print("Word replaced successfully")
'''


# Program 15
'''
file = open("set_20aug.py", "r")
out = open("newfile_03sep.py", "w")
for line in file:
    if not line.strip().startswith("#"):
        out.write(line)
file.close()
out.close()
print("Single line comments removed successfully!!")
'''


# Program 16
'''
file = open("student.txt", "r")
out = open("uppercase.txt", "w")
content = file.read()
out.write(content.upper())
file.close()
out.close()
print("Uppercase file created successfully")
'''


# Program 17
'''
file = open("students.txt", "w")
file.write("101,Amit,85\n")
file.write("102,Priya,92\n")
file.write("103,Rahul,78\n")
file.close()
file = open("students.txt", "r")
total = 0
total_count = 0
highest = 0
highest_name = ""
print("All Records:")
for line in file:
    roll, name, marks = line.strip().split(",")
    marks = int(marks)
    print(roll, name, marks)
    total += marks
    total_count += 1
    if marks > highest:
        highest = marks
        highest_name = name
    if marks > 80:
        print("Scored more than 80:", name)
print("Highest Marks:", highest_name, highest)
print("Average Marks:", total / total_count)
file.close()
'''


# Program 18
'''
file = open("employee.txt", "w")
file.write("101,Amit,IT,50000\n")
file.write("102,Priya,HR,60000\n")
file.write("103,Rahul,Sales,45000\n")
file.close()
file = open("employee.txt", "r")
total = 0
total_count = 0
highest = 0
highest_name = ""
print("All Employees:")
for line in file:
    empid, name, dept, salary = line.strip().split(",")
    salary = int(salary)
    print(empid, name, dept, salary)
    total += salary
    total_count += 1
    if salary > highest:
        highest = salary
        highest_name = name
print("Highest Paid Employee:", highest_name, highest)
print("Average Salary:", total / total_count)
file.seek(0)
limit = int(input("Enter salary limit: "))
print("Employees earning above", limit, ":")
for line in file:
    empid, name, dept, salary = line.strip().split(",")
    salary = int(salary)
    if salary > limit:
        print(name, salary)
file.close()
'''


# Program 19
'''
file = open("attendance.txt", "w")
file.write("Amit,80,100\n")
file.write("Priya,70,100\n")
file.write("Rahul,90,100\n")
file.close()
file = open("attendance.txt", "r")
for line in file:
    name, present, total = line.strip().split(",")
    present = int(present)
    total = int(total)
    percentage = (present / total) * 100
    print(name, "Attendance:", percentage, "%")
    if percentage < 75:
        print("Attendance below 75%")
file.close()
'''


# Program 20
'''
file = open("transactions.txt", "w")
file.write("deposit,5000\n")
file.write("withdraw,1000\n")
file.write("deposit,3000\n")
file.write("withdraw,500\n")
file.close()
file = open("transactions.txt", "r")
deposits = 0
withdrawals = 0
largest = 0
for line in file:
    typ, amount = line.strip().split(",")
    amount = int(amount)
    if typ == "deposit":
        deposits += amount
    else:
        withdrawals += amount
    if amount > largest:
        largest = amount
print("Total Deposits:", deposits)
print("Total Withdrawals:", withdrawals)
print("Final Balance:", deposits - withdrawals)
print("Largest Transaction:", largest)
file.close()
'''


# Program 21
'''
books = {}
while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        book_id = input("Enter Book ID: ")
        title = input("Enter Title: ")
        books[book_id] = [title, "Available"]
        print("Book added")
    elif choice == 2:
        book_id = input("Enter Book ID: ")
        if book_id in books:
            print("Book:", books[book_id])
        else:
            print("Book not found")
    elif choice == 3:
        book_id = input("Enter Book ID: ")
        if book_id in books:
            books[book_id][1] = "Issued"
            print("Book issued")
        else:
            print("Book not found")
    elif choice == 4:
        book_id = input("Enter Book ID: ")
        if book_id in books:
            books[book_id][1] = "Available"
            print("Book returned")
        else:
            print("Book not found")
    elif choice == 5:
        print("Available Books:")
        for book_id, details in books.items():
            if details[1] == "Available":
                print(book_id, details[0])
    elif choice == 6:
        print("Exit")
        break
'''


# Program 22
'''
file1=open("student.txt","r")
file2=open("newfile_03sep.py","r")
file3=open("file3.txt","w")
file3.write(file1.read())
file3.write(file2.read())
file1.close()
file2.close()
file3.close()
print("Files merged successfully")
'''



# Program 23
'''
file1 = open("student.txt", "r")
file2 = open("file3.txt", "r")
lines1 = file1.readlines()
lines2 = file2.readlines()
if lines1 == lines2:
    print("Files are identical")
else:
    print("Files are different")
    for i in range(min(len(lines1), len(lines2))):
        if lines1[i] != lines2[i]:
            print("First difference is at line:", i + 1)
            break
    if len(lines1) != len(lines2):
        print("The files have different numbers of line_list.")
file1.close()
file2.close()
'''







