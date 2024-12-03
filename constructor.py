# class person:
#     name = 'Dhananjay'
#     ocu = "Creator "

#     def info(self):   # apna method define kar rahe ho to self dena padega  
#         print(f'{self.name}is a {self.ocu}')
# a = person()
# a.info()
class person:
    def __init__(self,n,o):     # this will run automatically       called a constructor
        self.name = n #  self.name matlab self ke andar ka naam = n
        self.occupation = o  # self.occupation matlab slef ke andar ka occupation == o
        print(f"{n} is a {o}")
a = person('Dhananjay',"Creator") # here the person() is first argument  ,  this is also act as an self here in which the dhananjay and creator are one and second argument
# dhananjay is second argument                                              all three argument run automtially
# creator is the third argument
class person:
      def __init__(sd,a,y):#a constructor in a class is a method that helps set up the initial state of an object
      #  x.name = a
      #  x.cu = y
       print(f"hi how are you {a} the {y}")
x = person("dhananjay","creator") # from using person() python inderstand that you want to create a obj from class  

