# In the last exercise, you were able to import flat files containing columns with different datatypes as numpy arrays. 
# However, the DataFrame object in pandas is a more appropriate structure in which to store such data and,
# thankfully, we can easily import files of mixed data types as DataFrames using the pandas functions read_csv() and read_table().

# 1. Import the pandas package using the alias pd.
# 2. Read titanic.csv into a DataFrame called df. The file name is already stored in the file object.
# 3. In a print() call, view the head of the DataFrame.

# Import pandas as pd
import pandas as pd

# Assign the filename: file
file = 'titanic.csv'

# Read the file into a DataFrame: df
# df = pd.read_csv(file)

# View the head of the DataFrame
# print(df.head())

# Read the first 5 rows of the file into a DataFrame: data
data = pd.read_csv(file, nrows=5, header=None)

# Build a numpy array from the DataFrame: data_array
data_array = data.values

# Print the datatype of data_array to the shell
print(type(data_array))
# <class 'numpy.ndarray'>