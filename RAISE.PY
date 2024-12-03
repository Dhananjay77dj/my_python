# user_input = input('Enter any value between one and nine (or type "quit" to exit): ')

# if user_input.lower() == 'quit':
#     print('Exiting...')
#     exit()

# try:
#     a = int(user_input)
#     if a < 1 or a > 9:
#         print('This is wrong. Please enter a value between one and nine.')
#     else:
#         print('Input is valid.')
# except ValueError:
#     print('Invalid input. Please enter a valid number or type "quit" to exit.')


a = input('enter any number or quit')
if a =="quit":
    print('okay')
    exit()

try:
      b=int(a)
      if a <5 or a >9:
        print("okay")   
           
      
except ValueError:
     print("nothing")
