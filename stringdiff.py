c1=0
c2=0
s= input()
''' l= list(s)
     for c in l:''' #convert directly into list from string input using
for c in s.strip():  
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
