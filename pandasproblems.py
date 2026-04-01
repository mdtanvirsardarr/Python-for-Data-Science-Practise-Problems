import pandas as pd

# Create a dictionary containing student data
data = {
    "ID": [1, 2, 3, 4, 5, 6, 7, 8],
    "Name": ["Ali", "Sara", "John", "Mina", "David", "Emma", "Noah", "Lily"],
    "Age": [20, 21, 19, 22, 20, 21, 19, 22],
    "Marks": [78, 85, 67, 90, 72, 88, 60, 95],
    "StudyHours": [3, 4, 2, 5, 3, 4, 2, 6],
    "Attendance": [85, 90, 75, 95, 80, 92, 70, 98]
}

# Convert the dictionary into a Pandas DataFrame
df = pd.DataFrame(data)

# Display the complete DataFrame
print(df)

# Display the first 5 rows of the DataFrame
print("\n1. First 5 rows")
print(df.head())

# Display the last 3 rows of the DataFrame
print("\n2. Last 3 rows")
print(df.tail(3))

# Display the number of rows and columns
print("\n3. Shape")
print(df.shape)

# Display the column names
print("\n4. Column names")
print(df.columns)

# Display the data type of each column
print("\n5. Data types")
print(df.dtypes)

# Display general information about the DataFrame
print("\n6. Info")
print(df.info())

# Display summary statistics for numerical columns
print("\n7. Summary statistics")
print(df.describe())

# Select and display only the Marks column
print("\n8. Marks column")
print(df["Marks"])

# Select and display Name and Marks columns
print("\n9. Name and Marks")
print(df[["Name", "Marks"]])

# Select and display Age, Marks, and Attendance columns
print("\n10. Age, Marks, Attendance")
print(df[["Age", "Marks", "Attendance"]])

# Select and display the row with index 0
print("\n11. Row index 0")
print(df.loc[0])

# Select and display rows from index 2 to 5
print("\n12. Rows from index 2 to 5")
print(df.loc[2:5])

# Display the last 2 rows
print("\n13. Last 2 rows")
print(df.tail(2))

# Select and display Name and Marks from row index 3
print("\n14. Row 3, Name and Marks")
print(df.loc[3, ["Name", "Marks"]])

# Filter students with marks greater than 80
print("\n15. Marks greater than 80")
print(df[df["Marks"] > 80])

# Filter students with attendance below 80
print("\n16. Attendance below 80")
print(df[df["Attendance"] < 80])

# Filter students aged 20
print("\n17. Students aged 20")
print(df[df["Age"] == 20])

# Filter students with marks above 75 and attendance above 85
print("\n18. Marks above 75 and attendance above 85")
print(df[(df["Marks"] > 75) & (df["Attendance"] > 85)])

# Filter students whose study hours are less than or equal to 3
print("\n19. Study hours less than or equal to 3")
print(df[df["StudyHours"] <= 3])

# Filter students whose marks are between 70 and 90
print("\n20. Marks between 70 and 90")
print(df[(df["Marks"] >= 70) & (df["Marks"] <= 90)])

# Calculate and display the average marks
print("\n21. Average marks")
print(df["Marks"].mean())

# Find and display the maximum marks
print("\n22. Maximum marks")
print(df["Marks"].max())

# Find and display the minimum marks
print("\n23. Minimum marks")
print(df["Marks"].min())

# Calculate and display the total attendance
print("\n24. Total attendance")
print(df["Attendance"].sum())

# Calculate and display the average study hours
print("\n25. Average study hours")
print(df["StudyHours"].mean())

# Count and display the total number of students
print("\n26. Total number of students")
print(df.shape[0])

# Calculate and display the median marks
print("\n27. Median marks")
print(df["Marks"].median())

# Calculate and display the standard deviation of marks
print("\n28. Standard deviation of marks")
print(df["Marks"].std())

# Sort the DataFrame by marks in ascending order
print("\n29. Sort by marks ascending")
print(df.sort_values("Marks"))

# Sort the DataFrame by attendance in descending order
print("\n30. Sort by attendance descending")
print(df.sort_values("Attendance", ascending=False))

# Sort the DataFrame by age and then by marks
print("\n31. Sort by age and then marks")
print(df.sort_values(["Age", "Marks"]))

# Create a Pass column where 1 means pass and 0 means fail
print("\n32. Add Pass column")
df["Pass"] = (df["Marks"] >= 70).astype(int)
print(df)

# Create a Grade column based on marks
print("\n33. Add Grade column")
df["Grade"] = "D"
df.loc[df["Marks"] >= 70, "Grade"] = "C"
df.loc[df["Marks"] >= 80, "Grade"] = "B"
df.loc[df["Marks"] >= 90, "Grade"] = "A"
print(df)

# Create a PerformanceScore column by adding Marks, StudyHours, and Attendance
print("\n34. Add PerformanceScore column")
df["PerformanceScore"] = df["Marks"] + df["StudyHours"] + df["Attendance"]
print(df)

# Replace marks below 70 with 70 in a copied DataFrame
print("\n35. Replace marks below 70 with 70")
df_marks_fixed = df.copy()
df_marks_fixed.loc[df_marks_fixed["Marks"] < 70, "Marks"] = 70
print(df_marks_fixed)

# Add 5 bonus marks to all students in a copied DataFrame
print("\n36. Add 5 bonus marks")
df_bonus = df.copy()
df_bonus["Marks"] = df_bonus["Marks"] + 5
print(df_bonus)

# Increase attendance by 2 in a copied DataFrame
print("\n37. Increase attendance by 2")
df_attendance = df.copy()
df_attendance["Attendance"] = df_attendance["Attendance"] + 2
print(df_attendance)

# Change study hours to 7 for students with marks above 90
print("\n38. Change study hours to 7 for students with marks above 90")
df_hours = df.copy()
df_hours.loc[df_hours["Marks"] > 90, "StudyHours"] = 7
print(df_hours)

# Display the unique ages in the dataset
print("\n39. Unique ages")
print(df["Age"].unique())

# Count how many students belong to each age
print("\n40. Count students in each age")
print(df["Age"].value_counts())

# Count how many students passed
print("\n41. Count passed students")
print((df["Marks"] >= 70).sum())

# Count the frequency of each grade
print("\n42. Count frequency of each grade")
print(df["Grade"].value_counts())

# Calculate the average marks for each age group
print("\n43. Average marks for each age group")
print(df.groupby("Age")["Marks"].mean())

# Calculate the average attendance for each age group
print("\n44. Average attendance for each age group")
print(df.groupby("Age")["Attendance"].mean())

# Find the maximum marks for each age group
print("\n45. Maximum marks for each age group")
print(df.groupby("Age")["Marks"].max())

# Check whether there are any missing values in each column
print("\n46. Check missing values")
print(df.isnull().any())

# Count the total missing values in each column
print("\n47. Count missing values")
print(df.isnull().sum())

# Fill missing values with 0 and display the result
print("\n48. Fill missing values with 0")
print(df.fillna(0))

# Drop rows with missing values and display the result
print("\n49. Drop rows with missing values")
print(df.dropna())