import pandas as pd

# From dictionary
data_dict = {'a': 10, 'b': 20, 'c': 30}
series_from_dict = pd.Series(data_dict)
print(series_from_dict)


data_list = [100, 200, 300]
labels = ['x', 'y', 'z']
series_from_list = pd.Series(data_list, index=labels)
print(series_from_list)

# Access by label
print(series_from_dict['b']) 

print(series_from_list[0])


print(series_from_dict['a':'c'])
