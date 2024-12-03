class employee:
    companyname = "dj.aai" # this is a class variable
    noemployee = 0
    def __init__(self,name):
        employee.noemployee +=1
        self.name = name
        self.raiseamount = 67 # this is an instance variable because this is associated with an instance/obj which is going to made form this
    def showdetail(self):
        print(f"the name of this employee is {self.name} his number is {employee.noemployee} who works in {employee.companyname}") 
emp1 = employee("Dhananjay") #                           {self.noemployee} is same as {employee.noemployee}
emp1.showdetail()
employee.showdetail(emp1)
emp2 = employee("ayesha") # now this will make a obj from this class 
print(emp2.raiseamount)
emp2.raiseamount = 8989
print(emp2.raiseamount)
emp2.companyname = 'dj.aai india'
emp2.showdetail()
employee.companyname = 'spacex '
emp2.showdetail()
emp3 = employee('kratika')
emp3.showdetail()
