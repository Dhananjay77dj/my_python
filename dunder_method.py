class employee:
    name = "dhananjay"
    # def __init__(self,name):  this is only a constructor. No one can be this
    #     self.name = name
    def __len__(self):
          i = 0
          
          for c in self.name:
               i = i+1
            #    print(i)
          return i
    def __call__(self):
         print('hi how are you')
e = employee()
print(e.name)
print(len(e)) # this will call the len method
e()