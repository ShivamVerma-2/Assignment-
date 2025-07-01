import pandas as pd

df_a = pd.DataFrame({'ID': [1, 2], 'Value': ['A', 'B']})
df_b = pd.DataFrame({'ID': [3, 4], 'Value': ['C', 'D']})
df_c = pd.DataFrame({'ID': [2, 3, 4], 'Score': [70, 80, 90]})

# Vertically concatenate df_a and df_b
concat_df = pd.concat([df_a, df_b], ignore_index=True)
print("\nConcatenated DataFrame:\n", concat_df)

# Merge with df_c on 'ID'
final_merged = pd.merge(concat_df, df_c, on='ID', how='inner')
print("\nFinal Merged after concatenation:\n", final_merged)
