def decimalToBinary(n):
    return bin(n).replace("0b", "")

n= int(input())
s= input()
given=[]
for l in s:
    given.append(int(l))
    print(l)
    
count=0
actual= decimalToBinary(n)
print(actual)

for i in range(len(actual)):
    if(int(given[i])!= actual[i]):
        count+=1
print(count)        
