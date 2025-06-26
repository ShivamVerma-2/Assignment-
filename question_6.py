import  pandas as pd
# Create 3 DataFrames
df_a = pd.DataFrame({'ID': [1, 2], 'ValueA': ['A1', 'A2']})
df_b = pd.DataFrame({'ID': [3, 4], 'ValueA': ['A3', 'A4']})
df_c = pd.DataFrame({'ID': [2, 3], 'ValueC': ['C2', 'C3']})

# Vertical concatenation
df_concat = pd.concat([df_a, df_b], axis=0)

# Merge with df_c on common key 'ID'
merged_df = pd.merge(df_concat, df_c, on='ID', how='inner')
print("Concatenated and Merged:\n", merged_df)
