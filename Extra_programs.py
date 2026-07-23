#Program 1
#create a pgm to calculate area of triangle, volume of sphere, total surface area of cylinder, area of square

# Program to calculate the area of a triangle
'''
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

a= 0.5 * base * height

print("Area of Triangle:", a)
'''

# Program to calculate the area of a square
'''
side = float(input("Enter the side of the square: "))

a = side*side

print("Area of Square:", a)

'''
# Program to calculate the volume of a sphere

'''
pi = 3.14159

radius = float(input("Enter the radius of the sphere: "))

volume = (4/3) * pi * radius ** 3

print("Volume of Sphere:", volume)
'''

# Program to calculate the total surface area of a cylinder

'''
pi = 3.14159

radius = float(input("Enter the radius of the cylinder:"))
height = float(input("Enter the height of the cylinder:"))

tsa = 2 *pi*radius *(radius + height)

print("Total Surface Area of Cylinder =", tsa)
'''




#Program 2
#wap to convert pounds into kg,km into miles

'''
pound = float(input("Enter weight in pounds:"))
kg = pound * 0.453592
print("Weight in kg:", kg)

km = float(input("Enter distance in kilometers:"))
mile = km * 0.621371
print("Distance in miles:", mile)

'''



#program 3
#wap to calculate factorial number

'''
n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact = fact*i

print("Factorial:",fact)
'''




#program 4
#write a pgm to check wheather the no. is prime or not

'''
n = int(input("Enter a number: "))

if n <= 1:
    print(n,"is not a Prime Number")
else:
    for i in range(2,n):
        if n % i == 0:
            print(n, "is not a Prime Number")
            break
    else:
        print(n, "is a Prime Number")

'''



#program 5
#wap to check number is pallindrome or not
'''
num = int(input("Enter a number: "))
temp = num
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

if num == rev:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

'''



#program 6
#wap to convert decimal to binary,decimal to octal,to hexadecimal
'''
n = int(input("Enter a decimal number:"))

print("Binary:", bin(n))
print("Octal:", oct(n))
print("Hexadecimal:", hex(n))

'''



#program 7
#write a pgm to calculate factors of the number

'''
n = int(input("Enter a number:"))
print("Factors are:")

for i in range(1, n + 1):
    if n % i == 0:
        print(i)
'''




#Program 8
#write a pgm to find Ascii value of a character

'''
ch= input("Enter a character:")

ascii_val = ord(ch)

print("ASCII value of", ch, "is", ascii_val)


'''

