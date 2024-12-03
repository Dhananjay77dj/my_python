# a = True
# print(a:=False )
list = [1,2,3,4,5]
# print(list.pop())
while (n:= len(list)) >0:  # when you write n:= len(list), you are both calculating the length of the list and assigning it to the variable n in one step
    print(list.pop())
# n  = len(list)
# while n >0:
#     print(list.pop())