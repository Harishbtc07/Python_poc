#Seaborn

#Distribution plots
'''
*distplot
*jointplot
*pairplot
'''

import seaborn as sns
import matplotlib.pyplot as plt
#loading the data set
df=sns.load_dataset("tips")
print(df.head())

#Correlation with Heatmap
'''
A correlation heatmap uses colored cells,typically in a monochromatic scale,to show a 2D correlation matrix
(table) between two discrete dimensions or event types.it is very important in feature selection
'''
print(df.dtypes)
print(df.corr())
sns.heatmap(df.corr())
plt.title('Heatmap')
plt.show()

#Join plot
'''
A join plot allows to study the relationship between 2 numeric variables.
The central chart display their correlation. it is usually a scatterplot,
a hexbinplot,a 2Dhistogram or a 2D density plot
'''
#Univariate Analysis
sns.jointplot(x='tip',y='total_bill',data=df,kind='hex')
plt.title('Joint plot')
plt.show()

sns.jointplot(x='tip',y='total_bill',data=df,kind='reg')
plt.title('Joint plot')
plt.show()

#Pair plot
'''
pairs plot is also known as scatterplot,in which one variable in the same data row
is matched with another variables value,like this.Pairs plots are just elaborations 
on this, showing all variables paired with all the other variables
'''

sns.pairplot(df)
plt.title('Pair plot')
plt.show()

sns.pairplot(df,hue='sex')
plt.title('Pair plot')
plt.show()
print(df['sex'].value_counts())

sns.pairplot(df,hue='smoker')
plt.title('pair plot')
plt.show()

#Dist plot
#Dist plot helps us to check the distribution of the columns feature

sns.distplot(df['tip'])
plt.title('Dist plot')
plt.show()

#Categorical plots
tips_data = sns.load_dataset("tips")
sns.countplot(x='sex', data=tips_data)
plt.title('Count plot')
plt.show()
sns.countplot(x='smoker', data=tips_data)
plt.show()
sns.countplot(y='day', data=tips_data)
plt.show()


#Bar plot
sns.barplot(x='total_bill',y='sex',data=df)
plt.title('Barplot')
plt.show()

#Box plot
'''
A box and wisker plot(sometimes called a boxplot) is a graph that presents
information from a fie-number summary.
'''
sns.boxplot(x='sex',y='total_bill',data=df)
plt.title('Box plot')
plt.show()

sns.boxplot(x='day',y='total_bill',data=df,palette='rainbow')
plt.title('Box plot')
plt.show()

#categorizing the data based on some other categories
sns.boxplot(x='total_bill',y='day',hue='smoker',data=df)
plt.title('Box plot')
plt.show()