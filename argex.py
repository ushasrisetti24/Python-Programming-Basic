def myfun(arg1, *argv):
    print("first arguement= ",arg1)
    for arg in argv:
        print("Next arguement= ",arg)

myfun('Hello','this','is','usha')        
