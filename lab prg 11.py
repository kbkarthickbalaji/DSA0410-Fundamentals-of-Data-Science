import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample data to simulate reading from a table (like a CSV file)
data = {
    'name': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'm1': [80, 75, 90, np.nan, 60, 85, 70, 95, np.nan, 88],
    'm2': [85, 80, np.nan, 70, 75, 90, 60, 88, 92, 85],
    'm3': [78, 82, 89, 91, 84, 95, 88, 77, 85, 90]
}

# i) Read the data from the table (Here we create a DataFrame)
marks = pd.DataFrame(data)
print("i) DataFrame:\n", marks)

# ii) Retrieve only the first and last 5 rows
print("\nii) First 5 rows:\n", marks.head())
print("\nLast 5 rows:\n", marks.tail())

# iii) Purpose of describe() function
print("\niii) Purpose of describe():")
print("→ It gives statistical summary like count, mean, std, min, 25%, 50%, 75%, max for numeric columns.")
print("\nDescribe Output:\n", marks.describe())

# iv) Select only 3rd to 6th row (i.e., rows with index 2 to 5)
print("\niv) Rows 3rd to 6th:\n", marks.iloc[2:6])

# v) Select only the rows where m3 > 84 marks
print("\nv) Rows where m3 > 84:\n", marks[marks['m3'] > 84])

# vi) Filter the rows with missing values
print("\nvi) Rows with missing values:\n", marks[marks.isnull().any(axis=1)])

# vii) Remove the rows with missing values
cleaned_marks = marks.dropna()
print("\nvii) After removing missing value rows:\n", cleaned_marks)

# viii) Sort the m1 column in descending order
sorted_marks = marks.sort_values(by='m1', ascending=False)
print("\nviii) m1 column sorted in descending order:\n", sorted_marks)

# ix) Plot the table (bar plot of m1, m2, m3)
print("\nix) Plotting the marks (bar chart)...")
marks[['m1', 'm2', 'm3']].plot(kind='bar', title='Student Marks Comparison', figsize=(10, 6))
plt.xlabel('Student Index')
plt.ylabel('Marks')
plt.legend(title="Subjects")
plt.tight_layout()
plt.show()

# x) Output for marks.ix[3:6, [‘m2’,’m3’]] (use loc instead of deprecated ix)
print("\nx) Rows 3 to 6, Columns 'm2' and 'm3':\n", marks.loc[3:6, ['m2', 'm3']])
