import random
#Day 4 Project: Rock Paper Scissors
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
gameImages = [rock, paper, scissors]
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(gameImages[player])
print("Computer chose:")
computer = random.randint(0, 2)
print(gameImages[computer])

if player == 0 and computer == 2:
    print("You win!")
elif player == 2 and computer == 0:
    print("You lose!")
elif player < computer:
    print("You lose!")
elif player > computer:
    print("You win!")
else:
    print("It's a draw!")