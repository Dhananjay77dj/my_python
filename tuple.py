# tuple = ('hi my name is dhananjay',)
# print(type(tuple), tuple)
# # tuple[0]=3  you can not change the value of a tuple . You can do this only in string.
# # so many of the things of tuples are as same as list
# print(len(tuple))
# k = tuple(element.upper() for element in tuple)
# print(k)
# Original tuple
kk = ('hi my name is dhananjay',)

# Print the type and the tuple itself
print(type(kk), kk)

# Tuple length
print(len(kk))

# Convert the element to uppercase and create a new tuple
k = tuple(element.upper() for element in kk)

# Print the new uppercase tuple
print(k)  # if you are using the word tuple as a variable then it will shoe error because tuple is an inbuilt function in python
