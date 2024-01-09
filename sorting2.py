a = [1,4,4,1,0,1]
k = 5
count = [1,3,0,0,2]
index =0
for i in range(k):
 for j in range(count[i]):
    #  print( j , end="")
    a[index] = i
    print("count" , count[i] )

    print("a[index]" , a[index] )

    # print(a[index]) , print(i , end="")
    index+=1

print(a)

def cycle(a,n):
  count=0
  res =0
  for j in range(0,n):
    count = 0
   

    for i in range(0,n):
    
     if a[j] > a[i]:
        count+=1
    else:
      a[count] , a[j] = a[j] , a[count]
    # res+= 1

  return a

a =[20,40,50,10,30]
n =len(a)
print(cycle(a,n))
# a = [890,789,678]
# # s =max(a)
# s = max(a)
# # for i in a:
# #    a  = (i%2)

# # print(a.count(890))
# print(a)

# print(319%10)

# index =(319//1)%10
# print("index" ,index)
# s   = [1,2,3,4,5,6]
# a = [x in a for x in range(10)]
# print(a)
# bucket = [[]for i in range(5)]
# bucket[i] = range(19)
# print(bucket[i])
# if s[0] < bucket[i]:
#   print(s[0])

# h ="000" , "678678"


def zero_one_two(a,n):
  j =0
  for i in range(0,n):
    if a[i] <1:
      j+=1
    if a[i] == 1:
      a[i] , a[j] = a[j] , a[i]
    
  # a[i-1] ,a[j] = a[j] ,a[i-1]

  return a
a = [0,2,1,2,0]
n =len(a)
print(zero_one_two(a,n))

def gg(a,n,k):
  # if k >=n:
    # return -1
  for i in range(n):
    if a[i] == k:
      return i
  return -1

a =[3,2,10,4,20]
n =len(a)
print(gg(a,n,20))
# def ss(a,n,k):
#   l =0
#   h =n-1
#   while l<h:
#     mid = (l+h)//2
#     if a[mid] == k:
#       return mid
#     if mid<h and a[mid+1] == k:
#       return mid+1

#     if mid>l and a[mid-1] == k:
#       return mid-1
    

