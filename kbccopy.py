print('BOHOT BOHOT SUAGAT HAI AAPKA HAMARE IS SHOW " KON BANEGA CROREPATI " ME')
import random


rs = ('Which spacecraft was the first to land astronauts on the Moon?',
        "WHAT IS THE LARGEST PLANET IN OUR SOLAR SYSTEM?",
        "WHAT DOES THE ABBREVIATION 'GPS' STAND FOR IN THE CONTEXT OF TECHNOLOGY?",
        'WHICH SPACE TELESCOPE IS FAMOUS FOR ITS STUNNING IMAGES OF DEEP SPACE OBJECTS AND PHENOMENA?')
rs = random.choice(list)
print(rs)
if rs =="Which spacecraft was the first to land astronauts on the Moon?":
    input =input("A) Apollo 1\nB) SPACE SHUTTLE\nC)  SOYUZ\nD)  MARS ROVER ") 
    if input =="a":
        print("3,20,000    CONGRATULATIONS   !    ")
    else:
        print('YE UTTAR GALAT HAI')
if rs == "WHAT IS THE LARGEST PLANET IN OUR SOLAR SYSTEM?":
    input=input('A) Earth\nB) Venus\nC) Jupiter\nD) Saturn')
    if input =="c":
        print("3,20,000    CONGRATULATIONS   !  bohot hi sahi    ")
    else:
        print('YE UTTAR GALAT HAI')
if rs =="WHAT DOES THE ABBREVIATION 'GPS' STAND FOR IN THE CONTEXT OF TECHNOLOGY?":
    k= input("A) Global Positioning System\nB) GeProgramming Standard\nC) Groundbreaking Photon Sensor\nD) Gravitational Propulsion System")
    if k == "a":
                print('congrats ! you empty the bank account of KBC')            
    else:
                print('dhyanwad  ,  thode rupay bach gaye hamare !!')
elif rs =="WHICH SPACE TELESCOPE IS FAMOUS FOR ITS STUNNING IMAGES OF DEEP SPACE OBJECTS AND PHENOMENA?":
    image = input("A) Kepler Space Telescope\nB) Hubble Space Telescope\nC) James Webb Space Telescope\nD) Chandra X-ray Observatory  ")
    if image =="c":
          print('YOU WIN 12,000 ')
    else: 
          print("kuch bhi nahi milaa")

print('welcome to kaun banega corepati')
list=['what is the name of our moon ?',"luna","ceres","saturn","titan",1,
       'what is the name of our moon ?',"luna","ceres","saturn","titan",2,
         'what is the name of our moon ?',"luna","ceres","saturn","titan",1]
for i in list:
    print(i)
    if list == list[0]:
        print(list[1])    ,             print(list[2])
        print(list[3]),                 print(list[4])
    elif list ==list[5]:
        print(list[6]),                 print(list[7])
        print(list[8]),                 print(list[9])
    else:
        pass