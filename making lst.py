l=[1,2,3,44,55,666,77777,4,3,5]
print(l)
l.append(88 )#this will add any number tot e list
print(l)
l.sort()# this will rearnge the number of list
print(l)
l.sort(reverse = True) # this will reverse the list
print(l)
l.reverse()# this will also reverse the list
print(l)
print(l.index(3))# this will give the postion  of the give number ( dont forget that its counting starts from 0 ,1,2,3,4...)
print(l.count(3)) # this will tell us that how many times a number occurs

l[5]= 0 # this will insert a number in the given place
print(l)
l[0]= 32 #this will REPLACE the  0 position with 32
print(l)
l.insert(0,44) # this will TAKE  the 0 postion and fill it with 44 and increase the lost length
print(l)
m= [33333,444444,555555]
l.extend(m)# this will add the new "m" list in the l list  
print(l)
