import time 
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate',200)
def remind():
    engine.say( 'sir ,  its time for a break '   )
    engine.runAndWait()


try:
    while True:
      remind()   # if this will stop then except will run 
      time.sleep(15)
except KeyboardInterrupt:
   engine.say('boss,, your  reminder is stop now')
