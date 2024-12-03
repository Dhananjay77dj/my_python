class library:
#    total_book = 0 this will be a class
   def __init__(self):
      self.nobook = 0 # this is an intance variable
      self.books = [] # this is an instance variable

   def addbooks(self, books):
      self.books.append(books) 
      self.nobooks = len(self.books)
   def showinfo(self):
      print(f"he library has {self.nobooks} books")
li = library()
li.addbooks("harry potter")
li.addbooks("harry potter")

li.addbooks("harry potter")
li.addbooks("harry potter")
li.addbooks("harry potter")
li.addbooks("harry potter")
li.addbooks("harry potter")
li.addbooks("harry potter")
li.addbooks("harry potter")
li.addbooks("harry ")
li.showinfo()