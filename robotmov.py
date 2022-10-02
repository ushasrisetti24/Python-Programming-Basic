import math
pos= [0,0]
while True:
    s= input()
    if not s:
        break
    mov= s.split(" ")
    dir= mov[0]
    step= int(mov[1])

    if dir== 'UP':
        pos[0]+= step
    elif dir== 'DOWN':
        pos[0]-= step
    elif dir== 'RIGHT':
        pos[1]+= step
    elif dir== 'LEFT':
        pos[1]-= step
    else:
        pass

print(int(round(math.sqrt(pos[0]**2 + pos[1]**2))))
