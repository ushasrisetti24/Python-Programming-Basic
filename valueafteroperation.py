def valueafterop(nums):
    x=0
    for i in nums:
        if(i=="++X" or i=="X++"):
            x+=1
        elif(i=="--X" or i=="X--"):
            x-=1
    return x

nums= list(map(str,input().split()))
print(valueafterop(nums))
