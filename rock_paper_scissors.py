import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images = [rock, paper, scissors]
user_choise = int(input("Whats do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_list = [0, 1, 2]
computer_choise = random.choice(computer_list)


if user_choise == 0 or user_choise == 1 or user_choise == 2:
    print(images[user_choise])      
    print(f"Computer chose {computer_choise}")
    print(images[computer_choise])       
    if user_choise == 0 and computer_choise == 2:
        print("You win!")
    elif computer_choise > user_choise:
        print("You lose!")
    elif computer_choise == user_choise:
        print("It's a draw.")
    elif user_choise > computer_choise:
        print("You win!")
else:   
    print("You typed an invalid number, you lose!")