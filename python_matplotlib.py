## MatplotLib

'''
Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK+.

Some of the major Pros of Matplotlib are:

* Generally easy to get started for simple plots
* Support for custom labels and texts
* Great control of every element in a figure
* High-quality output in many formats
* Very customizable in general
'''

import matplotlib.pyplot as plt
import numpy as np

## Simple Examples

x=np.arange(0,10)
y=np.arange(11,21)

a=np.arange(40,50)
b=np.arange(50,60)

##plotting using matplotlib 

##plt scatter

plt.scatter(x,y,c='g')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Scatter')
plt.show()

y=x*x
##plt plot
plt.plot(x,y,'g*',linestyle="dashed",linewidth=2,markersize=12)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Plot")
plt.show()

#creating subplots
plt.subplot(2,2,1)
plt.plot(x,y,"r--")
plt.title("subplot")
plt.subplot(2,2,2)
plt.plot(x,y,"b*")
plt.subplot(2,2,3)
plt.plot(x,y,"go")
plt.show()  

#subplot()
#compute the x and y coordinates for points on sine and cosine curves
x=np.arange(0,5*np.pi,0.1)
y_sin=np.sin(x)
y_cos=np.cos(x)

#subplot grid that has height 2 and width 1,
#and setthe first such subplot as active
plt.subplot(2,1,1)
plt.title("sine")
plt.plot(x,y_sin,"r--")


plt.subplot(2,1,2)
plt.plot(x,y_cos,"y*")
plt.title("cos")
plt.show()

#Bar plot
x=[2,8,10]
y=[11,16,9]

x2=[3,9,11]
y2=[6,15,7]
plt.bar(x,y)
plt.bar(x2,y2,color='g')
plt.title("Barplot")
plt.show()

#line plot

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line plot example')
plt.show()

#Histograms
a=np.array([22,56,87,97,76,12,23,45,75,89,])
plt.hist(a)
plt.title("Histogram")
plt.show()

#Box plot

data=[np.random.normal(0,std,100) for std in range(1,4)]

#rectangular box plot
plt.boxplot(data,vert=True,patch_artist=True);
plt.title("Box plot")
plt.show()
print(data)

#pie chart
labels='python','java','R','Ruby'
colors=['gold','yellowgreen','lightcoral','lightskyblue']
sizes=[215,130,245,210]
explode=(0.1,0,0,0)#explode ist slice

#plot
plt.pie(sizes,colors=colors,labels=labels,explode=explode,autopct='%1.1f%%' , shadow=True)
plt.axis('equal')# Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('pie chart')
plt.show()