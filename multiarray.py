dimensions= [int(x) for x in input().split(',')]
rownum= dimensions[0]
colnum= dimensions[1]
myarray= [[0 for col in range(colnum)] for row in range(rownum)]

for row in range(rownum):
    for col in range(colnum):
        myarray[row][col]= row*col;
             
print(myarray)             
             
                 


             
                 
             
