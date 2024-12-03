def cube(x):
    return x*x*x
l =[1,2,3,4,5,6]
newl =[]
# item = 0
# for item in l :
#     item = item +1
#     newl.append(cube(item))                       now there is a short cut for that
    
# print(newl)

newl = list(map(cube,l))          #  pehle map me dedo function phir dedo vo list jiske har element par aap function apply karoge 
print(newl)


# FILTER

def filter_function(a):
    return a>4         # after putting the value of a , this will return true or false if true then a>4 if false a<4 
new2 = list(filter(filter_function,l))        #        this will take the value of l into filter_function
print(new2)

 # LAMBDA
new3=  list(map(lambda x: x*x*x, (l)))  
print(new3)
# REDUCE
from functools import reduce
number = [1,2,3,4,5]
def sm(x,y) :
    
    return x +y
k = reduce(sm,number)     
print(k)
