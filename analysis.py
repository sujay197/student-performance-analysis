import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("students.csv")

# Show dataset
print("Dataset:\n", df)

# Average 
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

# Pass/Fail
df["Result"] = df["Average"].apply(lambda x: "Pass" if x >= 40 else "Fail")
print("\nResult:")
print(df[["Name", "Result"]])

print("\nAverage Marks:\n", df[["Name", "Average"]])

# Find Topper
topper = df.loc[df["Average"].idxmax()]
print("\nTop Performer:\n", topper["Name"])

# Plot graph
df.plot(x="Name", y=["Math", "Science", "English"], kind="bar")
plt.title("Student Marks Comparison")
plt.ylabel("Marks")
plt.show()