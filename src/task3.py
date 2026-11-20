#Task 3

#Numpy Arrays

import numpy as np

marks = np.array([
    [80, 75, 90],
    [65, 70, 85],
    [90, 95, 88],
    [75, 80, 70]
])

print("Shape:", marks.shape)
student_averages = np.mean(marks, axis=1)
print("Student averages:", student_averages)
subject_averages = np.mean(marks, axis=0)
print("Subject averages:", subject_averages)
grace_marks = marks + 5
print("Marks after grace:", grace_marks)
weights = np.array([0.3, 0.3, 0.4])
weighted_scores = np.dot(grace_marks, weights)
print("Weighted scores:", weighted_scores)

#Pandas Operations

import pandas as pd

df = pd.read_csv("data/employee18.csv")
print("Employee Information")
print(df.info())
print("Statistical Description")
print(df.describe())
print("Using loc")
print(df.loc[0:3, ["employee_name", "salary"]])
print("Using iloc")
print(df.iloc[0:3, 0:3])
print("Employees with salary above 50000")
print(df[df["salary"] > 50000])

#Clean data

df_dirty = pd.read_csv("data/employee18.csv")
df_dirty.loc[1, "salary"] = None
df_dirty.loc[4, "salary"] = None

df_dirty = pd.concat(
    [df_dirty, df_dirty.iloc[[0]]],
    ignore_index=True
)

df_dirty.to_csv("data/employees_dirty.csv", index=False)
print("Dirty dataset created")
df = pd.read_csv("data/employees_dirty.csv")
df.columns = df.columns.str.strip().str.lower()
print("Column Names:", df.columns.tolist())
departments = pd.read_csv("data/departments.csv")
print("Missing values before cleaning:")
print(df.isnull().sum())
median_salary = df["salary"].median()
df["salary"] = df["salary"].fillna(median_salary)
df = df.drop_duplicates()
df["employee_id"] = df["employee_id"].astype(int)
df["salary"] = df["salary"].astype(float)
print("Missing values after cleaning:")
print(df.isnull().sum())
print("Cleaned dataset")
print(df)

department_summary = df.groupby("department").agg(
    headcount=("employee_id", "count"),
    average_salary=("salary", "mean"),
    maximum_salary=("salary", "max")
)
print("Department Summary")
print(department_summary)

#Inner Join

inner_join = pd.merge(
    df,
    departments,
    on="department",
    how="inner"
)
print("Inner Join")
print(inner_join)

#Left Join

left_join = pd.merge(
    df,
    departments,
    on="department",
    how="left"
)
print("Left Join")
print(left_join)

#Outer Join

outer_join = pd.merge(
    df,
    departments,
    on="department",
    how="outer"
)
print("Outer Join")
print(outer_join)

import matplotlib.pyplot as plt

#Bar Chart

department_avg = df.groupby("department")["salary"].mean()
plt.bar(department_avg.index, department_avg.values, label="Average Salary")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.legend()
plt.savefig("reports/department_bar.png")
plt.show()

#Histogram

plt.hist(df["salary"], bins=5, label="Salary Distribution")
plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.legend()
plt.savefig("reports/salary_histogram.png")
plt.show()

#Scatter Plot

plt.scatter(df["employee_id"], df["salary"], label="Employee Salary")
plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()
plt.savefig("reports/salary_scatter.png")
plt.show()

#Line Chart

plt.plot(df["employee_name"], df["salary"], marker="o", label="Salary Trend")
plt.title("Employee Salary Trend")
plt.xlabel("Employee Name")
plt.ylabel("Salary")
plt.legend()
plt.savefig("reports/salary_line.png")
plt.show()
