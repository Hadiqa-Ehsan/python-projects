# Sample dataset for students
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

data = {
    "Hours_Studied": [5, 2, 8, 3, 4, 6],
    "Attendance": [80, 60, 90, 50, 70, 85],
    "Pass_Fail": ["Pass", "Fail", "Pass", "Fail", "Pass", "Pass"]
}

df = pd.DataFrame(data)

print(df)

# Features (X) aur label (y) separate karna
X = df[["Hours_Studied", "Attendance"]]
y = df["Pass_Fail"]

# Model create karna
model = DecisionTreeClassifier()

# Model train karna
model.fit(X, y)

print("Model trained successfully!")

# New student data
new_student = [[4, 75]]  # 4 hours studied, 75% attendance

# Prediction
prediction = model.predict(new_student)

print("Prediction for new student:", prediction[0])

# Tree visualization
plt.figure(figsize=(10,6))
tree.plot_tree(model, feature_names=["Hours_Studied", "Attendance"],
               class_names=["Fail", "Pass"], filled=True)
plt.show()