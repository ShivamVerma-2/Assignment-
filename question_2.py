import pandas as pd

# Sample DataFrames
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'ID': [2, 3, 4],
    'Score': [85, 90, 75]
})


inner_merged = pd.merge(df1, df2, on='ID', how='inner')
print("Inner Merge:\n", inner_merged)



left_merged = pd.merge(df1, df2, on='ID', how='left')
print("Left Join:\n", left_merged)


right_merged = pd.merge(df1, df2, on='ID', how='right')
print("Right Join with merge:\n", right_merged)


df1_indexed = df1.set_index('ID')
df2_indexed = df2.set_index('ID')

joined_index = df1_indexed.join(df2_indexed, how='right')
print("Right Join with join():\n", joined_index)
