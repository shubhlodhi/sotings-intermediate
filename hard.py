def pairs(n,p):
    pairs = [ [0,2]]
    res=0
    pairs_A =[]
    for i in range(0,p):
        for j in range(i+1,p):
            if pairs[i][0] == pairs[j][0] or pairs[i][0] == pairs[j][1]:
               pairs_A.append(pairs[i])
               pairs_A.append(pairs[j])

            if pairs[i][1] == pairs[j][1]  or pairs[i][1] == pairs[j][0]:
                pairs_A.append(pairs[i])
                pairs_A.append(pairs(j))

       
        return pairs_A


    for i in range(1, len(pairs_A)):
        pairs_A[i] += pairs[i-1]

        return pairs_A
        

    

    

print(pairs(5,3))
    