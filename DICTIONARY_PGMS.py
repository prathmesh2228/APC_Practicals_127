
                            #DICTIONARY PGMS....

# Program1
student = {"roll_number": 128, "name": "Amit", "department": "CSE", "marks": 85}
print(student)

# Program2
employee = {"id": 128, "name": "Amit", "department": "CSE", "salary": 85000}
print(employee)


# Program3
products = {"laptop": 25000, "pen": 50, "textbook": 100, "mobile": 10000}
products.update({"keyboard": 1500})
print(products)


# Program4
marks = {"ak": 85, "rk": 90, "sk": 95}
print(marks)
marks.update({"sk": 99})
print(marks)


# Program5
cities = {"satara": 800, "pune": 1000, "karad": 1500, "sangli": 900}
removed = cities.pop("pune")
print(cities)


# Program6
employees = {101: "ak", 102: "rk", 103: "sk"}
emp_id = int(input("Enter employee ID: "))
print("Employee exists" if emp_id in employees else "Employee not found")


# Program7
records = {"ak": 85, "rk": 90, "sk": 95}
print(records)
print("Number of records:", len(records))


# Program8
marks = {"ak": 85, "rk": 90, "sk": 95}
print("Keys:", marks.keys())
print("Values:", marks.values())
print("Dictionary:", marks)


# Program9
languages = {"Python": "Guido van Rossum", "C": "Dennis Ritchie", "Java": "James Gosling"}
for language in languages:
    print(language, ":", languages[language])

    
# Program10
students = {}
for i in range(5):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[name] = marks
print(students)


# Program11
students = {"ak": 85, "rk": 78, "sk": 95, "pk": 88}
highest_name = max(students, key=students.get)
print("Highest:", highest_name, students[highest_name])


# Program12
students = {"ak": 85, "rk": 78, "sk": 95, "pk": 88}
lowest_name = min(students, key=students.get)
print("Lowest:", lowest_name, students[lowest_name])


# Program13
students = {"ak": 85, "rk": 78, "sk": 95, "pk": 88}
total = sum(students.values())
average = total / len(students)
print("Average:", round(average, 2))


# Program14
text = input("Enter a string: ")
freq = {}
for ch in text:
    freq[ch] = 1 + freq.get(ch, 0)
print(freq)


# Program15
sentence = input("Enter a sentence: ")
freq = {}
for word in sentence.split():
    freq[word] = freq.setdefault(word, 0) + 1
print(freq)


# Program16
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1.copy()
merged.update(dict2)
print(merged)


# Program17
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 5, "c": 6, "d": 7}
common_keys = set(dict1).intersection(dict2)
print("Common keys:", common_keys)


# Program18
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"x": 20, "y": 40, "z": 30}
common_values = set(dict1.values()).intersection(dict2.values())
print("Common values:", common_values)


# Program19
data = {"a": 10, "b": 20, "c": 10, "d": 30, "e": 20}
result = {}
seen_values = set()
for key, value in data.items():
    if value not in seen_values:
        result[key] = value
        seen_values.add(value)
print(result)


# Program20
data = {4: "m", 1: "e", 3: "x", 2: "a"}
for key in sorted(data.keys()):
    print(key, ":", data[key])


# Program21
squares = {}
for i in range(1, 11):
    squares[i] = i ** 2
print(squares)



# Program22
squares = {num: num ** 2 for num in range(2, 21, 2)}
print(squares)


# Program23
numbers = [1, 1, 1, 8, 5, 2, 2, 0, 2, 1, 3, 8]
frequency = {}
for number in numbers:
    frequency[number] = frequency.setdefault(number, 0) + 1
print(frequency)


# Program24
cubes = {}
for i in range(1, 11):
    cubes[i] = i ** 3
print(cubes)



# Program25
students = {"mk": 85,"jk": 78,"rm": 95,"jm": 88}
while True:
    print("\n1. Add Student")
    print("2. Update Marks")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Display All")
    print("6. Highest Marks")
    print("7. Average")
    print("8. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        name = input("Enter name: ")
        marks = float(input("Enter marks: "))
        students[name] = marks
    elif choice == 2:
        name = input("Enter name: ")
        if name in students:
            students[name] = float(input("Enter new marks: "))
        else:
            print("Student not found")
    elif choice == 3:
        name = input("Enter name: ")
        if name in students:
            del students[name]
        else:
            print("Student not found")
    elif choice == 4:
        name = input("Enter name: ")
        if name in students:
            print(name, ":", students[name])
        else:
            print("Student not found")
    elif choice == 5:
        print(students)
    elif choice == 6:
        name = max(students, key=students.get)
        print("Highest:", name, students[name])
    elif choice == 7:
        print("Average:", sum(students.values()) / len(students))
    elif choice == 8:
        break
    else:
        print("Invalid choice")


# Program26
employees = {"Amit": 65000, "Rohit": 48000, "Sneha": 72000, "Kiran": 55000}

salaries = employees.values()
print("Highest salary:", max(salaries))
print("Lowest salary:", min(salaries))
print("Average salary:", sum(salaries) / len(salaries))

print("Employees earning more than 50000:")
for name, salary in employees.items():
    if salary > 50000:
        print(name, salary)


# Program27
products = {"pen": 20,"book": 5,"bag": 15}
while True:
    print("\n1. Add Product")
    print("2. Update Quantity")
    print("3. Delete Product")
    print("4. Search Product")
    print("5. Products Below 10")
    print("6. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        name = input("Enter product: ")
        quantity = int(input("Enter quantity: "))
        products[name] = quantity
    elif choice == 2:
        name = input("Enter product: ")
        if name in products:
            products[name] = int(input("Enter new quantity: "))
        else:
            print("Product not found")
    elif choice == 3:
        name = input("Enter product: ")
        if name in products:
            del products[name]
        else:
            print("Product not found")
    elif choice == 4:
        name = input("Enter product: ")
        if name in products:
            print(name, ":", products[name])
        else:
            print("Product not found")
    elif choice == 5:
        for name, quantity in products.items():
            if quantity < 10:
                print(name, quantity)
    elif choice == 6:
        break
    else:
        print("Invalid choice")


# Program28
contacts = {
    "MK": "8390842054",
    "vk": "9371321748"
}

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts[name] = phone

    elif choice == 2:
        name = input("Enter name: ")
        if name in contacts:
            print(name, ":", contacts[name])
        else:
            print("Contact not found")

    elif choice == 3:
        name = input("Enter name: ")
        if name in contacts:
            contacts[name] = input("Enter new phone: ")
        else:
            print("Contact not found")

    elif choice == 4:
        name = input("Enter name: ")
        if name in contacts:
            del contacts[name]
        else:
            print("Contact not found")

    elif choice == 5:
        print(contacts)

    elif choice == 6:
        break

    else:
        print("Invalid choice")


# Program29
books = {101: "Python Programming",102: "Data Structures",103: "Computer Networks"}

while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Remove Book")
    print("4. Display All Books")
    print("5. Count Books")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        book_id = int(input("Enter book ID: "))
        name = input("Enter book name: ")
        books[book_id] = name

    elif choice == 2:
        book_id = int(input("Enter book ID: "))
        if book_id in books:
            print(books[book_id])
        else:
            print("Book not found")

    elif choice == 3:
        book_id = int(input("Enter book ID: "))
        if book_id in books:
            del books[book_id]
        else:
            print("Book not found")

    elif choice == 4:
        print(books)

    elif choice == 5:
        print("Total books:", len(books))

    elif choice == 6:
        break

    else:
        print("Invalid choice")


# Program30
students = {"mk": "CSE","Rm": "ECE","Ak": "CSE","Rj": "IT","Sn": "ECE"}

groups = {}

for name, department in students.items():
    if department not in groups:
        groups[department] = []
    groups[department].append(name)

print(groups)


# Program31
words = ["cat", "dog", "apple", "book", "banana", "sun"]
groups = {}

for word in words:
    length = len(word)
    if length not in groups:
        groups[length] = []
    groups[length].append(word)

print(groups)



# Program32
numbers = [2, 7, 11, 15]
target = 9
seen = {}

for num in numbers:
    complement = target - num
    if complement in seen:
        print("Numbers:", complement, num)
        break

# Program33
text = input("Enter a string: ")
frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

for ch in text:
    if frequency[ch] == 1:
        print("First non-repeating character:", ch)
        break



# Program34
text = input("Enter a string: ")
frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

for ch in text:
    if frequency[ch] > 1:
        print("First repeating character:", ch)
        break


# Program31
para = input("Enter a paragraph: ")
result = {}

for word in para.split():
    length = len(word)
    result[length] = result.get(length, 0) + 1

print(result)
