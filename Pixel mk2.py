import datetime
import random
from time import sleep
#import pygame # for voice services
#import machine #for controlling prossesor and microphone and speaker

cd = datetime.datetime.now()
ct = cd.strftime("%H:%M)

#intro for commandline
name = input('What would you like me to call you: ')
sirmiss = input("would you like me to call you sir or miss (you can change this by the way) ")

intro = ['Hello' + name, 'Hi' + sirmiss, 'Hello' + sirmiss, 'Hi' + name] 


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
                 
    else:
                 print("I don't understand please rephrase the question")
