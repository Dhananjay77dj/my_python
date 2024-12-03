print("hi my name is \nand what your name")
print("hi my n\"ame is \"DHNANANJAY what is your")
print(5,6,7 ,sep="~", end="  007")# sep = "" separate karta hai , end aane wale statement se pehle kuch print karta hai 
print("DJ") 
b=89
print(type(b))#typr() batata hai ki variable ka type kya hai
a= complex(8,6)#ye complex number banane ke liye
print(a)
print(type(a))
print(15//6)#// isse point ke baad wala number haat jaata hai
print(15%6)#ye (%) tumko remainder dega 
print(5**3)#** matlab 5 raise to the power 3
                     #int ek string ko integer me convert kar deta hai
x =float(7) 
y =(9.1)
print(x + y)
vishnu=("there are 9 character ")
name = "dhananjay"
print(name[1])# ye [1] kisi cheez ka pehla akshar deta hai . Dusra likho ge to susra , aur tisra likho ge to tisra.
for character in name :
    print(vishnu )# for statement se tum dekh sakte ho ki kitne chracter hai puri string me jo tumne banayi hai. Aur jis tareeke se dekne hai use tarike se sekh sakte ho
mango = 'aam admi         party'
len1= len(mango) # len se hame length pta chalti hai
print(len1)

print(mango[:4])#        [0:4] this gives the words which are on 1 2 3 place
print(mango[-5:-3])  #  [4: 9] this include   4 but not 9 , (less than 9 )
nm = 'harry'
         
print(nm[-4:-3])
name = "dhananjay is the greatest"
print(name.replace("dhananjay","dj the Ceo")) #replace the object that you choose from an another element choosen by you
print(name.split())              # convert you vaariable into a string
blog= 'hi my name is DHANANJAY'
print(blog.capitalize())                #  capitalize the first letter                                                                                                                                                                                              
print(blog.upper())
str = 'i am the ceo of india '
print(str.center(100))
print(len(str))
print(str.count('am'))  #   count hame batata hia ki jo word hsmne select kiys vo kitni baar aa raha hai

print(str.endswith('a'))  #  ye batata hai ki kya str wala variable "a" pe end ho raha ahi ya nahi  
print(str.endswith("m",1,4)) 
print(str.find('ceo')) # this will provide the index of the selected variable . Index matlab number of place
print(str.index('ceo'))  # this wil also provide the index lekin agar koi element string me nahi hai to yeh error de dega and find me error nahi deta balki 1 deta hai
print(str.islower())
print(str.isupper())
# startwith
print(str.title())
digits = (1,2,3,4,7,8,9,0)
print(max(digits))
print(min(digits))
square =[ value**2 for value in range(1,8)] # this will give the square of all the numbers and iske liye []  squarea brckets lagane honge
print(square)
age = int(input('enter you age: '))
if age >28:
    print('loll')
if age ==29:
    print('29')
if age ==89 :
        print('lolll')
else :          #          CONDITION OPERATOR -   >,<, ==, >= , <= , !=
    print('noo')
myname = ('asdfg') # this will simply print all the elements of your name in row wise
for i in myname:
     print(i)
i  = int (input('enter your name  '))
while i < 3:
     i = int(input('enter again'))

    