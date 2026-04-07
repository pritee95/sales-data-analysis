import numpy as np

# Sales data
sales = np.array([4000, 6000, 4500, 8000, 9000, 7500])

# Months
months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun"])

# Best month
best_month_index = np.argmax(sales)
best_month = months[best_month_index]

# Average sales
average_sales = np.mean(sales)

# Percentage change month-to-month
pct_change = np.diff(sales) / sales[:-1] * 100

# Output
print(sales)
print("Best_month :", best_month)
print("Average sales :", average_sales)
print(pct_change)
