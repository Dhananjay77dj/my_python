# f = open('.txt','r')
# while True:
#     line = f.readline()
#     m1 = line.split('.')[0]
#     # print(f"hi your dialouge is {m1}")
#     print(m1)
#     if not line:
#         break
# #     print(line)
# # # print('hola')
f = open('dhananjay.txt','w')
# f.write(line)
line=("hi how are you \n i am good ")
f.writelines(line)

f.close

