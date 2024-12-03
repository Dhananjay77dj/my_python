l = [1,2,3,99,77, 6,5, 334]  # this is a list
print(l)
l.append(00)
print(l)
l.sort()
print(l)
print(type(l))# this will tell the class , ki konsi class hai jaise - number,tuple,list ...etc
print(l[7])              #you can also add any other type of data in a list
m = [1,2,3,"dhananjay", "dj", True,False]
print(m)
print(m[-5])   # this is called negative index
print(m[len(m)-5])
print(8-5)
# if 1 in l:
#     print('yes, it is .')
# else:
#     print('nahi hai')
# if 'dh' in 'dhananjay':
#     print('yes')
# else:
#     print('nahi hai isme.')
print(m[1:4])  
print(m[1:4:2])  # pehle ye 1:4 ke bich me slicing karega , phit 1:4 me 1st  number print karega and uske badd 2-2 karke jump lega ,
#samajh nahi aaya to phir se chalao program
print(m[0:len(m)])   # agar tum puchoge ki total kitne element hai to jawab hai 7 , lekin : -- ye lagake nikalna par 0 se k=ginti hoti hai 
# to element ho jayenge 6
# the process we are using is list comprehension 
# while the real making of list is like that
list=[]
list.append(1)
list.append(2)
list.append(3)              #this process is real making of list not list comprehesion
list.append(5)
print(list)
number =[i for i in range(11)]  # first i is a variable  whereas  second i is for loop
print(number)

