def naruto(a,n):
    pivot = a[n-1]
    j = -1
    high = n-1
    for i in range(0,n):
        if a[i]<=pivot:
            j+=1
            a[i] ,a[j] = a[j] ,a[i]


    a[j+1] , a[high] = a[high] ,a[j+1]

    return a

a =[1,5,3,2,18,19,4]
n =len(a)
print(naruto(a,n))

