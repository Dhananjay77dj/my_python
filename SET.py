set = {9999,2,2,2,3,3,4,5,9,8,4,88}
print(set)   # it is a collection of objects like a set , not necessary that the set is in order
#cant add value in set
for value in set:
    print(value)
s1 ={1,2,3,4,}
s2 ={4,6,7,8,}
print(s1.union(s2))       # this is just like math set theory
s1.update(s2)                #this will update the set or this will add the s2 set in s1

print(s1)
# you can also use intersection in this 
print(s1.intersection(s2))
st1={3.6,33,55,6,77,3,23,45,"delhi",89}
st2={44,55,6,7,22,33,"delhi"}
print(st1.symmetric_difference(s2))       #this will give the value which are not common in two set
print(st1.difference(st2))             #this is like setA - set B 
print(st1.issuperset(st2))             #this will tell if st1 is superset of st2 or not
print(st1.issubset(st2))               # this will tell if this is a subset ir not
      # to add an element in the set 
st1.add('i am ironman')
st1.remove(3.6)       #this will remove an element from the set ans shows error if the element is not present
print(st1)
item = st1.pop()  #this will pop a random value from th e set
print(item)
del st1 # this will delete the whole set from the script
print(st1)
