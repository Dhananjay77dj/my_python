#using more than one inheritance in code
class A:
    pass
class B(A):  # single inheritance
    pass
class C(A):
    pass
class D(B,C): # multiple inheritance    
    pass
#  the whole stuff is called multilevel inheritacne

# now exmaple of hierarchical inheritance 
class baseclass:
    pass
class d1(baseclass):
    pass
class d2(baseclass):
    pass
class d3(d1):
    pass
