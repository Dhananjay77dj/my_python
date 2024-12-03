marks =[ 34,56,78,9]
# place = 0
# for numbers in marks:
#     print(numbers)
#     if place ==2:
        
#         print("hi how are you")
#     place +=1
    
    
    #  how is this working
    #  pehle marks ki ek value print hogi aur place ki bhi value print hogi
    #  for loop lagne ki wajah se marks ke sath sath place ki bhi value badegi
    # jaise hi place ki value 2 hogi , vo print ho jayega
for index,mar in enumerate(marks):
    print(mar)
    if index ==2:
        print("hello")
    print(index)
