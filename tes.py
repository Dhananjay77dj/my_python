import pyttsx3 

engine = pyttsx3.init()

while True:
    text = input("Enter the text: ")
    if text == "break":
        break 
    else:
        engine.say(text)

engine.runAndWait()
