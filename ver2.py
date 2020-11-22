import numpy as np
import random 
import time

def create():
  return np.zeros((3, 3), dtype=int)

def place(board, player, position): 
    board[position[0]][position[1]] = player

def possibilities(board): 
    place = np.where(board == 0)
    if place:
      result = []
      for i in range(len(place[0])):
          a = []
          for item in place: 
              a.append(item[i])
          result.append(tuple(a))
      return result
    return 

random.seed(1)
def random_place(board, player):
    plays = possibilities(board)
    x = random.choice(plays)
    place(board, player, x)

def row_win(board, player):
  if [board[0][0], board[0][1], board[0][2]] == [player, player, player]: 
    return True
  elif [board[1][0], board[1][1], board[1][2]] == [player, player, player]:
    return True
  elif [board[2][0], board[2][1], board[2][2]] == [player, player, player]:
    return True
  return False


def col_win(board, player):
  if [board[0][0], board[1][0], board[2][0]] == [player, player,player]:
      return True
  elif [board[0][1], board[1][1], board[2][1]] == [player, player,player]:
      return True
  elif [board[0][2], board[1][2], board[2][2]] == [player, player,player]:
      return True
  return False

def diag_win(board, player):
  if [board[0][0], board[1][1], board[2][2]] == [player, player,player]:
    return True
  elif [board[2][0], board[1][1], board[0][2]] == [player, player, player]:
    return True
  return False

def evaluate(board, player):
  if diag_win(board, player) or col_win(board, player) or row_win(board, player):
    return True
  return False

def play_game():
  table = create()
  table[1][1] = 1
  for i in range(1, 9): 
    if i % 2 == 0:
      random_place(table, 1)
      if evaluate(table, 1):
        return 1
    else: 
      random_place(table, 2)
      if evaluate(table, 2):
        return 2
  return 0

count = 0
for i in range(1000):
  a = play_game()
  if a == 1: 
    count += 1

print(count)