class Employee:
    def __init__(self):
        self.__name = "Dhananjay" # by using __ in name you cant acess to self.name directly n=but can indirectly
a = Employee() # now this obj go in the init method, 
# print(a.__name)  you cant acess it directly
print(a._Employee__name) # this is an indirect way to acess it