import pyttsx3

# name = ['rahul', 'priti']
engine = pyttsx3.init()

# for n in name:
while True:
    x = pyttsx3.init().say(input(f'enter-- '))

    engine.runAndWait()