def equilibrim(a,n):
    for i in range(1,n):
        if sum(a[0:i]) == sum(a[i+1:n]):
            return a[i]
a =[1,3,5,2,2]
n =len(a)        
print(equilibrim(a,n))
