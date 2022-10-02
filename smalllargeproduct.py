n=int(input())
arr= list(map(int,input().split()))
sum1=0
sum2=0
fin=[]

for i in range(0,len(arr)):
    sum1=0
    sum2=0
    for j in range(i+1,len(arr)):
        if(arr[j]>arr[i]):
            sum2+=arr[j]
        elif(arr[j]<arr[i]):
            sum1+=arr[j]
            
    fin.append(sum1*sum2)

for i in fin:
    print(i,end=" ")
