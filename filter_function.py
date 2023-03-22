#Filter Function

def even(num):
    if num%2==0:
        return True
    else:
        return False
lst=[1,2,3,4,5,6,7,8,9,0]
print(list(filter(even,lst)))


print(list(map(even,lst)))
'''The basic difference between map and filter is that map 
will print the all values in the given list where as 
filter will give only the values that are required(the function what we wrote for)
'''    