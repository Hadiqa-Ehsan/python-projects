import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Sample CSV file
filename = "hours_vs_scores.csv"
df = pd.read_csv(filename)

print(df)


# Features (Hours) aur Target (Scores)
X = df[['Hours']].values  # 2D array
y = df['Scores'].values   # 1D array

# Model create
model = LinearRegression()
# Model train karo
model.fit(X, y)

# Predict scores
predicted = model.predict(X)

# Display predictions
for i, score in enumerate(predicted):
    print(f"Hours: {X[i][0]}, Predicted Score: {score:.2f}")

# Original points
plt.scatter(X, y, color='blue', label='Original Data')

# Regression line
plt.plot(X, predicted, color='red', label='Regression Line')

plt.title("Hours vs Scores - Linear Regression")
plt.xlabel("Hours Studied")
plt.ylabel("Scores")
plt.legend()
plt.show()