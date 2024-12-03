# f = open('dhananjay.txt','r')
# # print(f)
# g= f.read()
# print(g)
# f.close'
# with open('dhananjay.txt','r') as f:
#      g= f.read()
#      print(g)            #isse tumhe close lagane ki zarurat nahi padegi

# f = open('dhananjay.txt','r')
# k =f.read(14)
# print(k)
# with open('dj.txt','r') as g:
#     g.seek(10)  #this will hide the first 10 words and starts reading after 10 words
#     #        
#     #       to kabhi bhi 10 chracter ke baad read karna hai to f.seek karlo
#     print(g.tell())       #this will tell ki kaha tak mene seek kiya hai

#     k = g.read()

#     print(k)
with open('hello.txt','w') as f:
    f.write('hi i am iron man')
    f.truncate(3)
     #truncate ka matlab hota hai size ko limit karna 
     # to turncate (3) likhne se file me sirf 3 character aayege
     