import calender
import datetime

 

Def classic_calculator():
      Num1 = input(‘put your first number here’)
      Num2 = input(‘put your second number here’)
      Add = int(Num1) + int(Num2)
      Print(Add)
      Mult = int(Num1) * int(Num2)
      Print(Mult)
      Divide = int(Num1) / int(Num2)
      Print(Divide)
      Sub = int(Num1) - int(Num2)
      Print(Sub)

def list():
      ('define words(type define than the word you want to define) \n tell you my name (make sure you type What is your name) \n What i am (type what are you) \n Tell you the time \n')

whatIsYourName = ('my name is Jarvis' )
WhatCanIDO = 'here is a list of things i can do'
WhatAreYou = 'I am a ANI or Artificial Narrow Intelligence'
now = datetime.datetime.now()
currentTime = datetime.time()
calender = now.date
input('Welcome My name is Jarvis what can i do for you today')            
while True:            
      Maininput = input('hi how can i help you')


      if Maininput == 'what is your name':
            print(whatIsYourName)

      if Maininput == 'what are you':
                  print(WHatCanIDo)

      if Maininput == 'Hey Jarvis' :
                  print (input('Yes'))

      if Maininput == 'what time is it':
                        print(currentTime)
      if Maininput == 'whats todays date':
                    print(calender)
                              
    

         
                  
