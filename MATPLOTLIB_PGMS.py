  vvv                                                    #MATPLOTLIB...

#DATASET OF MONTHLY SHOP SALES
import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = [45, 52, 48, 60, 65, 58, 72, 78, 70, 85, 92, 105]
expenses = [30, 34, 32, 38, 40, 37, 45, 48, 44, 52, 56, 62]
products_sold = [120, 140, 130, 160, 175, 155, 195, 210, 190, 230, 250, 280]
customers = [90, 105, 98, 120, 135, 115, 150, 165, 145, 180, 195, 220]
profit = [sales[i] - expenses[i] for i in range(len(months))]


# 1.LINE PLOT
'''
plt.plot(months, sales, marker="o")
plt.title("Monthly Shop Sales")
plt.xlabel("Month")
plt.ylabel("Sales (₹ thousands)")
plt.show()
'''

# 2.Vertical bar graph
'''
plt.bar(months, sales)
plt.title("Monthly Sales - Bar Graph")
plt.xlabel("Month")
plt.ylabel("Sales (₹ thousands)")
plt.show()
'''

# 3.Horizontal bar graph
'''
plt.barh(months, profit)
plt.title("Monthly profit - Horizontal Bar Graph")
plt.xlabel("Profit (₹ thousands)")
plt.ylabel("Month")
plt.show()
'''

# 4.Scatter plot: customers vs sales
'''
plt.scatter(customers, sales)
plt.title("Customers vs Sales")
plt.xlabel("Number of Customers")
plt.ylabel("Sales (₹ thousands)")
plt.show()
'''

# 5.Pie chart: sales share by quarter
'''
quarter_sales = [sum(sales[0:3]), sum(sales[3:6]), sum(sales[6:9]), sum(sales[9:12])]
plt.pie(quarter_sales, labels=["Q1", "Q2", "Q3", "Q4"], autopct="%1.1f%%")
plt.title("Sales Share by Quarter")
plt.show()
'''

# 6.Histogram: distribution of monthly sales
'''
plt.hist(sales, bins=5, edgecolor="black")
plt.title("Distribution of Monthly Sales")
plt.xlabel("Sales (₹ thousands)")
plt.ylabel("Number of Months")
plt.show()
'''

# 7. Box plot: sales and expenses
'''
plt.boxplot([sales, expenses], tick_labels=["Sales", "Expenses"])
plt.title("Sales and Expenses - Box Plot")
plt.ylabel("Amount (₹ thousands)")
plt.show()
'''

# 8.Stem plot: products sold
'''
plt.stem(months, products_sold)
plt.title("Products Sold by Month")
plt.xlabel("Month")
plt.ylabel("Products Sold")
plt.show()
'''

# 9.Step plot: customer counts
'''
plt.step(months, customers, where="mid")
plt.title("Monthly Customer Count")
plt.xlabel("Month")
plt.ylabel("Customers")
plt.show()
'''

# 10.Stack plot: expenses and profit (together equal sales)
'''
plt.stackplot(months, expenses, profit, labels=["Expenses", "Profit"])
plt.title("Monthly Sales Composition")
plt.xlabel("Month")
plt.ylabel("Amount (₹ thousands)")
plt.legend(loc="upper left")
plt.show()
'''

# 11.Area graph: monthly sales
'''
plt.fill_between(months, sales, alpha=0.5)
plt.plot(months, sales, marker="o")
plt.title("Monthly Sales - Area Graph")
plt.xlabel("Month")
plt.ylabel("Sales (₹ thousands)")
plt.show()
'''
