import pandas

# Define a dictionary 'x'
x = {'Name': ['Rose', 'John', 'Jane', 'Mary'], 'ID':[1, 2, 3, 4], 'Department':['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'],'Salary':[100000, 80000, 50000, 60000]}

# casting the dictionary to a Dataframe
df = pandas.DataFrame(x)

# display the result
print(df)
x = df['Name']
print(x)
print(type(x))
