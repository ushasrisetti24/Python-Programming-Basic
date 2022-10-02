class Inputoutputstring(object):
    def __init__(self):
        self.s= ""

    def getstring(self):
        self.s= input()

    def printstring(self):
        print(self.s.upper())


sobj= Inputoutputstring()
sobj.getstring()
sobj.printstring()
        
