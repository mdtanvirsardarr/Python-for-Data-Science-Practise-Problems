import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create the student dataset
data = {
    "ID": [1, 2, 3, 4, 5, 6, 7, 8],
    "Name": ["Ali", "Sara", "John", "Mina", "David", "Emma", "Noah", "Lily"],
    "Age": [20, 21, 19, 22, 20, 21, 19, 22],
    "Marks": [78, 85, 67, 90, 72, 88, 60, 95],
    "StudyHours": [3, 4, 2, 5, 3, 4, 2, 6],
    "Attendance": [85, 90, 75, 95, 80, 92, 70, 98]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# ---------------------------------------------------
# 1. Basic understanding of the dataset
# ---------------------------------------------------

# Display the full dataset
print("Full Dataset:")
print(df)

# Display the first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Display the last 5 rows
print("\nLast 5 rows:")
print(df.tail())

# Display the shape of the dataset
print("\nShape of dataset:")
print(df.shape)

# Display the column names
print("\nColumn names:")
print(df.columns)

# Display the data types
print("\nData types:")
print(df.dtypes)

# Display general information about the dataset
print("\nDataset information:")
df.info()

# ---------------------------------------------------
# 2. Statistical summary
# ---------------------------------------------------

# Display summary statistics for numerical columns
print("\nSummary statistics:")
print(df.describe())

# Display summary statistics including object columns
print("\nSummary statistics including all columns:")
print(df.describe(include="all"))

# ---------------------------------------------------
# 3. Missing values and duplicates
# ---------------------------------------------------

# Check for missing values in each column
print("\nMissing values in each column:")
print(df.isnull().sum())

# Check whether the dataset contains any missing value
print("\nDoes the dataset contain missing values?")
print(df.isnull().values.any())

# Check for duplicated rows
print("\nNumber of duplicated rows:")
print(df.duplicated().sum())

# ---------------------------------------------------
# 4. Unique values and frequencies
# ---------------------------------------------------

# Display unique ages
print("\nUnique ages:")
print(df["Age"].unique())

# Count frequency of each age
print("\nFrequency of ages:")
print(df["Age"].value_counts())

# Count frequency of each student name
print("\nFrequency of names:")
print(df["Name"].value_counts())

# ---------------------------------------------------
# 5. Column-wise analysis
# ---------------------------------------------------

# Find average marks
print("\nAverage marks:")
print(df["Marks"].mean())

# Find median marks
print("\nMedian marks:")
print(df["Marks"].median())

# Find standard deviation of marks
print("\nStandard deviation of marks:")
print(df["Marks"].std())

# Find minimum and maximum marks
print("\nMinimum marks:")
print(df["Marks"].min())

print("\nMaximum marks:")
print(df["Marks"].max())

# Find average study hours
print("\nAverage study hours:")
print(df["StudyHours"].mean())

# Find average attendance
print("\nAverage attendance:")
print(df["Attendance"].mean())

# ---------------------------------------------------
# 6. Filtering and simple insights
# ---------------------------------------------------

# Students with marks above 80
print("\nStudents with marks above 80:")
print(df[df["Marks"] > 80])

# Students with attendance below 80
print("\nStudents with attendance below 80:")
print(df[df["Attendance"] < 80])

# Students with study hours greater than 3
print("\nStudents with study hours greater than 3:")
print(df[df["StudyHours"] > 3])

# Students with marks above average
print("\nStudents with marks above average:")
print(df[df["Marks"] > df["Marks"].mean()])

# ---------------------------------------------------
# 7. Create new EDA columns
# ---------------------------------------------------

# Create a pass or fail column
df["Pass"] = np.where(df["Marks"] >= 70, "Pass", "Fail")

# Create a grade column
df["Grade"] = "D"
df.loc[df["Marks"] >= 70, "Grade"] = "C"
df.loc[df["Marks"] >= 80, "Grade"] = "B"
df.loc[df["Marks"] >= 90, "Grade"] = "A"

# Create a performance score column
df["PerformanceScore"] = df["Marks"] + df["StudyHours"] + df["Attendance"]

# Display the updated dataset
print("\nDataset after adding Pass, Grade, and PerformanceScore:")
print(df)

# Count pass and fail values
print("\nPass and Fail counts:")
print(df["Pass"].value_counts())

# Count grade frequency
print("\nGrade frequency:")
print(df["Grade"].value_counts())

# ---------------------------------------------------
# 8. Grouped analysis
# ---------------------------------------------------

# Average marks for each age group
print("\nAverage marks by age:")
print(df.groupby("Age")["Marks"].mean())

# Average attendance for each age group
print("\nAverage attendance by age:")
print(df.groupby("Age")["Attendance"].mean())

# Average study hours for each age group
print("\nAverage study hours by age:")
print(df.groupby("Age")["StudyHours"].mean())

# Maximum marks for each age group
print("\nMaximum marks by age:")
print(df.groupby("Age")["Marks"].max())

# ---------------------------------------------------
# 9. Correlation analysis
# ---------------------------------------------------

# Select only numerical columns
numeric_df = df.select_dtypes(include=[np.number])

# Display the correlation matrix
print("\nCorrelation matrix:")
print(numeric_df.corr())

# ---------------------------------------------------
# 10. Outlier detection using IQR for Marks
# ---------------------------------------------------

# Calculate first quartile and third quartile
Q1 = df["Marks"].quantile(0.25)
Q3 = df["Marks"].quantile(0.75)

# Calculate interquartile range
IQR = Q3 - Q1

# Define lower and upper bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Find outliers in marks
marks_outliers = df[(df["Marks"] < lower_bound) | (df["Marks"] > upper_bound)]

print("\nOutliers in Marks using IQR method:")
print(marks_outliers)

# ---------------------------------------------------
# 11. Visual EDA
# ---------------------------------------------------

# Histogram of marks
plt.figure(figsize=(7, 5))
plt.hist(df["Marks"], bins=5, edgecolor="black")
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# Boxplot of marks
plt.figure(figsize=(7, 5))
plt.boxplot(df["Marks"])
plt.title("Boxplot of Marks")
plt.ylabel("Marks")
plt.show()

# Scatter plot: Study hours vs Marks
plt.figure(figsize=(7, 5))
plt.scatter(df["StudyHours"], df["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

# Scatter plot: Attendance vs Marks
plt.figure(figsize=(7, 5))
plt.scatter(df["Attendance"], df["Marks"])
plt.title("Attendance vs Marks")
plt.xlabel("Attendance")
plt.ylabel("Marks")
plt.show()

# Bar chart of average marks by age
avg_marks_by_age = df.groupby("Age")["Marks"].mean()

plt.figure(figsize=(7, 5))
plt.bar(avg_marks_by_age.index.astype(str), avg_marks_by_age.values)
plt.title("Average Marks by Age")
plt.xlabel("Age")
plt.ylabel("Average Marks")
plt.show()

# Bar chart of grade counts
grade_counts = df["Grade"].value_counts()

plt.figure(figsize=(7, 5))
plt.bar(grade_counts.index, grade_counts.values)
plt.title("Grade Distribution")
plt.xlabel("Grade")
plt.ylabel("Count")
plt.show()

# ---------------------------------------------------
# 12. Final EDA observations
# ---------------------------------------------------

print("\nFinal observations:")
print("1. Total students:", len(df))
print("2. Average marks:", df["Marks"].mean())
print("3. Highest marks:", df["Marks"].max())
print("4. Lowest marks:", df["Marks"].min())
print("5. Pass count:", (df["Pass"] == "Pass").sum())
print("6. Fail count:", (df["Pass"] == "Fail").sum())
print("7. Correlation between StudyHours and Marks:", df["StudyHours"].corr(df["Marks"]))
print("8. Correlation between Attendance and Marks:", df["Attendance"].corr(df["Marks"]))