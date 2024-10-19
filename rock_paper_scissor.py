#We are going to ask the user to make choice
#if choice is not valid -> Print an error
#Let the computer to make a choice -> print choices(emojies)
#Determine the winner
#ASk the user if they want to continue -> if not -> Terminate
import random 
while True:
    emojis = {'r': ' 🪨', 's' : '✂️',  'p': '📄' }
    choices = ('r','p','s')

    user_choice = input("Rock, paper, or scissors? (r/p/s):").lower()
    if user_choice not in choices:
        print("Invalid choice")
        continue

    computer_choice = random.choice(choices)

    print(f'You chose {emojis[user_choice]}')
    print(f'Computer  chose {emojis[computer_choice]}') 

    if user_choice == computer_choice:
        print("Tie!")
    elif(
        (user_choice == "r" and computer_choice == "s") or
        (user_choice == "s" and computer_choice == "p") or  
        (user_choice == "p" and computer_choice == "r")):
        print("You are winner")  
    else:
        print('You lose')    


    should_continue = input('Continue? (yes/no) :').lower()
    if should_continue == 'no':
              break

