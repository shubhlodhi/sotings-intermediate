def two_pointer(a,n,k):
    i =0
    j =n-1
    while i<=j:
        if a[i] + a[j] == k:
            return True
        if a[i] + a[j] > k:
            j-=1
        else:
            i+=1
    return False

def triplet(a,n,k):
    for i in range(1,n):
        return two_pointer(a,n,k-a[i])
a= [12,3,4,1,6,9]
n =len(a)
print(triplet(a,n,24))

print(two_pointer(a,n,13))
        


        



    
