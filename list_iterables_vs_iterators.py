#Python List Iterables vs Iterators

#List is Iterable
lst=[1,2,3,4,5,6,7,8]
for i in lst:
    print(i)


'''
There is one in built function called iter which will convert
list into iterator 
'''
list1=iter(lst)
print(next(list1))
print(next(list1))
'''
The main functionality of iterator is that whatever value is there 
inside that will not inistialize in the memory at once. only one by one 
it will get initialized 

when we have million of list data(iterable) then each and every value is get 
stored in memory location even we dont need the entire data
in such cases we can convert it into iterator we can extract the data what we need
'''

for i in lst:
    print(i)



