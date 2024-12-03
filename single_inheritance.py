class animal:
    def __init__(self,name,animal):
        self.name = name
        self.t = animal


    def sound(self):
        print('The sound of this animal is vooo')
class bark(animal):
    def __init__(self,name,bread):
        self.bread = bread
        self.name = name
        
        # animal.__init__(self,name,animal)
        super().__init__(name,animal)  # both lines are same      
    def sound(self):
        print('bark')
d = bark("cat","cute")
d.sound()