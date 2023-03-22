#Functions in Python
'''
*why functions
*Function definition
*Positional and keyword Arguments in Functions
'''

num=12
if num%2==0:
    print("Even")
else:
    print("Odd")


def even_odd(num):
    if num%2==0:
        print("The Number is Even")
    else:
        print("The Number is Odd")
even_odd(11)


#print vs return

def hello_world():
    print("Hello Welcome to Python")
hello_world()

#Example for return
def begininng():
    return "welcome to ML"
obj=begininng()
print(obj)

#Example for adding two numbrs
def add_number(num1,num2):
    return num1+num2
val=add_number(22,44)
print(val)

#positional arguments
#keyword arguments
def details(name,age=22):
    print("my name is {} and my age is {}".format(name,age))
details('harish')

def hello(*args,**kwargs):
    print(args)
    print(kwargs)
hello("harish","reddy",age=22,dob=1999)

list=['harish','reddy']
dict_args={"age":22,"dob":1999}
hello(*list,**dict_args)

#returning multiple outputs from a function
lst=[1,2,3,4,5,6,7]
def evenoddsum(lst):
    even_sum=0
    odd_sum=0
    for i in lst:
        if i%2==0:
            even_sum=even_sum+i
        else:
            odd_sum=odd_sum+i
    return even_sum,odd_sum
val=evenoddsum(lst)
print(val)

