def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return  n * factorial(n-1)           #this is called recursion beacuse we call the function in the function
    # print is not running here 
x = int( input("enter the number\n"))
c = factorial(x)
print(c)

def fs(n):
    if n ==1:
        return 0
    elif n ==2:
        return 1
    else:
        return (n-1) + (n-2)
d = fs(9)
print(d)

    