import pandas as pd

# Example date string series
date_strings = ['2022-01-01', '2022-01-02', '2022-01-03']
date_series = pd.to_datetime(pd.Series(date_strings))

print(date_series)
