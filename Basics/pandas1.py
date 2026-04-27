import pandas as pd

print("===== IMPORTANT PANDAS SERIES METHODS =====")

# Creating a Series
s = pd.Series([10, 20, None, 40, 20])
print("\nSeries:")
print(s)

# head() and tail()
print("\nHead:")
print(s.head(2))
print("\nTail:")
print(s.tail(2))

# Basic statistics
print("\nSum:", s.sum())
print("Mean:", s.mean())
print("Max:", s.max())
print("Min:", s.min())

# Handling missing values
print("\nIs Null:")
print(s.isnull())

print("\nFill Na with 0:")
print(s.fillna(0))

# value_counts()
print("\nValue Counts:")
print(s.value_counts())


print("\n\n===== IMPORTANT PANDAS DATAFRAME METHODS =====")

# Creating DataFrame
data = {
    'Name': ['A', 'B', 'C'],
    'Marks': [85, 90, None],
    'Age': [18, 19, 20]
}
df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

# head() and tail()
print("\nHead:")
print(df.head(2))
print("\nTail:")
print(df.tail(1))

# shape and info()
print("\nShape:", df.shape)
print("\nInfo:")
df.info()

# Column access
print("\nMarks Column:")
print(df['Marks'])

# Handling missing values
print("\nFill missing values:")
print(df.fillna(0))

# Filtering rows
print("\nStudents with Marks > 85:")
print(df[df['Marks'] > 85])

# Sorting
print("\nSorted by Marks:")
print(df.sort_values(by='Marks'))

# Adding a column
df['Passed'] = ['Yes', 'Yes', 'No']
print("\nAfter Adding Column:")
print(df)

# Removing a column
df.drop('Passed', axis=1, inplace=True)
print("\nAfter Dropping Column:")
print(df)

# Basic statistics
print("\nTotal Marks:", df['Marks'].sum())
print("Average Marks:", df['Marks'].mean())
