'''
performing all the below steps in Feature Engineering

1.Missing values
2.Temporal variables
3.Categorical variables: remove rare labels
4.Standarise the values of the variables to the same range
'''

#importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Reading dataset
dataset=pd.read_csv("C://Users//Harish Reddy//Downloads//House_train.csv")
print(dataset.head())

#Missing Values

#capturing all the nan values
#first handling categorical features which are mising 
features_nan=[feature for feature in dataset.columns if dataset[feature].isnull().sum()>1 and dataset[feature].dtypes=='O']

for feature in features_nan:
    print("{}: {}% missing values".format(feature,np.round(dataset[feature].isnull().mean(),4)))

#Replacing missing values with a new label
def replace_cat_feature(dataset,features_nan):
    data=dataset.copy()
    data[features_nan]=data[features_nan].fillna('Missing')
    return data

dataset=replace_cat_feature(dataset,features_nan)

print(dataset[features_nan].isnull().sum())

print(dataset.head())


#cheking for numerical variables that contains missing values
numerical_with_nan=[feature for feature in dataset.columns if dataset[feature].isnull().sum()>1 and dataset[feature].dtypes!='O']

#printing the numerical nan variables and percentage of missing values
for feature in numerical_with_nan:
    print("{}: {}% missing value".format(feature,np.around(dataset[feature].isnull().mean(),4)))

#Replacing the numerical Missing Values
for feature in numerical_with_nan:
    #replacing by using median since there are outliers
    median_value=dataset[feature].median()

    #Creating a new feature to capture nan values
    dataset[feature+'nan']=np.where(dataset[feature].isnull(),1,0)
    dataset[feature].fillna(median_value,inplace=True)
    
print(dataset[numerical_with_nan].isnull().sum())

#Temporal Variables(Date Time Variables)
for feature in ['YearBuilt','YearRemodAdd','GarageYrBlt']:
    dataset[feature]=dataset['YrSold']-dataset[feature]

print(dataset.head())

print(dataset[['YearBuilt','YearRemodAdd','GarageYrBlt']].head())

#Since the numerical variables are skewed we wil perform log normal distribution
print(dataset.head())


num_features=['LotFrontage','LotArea','1stFlrSF','GrLivArea','SalePrice']

for feature in num_features:
    dataset[feature]=np.log(dataset[feature])

print(dataset.head())


#Handling Rare Categorical Feature
#Removing Categorical variables that are present less than 1% of the observations

categorical_features=[feature for feature in dataset.columns if dataset[feature].dtype=='O']
print(categorical_features)


for feature in  categorical_features:
    temp=dataset.groupby(feature)['SalePrice'].count()/len(dataset)
    temp_df=temp[temp>0.01].index
    dataset[feature]=np.where(dataset[feature].isin(temp_df),dataset[feature],'Rare_var')

print(dataset.head()) 


#Feature Scalling
feature_scale=[feature for feature in dataset.columns if feature not in ['Id','SalePrice']]

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
scaler.fit(dataset[feature_scale])

# transform the dataset, and add on the Id and SalePrice variables
data = pd.concat([dataset[['Id', 'SalePrice']].reset_index(drop=True),
                    pd.DataFrame(scaler.transform(dataset[feature_scale]), columns=feature_scale)],
                    axis=1)

print(data.head())  