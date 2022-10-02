value=[]
items= [x for x in input().split(",")]

for i in items:
    bintodec= int(i,2)
    if(bintodec%5==0):
        value.append(i)

print(",".join(value))
