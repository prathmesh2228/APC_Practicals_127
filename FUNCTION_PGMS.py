                                #FUNCTION PGMS...
#Program 1
'''
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

n = int(input("Enter number: "))
print("Factorial =", factorial(n))
'''

#Program 2
'''
def EO(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

n = int(input("Enter number: "))
print(EO(n))
'''

#Program 3
'''
def f(n1,n2):
    if n1>n2:
        print(n1 ,"is greater number")
    else:
        print(n2 ,"is greater number")
n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
print(f(n1,n2))
'''

#Program 4
'''
def si(p, r, t):
    s = (p * r * t) / 100
    return s

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

print("Simple Interest =", si(p, r, t))
'''

#Program 5
'''
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

n = int(input("Enter number: "))

if is_prime(n):
    print("Prime")
else:
    print("Not Prime")

'''

#Program 6
'''
def circle_area(r):
    area = 3.14 * r * r
    return area

r = float(input("Enter radius: "))

print("Area of circle =", circle_area(r))
'''

#Program 7
'''
def natural_sum(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total

n = int(input("Enter n: "))

print("Sum =", natural_sum(n))
'''

#Program 8
'''
def power(base, exponent):
    result = 1

    for i in range(exponent):
        result = result * base

    return result

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

print("Power =", power(base, exponent))
'''

#Program 9
'''
def largest(numbers):
    big = numbers[0]

    for num in numbers:
        if num > big:
            big = num

    return big

numbers = list(map(int, input("Enter numbers: ").split()))

print("Largest =", largest(numbers))
'''

#Program 10
'''
def count_vowels(text):
    count = 0

    for ch in text:
        if ch in "aeiouAEIOU":
            count = count + 1

    return count

text = input("Enter string: ")

print("Number of vowels =", count_vowels(text))
'''

#Program 11
'''
def reverse_string(text):
    return text[::-1]

text = input("Enter string: ")
print("Reverse =", reverse_string(text))
'''

#Program 12
'''
def palindrome(value):
    value = str(value)

    if value == value[::-1]:
        return True
    else:
        return False

value = input("Enter string or number: ")

if palindrome(value):
    print("Palindrome")
else:
    print("Not Palindrome")
'''

#Program 13
'''
def average(numbers):
    total = 0

    for num in numbers:
        total = total + num

    return total / len(numbers)

numbers = list(map(int, input("Enter numbers: ").split()))

print("Average =", average(numbers))
'''

#Program 14
'''
def count_element(numbers, element):
    count = 0

    for num in numbers:
        if num == element:
            count = count + 1

    return count

numbers = list(map(int, input("Enter numbers: ").split()))
element = int(input("Enter element: "))

print("Occurrences =", count_element(numbers, element))
'''

#Program 15
'''
def unique_elements(numbers):
    result = []

    for num in numbers:
        if num not in result:
            result.append(num)

    return result

numbers = list(map(int, input("Enter numbers: ").split()))

print("Unique elements =", unique_elements(numbers))
'''

#Program 16
'''
def second_largest(numbers):
    largest = numbers[0]
    second = numbers[0]

    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second

numbers = list(map(int, input("Enter numbers: ").split()))

print("Second largest =", second_largest(numbers))
'''

#Program 17
'''
def fibonacci(n):
    a = 0
    b = 1
    result = []

    for i in range(n):
        result.append(a)
        a, b = b, a + b

    return result

n = int(input("Enter n: "))

print("Fibonacci =", fibonacci(n))
'''

#Program 18
'''
def calculate(m1, m2, m3, m4, m5):
    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5

    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "D"

    return percentage, grade

m1 = float(input("Enter marks 1: "))
m2 = float(input("Enter marks 2: "))
m3 = float(input("Enter marks 3: "))
m4 = float(input("Enter marks 4: "))
m5 = float(input("Enter marks 5: "))

percentage, grade = calculate(m1, m2, m3, m4, m5)

print("Percentage =", percentage)
print("Grade =", grade)
'''

#Program 19
'''
def electricity_bill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    else:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10

    return bill

units = int(input("Enter units consumed: "))

print("Electricity bill =", electricity_bill(units))
'''

#Program 20
'''
def gross_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10
    gross = basic + hra + da

    return gross

basic = float(input("Enter basic salary: "))

print("Gross salary =", gross_salary(basic))
'''

#Program 21
'''
def total_bill(price, quantity):
    total = price * quantity

    if total >= 1000:
        discount = total * 0.10
    else:
        discount = 0

    return total - discount

price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

print("Final bill =", total_bill(price, quantity))
'''

#Program 22
'''
def calculate(numbers):
    small = numbers[0]
    big = numbers[0]
    total = 0

    for num in numbers:
        if num < small:
            small = num
        if num > big:
            big = num
        total = total + num

    average = total / len(numbers)

    return small, big, total, average

numbers = list(map(int, input("Enter numbers: ").split()))

small, big, total, average = calculate(numbers)

print("Minimum =", small)
print("Maximum =", big)
print("Sum =", total)
print("Average =", average)
'''

#Program 23
'''
def student_result(name, roll, marks):
    total = sum(marks)
    percentage = total / 5

    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "D"

    return total, percentage, grade


students = []

for i in range(3):
    name = input("Enter name: ")
    roll = int(input("Enter roll number: "))

    marks = []
    for j in range(5):
        marks.append(float(input("Enter marks: ")))

    total, percentage, grade = student_result(name, roll, marks)

    students.append((name, roll, total, percentage, grade))

for student in students:
    print(student)

average = sum(s[3] for s in students) / len(students)

highest = max(students, key=lambda x: x[3])
lowest = min(students, key=lambda x: x[3])

print("Class Average =", average)
print("Highest Scorer =", highest[0])
print("Lowest Scorer =", lowest[0])
'''

#Program 24
'''
balance = 0
history = []


def deposit(amount):
    global balance
    balance = balance + amount
    history.append("Deposited " + str(amount))


def withdraw(amount):
    global balance

    if amount <= balance:
        balance = balance - amount
        history.append("Withdrawn " + str(amount))
    else:
        print("Insufficient balance")


def show_balance():
    print("Balance =", balance)


def show_history():
    print("Transaction History:")
    for item in history:
        print(item)


deposit(5000)
withdraw(1000)
show_balance()
show_history()
'''

#Program 25
'''
books = {
    101: ["Python", True],
    102: ["Java", True],
    103: ["Data Structures", True]
}


def add_book(book_id, name):
    books[book_id] = [name, True]


def issue_book(book_id):
    if book_id in books and books[book_id][1]:
        books[book_id][1] = False
        print("Book issued")
    else:
        print("Book not available")


def return_book(book_id):
    if book_id in books:
        books[book_id][1] = True
        print("Book returned")


def search_book(book_id):
    if book_id in books:
        print("Book:", books[book_id][0])
    else:
        print("Book not found")


def display_books():
    for book_id, book in books.items():
        if book[1]:
            print(book_id, book[0])


add_book(104, "Computer Networks")
issue_book(101)
return_book(101)
search_book(102)
display_books()
'''

#Program 26
'''
def electricity_bill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    else:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10

    fixed = 100
    bill = bill + fixed

    tax = bill * 0.05
    bill = bill + tax

    if bill > 2000:
        bill = bill - 100

    return bill


units = int(input("Enter units: "))

print("Final electricity bill =", electricity_bill(units))
'''

#Program 27
'''
def consultation():
    return 500


def laboratory():
    return 1000


def medicine():
    return 1500


def room():
    return 2000


def final_bill(category):
    total = consultation() + laboratory() + medicine() + room()

    if category == "senior":
        total = total - total * 0.10
    elif category == "child":
        total = total - total * 0.05

    return total


category = input("Enter patient category: ")

print("Final bill =", final_bill(category))
'''

#Program 28
'''
products = {}


def add_product(name, price, quantity):
    products[name] = [price, quantity]


def remove_product(name):
    if name in products:
        del products[name]


def subtotal():
    total = 0

    for price, quantity in products.values():
        total = total + price * quantity

    return total


def final_invoice():
    total = subtotal()

    coupon = 100 if total >= 1000 else 0
    gst = (total - coupon) * 0.18

    return total - coupon + gst


add_product("Bag", 800, 1)
add_product("Book", 300, 2)

print("Subtotal =", subtotal())
print("Final Invoice =", final_invoice())
'''

#Program 29
'''
def binary_search(numbers, low, high, key):
    if low > high:
        return -1

    mid = (low + high) // 2

    if numbers[mid] == key:
        return mid
    elif key < numbers[mid]:
        return binary_search(numbers, low, mid - 1, key)
    else:
        return binary_search(numbers, mid + 1, high, key)


numbers = [10, 20, 30, 40, 50]
key = int(input("Enter number to search: "))

result = binary_search(numbers, 0, len(numbers) - 1, key)

if result == -1:
    print("Not found")
else:
    print("Found at index", result)
'''

#Program 30
'''
def decimal_binary(n):
    if n == 0:
        return ""

    return decimal_binary(n // 2) + str(n % 2)


n = int(input("Enter decimal number: "))

if n == 0:
    print("Binary = 0")
else:
    print("Binary =", decimal_binary(n))
'''

#Program 31
'''
def palindrome(text):
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return palindrome(text[1:-1])


text = input("Enter a string: ")

if palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")
'''

#Program 32
'''
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def calculate(func, a, b):
    return func(a, b)


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition =", calculate(add, a, b))
print("Subtraction =", calculate(subtract, a, b))
print("Multiplication =", calculate(multiply, a, b))

if b != 0:
    print("Division =", calculate(divide, a, b))
else:
    print("Division not possible")
'''
