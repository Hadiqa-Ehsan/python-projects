import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Sample dataset
data = {
    "Age": [25, 35, 45, 20, 30, 50],
    "Income": [30000, 50000, 80000, 20000, 40000, 90000],
    "Loan_Status": [0, 1, 1, 0, 1, 1]  # 0 = Not Eligible, 1 = Eligible
}

df = pd.DataFrame(data)

print(df)


# Features aur label separate karna
X = df[["Age", "Income"]]
y = df["Loan_Status"]

# Model create
model = LogisticRegression()

# Train model
model.fit(X, y)

print("Model trained successfully!")

# New user data
new_user = [[28, 45000]]  # Age = 28, Income = 45000

# Prediction
prediction = model.predict(new_user)

if prediction[0] == 1:
    print("Loan Approved ✅")
else:
    print("Loan Not Approved ❌")



# Same data par prediction
y_pred = model.predict(X)

# Accuracy calculate
accuracy = accuracy_score(y, y_pred)

print("Model Accuracy:", accuracy)