class student:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    @classmethod         # now this method is a class method because we use @classmethod  
    def fromstr(cls,string): # the cls here  is s2 = student  and string here is .fromstr(str)
        return cls(string.split('-')[0],string.split("-")[1])    
s1 = student('dhananjay','10000')
print(s1.name)
stri = 'dj-34444' #                    in fromstr   string = stri = ' dj - 34444'
s2 = student.fromstr(stri)   # this will work as same as s1  = student('dhananjay','10000')
print(s2.name)

# a = 'dhananjay-12-python'
# print(a.split("-"))     this will make a string of this a variable's data
# # print(a.split('2'))
# print(a.split("-")[2])   
# x = 'dhananjay-345678' 
# s2 = student(x.split('-')[0],x.split('-')[1])
# print(s2.name)
# print(s2.salary)
