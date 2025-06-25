import pandas as pd


data = {
    'Name': ['Shivam ', 'Boy', 'verma', 'Rohit', 'Ishan'],
    'Age': [24, 30, 22, 29, 35],
    'Score': [85, 92, 88, 76, 95]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df, "\n")

print("1. Iterating using iterrows():")
for index, row in df.iterrows():
    print(f"{row['Name']} is {row['Age']} years old.")

print("\nIterating using itertuples():")
for row in df.itertuples():
    print(f"{row.Name} scored {row.Score}")


print("\n2. Rows where Score > 90:\n", df[df['Score'] > 90], "\n")


print("3. Third row using iloc:\n", df.iloc[2], "\n")


print("4. First 3 Names:\n", df.loc[:2, 'Name'], "\n")


df_dropped = df[df['Score'] >= 90]
print("5. After dropping rows with Score < 90:\n", df_dropped, "\n")


new_row = pd.DataFrame([{'Name': 'Frank', 'Age': 28, 'Score': 89}])
df = pd.concat([df.iloc[:2], new_row, df.iloc[2:]]).reset_index(drop=True)
print("6. After inserting new row at index 2:\n", df, "\n")


row_list = df.to_dict(orient='records')
print("7. List from DataFrame rows:\n", row_list)
