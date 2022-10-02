n= int(input())
li=[]
for i in range(n):
    li.append(int(input()))
sum=0
for i in range(n):
    count=0
    for j in range(2,i+1):
        if(i%2==0):
            count+=1
    if(count==0):
        sum+= li[i]    
print(sum)
        
