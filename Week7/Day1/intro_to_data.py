# Categorical Data: Data that separates the data into specific groups
# Numeric Data: Related to numbers that can be measured/quantified
import pandas as pd

# # data = pd.Series([1, 3, 5, 7, 9])

# data = {
#     'Name' : ['Jon', 'Anna', 'Peter', 'Linda'],
#     'Age' : [28, 34, 29, 32],
#     'City' : ['New York', 'Paris', 'Berlin', 'London']
# }

# df = pd.DataFrame(data)
# # print(df.head(1)) # Prints only the first row from the dataframe (table)

# ages = df['Age'] # Selects the Age column ([28, 34, 29, 32])
# # print(ages)

# condition = df['Age'] > 30 # Return all rows (items) where the age is greater than 30 (This is basically a SELECT * FROM table WHERE Age > 30)

# # print(df[condition])

# Class Exercise 1:

data = {
    'Book Title': ['The Great Gatsby', 'To Kill a Mockingbird', '1984', 'Pride and Prejudice', 'The Catcher in the Rye'],
    'Author': ['F. Scott Fitzgerald', 'Harper Lee', 'George Orwell', 'Jane Austen', 'J.D. Salinger'],
    'Genre': ['Classic', 'Classic', 'Dystopian', 'Classic', 'Classic'],
    'Price': [10.99, 8.99, 7.99, 11.99, 9.99],
    'Copies Sold': [500, 600, 800, 300, 450]
}

df = pd.DataFrame(data)

# print(df.head())
# print(df.describe()) # Gives a quick statistical summary of the DataSet (min, max, mean, .25 - .50 - .75 percentiles, std, count)
# print(df.info())  # Gives a quick summary if the data type and non-null count

## SORT BY
# print(df.sort_values(by='Price', ascending=False))
# print(df.sort_values(by='Copies Sold'))

# # Filters
# print(df[df['Genre'] == 'Classic'])
# # OR
# condition = df['Price'] >= 10
# print(df[condition])

# print(df.groupby('Author').sum('Copues Sold'))
