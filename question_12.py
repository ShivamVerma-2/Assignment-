import pandas as pd

# 1. DataFrame from two-dimensional Python list
data1 = [[1, 'Alice'], [2, 'Bob'], [3, 'Charlie']]
df1 = pd.DataFrame(data1, columns=['ID', 'Name'])
print("1. DataFrame from 2D list:\n", df1, "\n")


data2 = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}
df2 = pd.DataFrame(data2)
print("2. DataFrame from dict:\n", df2, "\n")


data3 = [['Math', 90], ['Science', 85], ['English', 88]]
df3 = pd.DataFrame(data3, columns=['Subject', 'Score'])
print("3. DataFrame from list of lists:\n", df3, "\n")


data4 = [(101, 'Alice'), (102, 'Bob'), (103, 'Charlie')]
df4 = pd.DataFrame(data4, columns=['Roll No', 'Name'])
print("4. DataFrame from list of tuples:\n", df4, "\n")


data5 = [
    {'Name': 'Alice', 'Marks': 85},
    {'Name': 'Bob', 'Marks': 90},
    {'Name': 'Charlie', 'Marks': 88}
]
df5 = pd.DataFrame(data5)
print("5. DataFrame from list of dicts:\n", df5)
