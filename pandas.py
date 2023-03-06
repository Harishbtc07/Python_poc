'''Pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and 
data analysis tools for the Python programming language.
'''

'''
Agenda

What is Data Frames?
What is Data Series?
Different operation in Pandas
'''

#importing required libraries
import pandas as pd
import numpy as np

df=pd.DataFrame(np.arange(0,20).reshape(5,4),index=['Row1','Row2','Row3','Row4','Row5'],columns=["Column1","Column2","Column3","Coumn4"])

#printing the first five rows
print(df.head())

## Accessing the elements
df.loc['Row1']

## Check the type
type(df.loc['Row1'])

df.iloc[:,:]

## Take the elements from the Column2
df.iloc[:,1:]

#convert Dataframes into array
df.iloc[:,1:].values

#To count the unique values in a column
df['Column1'].value_counts()

#reading csv file and coverting into dataframe
df=pd.read_csv("C://Users//Harish Reddy//Downloads//test.csv")
print(df.head())

'''
The 'info()' method provides a summary of the DataFrame that includes:

The number of non-null values in each column
The data type of each column
The memory usage of the DataFrame
The total number of columns and rows in the DataFrame
'''
print(df.info())

'''
The describe() method in pandas provides a statistical summary of a DataFrame. 
It computes various descriptive statistics for each numerical column in the 
DataFrame, such as count, mean, standard deviation, minimum and maximum values, and the quartiles.
'''
df.describe()

#Get the unique category counts
df['X0'].value_counts()

df['X11'].value_counts()

#contains nan values
lst_data=[[1,2,3],[3,4,np.nan],[5,6,np.nan],[np.nan,np.nan,np.nan]]

#converting to pandas dataframe
df=pd.DataFrame(lst_data)

print(df.head())

## HAndling Missing Values

##Drop nan values

print(df.dropna(axis=0))#drops all rows containing at least one missing value

print(df.dropna(axis=1))# drops all columns containing at least one missing value

#creating random values
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f', 'h'],
                     columns=['one', 'two', 'three'])

print(df.head())

#reindexing
df2=df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print(df2)

print(df2.dropna(axis=0))

#returns boolean value if the 'one' coloumn contains nan (True for nan and False otherwise)
print(pd.isna(df2['one']))

print(df2['one'].notna())

print(df2.fillna('Missing'))

