class vector:
    def __init__(self,i,j,k): # i,j,k are parameter which has no value of itself 
        #  tumhe i,j,k  ki jagah pe khud hi kuch dalna/ value deni  padega/padegi
        self.i  =i # from this you are telling python that what is the value of i 
        self.j  =j # from this you are telling python that what is the value of j
        self.k  =k  # from this you are telling python that what is the value of k
    def __str__(self): # to make it readable
        return f"{self.i}i + {self.j}j + {self.k}k"
    def __add__(self,x):
        return f"{self.i + x.i}i + {self.j + x.k}k + {self.k + x.k}k"  #In __init__(), other parameters are used to initialize the object's attributes.
       #In __add__(), the other parameter is used to define how the addition operation works between the instance (self) and another object (other).





v1 = vector(3,4,5)  # here 3 is self.i , 4 is self.k, 5 is self.k
v2 = vector(5,6,7)
print(v1 + v2)
# class v:
#     def __init__(sel,c,v): # here sel,c , v are parameters which is not defined or has no value that id the difference between a parameter and an argument

#         sel.name = c
#         sel.age = v
# c = v("dhananjay",17)
# print(c.name)