#parameterized constructor

class constructex:
    num1=0
    num2=0
    ans=0
    def __init__(self,f,s):
        self.num1= f
        self.num2= s

    def calculate(self):
        self.ans= self.num1+self.num2

    def display(self):
        print("1st num= ",self.num1)
        print("2nd num= ",self.num2)
        print("answer= ",self.ans)
                
obj= constructex(100,200)
obj.calculate()
obj.display()
