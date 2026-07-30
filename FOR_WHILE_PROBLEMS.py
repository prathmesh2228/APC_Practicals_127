                                                                    #FOR-PROBLEMS...
#pgm 1
#Write a PYTHON program to print the natural numbers up to n
'''
n=int(input("Enter the No.:"))
for i in range(0,n+1):
    print(i)
'''

#pgm 2
#Write a PYTHON program to print even numbers up to n
'''
n=int(input("Enter the No.:"))
for i in range(0,n+1):
    if(i%2==0):
        print(i)
'''

#pgm 3
#Write a PYTHON program to print odd numbers up to n

'''
n=int(input("Enter the No.:"))
for i in range(0,n+1):
    if(i%2!=0):
        print(i)
'''
#pgm 4
#Write a PYTHON program that prints  1 2 4 8 16 32 … n2

'''
n=int(input("Enter the No.:"))
z=1
for i in range(1,n+1):
    print(z)
    z*=2
'''

#pgm 5
#Write a PYTHON program to sum the given sequence 1 + 1/ 1! + 1/ 2! + 1/3! + ….  + 1/n!

'''
n =int(input("Enter no.: "))

sum = 1
fact = 1

for i in range(1, n + 1):
    fact = fact * i
    sum = sum + (1 / fact)

print("Sum =", sum)
'''

#pgm 6
#Write a PYTHON program to compute the cosine series cos(x) = 1 – x2 / 2! + x4 / 4! – x6 / 6! + … xn / n!

'''
x = float(input("Enter x: "))
n = int(input("Enter n: "))

sum = 1
fact = 1
sign = -1

for i in range(2, n + 1, 2):
    fact = 1
    for j in range(1, i + 1):
        fact = fact * j

    sum = sum + sign * (x ** i) / fact
    sign = sign * -1

print("cos(x) =", sum)
'''

#pgm 7
#Write a short PYTHON program to check weather the square root of number is prime or  not.
'''
n = int(input("Enter a number: "))

r = int(n ** 0.5)

c = 0
for i in range(1, r + 1):
    if r % i == 0:
        c = c + 1

if c == 2:
    print("Square root is Prime")
else:
    print("Square root is Not Prime")

'''


#pgm 8
#Write a PYTHON program to produce following design
			#A B C 
			#A B C 
			#A B C 
'''
for i in range(3):
    print("   A B C")
'''


#pgm 9
'''Write a PYTHON program to produce following design
      A
      A B
      A B C
      A B C D 
      A B C D E
      If user enters n value as 5'''

'''
n =int(input("Enter a number: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(chr(64 + j), end=" ")
    print()

'''

#pgm 10
'''
Write a PYTHON program to produce following design
       A B C D E
       A B C D
       A B C
       A B
       A                      
      (If user enters n value as 5) '''

'''
n =int(input("Enter a number: "))
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(chr(64 + j), end=" ")
    print()
'''

#pgm 11
#Write a PYTHON program to produce following  
'''
      design
      1
      1 2
      1 2 3
      1 2 3 4
      1 2 3 4 5
      If user enters n value as 5

'''

'''
n =int(input("Enter a number: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

'''

#pgm 12
#Write a PYTHON program to produce following design
'''   1
      2 2
      3 3 3
      4 4 4 4 
      5 5 5 5 5
      If user enters n value as 5'''

'''
n =int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()
'''
                                                                    #WHILE PROGRAMS...

#   BELOW AVERAGE...
#pgm 1
'''
n = int(input("Enter num: "))

i = 1
while i <= n:
    print(i)
    i = i + 1

'''
#pgm 2
'''
n = int(input("Enter num: "))

i = 2
while i <= n:
    print(i)
    i = i + 2

'''
#pgm 3
'''
n = int(input("Enter num: "))

i = 1
while i <= n:
    print(i)
    i = i + 2
'''

#pgm 4
'''
n = int(input("Enter num: "))

i = 1
sum = 0

while i <= n:
    sum = sum + i
    i = i + 1

print("Sum =", sum)
'''

#   AVERAGE...
#pgm 1
'''
n = int(input("Enter num: "))

i = 1
sum = 0

while i <= n:
    sum = sum + i
    i = i + 2

print(sum)
'''

#pgm 2
'''
n = int(input("Enter num: "))

i = 2
sum = 0

while i <= n:
    sum = sum + i
    i = i + 2

print(sum)

'''

#pgm 3
'''
n = int(input("Enter num: "))

while n >= 1:
    print(n)
    n = n - 1

'''
#pgm 4
'''
n = int(input("Enter num: "))

a = 0
b = 1
i = 1

while i <= n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    i = i + 1
'''
#pgm 5
'''
n = int(input("Enter number: "))

fact = 1

while n > 0:
    fact = fact * n
    n = n - 1

print(fact)

'''

#   ABOVE AVERAGE...
#pgm 1
'''
n = int(input("Enter number: "))

i = 2
prime = True

while i < n:
    if n % i == 0:
        prime = False
        break
    i = i + 1

if prime and n > 1:
    print("Prime Number..")
else:
    print("Not Prime")
'''

#pgm 2

'''
n = int(input("Enter number: "))

sum = 0

while n > 0:
    sum = sum + (n % 10)
    n = n // 10

print(sum)
'''

#pgm 3
'''
n = int(input("Enter number: "))

temp = n
rev = 0

while n > 0:
    rev = rev * 10 + (n % 10)
    n = n // 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
'''

#pgm 4
'''
n = int(input("Enter number: "))

rev = 0

while n > 0:
    rev = rev * 10 + (n % 10)
    n = n // 10

print(rev)
'''

#pgm 5
'''
n = int(input("Enter number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)

     '''
 
#pgm 6
'''
n = int(input("Enter how many numbers: "))

large = int(input("Enter number: "))

for i in range(1, n):
    x = int(input("Enter number: "))
    if x > large:
        large = x

print("Largest =", large)

'''
#pgm 7
'''

n = int(input("Enter how many numbers: "))

small = int(input("Enter number: "))

for i in range(1, n):
    x = int(input("Enter number: "))
    if x < small:
        small = x

print("Smallest =", small)

'''
