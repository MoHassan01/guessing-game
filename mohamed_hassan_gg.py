# -*- coding: utf-8 -*-
"""Mohamed Hassan GG

 Show the game levels
"""

def show_levels():
  # write your code here
  print("Easy: Limits [1, 10], no. of trials 3\nMedium: Limits [1, 100], no. of trials 7\nHard: Limits [1, 1000], no. of trials 15")

""" Ask the user for the game level"""

def game_level_choice():
  # write your code here
  level = input("Please enter the desired level: ")
  while level.lower() not in ["easy", "medium", "hard"]:
    level = input("Please enter the level name correctly: ")
  game_level = level 
  return game_level

"""Set the game settings according to the game level:"""

def set_game_settings(game_level):
  # write your code here
  global limit
  global trials
  if game_level == 'easy':
    limit = list(range(1, 11))
    trials = 3
  elif game_level == 'medium':
    limit = list(range(1, 101))
    trials = 7
  elif game_level == 'hard':
    limit = list(range(1, 1001))
    trials = 15
  return limit, trials

set_game_settings("easy")

"""Start Playing"""

import random
def start_play(limit, trials):
  # write your code here
  num = random.choice(range(1, limit[-1]))
  i = 0
  while i < trials:
    i += 1
    guess = int(input("Type your guess: "))
    if guess < num:
      print("No, increase.")
    elif guess > num:
      print("No, decrease.")
    elif guess == num:
      print(f"You're correct!\nYou made it in {i} trials.")
      break
    if i == trials:
      print("Sorry, your guesses were wrong and trials are over.")

"""Let's Play"""

def play():
  show_levels()
  game_level = game_level_choice()
  limits, n_trials = set_game_settings(game_level)
  start_play(limit, trials)

play()

