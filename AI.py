import datetime

 
while True:
   import random
   Jarvis_Random = input(random.choice(['hi how can i help','whats up', 'yes']))
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

whatIsYourName = ('my name is Jarvis')
WhatCanIDO = 'here is a list of things i can do'
WhatAreYou = 'I am a ANI or Artificial Narrow Intelligence'
cdt = datetime.datetime.now()
currentTime = cdt.strftime("%H:%M")
date = datetime.date.today()
Welcome = input('Welcome my name is Jarvis how can i help')           
while True:            
      Maininput = input()

      
      if Maininput == 'open calculator':
               print(classic_calculator)
   
      if Jarvis_Random == 'open calculator':
              print (classic_calculator)
      if Jarvis_Random == 'what is your name':
              print(whatIsYourName)
      if Jarvis_Random == 'can you do me a favor'
              print('whats up')
      if Jarvis_Random == 'whats the date'
              print('the date is' + date)
      if Jarvis_Random == 'what time is it'
              print('The time is' + currentTime)
      if Jarvis_Random == 'can you do me a favor'
              print(')
   
    
      if Maininput == 'what is your name':
            print(whatIsYourName)

      if Maininput == 'what are you':
                  print(WhatCanIDo)

      if Maininput == 'Hey Jarvis' :
                  print (Jarvis_Random)

      if Maininput == 'what time is it':
                   print(currentTime)
      if Maininput == 'whats todays date':
                    print(date)
                              
    

         
                  
