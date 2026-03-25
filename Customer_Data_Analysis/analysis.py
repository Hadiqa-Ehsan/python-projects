import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample customer dataset
data = {
    "Customer_ID": [101, 102, 103, 104, 105, 106],
    "Age": [25, 35, 45, 23, 33, 52],
    "Income": [30000, 50000, 80000, 25000, 40000, 90000],
    "Spending_Score": [60, 50, 90, 40, 70, 95]  # 0-100
}

df = pd.DataFrame(data)

print(df)

# ---------------- Step 3: Basic Stats ----------------

# Average (Mean) Age, Income, Spending_Score
print("\nAverage Age:", df["Age"].mean())
print("Average Income:", df["Income"].mean())
print("Average Spending Score:", df["Spending_Score"].mean())

# Median
print("\nMedian Age:", df["Age"].median())
print("Median Income:", df["Income"].median())
print("Median Spending Score:", df["Spending_Score"].median())

# Maximum & Minimum
print("\nMaximum Income:", df["Income"].max())
print("Minimum Income:", df["Income"].min())
print("Maximum Spending Score:", df["Spending_Score"].max())
print("Minimum Spending Score:", df["Spending_Score"].min())

# ---------------- Step 4: Visualization ----------------

# 1️⃣ Age Distribution
plt.figure(figsize=(6,4))
sns.histplot(df["Age"], bins=5, kde=True, color="skyblue")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.show()

# 2️⃣ Income vs Spending Score
plt.figure(figsize=(6,4))
sns.scatterplot(x="Income", y="Spending_Score", data=df, s=100, color="green")
plt.title("Income vs Spending Score")
plt.xlabel("Income")
plt.ylabel("Spending Score")
plt.show()

# 3️⃣ Spending Score by Age (Bar Plot)
plt.figure(figsize=(6,4))
sns.barplot(x="Customer_ID", y="Spending_Score", data=df, palette="viridis")
plt.title("Spending Score per Customer")
plt.xlabel("Customer ID")
plt.ylabel("Spending Score")
plt.show()

# ---------------- Step 5: Insights ----------------

print("\n----- Insights from Customer Data -----")

# 1️⃣ Average values
avg_age = df["Age"].mean()
avg_income = df["Income"].mean()
avg_spending = df["Spending_Score"].mean()
print(f"Average Age: {avg_age:.1f}")
print(f"Average Income: ${avg_income:.0f}")
print(f"Average Spending Score: {avg_spending:.1f}")

# 2️⃣ Highest spender
max_spender = df.loc[df["Spending_Score"].idxmax()]
print(f"\nHighest Spender: Customer {max_spender['Customer_ID']} with Spending Score {max_spender['Spending_Score']}")

# 3️⃣ Customer with highest income
richest = df.loc[df["Income"].idxmax()]
print(f"Highest Income: Customer {richest['Customer_ID']} with Income ${richest['Income']}")

# 4️⃣ Pattern observation
print("\nPattern Observations:")
print("- Young customers (20s) tend to have moderate spending.")
print("- Older customers (50s) may have higher spending score.")
print("- High income often correlates with higher spending score, but not always.")