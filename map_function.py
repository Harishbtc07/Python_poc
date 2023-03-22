#Map Feunction in Python
def even_or_odd(num):
    if num%2==0:
        return "The number {} is even".format(num)
    else:
        return "The number {} is odd".format(num)
print(even_or_odd(12))

lst=1,2,3,4,5,6,7,8,9,45,3,5,64,45,43
print(list(map(even_or_odd,lst)))

def prime_or_not(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return "not a prime"
        else:
            return "prime"
    else:
        return "not a prime"
val=prime_or_not(2)
print(val)

lst1=[1,2,3,4,5897,76,445]
print(list(map(prime_or_not,lst1)))

