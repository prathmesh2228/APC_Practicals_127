                                                   #Tuple Programs...
# 1.
'''
t=(2,5,3,8,9)
print(t)
'''

#2.
'''
t=("Pune","Kolhapur","Sangli","Satara","Thane")
print("First City",t[0])
print("Third City",t[2])
print("Last City",t[-1])
'''


#3.
"""
s=("Sham","Ram","Bhim","Ganesh","Raju","Divya")
print("Total no. of students:",len(s))
"""


#4.
'''
c=("Red","Blue","Pink","Green","Purple")
if "Yellow" in c:
    print("Color is present")
else:
    print("Color is not present")
'''


#5.
'''
f=("Mango","Orange","Apple","Greps")
for i in f:
    print(i)
'''

#6.
'''
t=(2,5,6,3,3,5,1,5)
c=t.count(5)
print("Count of no. 5:",c)
'''

#7.
'''
id=(101,102,103,104,105)
print("index of id 102:",id.index(102))
'''

#8.
'''
t1=(1,2,3)
t2=(4,5,7)
print(t1+t2)
'''

#9.
'''
t1=(1,2,3)
print(t1*4)
'''

#10.
'''
n=(2,6,5,3,11,43,23,9,54,89)
print("First Five elements:",n[:5])
print("last five elements:",n[5:10])
print("middle Four elements:",n[3:7])
print("Alternative elements:",n[0:10:2])
print("Reverse elements:",n[::-1])
'''


#11.
'''
t=(12,20,34,55)
l=list(t)
l.append(66)
print(l)
'''

#12.
'''

l=[]
for j in range(5):
    i=input("Enter 5 elements:")
    l.append(i)
print(l)
t=tuple(l)
print(t)
'''

#13.
'''
t=(12,20,34,55)
list1=list(t)
print(type(list1))
tuple1 =tuple(list1)
print(type(tuple1))

'''

#14.
'''
t=(12,20,34,55)
print(t)
del t
print("tuple is deleted!")
'''

#15
'''
stu=((10,"jay","cse"),
    (11,"gita","ai"),
    (12,"Sham","civil"),
    (13,"raju","ds"),
    (14,"ajay","cse")
)
for j in stu:
    print("Id:",j[0])
    print("Name:",j[1])
    print("Department:",j[2])
'''

#16.
'''
n=(1,2,3,4,5,6,7,8,9,10)
sum=0
for i in n:
    sum+=i
print("Sum:",sum)
'''

#17.
'''
n=(2,6,5,3,11,43,23,9,54,89)
s=n[0]
l=n[0]

for i in n:
    if i>l:
        l=i
    if i<s:
        s=i
print("smallest",s)
print("largest",l)
'''

#18.
'''
n=(1,2,3,4,5,6,7,8,9,10)
sum=0
for i in n:
    sum+=i
print("Average of tuple is:"sum/len(n))
'''

#19.
'''
n=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
e=0
od=0
for i in n:
    if i%2==0:
        e+=1
    else:
        od+=1
print("Count of even:",e)
print("Count of odd:",od)
'''

#20.
'''
n=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
num=int(input("Enter the number to be check whether it is in the tuple: "))
if num in n:
    print("Present")
else:
    print("Not present")
'''

#21.
'''
roll=int(input("Enter the roll no.:"))
name=input("Enter the name:")
dep=input("Enter the dept:")
mark=int(input("Enter the marks:"))
stu=(roll,name,dep,mark)
for j in stu:
    print(j)
'''

#22.
'''
employees = (
    (101, "Rahul", 25000),
    (102, "Amit", 30000),
    (103, "Sneha", 28000)
)

for emp in employees:
    print("Employee ID:", emp[0])
    print("Name:", emp[1])
    print("Salary:", emp[2])
    print()
'''

#23.
'''
prices = (100, 250, 150, 500, 200)

total = 0

for price in prices:
    total = total + price

average = total / len(prices)

highest = prices[0]
lowest = prices[0]

for price in prices:
    if price > highest:
        highest = price

    if price < lowest:
        lowest = price

print("Total Bill:", total)
print("Average Price:", average)
print("Highest Price:", highest)
print("Lowest Price:", lowest)
'''

#24.
'''
temperature = (32, 35, 31, 38, 36, 34, 30)

total = 0
maximum = temperature[0]
minimum = temperature[0]

for temp in temperature:
    total = total + temp

    if temp > maximum:
        maximum = temp

    if temp < minimum:
        minimum = temp

average = total / len(temperature)

print("Maximum Temperature:", maximum)
print("Minimum Temperature:", minimum)
print("Average Temperature:", average)
'''

#25.
'''
runs = (45, 78, 23, 90, 56, 34, 100, 67, 12, 81)

total = 0
highest = runs[0]
lowest = runs[0]

for run in runs:
    total = total + run

    if run > highest:
        highest = run

    if run < lowest:
        lowest = run

average = total / len(runs)

print("Total Runs:", total)
print("Highest Score:", highest)
print("Lowest Score:", lowest)
print("Average Score:", average)
'''

#26.
"""
tuple1 = (10, 20, 30, 40, 50)
tuple2 = (30, 40, 50, 60, 70)

common = ()

for x in tuple1:
    if x in tuple2:
        common = common + (x,)

print("Common Elements:", common)
"""

#27.
"""
tuple1 = (10, 20, 30, 40)
tuple2 = (30, 40, 50, 60)

merged = tuple1 + tuple2

result = ()

for x in merged:
    if x not in result:
        result = result + (x,)

print("Merged Tuple:", result)
"""

#28.
"""
numbers = (10, 20, 10, 30, 20, 10, 40)

for x in numbers:

    if x not in numbers[:numbers.index(x)]:
        count = 0

        for y in numbers:
            if x == y:
                count = count + 1

        print(x, "=", count)

"""

#29.
'''
numbers = (50, 20, 80, 10, 40, 30)

ascending = tuple(sorted(numbers))
descending = tuple(sorted(numbers, reverse=True))

print("Ascending:", ascending)
print("Descending:", descending)
'''

#30.
'''
patients = (
    (101, "Jay", 25, "A+"),
    (102, "Bhim", 30, "B+"),
    (103, "Amit", 22, "O+"),
    (104, "Priya", 28, "A+")
)


print("All Patient Records:")

for patient in patients:
    print(patient)


search_id = int(input("\nEnter Patient ID: "))

found = False

for patient in patients:
    if patient[0] == search_id:
        print("Patient Found:", patient)
        found = True

if found == False:
    print("Patient Not Found")


print("\nTotal Patients:", len(patients))


blood = input("\nEnter Blood Group: ")

print("Patients with", blood, ":")

for patient in patients:
    if patient[3] == blood:
        print(patient)
'''s
