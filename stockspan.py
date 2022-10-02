def createspan(price, n, s):
    s[0]=1

    for i in range(1,n,1):
        s[i]=1
        j=i-1

        while((j>=0) and price[i]>=price[j]):
            s[i]+=1
            j-=1

def printarray(arr,n):
    for i in range(n):
        print(arr[i], end= " ")

price= [100,80,60,70,60,75,85]
n= len(price)
s= [None]*n

createspan(price,n,s)
printarray(s,n)
