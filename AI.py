import datetime

 

def classic_calculator():
      Num1 = input('what is your fist number')
      Num2 = input('what is your second number')
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

Hey_Jarvis = input('yes')
whatIsYourName = ('my name is Jarvis')
WhatCanIDO = 'here is a list of things i can do'
WhatAreYou = 'I am a ANI or Artificial Narrow Intelligence'
now = datetime.datetime.now()
currentTime = datetime.time()
calender = datetime.date.today()
Welcome = input('Welcome my name is Jarvis how can i help')           
while True:            
      Maininput = input()

      
      if Maininput == 'open calculator':
               print(classic_calculator)
   
      if Hey_Jarvis == 'open calculator':
              print (classic_calculator)
      if Hey_Jarvis == 'what is your name':
              print(whatIsYourName)
      if Hey_Jarvis == 'can you do me a favor'
              print('whats up')
   
    
      if Maininput == 'what is your name':
            print(whatIsYourName)

      if Maininput == 'what are you':
                  print(WhatCanIDo)

      if Maininput == 'Hey Jarvis' :
                  print (Hey_Jarvis)

      if Maininput == 'what time is it':
                        print(currentTime)
      if Maininput == 'whats todays date':
                    print(calender)
                              
    

         
                  
