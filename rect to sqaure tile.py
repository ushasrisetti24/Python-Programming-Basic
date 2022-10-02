lnt= int(input())
bre= int(input())
i=1
sq=0
n1=n2=0
while(i<=lnt and i<=bre and i<=(lnt*bre)):
    if(lnt%i==0 and bre%i==0):
        sq= i
        i+=1
        
n1= lnt/sq
n2= bre/sq
print(n1*n2)





