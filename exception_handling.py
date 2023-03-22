#Python Exception Handling
'''
Exception handling is an important concept in Python 
(and in programming in general) because it allows developers 
to write code that can handle errors and unexpected situations 
in a controlled manner.
'''
#Difference between exception and error
'''
error is a broad term that refers to any unexpected behavior 
in a program, while an exception is a specific type of error 
that is raised when a piece of code encounters an unexpected 
condition during program execution.
'''

try:
    #code block where exception can occur
    a=b
except Exception as ex:
    print(ex)

#writing own message
try:
    #code block where exception can occur
    a=b
except NameError as ex1:
    print("The user have not defined the variable")
except Exception as ex:
    print(ex)





try:
    #code block where exception can occur
    a=1
    b="H"
    c=a+b
except NameError as ex1:
    print("The user have not defined the variable")
except Exception as ex:
    print(ex)


try:
    #code block where exception can occur
    a=1
    b="H"
    c=a+b
except NameError as ex1:
    print("The user have not defined the variable")
except TypeError as ex1:
    print("Try to make datatype similar")
except Exception as ex:
    print(ex)

'''
From the above code we can observe that first it will check the first
exception wheather it caught or not if that is not getting caught it 
will go to the next exception then it will go to the next eception
'''

try:
    #code block where exception can occur
    a=int(input("Enter the number 1 "))
    b=int(input("Enter the number 2 "))
    c=a/b
    d=a*b
    e=a+b
    print(c)
    print(d)
    print(e)
except NameError as ex1:
    print("The user have not defined the variable")
except ZeroDivisionError:
    print("Please provide the number greater than 0")
except TypeError:
    print("Try to make datatype similar")
except Exception as ex:
    print(ex)



#try else
try:
    #code block where exception can occur
    a=int(input("Enter the number 1 "))
    b=int(input("Enter the number 2 "))
    c=a/b
    d=a*b
    e=a+b
    
except NameError as ex1:
    print("The user have not defined the variable")
except ZeroDivisionError:
    print("Please provide the number greater than 0")
except TypeError:
    print("Try to make datatype similar")
except Exception as ex:
    print(ex)
else:
    print(c)
    print(d)
    print(e)


#try els finally
#try else
try:
    #code block where exception can occur
    a=int(input("Enter the number 1 "))
    b=int(input("Enter the number 2 "))
    c=a/b
    d=a*b
    e=a+b
    
except NameError as ex1:
    print("The user have not defined the variable")
except ZeroDivisionError:
    print("Please provide the number greater than 0")
except TypeError:
    print("Try to make datatype similar")
except Exception as ex:
    print(ex)
else:
    print(c)
    print(d)
    print(e)
finally:
    print("The execution is done")