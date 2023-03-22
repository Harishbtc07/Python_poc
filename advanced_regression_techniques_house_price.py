'''
The main aim of this project is to predict the house price based 
on various featres
'''

#All The Lifecycle in a Data Scienced Projects
#1.Data Analysis
#2.Feture Engineerig
#3.Feature Selection
#4.Model Building
#5.Model Deployment


#importing the required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataset=pd.read_csv("C://Users//Harish Reddy//Downloads//House_train.csv")
print(dataset.head())
print(dataset.columns)

#in Data Analysis we will analyse to find out the below stuff
'''
#1.Missing Values
#2.All The Numerical Variables
#3.Distribution of the Numerical Variables
#4.Categorical Variables
#5.Cardinality of Categorical Variables
#6.Outliers
#7.Relationship between independent and dependent feature(SalePrice)
'''

#Missing Values

# Here we will check the percentage of nan values present in each feature
# 1 -step make the list of features which has missing values
features_with_na=[features for features in dataset.columns if dataset[features].isnull().sum()>1]
# 2- step print the feature name and the percentage of missing values

for feature in features_with_na:
    print(feature, np.round(dataset[feature].isnull().mean(), 4),  ' % missing values')

'''
Since they are many missing values, we need to find the relationship between missing values and Sales Price
'''
#plotting diagram for this relationship

for feature in features_with_na:
    data=dataset.copy()

     #making a variable that indicates 1 if the observation was missing or zero otherwise
    data[feature]=np.where(data[feature].isnull(),1,0)
    # let's calculate the mean SalePrice where the information is missing or present
    data.groupby(feature)['SalePrice'].median().plot.bar()
    plt.show()

'''
Here With the relation between the missing values and the dependent variable is clearly visible.
So We need to replace these nan values with something meaningful which we will do in the Feature Engineering section
'''
#From the above dataset some of the features like id is not required

print("Id of Houses {}".format(len(dataset.Id)))


#Numerical Variables
#list of numerical variables
numerical_features=[feature for feature in dataset.columns if dataset[feature].dtypes !='O']

print('Number of numerical variables: ',len(numerical_features))

#visualise the numerical variables
print(dataset[numerical_features].head())

'''
Temporal Variables(Eg: Datetime Variables)
From the Dataset we have 4 year variables. We have extract information from 
the datetime variables like no of years or no of days. One example in this specific scenario 
can be difference in years between the year the house was built and the year the house was sold. 
'''
#List of variables that contain year information

year_feature=[feature for feature in numerical_features if 'Yr' in feature or 'Year in feature']
print(year_feature)

# exploring the content of these year variables
for feature in year_feature:
    print(feature,dataset[feature].unique())

 
#analyzing the Temporal Datetime Variables
# checking whether there is a relation between year the house is sold and the sales price

dataset.groupby('YrSold')['SalePrice'].median().plot()
plt.xlabel('Year Sold')
plt.ylabel('Median House Price')
plt.title("House Price vs YearSold")
plt.show()

#comparing the difference between All years feature with SalePrice

for feature in year_feature:
    if feature!='YrSold':
        data=dataset.copy()
        # We will capture the difference between year variable and year the house was sold for
        data[feature]=data['YrSold']-data[feature]
        plt.scatter(data[feature],data['SalePrice'])
        plt.xlabel(feature)
        plt.ylabel('SalePrice')
        plt.show()


#Numerical variables are usually of 2 type
#1. Continous variable and Discrete Variables

discrete_feature=[feature for feature in numerical_features if len(dataset[feature].unique())<25 and feature not in year_feature+['Id']]
print("Discrete Variables Count: {}".format(len(discrete_feature)))

print(discrete_feature)

print(dataset[discrete_feature].head())

#Finding the realtionship between them and Sale PRice

for feature in discrete_feature:
    data=dataset.copy()
    data.groupby(feature)['SalePrice'].median().plot.bar()
    plt.xlabel(feature)
    plt.ylabel('SalePrice')
    plt.title(feature)
    plt.show()
# There is a relationship between variable number and SalePrice


#Continuous Variable
continuous_feature=[feature for feature in numerical_features if feature not in discrete_feature+year_feature+['Id']]
print("Continuous feature Count {}".format(len(continuous_feature)))

#analysing the continuous values by creating histograms to understand the distribution

for feature in continuous_feature:
    data=dataset.copy()
    data[feature].hist(bins=25)
    plt.xlabel(feature)
    plt.ylabel("Count")
    plt.title(feature)
    plt.show()


#Using logarithmic transformation in order to perform log normal distributon
for feature in continuous_feature:
    data=dataset.copy()
    if 0 in data[feature].unique():
        pass
    else:
        data[feature]=np.log(data[feature])
        data['SalePrice']=np.log(data['SalePrice'])
        plt.scatter(data[feature],data['SalePrice'])
        plt.xlabel(feature)
        plt.ylabel('SalesPrice')
        plt.title('feature')
        plt.show()




#Outliers
#An outlier is an observation that lies an abnormal distance from other values in a random sample from a population


for feature in continuous_feature:
    data=dataset.copy()
    if 0 in data[feature].unique():
        pass
    else:
        data[feature]=np.log(data[feature])
        data.boxplot(column=feature)
        plt.ylabel(feature)
        plt.title('feature')
        plt.show()


#Categorical Variables

categorical_features=[feature for feature in dataset.columns if data[feature].dtype=='O']
print(categorical_features)

dataset[categorical_features].head()

for feature in categorical_features:
    print('The feature is {} and number f categories are {}'.format(feature,len(dataset[feature].unique())))


#Find out the relationship between categorical variable and dependent feature SalesPrice
for feature in categorical_features:
    data=dataset.copy()
    data.groupby(feature)['SalePrice'].median().plot.bar()
    plt.xlabel(feature)
    plt.ylabel('SalePrice')
    plt.title(feature)
    plt.show()
 



