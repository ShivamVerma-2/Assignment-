import pandas as pd

# Create a sample DataFrame with a date column
df = pd.DataFrame({
    'Event': ['A', 'B', 'C', 'D'],
    'Date': ['2025-06-01', '2025-06-05', '2025-06-10', '2025-06-15']
})

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Extract year, month, day
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

# Extract weekday
df['Weekday'] = df['Date'].dt.day_name()

# Add 5 days to each date
df['Date_plus_5'] = df['Date'] + pd.Timedelta(days=5)

# Calculate difference from today's date
df['Days_from_today'] = (pd.Timestamp.today() - df['Date']).dt.days

print(df)
