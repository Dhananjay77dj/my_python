class employee:
    def __init__(self,name,id): #constructor , this will initiate the value
          self.name = name
          self.id = id
    def showdata(self): #by writting self in any method it will take the object (or future obj) as it first argument
         print(f"The name of emloyee {self.id} is  {self.name}")
e = employee("Dhananjay",678) # now this is an obj
e.showdata()  

class programmer(employee): # from this you are making a new class in which there is a already a employee calss
     def language(self):#the self here is putting your class "e2" to language()
          print("This is python")
e2 = programmer('dhananjay', 898)
e2.language()
