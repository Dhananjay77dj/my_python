# x = [1,2,3]
# print(dir(x))

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.version= 2
p = person('dhananjay',17)
print(p.__dict__)
print(help(person))  # this will tell all the information about the person because if you know nothing about the class then it will help you 