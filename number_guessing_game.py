#Our program must generate a random number:
#looping
#ask the user make a guess ; if not vaild number print an error
#if number < guess
# print too low ; if number > guess  print too high :else print well done

import random

number_to_guess = random.randint(1, 100)
while True:
    try:
     guess = int(input("Guess the number between 1 and 100: "))

     if guess < number_to_guess:
       print("Too low:")
     elif guess > number_to_guess:
       print("Too high")
     else:
       print("Congratulations: You have guessed the number :)")
       break    
    except ValueError:
     print("Enter the vaild number")

