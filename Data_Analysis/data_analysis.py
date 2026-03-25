import pandas as pd
import matplotlib.pyplot as plt


filename = "sales_data.csv"
df = pd.read_csv(filename)

print(df)
# Total sales
total_sales = df['Sales'].sum()
print("Total Sales:", total_sales)

# Average sales
average_sales = df['Sales'].mean()
print("Average Sales:", average_sales)

# Maximum sales
max_sales = df['Sales'].max()
print("Maximum Sales:", max_sales)


# Line plot
plt.plot(df['Month'], df['Sales'], marker='o')
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
# Bar Chart
plt.bar(df['Month'], df['Sales'], color='skyblue')
plt.title("Monthly Sales - Bar Chart")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# Histogram
plt.hist(df['Sales'], bins=3, color='orange', edgecolor='black')
plt.title("Sales Distribution - Histogram")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()