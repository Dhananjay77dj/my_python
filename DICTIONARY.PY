dic = {'dj': 44, "mj":89,"j":454}     #this is called a simple dictionary 
print(dic['dj'])     #you can access the value of dic like this
print(dic.keys())        #this will print all the values of a dictionary
for key in dic:
    print(key)
for key in dic.keys():                 #BOTH ARE SAME
    print(key)
for i in dic:
    print(f"the value of key  {  i} is {dic[i]}")
print(dic.items())
for key, value in dic.items():
     print(f'the value corresponding to the key {key} is {value}')
s = {22:34,33:44,555:56}
k = {22:3,33:44,55:55,}
k.update(s)
print(k)
#    to clear a dic , type s.clear()
j ={"dj":78, 78:88}
j.pop("dj")
print(j)    #this will remove the selected value
j.popitem()   #this will remove the lasr key forom the list
