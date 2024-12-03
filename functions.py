#let suppose we want to find the geometric mean of two numbers
a= 7
b=9
gmean = (a*b)/(a+b)
print(gmean)
#but what if we want to find another gmean of two differernt number then what ? kya phirse sara priogramm likhna padega, nahi
# iske liye ham log khud ka function banayege by def
def gmeanCALCULATOR(a,b): #this is a function made by me
    mean = (a*b)/(a+b)
    print(mean)
def ifgreater(a,b): #this is an build function made by me
    if (a>b):
       print("a is greater than b")
    else:
        print('b is greater than a')
def iflesser(a,b):#user define fucntion
    pass #kyuki abhi function ki body nahi likhi hai to pass likhna padega nahi to error aa jaayega
gmeanCALCULATOR(a,b)
ifgreater(a,b)


