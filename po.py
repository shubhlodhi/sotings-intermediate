# def d(a,n):
#     res = 0
#     for i  in range(1,n):
#         if a[i]>a[i-1]:
#             res = max(res,a[i]-a[i-1])

#     if res <=0:
#         return 0
#     else:
#         return 1
    
# a = [4,2,2,2,4] 
# n =len(a)
# print(d(a,n))

# def d(a,n,l,h):
#     res =0
#     for i in range(l,h):
#         count =0
#         for j in range(i+1,h+1):
#             if a[j]>a[i]:
#                 count = a[j]-a[i] +d(a,n,l,i-1)+d(a,n,j+1,h)
#                 # print(count,end="")
#                 res = max(count,res)
#     return res

    
# a = [4,2,2,2,4] 
# n =len(a)
# print(d(a,n,0,n-1))

# def oddeven(a,n):
#     count =1
#     for i in range(1,n):
#         if a[i]%2==0:
#             if a[i-1]%2!=0:
#                 count+=1
#         if a[i]%2!=0:
#             if a[i-1]%2==0:
#                 count+=1
#     return count

# a =[10,12,14,7,8]
# n=len(a)
# print(oddeven(a,n))

from cmath import sqrt
import math


def maximum_circular(a,n):
    res =0
    for i in range(0,n):
        maximum_ele = a[i]
        maximum_sum = a[i]
    for j in range(1,n):
        index = (i+j)%n
        maximum_ele+=a[index]
        maximum_sum = max(maximum_sum,maximum_ele)
    res= max(res,maximum_sum)
    return res
a =[1,-2,3,-1,2]
n= len(a)
print(maximum_circular(a,n))
def sub(str,curr,index):
    if index == len(str):
        print(curr , end=" ")
    
        return
    sub(str,curr , index+1)    
    sub(str,curr+str[index],index+1)


a = "ABC"
print(sub(a,"",0))

def power(a,k):
    if k == 1:
        return a 
    return power (a,k-1)*a

print(power(9,9))

# def phone(n,a ,curr, index):
#     if index == len(a):
#         return 1
#     phone(n,a,a[curr] ,index+1)
#     phone(n,a,a[curr][index+1] ,index+1)
    

# # a = [[1,2,3],[123] ]
# # print(a[0][1])
# a = [2,3,4]
# a[0] = ["a" , "b" , "c"]
# a[1] = ["d" , "e" , "f"]
# a[2] = ["g" , "h" , "i"]
# len(a)
# print(phone(n,a,0,0))
def mid(a,n):
    low = 0
    high = n-1
    mid = low+high//2
    
    while low<high:
        mid = low+high//2
        if mid == 0 or a[mid]>a[mid-1] and mid == n-1 or a[mid]>a[mid+1]:
            return mid 
        if mid>0 and a[mid-1] > a[mid]:

            high = mid-1

        else:
            low = mid+1


def ben(a,n , s):
    low = 0
    high = n-1
    count = 0
    while low<high:
        mid = (low+high)//2
        
        if a[mid] == s:
            count+=1 
            if a[mid+1] == s:
                count+=1
            if a[mid-1] == s:
                count+=1

        if a[mid]>= s:
            high = mid-1
        else:
            low = mid+1
    return count
a = [1,2,2,2,3,3,3,3]
n = len(a)
print(ben(a,n , 3))


def tripet(a,n,k):
    for i in range(0,n):
        res =0
        res = k-a[i]
        j = i+1
        # print(j)
        k =n-1
        while j<k:
            if a[j]+a[k] == res:
                # print(j ,k)
                return True
            if a[j]+a[k] > res:
                k-=1
                print(j,k,end=" ")
            # if a[j]+a[k] < res:
            else:
                j+=1
                # print(k,j)
                # j+=1
        # print(a[i]+a[j]+a[k])
        # print(i)
        # print(j)
        # print(k)
    print(res)
    return False
a = [2,3,4,8,9,20,40]
n = len(a)
print(tripet(a,n,32))

def repaet(a,n):
    counnt  =0
    for i in range(0,n):
        for j in range(i+1,n):
            if a[i] == a[j]:
                count = a[j]

    return count

a = [0,1,2,3,0,2,2,3,3,3]
n =len(a)
print(repaet(a,n))


def allocate(a,n,k):
    res =0
    if k == 1:
        return(sum(a[0:n]))

    if n == 1:
        return (sum(a))
    for i in range(1,n):
        res = float(math.inf)

        res = min(res , max(allocate(a,i,k-1) , sum(a[i:n])))

    return res 

a = [12,34,67,90]       
n =len(a)
print(allocate(a,n,2))

a = 10


# The square root of a number is the inverse operation of squaring a number. The square of a number is the value that is obtained when we multiply the number by itself, while the square root of a number is obtained by finding a number that when squared gives the original number.

# If 'a' is the square root of 'b', it means that a × a = b. The square of any number is always a positive number, so every number has two square roots, one of a positive value, and one of a negative value. For example, both 2 and -2 are square roots of 4. However, in most places, only the positive value is written as the square root of a number.

# What is Square Root?
# The square root of a number is that factor of a number which when multiplied by itself gives the original number. Squares and square roots are special exponents. Consider the number 9. When 3 is multiplied by itself, it gives 9 as the product. This can be written as 3 × 3 or 32. Here, the exponent is 2, and we call it a square. Now when the exponent is 1/2, it refers to the square root of the number. For example, √n = n1/2, where n is a positive integer.

# Square Root Definition
# The square root of a number is the value of power 1/2 of that number. In other words, it is the number whose product by itself gives the original number. It is represented using the symbol '√ '. The square root symbol is called a radical, whereas the number under the square root symbol is called the radicand.

# How to Find Square Root?
# To find the square root of a number, we just see by squaring which number would give the actual number. It is very easy to find the square root of a number that is a perfect square. Perfect squares are those positive numbers that can be expressed as the product of a number by itself. In other words, perfect squares are numbers which are expressed as the value of power 2 of any integer. We can use four methods to find the square root of numbers and those methods are as follows:

# Repeated Subtraction Method
# Prime Factorization Method
# Estimation Method
# Long Division Method
# It should be noted that the first three methods can be conveniently used for perfect squares, while the fourth method, i.e., the long division method can be used for any number whether it is a perfect square or not.

# Repeated Subtraction Method of Square Root
# This is a very simple method. We subtract the consecutive odd numbers from the number for which we are finding the square root, till we reach 0. The number of times we subtract is the square root of the given number. This method works only for perfect square numbers. Let us find the square root of 16 using this method.

# 16 - 1 = 15
# 15 - 3 =12
# 12 - 5 = 7
# 7- 7 = 0
# You can observe that we have subtracted 4 times. Thus,√16 = 4


a = 5
count =0
for i in range(1,a,2):
    # if a < 0:

     a = (a-i)
    #  print(a)
    # print(i)
     count +=1
     if a <0:
        print("cunt", count-1)
        break


    #  print("count" ,count)

def county(a,n):
    
    half = (n//2)
    for i in range(0,n):
        count = 1
        for j in range(i+1,n):
            if a[i] == a[j]:
                count+=1
        if count >= half:
            return a[i]
        
a = [1,2,3,4,5]
n= len(a)
print(county(a,n))

def midid(a,n):
    low  =0
    high =n-1
    mid = (low+high)//2
    while low<high:
        if a[mid] > a[low] and a[mid] > a[high]:
            low = mid+1
        else:
            high = mid-1
        for i in range(low,high+1):
            res = a[i]
            res = min(a[i] , res)                 
        return res
    
a = [3,4,5,6,7,8,9,10,1,2]
n = len(a)
print(midid(a,n))

def ggg(a,n):
    res =a[0]
    for i in range(0,n):
        # if a[i] < res:
            res = min(res,a[i])
    return res

a =[4,5,6,7,8,9]
n = len(a)
print(ggg(a,n))

def visi(a,n):
    visi = [False]*n
    astrix = []
    for i in range(0,n):
        if visi[a[i]] == True:
            astrix.append(a[i])
        else:
            visi[a[i]] = True
    return astrix
a = [1,2,2,3,4,4 ,7,7]
n =len(a)
print(visi(a,n))
def bulidng(a,n):
    count =0
    res =0
    for i in range(1,n):
         if a[i-1] <a[i]:
             count+=1
         if a[i-1] > a[i]:
             count-=1
         else:
             res = count
    res = count
    return res
a =[1,4,5,2,3,2,4]
n =len(a)
print(bulidng(a,n))
def building(a,n):
    count =0
    if a[0] <= a[n-1]:
        building = a[0]
    else:
        return 0

    for i in range(1,n-1):
        count+=1

    trapped_water = building*count
    return trapped_water

a = [4,1,2,4,6] 
n = len(a)
print(building(a,n))

def inmm(a,n):
    count =0
    for i in range(0,n):
        if a[i] == 0:
            continue
        if a[i] != i+1:
            return i+1
        
    return n+1

a = [0,1,3,4,5]
n =len(a)
print(inmm(a,n))

def naives(a,n,k):
    spit = n//k
    res = 0
    for i in range(0,n):
        count =1
        for j in range(i+1,n):
            if a[i] == a[j]:
                count+=1
        if count> spit:
            res+=1

    return f"the element are {res}"

a = [1,2,3,4,4,4,4]
n = len(a)


print(naives(a,n,4))

def naives1(a,n,k):
    split = n//k
    res =0
    rest =0
    while res<n-1:
        count =1
        for i in range(res+1,n):
            if a[i] == a[res]:
                count+=1
        # print(count)
        if count > split:
            rest+=1
        res+=1
    return rest

a = [3,1,2,2,1,3,3,2,4,4,4,4]
n= len(a)
print(naives1(a,n,4))
a =[1,2,3,3,3,2,2,1]
print(a.count(1))

def given_sum(a,n,sum):
    res =0
    i= 0
    while i<n:
        count =0
        for j in range(i,n):
            count+=a[j]
            if count == sum:
                return i ,"to" ,j 
        i+=1
    return res
a =[1,2,3,7,5]
n =len(a)
print(given_sum(a,n,3))

def eaaapp(a,b,n1,n2):

    left = []
    right = []
    i1 = n2//2
    i2 = (n1+n2+1)//i1
    for i in range(0,n1):
        if i<i1-1:
            left.append(a[i])
        else:
            right.append(a[i])

    for i in range(0,n2):
        if i<i2:
            left.append(b[i])
        else:
            right.append(b[i])

    leftmax = max(left)
    rightmin = min(right)
    median = (leftmax+rightmin)//2
    print(right)
    print(left)
    
    print(i1,i2)
    return median

a = [1,2]
b = [2,3,4]
n1  = len(a)
n2 = len(b)
print(eaaapp(a,b,n1,n2))


def sliding(a,n,k):
    res =0
    for i in range(0,n):
        sum = 0
        for j in range(i,k):
            if k > n:
                break
            sum+=a[j]
        res = max(res,sum)
        k+=1
    return res
a = [5,-10,6,90,3]
n =len(a)
print(sliding(a,n,2))

def easliding(a,n ,k):
    sum =0
    res= 0
    i =0
    while i<k:

        sum+=a[i]
        res = sum
        i+=1
    for i in range(k,n):
        sum+=a[i]-a[i-k]
        res = max(res,sum)
    return res
a =[1,8,30,-5,20,7]
n =len(a)
print(easliding(a,n,3))

def equilibrim(a,n):
    eq =1
    
    while eq<n:
        sum1 =0
        sum2 =0
        for i in range(0,eq):
            # sum1 =0  inko yha lgane se hr barr jb bhi loop chlega tb hi ye dono kam as a 0 nhi krenge
            sum1+=a[i]
            
        for i in range(eq+1,n):
            # sum2 =0
            sum2+=a[i]
        if sum1 == sum2:
            return eq , True
        
        eq+=1
    return False

a =[3,4,8,-9,20,6]
n = len(a)
print(equilibrim(a,n))

def prefix(a,start,ending):
    if start == 0:

      res =sum(a[0:ending+1])
    else:
        # minus = a[0:start]
        res =sum(a[start:ending+1])
        
    return res

a =[2,8,3,9,6,5,4]
print(prefix(a,0,1))
# print(sum(a[0:3]))