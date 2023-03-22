#String Formatting in Python
print("Hello everyone")

#we can store ita variable also(This is th basic way of storing a string)
str='Hello everyone'
print(str)

'''example for dynamic replacement of values from some
 variables that are predefined or some variables that are coming from 
 from some functions'''

def greeting(name):
    return "Hello {} welcome to python".format(name)
var=greeting("harish")
print(var)
#In the above example we can see that the placeholder is replaced with name with hepl of format function
def welcome_email(name,age):
    return "Hello {} your age is {}".format(name,age)
var1=welcome_email('Harish',22)
print(var1)

#reversing the positon of arguments
def welcome_email(name,age):
    return "Hello {} your age is {}".format(age,name)
var1=welcome_email('kanaka',22)
print(var1)

'''
The ordering of arguments is very much important if we reverse the position of arguments
we will get the improper output(in above example), in order to fix this we can give temporary variable inside 
inside the placeholders
'''

def welcome_email(name,age):
    return "Hello {na} your age is {ag}".format(ag=age,na=name)
var1=welcome_email('Reddy',23)
print(var1)
