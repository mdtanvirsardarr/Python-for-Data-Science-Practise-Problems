import numpy as np

# Student dataset
# Columns: [ID, Age, Marks, StudyHours, Attendance]
data = np.array([
    [1, 20, 78, 3, 85],
    [2, 21, 85, 4, 90],
    [3, 19, 67, 2, 75],
    [4, 22, 90, 5, 95],
    [5, 20, 72, 3, 80],
    [6, 21, 88, 4, 92],
    [7, 19, 60, 2, 70],
    [8, 22, 95, 6, 98]
])

print("Original Dataset:")
print(data)

print("\n1. Extract all marks")
marks = data[:, 2]
print(marks)

print("\n2. Find average marks")
avg_marks = np.mean(marks)
print(avg_marks)

print("\n3. Find maximum and minimum marks")
print("Maximum marks:", np.max(marks))
print("Minimum marks:", np.min(marks))

print("\n4. Count total number of students")
total_students = data.shape[0]
print(total_students)

print("\n5. Extract ages of all students")
ages = data[:, 1]
print(ages)

print("\n6. Find students with marks greater than 80")
students_above_80 = data[data[:, 2] > 80]
print(students_above_80)

print("\n7. Find students with attendance below 80")
attendance_below_80 = data[data[:, 4] < 80]
print(attendance_below_80)

print("\n8. Calculate average study hours")
avg_study_hours = np.mean(data[:, 3])
print(avg_study_hours)

print("\n9. Find index of student with highest marks")
highest_marks_index = np.argmax(data[:, 2])
print(highest_marks_index)

print("\n10. Sort dataset based on marks")
sorted_by_marks = data[data[:, 2].argsort()]
print(sorted_by_marks)

print("\n11. Find students who study more than 3 hours and have marks above 75")
filtered_students = data[(data[:, 3] > 3) & (data[:, 2] > 75)]
print(filtered_students)

print("\n12. Normalize marks between 0 and 1")
normalized_marks = (marks - np.min(marks)) / (np.max(marks) - np.min(marks))
print(normalized_marks)

print("\n13. Find correlation between study hours and marks")
study_hours = data[:, 3]
correlation = np.corrcoef(study_hours, marks)[0, 1]
print(correlation)

print("\n14. Replace marks below 70 with 70")
updated_data = data.copy()
updated_data[updated_data[:, 2] < 70, 2] = 70
print(updated_data)

print("\n15. Add a new column 'Pass' (1 if marks >= 70 else 0)")
pass_column = np.where(data[:, 2] >= 70, 1, 0).reshape(-1, 1)
data_with_pass = np.hstack((data, pass_column))
print(data_with_pass)

print("\n16. Find students scoring above average marks")
above_average_students = data[data[:, 2] > avg_marks]
print(above_average_students)

print("\n17. Identify top 3 students based on marks")
top_3_students = data[data[:, 2].argsort()][-3:]
print(top_3_students)

print("\n18. Check whether more study hours increase marks")
print("Study Hours:", study_hours)
print("Marks:", marks)
print("Correlation value:", correlation)

print("\n19. Detect low performers with marks less than 65")
low_performers = data[data[:, 2] < 65]
print(low_performers)

print("\n20. Create summary")
print("Mean age:", np.mean(data[:, 1]))
print("Mean marks:", np.mean(data[:, 2]))
print("Mean attendance:", np.mean(data[:, 4]))

print("\n21. Create grade column")
grades = np.empty(data.shape[0], dtype='<U1')
grades[data[:, 2] >= 90] = 'A'
grades[(data[:, 2] >= 80) & (data[:, 2] <= 89)] = 'B'
grades[(data[:, 2] >= 70) & (data[:, 2] <= 79)] = 'C'
grades[data[:, 2] < 70] = 'D'
print(grades)

print("\n22. Find student with best attendance and highest marks")
best_student_index = np.argmax(data[:, 4] + data[:, 2])
best_student = data[best_student_index]
print(best_student)

print("\n23. Extract the first 3 students")
first_3_students = data[:3]
print(first_3_students)

print("\n24. Extract the last 2 students")
last_2_students = data[-2:]
print(last_2_students)

print("\n25. Extract only Age and Marks columns")
age_marks = data[:, [1, 2]]
print(age_marks)

print("\n26. Extract Marks, StudyHours, and Attendance of student ID 4")
student_id_4 = data[data[:, 0] == 4][:, 2:]
print(student_id_4)

print("\n27. Reverse the dataset row order")
reversed_data = data[::-1]
print(reversed_data)

print("\n28. Extract every second student")
every_second_student = data[::2]
print(every_second_student)

print("\n29. Extract students from row 2 to row 6")
rows_2_to_6 = data[1:6]
print(rows_2_to_6)

print("\n30. Extract only the last 3 columns")
last_3_columns = data[:, 2:]
print(last_3_columns)

print("\n31. Find students whose marks are between 70 and 85")
marks_between_70_85 = data[(data[:, 2] >= 70) & (data[:, 2] <= 85)]
print(marks_between_70_85)

print("\n32. Find students whose attendance is above 90")
attendance_above_90 = data[data[:, 4] > 90]
print(attendance_above_90)

print("\n33. Find students aged 20 only")
age_20_students = data[data[:, 1] == 20]
print(age_20_students)

print("\n34. Find students aged 20 and marks above 75")
age_20_marks_above_75 = data[(data[:, 1] == 20) & (data[:, 2] > 75)]
print(age_20_marks_above_75)

print("\n35. Find students with study hours less than or equal to 3")
study_hours_less_equal_3 = data[data[:, 3] <= 3]
print(study_hours_less_equal_3)

print("\n36. Find students who failed and also have low attendance")
failed_low_attendance = data[(data[:, 2] < 70) & (data[:, 4] < 75)]
print(failed_low_attendance)

print("\n37. Count how many students scored 80 or more")
count_80_or_more = np.sum(data[:, 2] >= 80)
print(count_80_or_more)

print("\n38. Count how many students got attendance below average")
avg_attendance = np.mean(data[:, 4])
count_attendance_below_avg = np.sum(data[:, 4] < avg_attendance)
print(count_attendance_below_avg)

print("\n39. Add 5 bonus marks to every student")
bonus_marks_data = data.copy()
bonus_marks_data[:, 2] = bonus_marks_data[:, 2] + 5
print(bonus_marks_data)

print("\n40. Increase attendance by 2 for all students")
attendance_increase_data = data.copy()
attendance_increase_data[:, 4] = attendance_increase_data[:, 4] + 2
print(attendance_increase_data)

print("\n41. Replace attendance below 75 with 75")
attendance_updated_data = data.copy()
attendance_updated_data[attendance_updated_data[:, 4] < 75, 4] = 75
print(attendance_updated_data)

print("\n42. Reduce marks by 5 for students whose attendance is below 80")
reduced_marks_data = data.copy()
reduced_marks_data[reduced_marks_data[:, 4] < 80, 2] = reduced_marks_data[reduced_marks_data[:, 4] < 80, 2] - 5
print(reduced_marks_data)

print("\n43. Change study hours of students with marks above 90 to 7")
study_hours_updated_data = data.copy()
study_hours_updated_data[study_hours_updated_data[:, 2] > 90, 3] = 7
print(study_hours_updated_data)

print("\n44. Create a new dataset where age is increased by 1")
age_increased_data = data.copy()
age_increased_data[:, 1] = age_increased_data[:, 1] + 1
print(age_increased_data)

print("\n45. Find total marks of all students")
total_marks = np.sum(data[:, 2])
print(total_marks)

print("\n46. Find total attendance of all students")
total_attendance = np.sum(data[:, 4])
print(total_attendance)

print("\n47. Find median marks")
median_marks = np.median(data[:, 2])
print(median_marks)

print("\n48. Find standard deviation of marks")
std_marks = np.std(data[:, 2])
print(std_marks)

print("\n49. Find variance of attendance")
variance_attendance = np.var(data[:, 4])
print(variance_attendance)

print("\n50. Find range of marks")
range_marks = np.max(data[:, 2]) - np.min(data[:, 2])
print(range_marks)

print("\n51. Find 25th percentile of marks")
percentile_25_marks = np.percentile(data[:, 2], 25)
print(percentile_25_marks)

print("\n52. Find 75th percentile of marks")
percentile_75_marks = np.percentile(data[:, 2], 75)
print(percentile_75_marks)

print("\n53. Find sum of marks for students aged 21 only")
sum_marks_age_21 = np.sum(data[data[:, 1] == 21, 2])
print(sum_marks_age_21)

print("\n54. Find average attendance of students who passed")
avg_attendance_passed = np.mean(data[data[:, 2] >= 70, 4])
print(avg_attendance_passed)

print("\n55. Find row-wise sum of Age, Marks, StudyHours, and Attendance")
row_wise_sum = np.sum(data[:, 1:], axis=1)
print(row_wise_sum)

print("\n56. Find row-wise average of Marks, StudyHours, and Attendance")
row_wise_average = np.mean(data[:, 2:], axis=1)
print(row_wise_average)

print("\n57. Find column-wise sums of Age, Marks, StudyHours, and Attendance")
column_wise_sum = np.sum(data[:, 1:], axis=0)
print(column_wise_sum)

print("\n58. Find column-wise averages of Age, Marks, StudyHours, and Attendance")
column_wise_average = np.mean(data[:, 1:], axis=0)
print(column_wise_average)

print("\n59. Find which column has the highest overall average")
feature_names = np.array(["Age", "Marks", "StudyHours", "Attendance"])
highest_avg_column = feature_names[np.argmax(column_wise_average)]
print(highest_avg_column)

print("\n60. Find which student has the highest total performance score using Marks, StudyHours, and Attendance")
performance_scores = data[:, 2] + data[:, 3] + data[:, 4]
best_performance_student = data[np.argmax(performance_scores)]
print(best_performance_student)

print("\n61. Sort dataset by age")
sorted_by_age = data[data[:, 1].argsort()]
print(sorted_by_age)

print("\n62. Sort dataset by attendance in descending order")
sorted_by_attendance_desc = data[data[:, 4].argsort()[::-1]]
print(sorted_by_attendance_desc)

print("\n63. Sort dataset by study hours and then marks")
sorted_by_study_marks = data[np.lexsort((data[:, 2], data[:, 3]))]
print(sorted_by_study_marks)

print("\n64. Find rank positions of students based on marks")
ranks = np.empty_like(data[:, 2])
ranks[np.argsort(-data[:, 2])] = np.arange(1, len(data[:, 2]) + 1)
print(ranks)

print("\n65. Find second highest marks")
second_highest_marks = np.unique(data[:, 2])[-2]
print(second_highest_marks)

print("\n66. Find third lowest attendance")
third_lowest_attendance = np.unique(data[:, 4])[2]
print(third_lowest_attendance)

print("\n67. Find top 5 students by attendance")
top_5_attendance = data[data[:, 4].argsort()][-5:]
print(top_5_attendance)

print("\n68. Find bottom 3 students by marks")
bottom_3_marks = data[data[:, 2].argsort()][:3]
print(bottom_3_marks)

print("\n69. Add a new column for total performance score")
performance_score_column = (data[:, 2] + data[:, 3] + data[:, 4]).reshape(-1, 1)
data_with_performance = np.hstack((data, performance_score_column))
print(data_with_performance)

print("\n70. Add a column for percentage of marks out of 100")
marks_percentage = (data[:, 2] / 100 * 100).reshape(-1, 1)
data_with_percentage = np.hstack((data, marks_percentage))
print(data_with_percentage)

print("\n71. Add a column called Excellent where marks greater than 85 and attendance greater than 90")
excellent_column = np.where((data[:, 2] > 85) & (data[:, 4] > 90), 1, 0).reshape(-1, 1)
data_with_excellent = np.hstack((data, excellent_column))
print(data_with_excellent)

print("\n72. Add a column for Risk where marks less than 70 or attendance less than 75")
risk_column = np.where((data[:, 2] < 70) | (data[:, 4] < 75), 1, 0).reshape(-1, 1)
data_with_risk = np.hstack((data, risk_column))
print(data_with_risk)

print("\n73. Add a detailed grade column with A, B, C, D, F")
detailed_grades = np.empty(data.shape[0], dtype="<U1")
detailed_grades[data[:, 2] >= 90] = "A"
detailed_grades[(data[:, 2] >= 80) & (data[:, 2] < 90)] = "B"
detailed_grades[(data[:, 2] >= 70) & (data[:, 2] < 80)] = "C"
detailed_grades[(data[:, 2] >= 60) & (data[:, 2] < 70)] = "D"
detailed_grades[data[:, 2] < 60] = "F"
print(detailed_grades)

print("\n74. Add a study category column with Low, Medium, High")
study_category = np.empty(data.shape[0], dtype="<U6")
study_category[data[:, 3] <= 2] = "Low"
study_category[(data[:, 3] >= 3) & (data[:, 3] <= 4)] = "Medium"
study_category[data[:, 3] >= 5] = "High"
print(study_category)

print("\n75. Count how many students belong to each age")
unique_ages, age_counts = np.unique(data[:, 1], return_counts=True)
print("Ages:", unique_ages)
print("Counts:", age_counts)

print("\n76. Count how many students got each grade")
unique_grades, grade_counts = np.unique(grades, return_counts=True)
print("Grades:", unique_grades)
print("Counts:", grade_counts)

print("\n77. Find unique ages")
print(np.unique(data[:, 1]))

print("\n78. Find unique marks")
print(np.unique(data[:, 2]))

print("\n79. Find frequency of attendance values")
unique_attendance, attendance_counts = np.unique(data[:, 4], return_counts=True)
print("Attendance values:", unique_attendance)
print("Counts:", attendance_counts)

print("\n80. Count number of pass and fail students")
pass_count = np.sum(data[:, 2] >= 70)
fail_count = np.sum(data[:, 2] < 70)
print("Pass:", pass_count)
print("Fail:", fail_count)

print("\n81. Reshape marks into a column vector")
marks_column_vector = data[:, 2].reshape(-1, 1)
print(marks_column_vector)

print("\n82. Reshape attendance into a row vector")
attendance_row_vector = data[:, 4].reshape(1, -1)
print(attendance_row_vector)

print("\n83. Flatten the dataset into one array")
flattened_data = data.flatten()
print(flattened_data)

print("\n84. Convert the flat array back into 8 rows and 5 columns")
reshaped_data = flattened_data.reshape(8, 5)
print(reshaped_data)

print("\n85. Transpose the dataset")
transposed_data = data.T
print(transposed_data)

print("\n86. Check shape, size, and number of dimensions")
print("Shape:", data.shape)
print("Size:", data.size)
print("Dimensions:", data.ndim)

print("\n87. Add one new student row to the dataset")
new_student = np.array([[9, 23, 82, 4, 88]])
data_with_new_student = np.vstack((data, new_student))
print(data_with_new_student)

print("\n88. Add one new feature column such as assignment score")
assignment_score = np.array([80, 85, 70, 90, 75, 88, 65, 95]).reshape(-1, 1)
data_with_assignment = np.hstack((data, assignment_score))
print(data_with_assignment)

print("\n89. Split the dataset into two parts")
split_data = np.array_split(data, 2)
print("Part 1:")
print(split_data[0])
print("Part 2:")
print(split_data[1])

print("\n90. Split only marks and attendance columns")
marks_and_attendance = data[:, [2, 4]]
print(marks_and_attendance)

print("\n91. Combine ages and marks into a new smaller array")
ages_and_marks = np.column_stack((data[:, 1], data[:, 2]))
print(ages_and_marks)

print("\n92. Join two NumPy arrays side by side")
ages_column = data[:, 1].reshape(-1, 1)
study_hours_column = data[:, 3].reshape(-1, 1)
joined_array = np.hstack((ages_column, study_hours_column))
print(joined_array)

print("\n93. Check if all students passed")
all_passed = np.all(data[:, 2] >= 70)
print(all_passed)

print("\n94. Check if any student got marks below 60")
any_below_60 = np.any(data[:, 2] < 60)
print(any_below_60)

print("\n95. Check if all attendance values are above 70")
all_attendance_above_70 = np.all(data[:, 4] > 70)
print(all_attendance_above_70)

print("\n96. Check if any student studies more than 5 hours")
any_study_more_than_5 = np.any(data[:, 3] > 5)
print(any_study_more_than_5)

print("\n97. Count how many students satisfy multiple conditions together")
count_multiple_conditions = np.sum((data[:, 2] > 75) & (data[:, 4] > 85))
print(count_multiple_conditions)

print("\n98. Convert marks to percentages")
marks_percentages = data[:, 2].astype(float)
print(marks_percentages)

print("\n99. Square the study hours column")
study_hours_squared = data[:, 3] ** 2
print(study_hours_squared)

print("\n100. Find square root of marks")
sqrt_marks = np.sqrt(data[:, 2])
print(sqrt_marks)

print("\n101. Standardize marks using z-score")
z_score_marks = (data[:, 2] - np.mean(data[:, 2])) / np.std(data[:, 2])
print(z_score_marks)

print("\n102. Scale attendance between 0 and 1")
scaled_attendance = (data[:, 4] - np.min(data[:, 4])) / (np.max(data[:, 4]) - np.min(data[:, 4]))
print(scaled_attendance)

print("\n103. Multiply marks and attendance element-wise")
marks_attendance_product = data[:, 2] * data[:, 4]
print(marks_attendance_product)

print("\n104. Check which students have marks greater than attendance")
marks_greater_than_attendance = data[:, 2] > data[:, 4]
print(marks_greater_than_attendance)

print("\n105. Find difference between marks and attendance")
difference_marks_attendance = data[:, 2] - data[:, 4]
print(difference_marks_attendance)

print("\n106. Find ratio of marks to study hours")
marks_study_ratio = data[:, 2] / data[:, 3]
print(marks_study_ratio)

print("\n107. Find students whose marks are more than 10 above the mean")
students_more_than_10_above_mean = data[data[:, 2] > (np.mean(data[:, 2]) + 10)]
print(students_more_than_10_above_mean)

print("\n108. Find students whose attendance is lower than the median attendance")
median_attendance = np.median(data[:, 4])
attendance_below_median = data[data[:, 4] < median_attendance]
print(attendance_below_median)

print("\n109. Create a pass and attendance summary")
summary_labels = np.empty(data.shape[0], dtype="<U20")
summary_labels[(data[:, 2] >= 70) & (data[:, 4] >= 80)] = "Pass_GoodAttendance"
summary_labels[(data[:, 2] >= 70) & (data[:, 4] < 80)] = "Pass_LowAttendance"
summary_labels[(data[:, 2] < 70) & (data[:, 4] >= 80)] = "Fail_GoodAttendance"
summary_labels[(data[:, 2] < 70) & (data[:, 4] < 80)] = "Fail_LowAttendance"
print(summary_labels)

print("\n110. Group students into high, medium, and low performers")
performance_group = np.empty(data.shape[0], dtype="<U10")
performance_group[data[:, 2] >= 85] = "High"
performance_group[(data[:, 2] >= 70) & (data[:, 2] < 85)] = "Medium"
performance_group[data[:, 2] < 70] = "Low"
print(performance_group)

print("\n111. Find students closest to average marks")
distance_from_avg = np.abs(data[:, 2] - np.mean(data[:, 2]))
closest_students = data[distance_from_avg == np.min(distance_from_avg)]
print(closest_students)

print("\n112. Find students farthest from average marks")
farthest_students = data[distance_from_avg == np.max(distance_from_avg)]
print(farthest_students)

print("\n113. Detect outlier marks using mean and standard deviation")
mean_marks = np.mean(data[:, 2])
std_marks = np.std(data[:, 2])
outliers = data[np.abs(data[:, 2] - mean_marks) > 2 * std_marks]
print(outliers)

print("\n114. Create a weighted score using marks, study hours, and attendance")
weighted_score = (0.6 * data[:, 2]) + (0.2 * data[:, 3]) + (0.2 * data[:, 4])
print(weighted_score)

print("\n115. Find best student using weighted score")
best_weighted_student = data[np.argmax(weighted_score)]
print(best_weighted_student)

print("\n116. Find relationship between attendance and marks")
attendance_marks_correlation = np.corrcoef(data[:, 4], data[:, 2])[0, 1]
print(attendance_marks_correlation)

print("\n117. Find relationship between age and marks")
age_marks_correlation = np.corrcoef(data[:, 1], data[:, 2])[0, 1]
print(age_marks_correlation)

print("\n118. Compare average marks of age 19, 20, 21, and 22 groups")
unique_age_groups = np.unique(data[:, 1])
for age in unique_age_groups:
    avg_marks_by_age = np.mean(data[data[:, 1] == age, 2])
    print("Age", age, "Average Marks:", avg_marks_by_age)