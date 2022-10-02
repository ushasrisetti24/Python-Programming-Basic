def runningSum(nums):
    li=[]
    for i in range(len(nums)):
        sum=0
        for j in range(0,i+1):
            sum+=nums[j]
        li.append(sum)    
    return li

li= list(map(int,input().split()))
print(runningSum(li))
