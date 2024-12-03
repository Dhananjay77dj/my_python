print("welcome to the worlds most addictive game")
import random

while True:
    a = input('\nROCK  \n\nPAPER \n\nSCISSORS \n\nINPUT AS -- r,p,s (or q to quit): ')
    
    if a == 'q':
        break
    
    l = ("ROCK ","PAPER","SCISSORS")
    rd = random.choice(l)
    print(rd)

    if (rd == "ROCK " and a == "r") or (rd == "PAPER" and a == "p") or (rd == "SCISSORS" and a == "s"):
        print('Draw')
    elif (rd == 'ROCK ' and a == "p") or (rd == "PAPER" and a == "s") or (rd == "SCISSORS" and a == "r"):
        print("You win!")
    else:
        print('You lose!')
# lis = 0
# for i in lis:
#     i = i +1
#     print(i)
    
    # print(f"COMPUTER CHOICE IS {rd}")

    
