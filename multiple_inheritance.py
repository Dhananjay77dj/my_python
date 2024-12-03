class employee:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f"the name is {self.name}")
class dance:
    def __init__(self,name,dance):
        self.name = name          #   in here you can add more than one class in a child class , this is called multiple inheritance
        self.dance = dance
    def show(self):
        print(f"the name of dance is{self.dance}")
class dhananjay(employee , dance   ):
    def __init__(self,name,dance):
        self.dance = dance
        self.name = name
o = dhananjay('dhananjay',"bharat_natayam")
print(o.name)
print(o.dance)
o.show()