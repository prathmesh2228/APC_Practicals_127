                                                        #STRING PROBLEMS...
#pgm 1
'''
s = input("Enter string: ")

count = 0
for i in s:
    count = count + 1

print("Length =", count)
'''

#pgm 2
'''
s = input("Enter string: ")

v = c = d = sp = sc = 0

for i in s:
    if i in "aeiouAEIOU":
        v += 1
    elif i.isalpha():
        c += 1
    elif i.isdigit():
        d += 1
    elif i == " ":
        sp += 1
    else:
        sc += 1

print("Vowels =", v)
print("Consonants =", c)
print("Digits =", d)
print("Spaces =", sp)
print("Special Characters =", sc)
'''

#pgm 3
'''
s = input("Enter string: ")

rev = ""

for i in s:
    rev = i + rev

print("Reverse =", rev)
'''

#pgm 4
'''
s = input("Enter string: ")

rev = ""

for i in s:
    rev = i + rev

if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
'''

#pgm 5
'''
s = input("Enter string: ")

u = l = 0

for i in s:
    if i.isupper():
        u += 1
    elif i.islower():
        l += 1

print("Uppercase =", u)
print("Lowercase =", l)
'''

#pgm 6
'''
s = input("Enter string: ")
a = input("Character to replace: ")
b = input("New character: ")

print(s.replace(a, b))
'''

#pgm 7
'''
s = input("Enter string: ")

print(s.replace(" ", ""))
'''

#pgm 8
'''
s = input("Enter string: ")
ch = input("Enter character: ")

count = 0

for i in s:
    if i == ch:
        count += 1

print("Frequency =", count)
'''

#pgm 9
'''
s = input("Enter string: ")

print("First =", s[0])
print("Last =", s[-1])
'''

#pgm 10
'''
s = input("Enter string: ")

for i in s:
    print(i, "=", ord(i))
'''

#pgm 11
'''
s = input("Enter sentence: ")

words = s.split()

print("Word Count =", len(words))
'''

#pgm 12
'''
s = input("Enter sentence: ")

words = s.split()

longest = words[0]

for i in words:
    if len(i) > len(longest):
        longest = i

print("Longest Word =", longest)
'''

#pgm 13
'''
s = input("Enter sentence: ")

words = s.split()

shortest = words[0]

for i in words:
    if len(i) < len(shortest):
        shortest = i

print("Shortest Word =", shortest)
'''
#pgm 14
'''
s = input("Enter sentence: ")

print(s.title())

'''

#pgm 15
'''
s = input("Enter string: ")

for i in s:
    if s.count(i) > 1:
        print(i, end=" ")
'''
#pgm 16

'''
s = input("Enter string: ")

for i in set(s):
    print(i, "=", s.count(i))
'''

#pgm 17
'''
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")
'''

#pgm 18
'''
s = input("Enter string: ")

r = ""

for i in s:
    if i not in r:
        r = r + i

print(r)
'''

#pgm 19
'''
s = input("Enter main string: ")
sub = input("Enter substring: ")

if sub in s:
    print("Found")
else:
    print("Not Found")
'''

#pgm 20
'''
s = input("Enter sentence: ")
w = input("Enter word: ")

words = s.split()

print("Occurrences =", words.count(w))
'''

#pgm 21
'''
p = input("Enter password: ")

u = l = d = s = 0

for i in p:
    if i.isupper():
        u = 1
    elif i.islower():
        l = 1
    elif i.isdigit():
        d = 1
    else:
        s = 1

if len(p) >= 8 and u and l and d and s:
    print("Valid Password")
else:
    print("Invalid Password")
'''

#pgm 22
'''
s = input("Enter string: ")

count = 1

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
    else:
        print(s[i] + str(count), end="")
        count = 1

print(s[-1] + str(count))
'''

#pgm 23
'''
s = input("Enter string: ")

r = ""
count = 1

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
    else:
        r = r + s[i] + str(count)
        count = 1

r = r + s[-1] + str(count)

if len(r) < len(s):
    print(r)
else:
    print(s)
'''

#pgm 24
'''
s = input("Enter string: ")

m = ""
c = 0

for i in s:
    if s.count(i) > c:
        c = s.count(i)
        m = i

print("Most Frequent =", m)
'''

#pgm 25
'''
s = input("Enter string: ")

f = {}

for i in s:
    f[i] = s.count(i)

a = sorted(f.items(), key=lambda x: x[1], reverse=True)

print("Second Most Frequent =", a[1][0])
'''

#pgm 26
'''
s = input("Enter message: ")
k = int(input("Enter key: "))

e = ""

for i in s:
    if i.isalpha():
        e = e + chr(ord(i) + k)
    else:
        e = e + i

print("Encrypted =", e)
'''

#pgm 27
'''
e = input("Enter email: ")

if "@" in e and "." in e:
    print("Valid Email")
else:
    print("Invalid Email")
'''

#pgm 28
'''
s = input("Enter sentence: ")

w = s.split()

for i in set(w):
    print(i, "=", w.count(i))
'''

#pgm 29
'''
s = input("Enter sentence: ")

w = s.split()

for i in range(len(w)-1, -1, -1):
    print(w[i], end=" ")
'''

#pgm 30
'''
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) == len(s2) and s2 in (s1 + s1):
    print("Yes")
else:
    print("No")
'''
