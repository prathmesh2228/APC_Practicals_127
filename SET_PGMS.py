                                                                #SET PROBLEMS...

#1
'''
s={23,67,44,11,88}
print(s)
'''


#2.
'''
l=[10,11,12,11,10,45,35,56,20,10]
s=set(l)
print(s)
'''

#3.
'''
s={"apple","Mango","Banana","DragonFruit","Orange"}
s.add("Greps")
s.add("Watermelon")
print(s)
'''

#4.
'''
s={23,67,44,11,88}
s.remove(11)
print(s)
'''

#5.
'''
s={"raj","sham","ganesh","bhim","raju"}
name=input("Enter the student name:").lower()

if name in s:
    print(name ,"is present")
else:
    print("Name not found")
'''

#6.
'''
city={"pune","Kolhapur","Sangli","Satara","Thane"}
print("Toatl no. of cities=",len(city))

'''

#7.
'''
l={"python",'c','c++','react','java'}
for i in l:
    print(i)
'''

#8.
'''
l=[10,11,12,11,10,45,35,56,20,10]
s=set()
for i in l:
    s.add(i)
print(s)
'''

#9.
'''
a={12,45,12,13,14,76,13}
b={36,45,78,23,11,12,89}
print(a.union(b))
'''

#10.
'''
a={12,45,12,13,14,76,13}
b={36,45,78,23,11,12,89}
print(a.intersection(b))
'''

#11.
'''
a={12,45,12,13,14,76,13}
b={36,45,78,23,11,12,89}
print(a.difference(b))
print(b.difference(a))
'''

#12.
'''
a={12,45,12,13,14,76,13}
b={36,45,78,23,11,12,89}
print(a.symmetric_difference(b))
'''

#13.
'''
a={12,45,44,78,23,36,89,90}
b={36,45,78}
print(b.issubset(a))
'''

#14.
'''
a = {10, 20, 30, 40, 50}
b = {20, 30, 40}

print(a.issuperset(b))
'''

#15.
'''
a = {10, 20, 30, 40}
b = {50, 60, 70, 80}

if a.isdisjoint(b):
    print("Sets have no elements in common")
else:
    print("Sets have elements in common")
'''


#16.
'''
a = {10, 20, 30, 40}
b = {40, 30, 20, 10}

if a==b:
    print("Both sets are equal")
else:
    print("Both sets are not equal")
'''

#17.
'''
s1 = {"Python", "Java", "DBMS", "AI"}
s2 = {"Java", "AI", "Cloud", "Web Development"}

common = s1.intersection(s2)

print("Subjects studied by both:", common)
'''

#18.
'''
sen = input("Enter a sentence: ")

w = set(sen.split())

print("Unique words:", w)
'''

#19.
'''
morning = {"Amit", "Jay", "Sneha", "Priya", "Ram"}
afternoon = {"Jay", "Priya", "Neha", "Ram", "Kiran"}

print("Both sessions:", morning.intersection(afternoon))
print("Only morning:", morning.difference(afternoon))
print("Only afternoon:", afternoon.difference(morning))
print("At least one session:", morning.union(afternoon))
'''

#20.
'''
py = {"Amit", "Rahul", "Sneha", "Priya"}
java = {"Rahul", "Priya", "Rohan", "Kiran"}

print("Python students:", py)
print("Java students:", java)
'''

#21.
'''
py = {"Amit", "Rahul", "Sneha", "Priya"}
java = {"Rahul", "Priya", "Rohan", "Kiran"}

both = py.intersection(java)
only_one = py.symmetric_difference(java)

print("Students in both courses:", both)
'''

#22.
'''
e1 = {"Python", "Java", "SQL", "Git"}
e2 = {"Python", "SQL", "HTML", "Docker"}

print("Common skills:", e1.intersection(e2))
print("Skills unique to Employee 1:", e1.difference(e2))
print("Skills unique to Employee 2:", e2.difference(e1))
print("All available skills:", e1.union(e2))
'''

#23.
'''
day1 = {101, 102, 103, 104, 105}
day2 = {103, 104, 105, 106, 107}

print("Unique visitors:", day1.union(day2))
print("Returning visitors:", day1.intersection(day2))
print("Only first day:", day1.difference(day2))
print("Only second day:", day2.difference(day1))
'''
#24.
'''
elec = {"Laptop", "Mobile", "Tablet", "Watch"}
gadgets = {"Mobile", "Watch", "Camera", "Laptop"}

common = elec.intersection(gadgets)

print("Products in both categories:", common)
'''

#25.
'''
user1 = {"Amit", "Rahul", "Sneha", "Priya", "Rohan"}
user2 = {"Rahul", "Priya", "Kiran", "Neha", "Rohan"}

print("Mutual friends:", user1.intersection(user2))
print("Friends unique to User 1:", user1.difference(user2))
print("Friends unique to User 2:", user2.difference(user1))
print("Total unique friends:", user1.union(user2))
'''
