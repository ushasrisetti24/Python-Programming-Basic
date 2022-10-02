from sys import maxsize

def createStack():
    stack= []
    return stack

def isEmpty(stack):
    return len(stack)==0

def push(stack,item):
    stack.append(item)
    print(item+ " pushed to the stack")

def pop(stack):
    if(isEmpty(stack)):
        return str(-maxsize-1)
    return stack.pop()

def peek(stack):
    if(isEmpty(stack)):
        return str(-maxsize-1) #returns - infinite
    return stack[len(stack)-1]

stack= createStack()
push(stack,str(10))
push(stack,str(20))
push(stack,str(30))

print(pop(stack)+"poppped from stack")
print(peek(stack))
    
    
