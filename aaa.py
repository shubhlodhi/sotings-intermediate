# a = [[10,3] ,[5,2] ,[3,4] ,[9,2] ,[2,5]]
# # for i in range(len(a)):
# (a.sort(key = lambda x : x[1]))
# print(a)
    # print(a[i][1].sort())
    # print(s)
# print(s)
count =1
# w =2
d =[]
s =d.append(1)
# s =d.append(2)
a =[]
a.append(s)
print(a)
l={}
# l[["shubh"]] = 34
print(l)



def abso(a,n,k):
    for i in range(0,n):
        for j in range(i+1,n):
            l = j+1
            while l<n:
                add = a[i]+a[j]+a[l]
                if add == k:
                    return a[l]
                
                l+=1
    return -1

a =[1,4,45,6,10,8]
n =len(a)
print(abso(a,n,13))

# m = {k: v in k , v in sorted(m.items()) , key=lambda item:item[1] }
