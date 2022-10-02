s= input().split(" ")
s1= list(map(list,s))
c1=0
c2=0
for c in s1:
    if(c=='*'):
        c1+=1
    if(c== '#'):
        c2+=1

if(c1>c2):
    print(c1-c2)
elif(c1<c2):
    print(c1-c2)
else:
    print(0)    
