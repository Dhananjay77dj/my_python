# in object iriented programming 
# classes are like  TEMPLATE
# and obj are like format made by using format 

# CREATIING A CLASS (TEMPLATE  TYPE)

#"class" in Python is a set of instructions for creating a certain kind of thing, and an 
#"object" is a real thing that's made based on those instructions.

class info:
    name = "elon musk"
    occupation = 'engineer'
    networth = '22340 $'     #        YOU CAN ALSO SAID THAT THIS IS DEFAULT INFORMATION
    def write(self):
        print(f'{self.name} is a good man') #
# print(info.name)  
# info.name = 'dhananjay'
# print(info.name)
# a=info()  # here the variable store the class, BY  prining a. something you are making a obj by template
# info().write()  # now you are running the programm write from info
# info().name
#     IS YOU ARE USING PARENTHESIS  THEN YOU ARE CALLING A FUCNTION
info.name ="dhananjay"
# info().write()
print(info().networth)
b = info()
c = info()
a = info()
a.name = 'dhananjay'
b.name ='bill gates'
c.name = "arnold"

print(a.write(),b.write(),c.write())
