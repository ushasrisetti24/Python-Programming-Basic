def merchant(n,ar):
    se= set(ar)
    sum=0
    for each in se:
        if(ar.count(each)>=2):
            sum+= (ar.count(each))//2
    return sum        

n= int(input())
ar= list(map(int,input().rstrip().split()))
result= merchant(n,ar)
print(result)
