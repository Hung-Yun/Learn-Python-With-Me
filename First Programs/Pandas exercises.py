
# coding: utf-8

# # Pandas 100 exercises
# <br/> [Practice with solution](https://github.com/ajcr/100-pandas-puzzles/blob/master/100-pandas-puzzles-with-solutions.ipynb)

# ## Importing pandas
# ### Getting started and checking your pandas setup

# In[1]:


import pandas as pd
print(pd.__version__)
print(pd.show_versions())
# Show every detail of pandas


# ## DataFrame basics
# ### A few of the fundamental routines for selecting, sorting, adding and aggregating data in DataFrames

# In[ ]:


import numpy as np

# import data and labels
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Create a DataFrame df from this dictionary data which has the index labels.
df = pd.DataFrame(data, index=labels)

# Display a summary of the basic information about this DataFrame and its data.
df.info()

# Return the first 3 rows of the DataFrame df.
print("\nThe first three tows of df")
print(df.head(3))

# Select just the 'animal' and 'age' columns from the DataFrame df.
print("\nSelect the animal and age columns")
print(df.loc[:, ['animal', 'age']].head(3))

# Another way of displaying specific columns
# print(df[["animal","age"]].head(3))

# Select the data in rows [3, 4, 8] and in columns ['animal', 'age'].
print("\nSelect specific columns and rows (with index)")
print(df.loc[df.index[[3, 4, 8]], ['animal', 'age']])

# Select only the rows where the number of visits is greater than 2.
print("\nSelect specific rows with criteria")
print(df[df["visits"]>2])

# Select the rows where the age is missing, i.e. is NaN.
print("\nSelect rows with NaN")
print(df[df["age"].isnull()])

# Select the rows where the animal is a cat and the age is less than 3.
print("\nSelect rows with 2 criteria")
print(df[ (df["animal"]=="cat") & (df["age"]<3) ])

# Select the rows the age is between 2 and 4 (inclusive).
print("\nSelect values between 2 numbers")
print(df[df['age'].between(2, 4)])

# Change the age in row 'f' to 1.5.
print("\nChange a selected value")
df.loc["f","age"]=1.5
print(df.loc["f","age"])

# Calculate the sum of all visits (the total number of visits).
df["visits"].sum()

# Calculate the mean age for each different animal in df.
print("\nGroupby")
print(df.groupby('animal')['age'].mean())


# Append a new row 'k' to df with your choice of values for each column.
# Then delete that row to return the original DataFrame.
df.loc["k"] = [5.5, 'dog', 'no', 2]
df = df.drop("k")


# Count the number of each type of animal in df.
print("\nCount the number of each type of animal--.valuecounts()")
print(df['animal'].value_counts())

# Sort df first by the values in the 'age' in decending order.
# Then by the value in the 'visit' column in ascending order.
print("\nsort_values")
print(df.sort_values(by=['age', 'visits'], ascending=[False, True]))

# The 'priority' column contains the values 'yes' and 'no'.
# Replace this column with a column of boolean values
print("\nReplace value using map method")
# df['priority'] = df['priority'].map({'yes': True, 'no': False})
# print(df)

# In the 'animal' column, change the 'snake' entries to 'python'.
print("\nReplace value using replace method")
df['animal'] = df['animal'].replace('snake', 'python')
print(df)

# For each animal type and each number of visits, find the mean age.
# In other words, each row is an animal, each column is a number of visits and the values are the mean ages
print("\nSort values with pivot_table")
print(df.pivot_table(index='animal', columns='visits', values='age', aggfunc='mean'))


# ## DataFrames: beyond the basics
# ### Slightly trickier: you may need to combine two or more methods to get the right answer
# The previous section was tour through some basic but essential DataFrame operations. Below are some ways that you might need to cut your data, but for which there is no single "out of the box" method.

# In[3]:


# You have a DataFrame df with a column 'A' of integers.
# How do you filter out rows which contain the same integer as the row immediately above?

A = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]}) 
print(A.loc[A['A'].shift() != A['A']])
print("\n")
B = pd.DataFrame({'B': [1, 1, 2, 2, 1, 1]}) 
print(B.loc[B['B'].shift() != B['B']])
print("\n")

C = pd.DataFrame({'C': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]}) 
print(C.drop_duplicates(subset="C"))
print("\n")

D = pd.DataFrame({'D': [1, 1, 2, 2, 1, 1]}) 
print(D.drop_duplicates(subset='D'))


# In[4]:


import numpy as np

df = pd.DataFrame(np.random.randint(0,100,size=(5, 3)))
print(df)
print("\n")

# how do you subtract the row mean from each element in the row?

df1 = df.sub(df.mean(axis=1), axis=0)
print(df1)
print("\n")

df2 = df.sub(df.iloc[1])
print(df2)

# DataFrame.sub(other, axis='columns', level=None, fill_value=None)
# other : Series, DataFrame, or constant
# axis : {0, 1, ‘index’, ‘columns’}
# For Series input, axis to match Series index on
# level : int or name
# Broadcast across a level, matching Index values on the passed MultiIndex level
# fill_value : None or float value, default None
# Fill existing missing (NaN) values.


# In[5]:


df = pd.DataFrame(np.random.randint(0,20,size=(5, 10)), columns=list('abcdefghij'), index=["A","B","C","D","E"])

# Which column of numbers has the smallest sum? (Find that column's label.)

print(df)
print("\n")

k=df.sum(axis=1)
l=df.std(axis=1).astype(int)

df["sum"]=pd.DataFrame(k)
df["std"]=pd.DataFrame(l)

print(df)
print("\n")
print("The lowest points goes to " + str(df["sum"].idxmin()))


# In[6]:


df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})

# How do you count how many unique rows a DataFrame has (i.e. ignore all rows that are duplicates)?
print(df)
print("\nThe number of different values "+str(len(df.drop_duplicates(keep="first"))))
print("The number if we kick out all duplicates "+str(len(df.drop_duplicates(keep=False))))

# drop_duplicates: keep must equal first, last, or False


# In[12]:


# You have a DataFrame that consists of 10 columns of floating--point numbers.
# Suppose that exactly 5 entries in each row are NaN values.
# For each row of the DataFrame, find the column which contains the third NaN value.

(A.isnull().cumsum(axis=1) == 3).idxmax(axis=1)


# In[26]:


df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'), 
                   'vals': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]})

# For each group, find the sum of the three greatest values.

print(df)
print(df.groupby('grps')['vals'].nlargest(3))
print(df.groupby('grps')['vals'].nlargest(3).sum(level=0))


# In[1]:


score = [10,30,50,70,90]
print(score)

print(sum(score)/len(score))

new_score =[]
for i in score:
    new_score.append(i**0.5*10)
print(new_score)

print(sum(new_score)/len(new_score))

