import pandas as pd

# Create two DataFrames with a common column 'ID'
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
})

df2 = pd.DataFrame({
    'ID': [3, 4, 5, 6],
    'Score': [85, 90, 95, 80]
})

print("DataFrame 1:\n", df1)
print("\nDataFrame 2:\n", df2)

# 1️⃣ Inner Merge
inner_merge = pd.merge(df1, df2, on='ID', how='inner')
print("\n1️⃣ Inner Merge on 'ID':\n", inner_merge)

# 2️⃣ Left Join
left_merge = pd.merge(df1, df2, on='ID', how='left')
print("\n2️⃣ Left Join on 'ID':\n", left_merge)

# Explanation:
# All rows from df1 are kept, missing matches from df2 are filled with NaN in 'Score'.

right_merge = pd.merge(df1, df2, on='ID', how='right')
print("\n3️⃣ Right Join on 'ID' using pd.merge():\n", right_merge)

# 4️⃣ Right Join using df.join() on index
# Setting 'ID' as the index for index-based join
df1_index = df1.set_index('ID')
df2_index = df2.set_index('ID')

right_join_index = df1_index.join(df2_index, how='right')
print("\n4️⃣ Right Join using df.join() on index:\n", right_join_index)

# Comparison:
# Both right joins include all rows from df2, but:
# - pd.merge() joins on columns.
# - df.join() joins on the index.

# 5️⃣ Merging with Multiple Keys (extended for your understanding)

# Adding an additional 'Dept' column for demonstration
df1['Dept'] = ['HR', 'IT', 'IT', 'HR']
df2['Dept'] = ['IT', 'HR', 'Finance', 'IT']

multi_key_merge = pd.merge(df1, df2, on=['ID', 'Dept'], how='inner')
print("\n5️⃣ Inner Merge on Multiple Keys ['ID', 'Dept']:\n", multi_key_merge)
