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
import random
hand_list = [rock, paper, scissors]
game_list = [0,1,2]
com_choice = random.choice(game_list)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if user_choice >= 2 or user_choice < 0:
  print("Invalid input, you lose")
else:
  print(f"You choose:")
  print(hand_list[user_choice])
  print("computer choose:")
  print(hand_list[com_choice])
  #invalid input
  
  #Tie 
  if user_choice ==  com_choice:
    print("It's a Tie")
  #User win
  elif user_choice == 0 and com_choice == 2:
    print("You win")
  elif user_choice == 2 and com_choice == 1:
    print("You win")
  elif user_choice == 1 and com_choice == 0:
    print("You win")
  #Computer win
  elif user_choice == 0 and com_choice == 1:
    print("You lose. Computer win")
  elif user_choice == 1 and com_choice == 2:
    print("You lose. Computer win")
  elif user_choice == 2 and com_choice == 0:
    print("You lose. Computer win")





    
  

