class shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def area(self):
        return self.x*self.y
class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius*self.radius
    
s = shape(10,28)
print(s.area())
c = circle(4)
print(c.area())