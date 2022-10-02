def migratoryBirds(arr):
    x= list(set(arr))
    y= [arr.count(i) for i in x]
    w= [x[i] for i in range(len(y)) if y[i]==max(y)]
    return min(w) if len(w)>1 else w[0]
    
arr_count = int(input().strip())
arr = list(map(int, input().rstrip().split()))
print(migratoryBirds(arr))
