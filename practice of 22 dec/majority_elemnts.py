def majority(a,n):
    res = a[0]
    curr = 1
    for i in range(1,n):
        if a[i-1] == a[i]:
            curr+1

        if a[i-1]!=a[i]:
            curr-=1

        if curr ==0:
            curr =1
            res =a[i]

    return res

def check_canditate(a,n):
    res = majority(a,n)
    cunt =0
    for i in range(0,n):
        if a[i] == res:
            cunt+=1

    if cunt > n//2:
        return True
    return False



a =[3,3,4,2,4,4,2]
n=len(a)
print(check_canditate(a,n))

