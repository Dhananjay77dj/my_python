class math:
    def __init__(self,num): # by self a = self
        self.num = num #                 self se ham us obj ko darshate hai jispe ye method chala hai
    def add(self,num):
        self.num = self.num + num
    @staticmethod  # from this , the as method is not in class it is different
    def ad(a,b):
        return a+b
a = math(5)
print(a.num)
a.add(6)
print(a.num)
