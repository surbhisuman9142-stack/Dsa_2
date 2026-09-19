def range_sum(A,Q):
    res = []
    for query in Q:
        s = query[0]#start index at left
        e = query[1]#start index at right
        current_sum = 0
        # Iterate from index "s" to index "e" inclusive
        for j in range(s,e+1):
            current_sum += A[j]
        res.append(current_sum)
    return res
A = [-3,6,2,4,5,2,8,-9,3,1]
Q = [[4,8],[3,7],[1,3],[0,4],[7,7]]
print(range_sum(A,Q))

