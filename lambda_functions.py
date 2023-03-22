#Lambda Function
'''
->we can also call it as anonymous function and
A function with no name
->it works very fast as compared to normal function
->It is only possible when we have only single expression
'''

#with normal function
def addition(a,b):
    print(a+b)
addition(12,12)

#using lambda function
addition=lambda a,b:a+b
print(addition(12,13))

#one more example
def even(num):
    if num%2==0:
        return True
    else:
        return False
    
print(even(13))

even=lambda a:a%2==0
print(even(13))

#Addition of two numbers
def add(a,b,c):
    print(a+b+c)
add(1,2,3)

add=lambda a,b,c:a+b+c
print(add(4,5,6))