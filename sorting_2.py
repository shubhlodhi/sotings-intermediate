def soting_char(a,n):
    count = [0]*256
    output = [0]*n
    for i in a:
        count[i]+=1

    for i in range(1,n):
        count[i] += count[i-1] 

    for i in reversed(a):
        # index = (i)%n
        output[count[i]-1] = i
        count[i]-=1
    return output
a = [1,2,3,1,1,2,3,1,2,1,2,1]
n =12
print(soting_char(a,n))
# s = (91%5)
# print(s)

def sorting(a,n):
    k = 2*n
    count = [0]*k

    for x in a:
        count[x]+=1
    index =0
    for i in range(n):
        for j in range(count[i]):
            a[index] = i
            index+=1
    return a

a = [1,2,3,5,4,7,6]
n =len(a)
print(sorting(a,n))

def intersection(a, b,n):
    i ,j =0,0
    while i<n:
        # if a[i] == a[i-1]:
            # i+=1


        if a[i]<b[j]:
            i+=1
        elif a[i]>b[j]:
            j+=1
        else:
            print(a[i] , end="")
            i+=1
            j+=1

a =[1,2,3,4] 
b = [1,2,3,4 ,5 ,6]
n = len(a)
print(intersection(a,b,n))

def inder(a,b,n):
    s = a+b
    s = set(s)
    return s


a =[1,2,3,4] 
b = [1,2,3,4]
n = len(a)
print(inder(a,b,n))

def possible_triangle(a,n):
    res =0
    for i in range(n):
        for j in range(i+1,n):
            
            adding = a[i] + a[j]
            for k in range(j+1,n):
                if a[k] < adding:
                    res+=1

    return res
a = [6,4,9,7,8]
n =len(a)
print(possible_triangle(a,n))

# def possible_triangle1(a,n):
#     res =0
#     i =0
#     j =1
#     k = 2
#     while i<n:
#         A = a[i] + a[j]
#         print(A)
#         if a[k] < A:
#             res+=1
#             k+=1
#             # print(res)
#         if k == n:
#             j+=1
#             k = j+1

#         # else:
#         if    j == n:
#             i+=1

#     return res    # return res

# a = [6,4,9,7,8]
# n = len(a)
# print(possible_triangle1(a,n))
    
# def triplet_zero(a,n):
#     res = 0
#     for i in range(0,n):
#         k = i+2
#         for j in range(i+1,n):
            
#             while i<n:
#             # for k in range(j+1,n):
#                 sum = a[i]+a[j]+a[k]
#                 if (sum) == 0:
#                     res+=1

#     return res

# a =[0,-1,2,-3,1]
# n = len(a)
# print(triplet_zero(a,n))


def triplet_zeroo(a,n):
    res = 0
    for i in range(0,n):
       for j in range(i+1,n):
        #    if k == n:
            k = j+1
            while k<n:
               if a[i]+a[j]+a[k] ==0:
                   res+=1
               k+=1
            #    if k==n:
                #    k = 0

    return res

a =[0,-1,2,-3,1] 
n = len(a)
print(triplet_zeroo(a,n))
            


    
    