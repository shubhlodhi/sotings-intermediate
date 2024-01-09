def differnce(A,n):
    A.sort()
    res = float("inf")
    for i in range(1,n):
        res = min(res,abs(A[i] - A[i-1]))

    return res
a = [1,8,12,5,18]

n =len(a)
print(differnce(a,n))

def pivot(a,n):
    pivot =1
    j =0
    for i in range(0,n):
        if a[i] <pivot:
            
            a[i],a[j] = a[j] ,a[i]
        
        
            j+=1
        # print(j)
    for i in range(j,n):
        if a[i] == pivot:
            a[i] , a[j] = a[j] , a[i]
            j+=1


        # else:
            # a[j],a[i] = a[i],a[j]
    
    return a


        
a = [0,1,0,2,1,2]
n =len(a)
print(pivot(a,n))

def pivot1(a,n):
    pivot_var = 2
    k ,j =0,0
    for i in range(0,n):
        if a[i] < pivot_var:
            a[i] , a[j] = a[j] ,a[i]
            j+=1
            k+=1
        if a[i]<= pivot_var:
            k+=1
            print(k)
    print(i)

    a[k] , a[i] = a[i] , a[k]
    return a
a =[2,1,2,20,10,20,1]
n =len(a)


print(pivot1(a,n))

a = range(5,10)
# a =[0,2,1,2,2,1]
def counter(a,n):
    pivot2 =2
    j =0
    for i in range(0,n):

        if a[i] <pivot2:
            a[i] ,a[j] = a[j] , a[i]
            j+=1
        if a[i] == pivot2:
            a[i] , a[j] = a[j] ,a[i]
            j+=1

    return a

a =[0,2,20,2,1,20,20,20]

n = len(a)
print(counter(a,n))
            

a = [[9,0] , [10,8]]
print(min(a[1] , a[0]))
print(max(a[0]))
# def mmmm(a,n):

a =[[2,3] ,[1,6]]
res =0
s = (a[res][1] , a[1])
print(s)
for i in range(len(a[1])):
    if a[i] == 1:
        a.pop(a[0])
    
print(a)

    # print(i)
# a =[90,89,78,67,56,45]
# n =len(a)
# def depta(arrival,departure,n):
#     res =1
#     for i in range(1,n):
#         # if departure[i-1] < arrival[i]:
        

#         if arrival[i] < departure[i-1]:
#             if departure[i] > arrival[i-1]:
#                 res+=1
#     return res

# a =[900,940,950,1100,1500,1800]


 
# b =[910,1200,1120,1130,1900,2000]
# n =len(a)
# print(depta(a,b,n))
def depta2(a,b,n):
    D_A = a+b
    D_A.sort()
    len_DA = len(D_A)
    count =0
    res =0
    for i in range(0,len_DA):
        for j in range(0,n):
           if D_A[i] ==  a[j]: 
               
               res +=1
               count = max(res ,count)
           if D_A[i] == b[j]:
               res-=1

    return count
a =[900,940,950,1100,1500,1800]


 
b =[910,1200,1120,1130,1900,2000]
n=len(a)
print(depta2(a,b,n))



# s =[[2,3] , [7,6]]
