# class myclass:
#     def __init__(self,value):
#       self.value = value
#     def show(self):
#       #  self.value = value
#        print(f"your value is {self.value}")
# obj =myclass(10)
# obj.show(11)
class MyClass:
    def __init__(self, value):
        self.value = value
    
    def show(self):
        print(f"Your value is {self.value}")
    @property
    def ad(self):
       return 10*self.value
    @ad.setter
    def ad(self,new_value):
        dd = new_value/10
        return dd
obj = MyClass(10)
# obj.show()  # Output: Your value is 10
obj.show()  # Output: Your value is 10
# print(obj.ad)
obj.ad = 200

print(obj.ad)