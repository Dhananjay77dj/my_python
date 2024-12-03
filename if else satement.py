bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
age = 19
if age >= 18 :
    print("you are addult")
    print("you can vote")
       
elif age < 18 and age > 13:
    print("you Re inschool")
else:
    print ("you are a child")
a = int(input('enter a number'))
b= int(input("enter second number"))
print('YOUR FIRST NUMBER IS BIGGER THAN SEOND') if a >b else print("BOTH AREA EQUAL") if a == b else print("SECOND IS GREATER THAN A  ") if a<b else""
# THIS IS CALLED THE SHORT HAND STATEMENT OF IF ELSE . THIS MAKES YOUR CODE MORE READABLE
