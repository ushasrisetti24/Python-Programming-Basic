class Parent(object):
    def __init__(self,name,idnumber):
        self.name= name
        self.idnumber= idnumber

    def display1(self):
        print(self.name)
        print(self.idnumber)

class Child(Parent):
    def __init__(self,name,idnumber,salary,work):
        self.salary= salary
        self.work= work
        Parent.__init__(self,name,idnumber)

    def display2(self):
        print(self.salary)
        print(self.work)

obj= Child("Krishna",2022,2000000,"law")
obj.display1()
obj.display2()
