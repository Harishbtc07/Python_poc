#EDA with python and appplying Logistic Regression
#importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#reading the csv file into a pandas dataframe
train=pd.read_csv('C://Users//Harish Reddy//Downloads//titanic_data.csv')
print(train.head())

#Exploratory Data Analysis

#Missing Data
print(train.isnull())

sns.heatmap(train.isnull(),yticklabels=False)
plt.show()

sns.set_style('whitegrid')
sns.countplot(x='Survived',data=train)
plt.show()

sns.set_style('whitegrid')
sns.countplot(x='Survived',hue='Sex',data=train)
plt.show()

sns.countplot(x='Sex',hue='Survived',data=train,palette='RdBu_r')
plt.show()

sns.set_style('whitegrid')
sns.countplot(x='Survived',hue='Pclass',data=train,palette='rainbow')
plt.show()

sns.distplot(train['Age'].dropna(),kde=False,color='darkblue')
plt.show()

sns.countplot(x='SibSp',data=train)
plt.show()

train['Fare'].hist(color='green',bins=40,figsize=(8,4))
plt.show()

#Data cleaning

plt.figure(figsize=(12,7))
sns.boxplot(x='Pclass',y='Age',data=train,palette='winter')
plt.show()

def impute_age(cols):
    Age=cols[0]
    Pclass=cols[1]

    if pd.isnull(Age):
        if Pclass==1:
            return 37
        
        elif Pclass==2:
            return 29
        else:
            return 24
    else:
        return Age

train['Age']=train[['Age','Pclass']].apply(impute_age,axis=1)

sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
plt.show()

train.drop('Cabin',axis=1,inplace=True)
print(train.head())

sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
plt.show()

#Coverting to Categorical Features
'''
converting categoriccal features to dummy variables using pandas because 
ml algo wont be ableto directly take those features as inputs.
'''

sex=pd.get_dummies(train['Sex'],drop_first=True)
embark=pd.get_dummies(train['Embarked'],drop_first=True)

train.drop(['Sex','Embarked','Name','Ticket'],axis=1,inplace=True)
print(train.head())

train=pd.concat([train,sex,embark],axis=1)
print(train.head())

#Building a Logistic Regression model
#splitting our data into traning set and test set

#Trian Test Split
x=train.drop('Survived',axis=1)#independent variables
y=train['Survived']#dependent variables

print(x)
print(y)

#importing the train test split from sklearn
from sklearn.model_selection import train_test_split



#splitting the data into train and testing
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=2)

#Training and predicting
from sklearn.linear_model import LogisticRegression

logmodel=LogisticRegression()
logmodel.fit(x_train,y_train)

predictions=logmodel.predict(x_test)
print(predictions)

from sklearn.metrics import accuracy_score
accuracy=accuracy_score(y_test,predictions)
print(accuracy)

