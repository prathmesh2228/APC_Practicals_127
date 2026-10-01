
                                                                            #PANDAS...

'''
import pandas as pd
print(pd.__version__)
'''

# Problem 1
'''
import pandas as pd

data = {
    "ID": [101, 102, 103, 104, 105],
    "Name": ["Jay", "Ganesh", "Sneha", "Arun", "Rohan"],
    "Python": [80, 70, 90, 60, 85],
    "DBMS": [75, 65, 88, 70, 80],
    "Maths": [85, 72, 92, 65, 78]
}

df = pd.DataFrame(data)

print(df)

df["Total"] = df["Python"] + df["DBMS"] + df["Maths"]
df["Average"] = df["Total"] / 3

print("\nTotal and Average:")
print(df)

print("\nStudents with average above 75:")
print(df[df["Average"] > 75])
'''

# Problem 2

'''
import pandas as pd

data = {
    "ID": [101, 102, 103, 104, 105],
    "Name": ["Raj", "Ajay", "Sneha", "Renu", "Ganesh"],
    "Department": ["IT", "HR", "Sales", "IT", "Finance"],
    "Salary": [60000, 45000, 55000, 70000, 50000],
    "Exp": [3, 5, 2, 7, 4]
}

df = pd.DataFrame(data)

print("Employees with salary greater than 50000:")
print(df[df["Salary"] > 50000])

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nHighest Salary:")
print(df["Salary"].max())

print("\nEmployee with highest experience:")
print(df[df["Exp"] == df["Exp"].max()])
'''

# Problem 3

'''
import pandas as pd

data = {
    "ID": [1, 2, 3, 4, 5],
    "Name": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Electronics"],
    "Price": [50000, 800, 1500, 12000, 15000],
    "Quantity": [2, 10, 5, 3, 2]
}

df = pd.DataFrame(data)

df["Total_Amount"] = df["Price"] * df["Quantity"]

print("DataFrame:")
print(df)

print("\nProduct with highest total sales:")
print(df[df["Total_Amount"] == df["Total_Amount"].max()])
'''

# Problem 4
'''
import pandas as pd

data = {
    "ID": [1, 2, 3, 4, 5],
    "Name": ["Jay", "Rahul", "Sahil", "Priya", "Ganesh"],
    "Age": [65, 45, 70, 55, 62],
    "Disease": ["Diabetes", "Fever", "Heart", "Cold", "Diabetes"],
    "Med_Charges": [60000, 20000, 80000, 30000, 55000]
}

df = pd.DataFrame(data)

print("Patients above 60:")
print(df[df["Age"] > 60])

print("\nAverage Medical Charge:")
print(df["Med_Charges"].mean())

print("\nMaximum Medical Charge:")
print(df["Med_Charges"].max())

print("\nPatients with charges greater than 50000:")
print(df[df["Med_Charges"] > 50000])
'''

# Problem 5

'''
import pandas as pd

data = {
    "ID": [1, 2, 3, 4, 5],
    "Customer": ["Jay", "Rahul", "Sahil", "Priya", "Ganesh"],
    "Product": ["Laptop", "Mobile", "Tablet", "Printer", "Monitor"],
    "Quantity": [2, 1, 3, 2, 1],
    "Price": [40000, 30000, 15000, 12000, 18000],
    "Discount": [2000, 1000, 1500, 500, 1000]
}

df = pd.DataFrame(data)

df["Final_Amount"] = df["Quantity"]*df["Price"]-df["Discount"]

print("All Orders:")
print(df)

print("\nOrders above 5000:")
print(df[df["Final_Amount"] > 5000])

print("\nHighest-value order:")
print(df.loc[df["Final_Amount"].idxmax()])

print("\nAverage Order Value:")
print(df["Final_Amount"].mean())
'''


# Problem 6

'''
import pandas as pd

data = {
    "ID": [101, 102, 103, 104, 105],
    "Name": ["Raj", "Ajay", "Sneha", "Renu", "Ganesh"],
    "Department": ["CSE", "CSE", "IT", "CSE", "MECH"],
    "Total_Classes": [100, 100, 100, 100, 100],
    "Attended": [80, 70, 90, 60, 75]
}

df = pd.DataFrame(data)

df["Attendance_Percentage"] = (
    df["Attended"] / df["Total_Classes"]
) * 100

print(df)

print("\nStudents with attendance below 75%:")
print(df[df["Attendance_Percentage"] < 75])

'''
# Problem 7

'''
import pandas as pd

data = {
    "ID": [1, 2, 3, 4, 5],
    "Name": ["Laptop", "Mobile", "Keyboard", "Monitor", "Printer"],
    "Category": ["Electronics", "Electronics", "Accessories", "Electronics", "Electronics"],
    "Price": [50000, 20000, 1500, 12000, 15000],
    "Quantity": [2, 3, 5, 2, 1]
}

df = pd.DataFrame(data)

df["Total_Sales"] = df["Price"] * df["Quantity"]

print("DataFrame:")
print(df)

print("\nProducts with sales greater than 10000:")
print(df[df["Total_Sales"] > 10000])

print("\nProduct with maximum sales:")
print(df[df["Total_Sales"] == df["Total_Sales"].max()])

print("\nAverage Sales:")
print(df["Total_Sales"].mean())
'''

# Problem 8
'''
import pandas as pd

marks = {
    "Bhim": 80,
    "Rahul": 65,
    "Sneha": 90,
    "Rakhi": 72,
    "Rohan": 85
}

s = pd.Series(marks)

print("Series:")
print(s)

print("\nMarks of Rohan:")
print(s["Rohan"])

print("\nMaximum Marks:")
print(s.max())

print("\nMinimum Marks:")
print(s.min())

print("\nAvg Marks:")
print(s.mean())

print("\nStudents scoring more than 75:")
print(s[s > 75])

'''

# Problem 9
'''
import pandas as pd

data={
    "Jay":60000,
    "Ram":70000,
    "Ganesh":36000,
    "Suyash":56000
    }

p=pd.Series(data)

print("Series:")
print(p)

print("\nHighest Salary:")
print(p.max())

print("\nMinimum Salary:")
print(p.min())

print("\navg Salary:")
print(p.mean())

print("\nHaving  Salary more than 50000:")
print(p[p>50000])
'''

# Problem 10
'''
import pandas as pd

products = {
    "Laptop": 50000,
    "Mobile": 20000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000
}

s = pd.Series(products)

print("Products and Prices:")
print(s)

s = s * 1.10

print("\nPrices after 10% increase:")
print(s)

print("\nMost expensive product:")
print(s.idxmax())

print("\nProducts costing more than 1000:")
print(s[s > 1000])
'''

# Problem 11

'''
import pandas as pd

data = {
    101: 65,
    102: 45,
    103: 72,
    104: 55,
    105: 68
}

s = pd.Series(data)

print("Average Age:")
print(s.mean())

print("\nOldest Patient:")
print(s.max())

print("\nYoungest Patient:")
print(s.min())

print("\nPatients above 60 years:")
print(s[s > 60])
'''

# Problem 12
'''
import pandas as pd

data = {
    "Amit": 80,
    "Rahul": 70,
    "Sneha": 95,
    "Priya": 65,
    "Rohan": 92
}

s = pd.Series(data)

print("Average Attendance:")
print(s.mean())

print("\nStudents below 75%:")
print(s[s < 75])

print("\nStudents above 90%:")
print(s[s > 90])

print("\nHighest Attendance:")
print(s.max())
'''

# Problem 13
'''
import pandas as pd

df = pd.read_csv("students.csv")

print("First 5 records:")
print(df.head())

print("\nLast 5 records:")
print(df.tail())

df["Total"] = df["Python"] + df["DBMS"] + df["Maths"]
df["Average"] = df["Total"] / 3

print("\nTotal and Average Marks:")
print(df)

print("\nStudents with average above 75:")
print(df[df["Average"] > 75])

print("\nStudent with highest average:")
print(df[df["Average"] == df["Average"].max()])

print("\nAverage marks of each subject:")
print(df[["Python", "DBMS", "Maths"]].mean())
'''

# Problem 14
'''
import pandas as pd

df = pd.read_csv("employees.csv")

print("Employees from CSE department:")
print(df[df["Department"] == "CSE"])

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nHighest Salary:")
print(df["Salary"].max())

print("\nLowest Salary:")
print(df["Salary"].min())

print("\nEmployees with salary greater than 50000:")
print(df[df["Salary"] > 50000])

print("\nDepartment-wise Average Salary:")
print(df.groupby("Department")["Salary"].mean())
'''

# Problem 15
'''
import pandas as pd

df = pd.read_csv("patients.csv")

print("Patients above 60 years:")
print(df[df["Age"] > 60])

print("\nAverage Medical Expense:")
print(df["Medical_Expense"].mean())

print("\nPatient with highest medical expense:")
print(df[df["Medical_Expense"] == df["Medical_Expense"].max()])

print("\nNumber of patients for each disease:")
print(df["Disease"].value_counts())

print("\nPatients with expense greater than 50000:")
print(df[df["Medical_Expense"] > 50000])
'''

# Problem 16
'''
import pandas as pd

df = pd.read_csv("weather.csv")

print("Maximum Temperature:")
print(df["Temperature"].max())

print("\nMinimum Temperature:")
print(df["Temperature"].min())

print("\nAverage Temperature:")
print(df["Temperature"].mean())

print("\nRecords with temperature above 35°C:")
print(df[df["Temperature"] > 35])

print("\nCity-wise Average Temperature:")
print(df.groupby("City")["Temperature"].mean())
'''
