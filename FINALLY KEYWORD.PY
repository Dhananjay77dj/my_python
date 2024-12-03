def fun():
    try:
     l =(1,2,3,4)
     i=int(input('enter'))
     print(l[i])
     return 000
    except:
      print('wrong')
      return 4
    finally:
      print('it will always executed') #This is the most important programm , agar tumne return kar diya hai
      #                                 phir bhi ye finally return karega
      

x =fun()
print(x)