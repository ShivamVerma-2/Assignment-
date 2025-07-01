import pandas as pd

# Load your CSV
df = pd.read_csv('your_file.csv')

# Explore first rows
print(df.head())

# Check missing values
print("\nMissing Values:\n", df.isnull().sum())

# Fill or drop missing values
df = df.dropna()  # OR df.fillna(value, inplace=True)

# Data type check and conversion if needed
print("\nData Types:\n", df.dtypes)
# Example: convert a column to datetime
# df['Date_Column'] = pd.to_datetime(df['Date_Column'])

# Descriptive statistics
print("\nSummary Statistics:\n", df.describe())

# Example analysis:
# Group by a categorical column and get average
if 'Category' in df.columns and 'Value' in df.columns:
    grouped = df.groupby('Category')['Value'].mean()
    print("\nAverage Value by Category:\n", grouped)

# Example filtering:
# Filter data where 'Value' > 100
if 'Value' in df.columns:
    filtered_df = df[df['Value'] > 100]
    print("\nFiltered Data (Value > 100):\n", filtered_df)

# Save cleaned data
df.to_csv('cleaned_file.csv', index=False)
