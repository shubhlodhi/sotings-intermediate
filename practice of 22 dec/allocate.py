import math


def allocate(a,n,k):
    res = math.inf
    if k == 1:
        return sum(a[0:n])

    if n == 0:
        return 0
    
    for i in range(1,n):
        res = min(res , max(allocate(a,i,k-1) , sum(a[i:n])))

    return res

a =[12,34,67,90]
n = len(a)
print(allocate(a,n ,2))


