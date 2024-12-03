a= input('enter a number')
print(f"your multiplication table of {  a} is")
try :
    for i in range(1,11):

     print(f"{a} X {i} = ", int(a)*(i))
except Exception as e:     #if you are using exception  then it means it will give you you an inbliut error 
   print(e) 
   