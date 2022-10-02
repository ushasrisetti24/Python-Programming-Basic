n= int(input())
li=[]
od=[]
ev=[]
sum1=0
sum2=0
li= [int(x) for x in input().split(" ")]
for i in range(n):
  if(li[i]%2==0):
    ev.append(li[i])
  else:
    od.append(li[i])
    
for i in ev:
  sum1+=i
ev.append(sum1)
ev.sort()

for i in od:
  sum2+=i
od.append(sum2)
od.sort()

for i in od:
    ev.append(i)
for i in ev:
    print(i,end= " ")
