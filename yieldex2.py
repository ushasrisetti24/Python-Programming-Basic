#program to print numbers divisible by 5 and 7 between 0 and n

def numgen(n):
    for i in range(n+1):
        if i%35==0:
            yield i


n= int(input())
values= []

for i in numgen(n):
    values.append(str(i))

print(",".join(values))    
