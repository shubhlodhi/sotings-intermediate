def circular(a,n ):
    res =0
    for i in range(0,n):
        curr_value = a[i]
        curr_sum = a[i]

    for j in range(1,n):
        index =(i+j)%n
        curr_value+=a[index]
        curr_sum = max(curr_value, curr_sum)

    res = max(res,curr_sum)
    return res

a =[8, -8, 9, -9, 10, -11, 12]
n =len(a)
print(circular(a,n))