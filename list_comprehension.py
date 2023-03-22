#List Comprehension
'''
List comprehension provide a consise lists. it consists of brackets
containing an expression followed by a for clause, then zero or more for or if clauses.
The expressions can be anything,meaning we can put in all kinds of objects
in lists.
'''

lst1=[]
def lst_square(lst):
    for i in lst:
        lst1.append(i*i)
    return lst1
val=lst_square([1,2,3,4,5,6,7,8,9])
print(val)

#list cpmprehension
lst2=[1,2,3,4,5,6,7,8,9]
ob=[i*i for i in lst2]
print(ob) 


#Squaring only even values
ob1=[i*i for i in lst2 if i%2==0]
print(ob1) 
#Squaring only odd values
ob2=[i*i for i in lst2 if i%2!=0]
print(ob2) 