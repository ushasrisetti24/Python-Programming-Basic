def countingValleys(n, s):
    sea = 0
    valley = 0
    for i in s:
        if sea == 0 and i == 'D':
            valley +=1
        if i == 'U':
            sea += 1
        if i == 'D':
            sea -= 1
    return valley
n= int(input())
step= input()
print(countingValleys(n,step))
