import datetime
import random
from time import sleep
import pygame # for voice services and GUI
#import machine #for controlling prossesor and microphone and speaker

today = datetime.date.today()
cd = datetime.datetime.now()
ct = cd.strftime("%H:%M")

#intro for commandline
name = input('What would you like me to call you: ')
sirmiss = input("would you like me to call you sir or miss ")

intro = ['Hello ' + name, 'Hi ' + sirmiss, 'Hello ' + sirmiss, 'Hi ' + name] 
TC = ["Good","good you","good how are you doing"]

while True:
    Termanal = input(random.choice(intro)).strip().lower()
    
    
    if Termanal == "hello" or Termanal == "hi" or Termanal == "whats up":
        random.choice(intro)
        
    elif Termanal == "time" or Termanal == "What time is it" or Termanal == "clock":
        print(ct)
                 
    elif Termanal == "system":
                 width = 128
                 higth = 64
                 window = pygame.display.set_mode((width,higth))
                 
    elif Termanal == "whats on my sceadule":
                 print()
                 
                 
    elif Termanal == "add something to my camender":
                 Cal = input("What would you like to add to your Calender and on what day,month,year ")
                 t = input("WHat time would you like me to alert you at")
                 
    elif Termanal == "hi how are you" or Termanal =="Hello How you been" or Termanal == "how are you":
                  print(random.choice(TC))
                  
    elif Termanal == "what is your name":
      print("My name is Pixel or commonly known as Personal Inteligence example for Enviormental Languages")
                 
    else:
                 print("I don't understand please rephrase the question")
