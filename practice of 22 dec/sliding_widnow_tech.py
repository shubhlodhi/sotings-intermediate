def sliding_window(a,n,k):
    res =0
    sum =0
    for i in range(0,k):
        
        sum += a[i]
        res = max(sum,res)

    for i in range(k,n):
        sum += a[i] - a[i-k]

        res = max( sum , res)
    return res
    
a = [1,4,2,10,23,3,1,0,20]
n =len(a)
print(sliding_window(a,n,4))