
def m(*args):
   p = 1
   for num in args:
      p *=num #               p = 2*1, then p = 2*1*3 , then p = 1*2*3*4
   return p             #         ek loop chala diya jisme p ki multiply karte jao num se 
k = m(2,3,4)
print(k)
 