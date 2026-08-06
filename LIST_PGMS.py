                                                            #List programs..

#program 1
#Create a list of five fruits and display the list

fruits = ["Apple", "Dragon Fruit", "Mango", "Watermellon", "Grapes"]
print("Fruits:", fruits)


#program 2
#Display first, last and third element

n =[70, 20, 80, 40, 89]

print("First Element:", n[0])
print("Last Element:", n[-1])
print("Third Element:", n[2])


#program 3
#Replace third color

colors = ["Orange", "Blue", "Grey", "Yellow", "Black"]

colors[2] = "Pink"

print("Updated List:", colors)


#program 4
#Add elements in list

n = [10, 20, 30, 40]

n.append(50)
n.insert(0, 5)
n.insert(2, 15)

print("Updated List:", n)


#program 5
#Remove students

students = ["Bhim", "Rahul", "Priya", "Jay", "Rakesh"]

students.pop(0)
students.pop()
students.remove("Priya")

print("Remaining Students:", students)


#program 6
#Largest and smallest without max() and min()

n = [25, 18, 90, 45, 60]

largest = n[0]
smallest = n[0]

for i in n:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Largest:", largest)
print("Smallest:", smallest)


#program 7
#Accept 10 numbers and find sum and average

numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

total = sum(numbers)
average = total / 10

print("Sum:", total)
print("Average:", average)


#program 8
#Count even and odd numbers

numbers = []

for i in range(15):
    num = int(input("Enter number: "))
    numbers.append(num)

even = 0
odd = 0

for i in numbers:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)


#program 9
#Search city

cities = ["Kolhapur", "Pune", "Mumbai", "Thane", "Nashik"]

city = input("Enter city name: ")

if city in cities:
    print("City Found")
else:
    print("City Not Found")

    
#program 10
#Reverse list without reverse()

n = [10, 20, 30, 40, 50]

rev = []

for i in range(len(n)-1, -1, -1):
    rev.append(n[i])

print("Original:", n)
print("Reversed:", rev)

#program 11
#Display list using slicing

n = [10,20,30,40,50,60,70,80,90,100]

print("First 5 Elements:", n[:5])
print("Last 5 Elements:", n[-5:])
print("Middle 4 Elements:", n[3:7])
print("Alternate Elements:", n[::2])
print("Reverse List:", n[::-1])


#program 12
#Display elements at even index positions

n = [10,20,30,40,50,60,70,80]

print("Elements at Even Index:")

for i in range(0, len(n), 2):
    print(n[i])

    
#program 13
#Sort list

n = []

for i in range(10):
    num = int(input("Enter Number: "))
    n.append(num)

asc = n.copy()
asc.sort()

desc = n.copy()
desc.sort(reverse=True)

print("Ascending Order:", asc)
print("Descending Order:", desc)


#program 14
#Display unique elements

n = [10,20,10,30,20,40,50,40]

unique =[]

for i in n:
    if i not in unique:
        unique.append(i)

print("Unique Elements:", unique)


#program 15
#Second largest element

n = [10, 25, 45, 78, 65, 90, 80]

n.sort()

print("Second Largest Element:", n[-2])


#program 16
#Student Details

students = [
    ["Jay",101,85],
    ["Rahul",102,90],
    ["Priya",103,88]
]

print("Student Details")

for s in students:
    print("Name:", s[0])
    print("Roll No:", s[1])
    print("Marks:", s[2])
    print()

    
#program 17
#Matrix Addition

A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

B = [
    [9,8,7],
    [6,5,4],
    [3,2,1]
]

C =[]

for i in range(3):
    row = []
    for j in range(3):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("Result Matrix:")

for row in C:
    print(row)

    
#program 18
#Shopping Cart

cart = ["Milk","Bread","Rice"]

cart.append("Sugar")
cart.remove("Bread")

item = input("Enter item to search: ")

if item in cart:
    print("Item Found")
else:
    print("Item Not Found")

print("Shopping Cart:", cart)
print("Total Items:", len(cart))


#program 19
#Student Attendance

s = ["Ganesh","Rakesh","Daya","Reva"]

print("Total Students:", len(s))

name = input("Enter student name to search: ")

if name in s:
    print("Present")
else:
    print("Absent")

new = input("Enter new student name: ")
s.append(new)

absent = input("Enter absent student name to remove: ")

if absent in s:
    s.remove(absent)

print("Updated List:", s)


#program 20
#Book List

b = ["Python","Java","C","DBMS"]

newbook = input("Enter new book: ")
b.append(newbook)

search = input("Enter book to search: ")

if search in b:
    print("Book Found")
else:
    print("Book Not Found")

remove = input("Enter book to remove: ")

if remove in b:
    b.remove(remove)

print("Books Available:")

for book in b:
    print(book)

print("Total Books:", len(b))


#program 21
#Merge two lists

list1 = []

list2 = []

print("Enter 5 elements for List 1")
for i in range(5):
    num = int(input())
    list1.append(num)

print("Enter 5 elements for List 2")
for i in range(5):
    num = int(input())
    list2.append(num)

merged = list1 + list2

print("Merged List:", merged)


#program 22
#Common elements

list1 = [10,20,30,40,50]
list2 = [30,40,50,60,70]

common = []

for i in list1:
    if i in list2 and i not in common:
        common.append(i)

print("Common Elements:", common)


#program 23
#Frequency of each element

numbers = [10,20,10,30,20,10,40]

visited = []

for i in numbers:
    if i not in visited:
        count = 0
        for j in numbers:
            if i == j:
                count += 1
        print(i, "=", count)
        visited.append(i)

        
#program 24
#Rotate list

numbers = [10,20,30,40,50]

left = numbers[1:] + [numbers[0]]

right = [numbers[-1]] + numbers[:-1]

print("Original:", numbers)
print("Left Rotation:", left)
print("Right Rotation:", right)


#program 25
#Remove duplicates

numbers = [10,20,10,30,40,20,50,30]

unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)

print("Original List:", numbers)
print("List Without Duplicates:", unique)


#program 26
#Student Marks Analysis

marks = []

for i in range(20):
    m = int(input("Enter Marks: "))
    marks.append(m)

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

above = 0
below = 0

for i in marks:
    if i > average:
        above += 1
    elif i < average:
        below += 1

print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)
print("Above Average:", above)
print("Below Average:", below)


#program 27
#Employee Salary Analysis

salary = []

n = int(input("Enter Number of Employees: "))

for i in range(n):
    s = int(input("Enter Salary: "))
    salary.append(s)

highest = max(salary)
lowest = min(salary)
average = sum(salary) / len(salary)

above50000 = 0
below30000 = 0

for s in salary:
    if s > 50000:
        above50000 += 1
    if s < 30000:
        below30000 += 1

print("Highest Salary:", highest)
print("Lowest Salary:", lowest)
print("Average Salary:", average)
print("Employees Above ₹50000:", above50000)
print("Employees Below ₹30000:", below30000)


#program 28
#Batsman's Score Analysis

scores = []

for i in range(10):
    score = int(input("Enter Score: "))
    scores.append(score)

highest = max(scores)
lowest = min(scores)
total = sum(scores)
average = total / len(scores)

century = 0
halfcentury = 0

for s in scores:
    if s >= 100:
        century += 1
    elif s >= 50:
        halfcentury += 1

print("Highest Score:", highest)
print("Lowest Score:", lowest)
print("Total Runs:", total)
print("Average Runs:", average)
print("Centuries:", century)
print("Half Centuries:", halfcentury)

#program 29
#Temperature Analysis

temp = []

for i in range(30):
    t = float(input("Enter Temperature: "))
    temp.append(t)

highest = max(temp)
lowest = min(temp)
average = sum(temp) / len(temp)

above = 0
below = 0

for t in temp:
    if t > average:
        above += 1
    elif t < average:
        below += 1

print("Hottest Temperature:", highest)
print("Coldest Temperature:", lowest)
print("Average Temperature:", average)
print("Days Above Average:", above)
print("Days Below Average:", below)

#program 30
#Patient Management

patients = ["Amit", "Rahul", "Sneha"]
ages = [25, 30, 22]

name = input("Enter New Patient Name: ")
age = int(input("Enter Age: "))

patients.append(name)
ages.append(age)

search = input("Enter Patient Name to Search: ")

if search in patients:
    index = patients.index(search)
    print("Patient Found")
    print("Name:", patients[index])
    print("Age:", ages[index])
else:
    print("Patient Not Found")

delete = input("Enter Patient Name to Delete: ")

if delete in patients:
    index = patients.index(delete)
    patients.pop(index)
    ages.pop(index)

print("\nPatient Details")

for i in range(len(patients)):
    print(patients[i], "-", ages[i])

print("Total Patients:", len(patients))
