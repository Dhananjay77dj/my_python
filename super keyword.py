# class parentclass:
    
#     def parent(self):
#       print('this  is a parent class')
# class childclass(parentclass): # this will move all the atribute or method in this child class to make it a child like transfer of genes
#     def parent(self):
#        print("dhananjay")
#        super().parent() # by using super you can call the method of parent class 
#     def child(self):
#        print('this is a child class')
#        super().parent() # this will run the parent method of the PARENT CLASS

# x = childclass()
# x.child()
# x.parent()# from this you can call the parent method of child class

class employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
class student(employee):
    def __init__(self,name,id):
     super().__init__(name,id) # from this you are calling the parent class method __init__(name , id)
x = student('dhananjay',21236874)
print(x.name)