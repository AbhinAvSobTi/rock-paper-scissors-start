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

x = input(" Enter your input, 0 for ROCK, 1 for PAPER and 2 for SCISSORS ")
if x == 0:
  choice = rock
elif x == 1:
  choice = paper
else:
  choice = scissors

import random
y = random.randint(0,2)
if y == 0:
  choice_c = rock
elif y == 1:
  choice_c = paper
else:
  choice_c = scissors


print("you chose")
print(choice)
print("computer chose")
print(choice_c)

if choice == rock:
  if choice_c == scissors:
    print (" you win")
  elif choice_c == paper:
    print(" you loose")
  else:
    print(" its a tie")
elif choice == scissors:
  if choice_c == scissors:
    print (" its a tire")
  elif choice_c == paper:
    print(" you win")
  else:
    print(" you loose")
else:
  if choice_c == scissors:
    print (" you win")
  elif choice_c == paper:
    print(" its a tie")
  else:
    print(" you win")

