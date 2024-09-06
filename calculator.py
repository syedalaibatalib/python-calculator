from sqlalchemy import true


print("lets play with some calculation")

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
 if y!= 0:
    return x/y 
 else:
    print("enter valid number")

def calculator():

   print("lets calculate")
   print("select opertaion: ")
   print("1: add")
   print("2: subtract")
   print("3: multiplication")
   print("4: division")

   while true:
      #take user input
      choice = input('enter what you want to do (1/2/3/4):')
      # slection of choice
      if choice in ['1','2','3','4']:
         #take input number by user
        try:
            num1= float(input('Enter 1st number:'))
            num2= float(input('Enter 2nd number:'))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == '1':
           print(f'{num1} + {num2} = {add(num1,num2)}')
           
        if choice == '2':
           print(f'{num1} - {num2} = {subtract(num1,num2)}')

        if choice == '3':
           print(f'{num1} * {num2} = {multiplication(num1,num2)}')

        if choice == '4':
           print(f'{num1} / {num2} = {division(num1,num2)}')

      else:
       print('plz enter valid choice number')

      next_calculation = input("Do you want to perform more calculation? (yes/no): ")
      if next_calculation.lower() != 'yes':
          break
        
    
calculator()
   