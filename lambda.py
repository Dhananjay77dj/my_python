#you can a function into a function 
def aplly(g,y):
    return g(y)
double  = lambda x : x*x                     #by this you can add function into a function
triple = lambda x: x*x*x
add = lambda number: sum(number)            # this function name aplly return you 
#                                                                   duoble(5)
# you can make a function without def like
cube = lambda x:x*x
print(cube(5))