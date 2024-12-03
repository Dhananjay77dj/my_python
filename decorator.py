def my_decorator(fun): # here fun is the function that you want to modify in this case it is say()
    def wr():#    my_decorator me pehli cheeze hamesha script ka pehla function hoga
        print('hi how it going on')
        fun()
    return wr
@my_decorator

def say():
    print('hello')
def dj():
    print('hoo hooooooo')

say()  # now this function will go  in the my_decorator function which is acting as a decorator (which decorates a function)
dj()

