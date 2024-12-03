y = 20 # this is a global variable
def fun():
   global y # this will siply change the global variable to 89
   y = 89
   print(y)
fun()
print(y)
