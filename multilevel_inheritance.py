#ek se dusri , dusri se teesri
class animal:
    def __init__(self,name,species):
        self.name = name           # again i want to remind that this is a constructor who take initial value of that instance so that you can use it in deifferent methods
        self.species = species

    def show(self):
        print(f'the name {self.name}')
        print(f'the speci {self.species}')
class dog(animal):
    def  __init__(self, name,breed):
        # super().__init__(name,species="dog") # here ou dont have to use self paramtere because it will automatically passs
        animal.__init__(self,name,species="dog")  # the thing use that use have to use self parameter here 
        self.breed = breed

    def show(self): # this is called overwriting of a method
        animal.show(self)
        print(f'breed = {self.breed}')
class another(dog):
    def __init__(self,name,colour):
        dog.__init__(self,name,breed="bull_dog")
        self.k = colour
    def show(self):
        dog.show(self)
        print(f'colour:  {self.k}')
o = another("shampoo","black")
o.show()
# this method will first call the show  method of  dog()
# then it will call the animal show detail method 
