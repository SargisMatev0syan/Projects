#Looping
#Ask: roll th dice? If users enters y Generate 2 random numbers
#print them if user enters n print thank you message terminate
#else  print invalid choice 
import random

while True:
 choice = input('Roll the dice? (yes/no): ').lower()
 if choice == 'yes':
    n1 = random.randint(1, 10)
    n2 = random.randint(1, 10)
    print(f'({n1}, {n2})')
 elif choice == 'n':
    print("Thank you for playing:")    
    break
 else:
   print("Invalide choice:")
