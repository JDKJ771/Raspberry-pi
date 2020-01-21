import datetime

 
while True:
   import random
   hello = ['hi how can i help','wassup', 'yes']
   Pixel_Random = (random.choice(hello))
def classic_calculator():
      Num1 = input('what is your fist number')
      Num2 = input('what is your second number')
      Add = int(Num1) + int(Num2)
      print(Add)
      Mult = int(Num1) * int(Num2)
      print(Mult)
      Divide = int(Num1) / int(Num2)
      print(Divide)
      Sub = int(Num1) - int(Num2)
      Print(Sub)

def list():
      ('define words(type define than the word you want to define) \n tell you my name (make sure you type What is your name) \n What i am (type what are you) \n Tell you the time \n')
whatIsYourName = ('my name is Pixel')
WhatCanIDO = 'here is a list of things i can do'
WhatAreYou = 'I am a ANI or Artificial Narrow Intelligence'
cdt = datetime.datetime.now()
currentTime = cdt.strftime("%H:%M")
date = datetime.date.today()
Welcome = input('Welcome my name is Pixel how can i help you today')           

while True:            
      Maininput = input(Welcome)
      
      
      
      if Maininput == 'open calculator':
               print(Num1)
   
      if Pixel_Random == 'open calculator':
              print (classic_calculator)
      if Pixel_Random == 'what is your name':
              print(whatIsYourName)
      if Pixel_Random == 'can you do me a favor':
              print('whats up')
      if Pixel_Random == 'whats the date':
              print('today is' + date)
      if Pixel_Random == 'what time is it':
              print('The time is' + currentTime)
      if Pixel_Random == 'can you do me a favor':
             print('sure whats up')
   
    
      if Maininput == 'what is your name':
            print(whatIsYourName)

      if Maininput == 'what are you':
                  print(WhatCanIDo)

      if Maininput == 'Hey Pixel' :
                  print (Pixel_Random)

      if Maininput == 'what time is it':
                   print(currentTime)
      if Maininput == 'whats todays date':
                    print(date)
                              
    

         
def databank():
        file1 = raw_input()
        Note_TO_Self = raw_input()
        
                                
