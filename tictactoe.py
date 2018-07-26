def printBoard(board, position=None, marker=None):
  '''
    DOCSTRING: prints and updates the board
    INPUT: current board, position to edit, which marker to edit with
    OUTPUT: new board
  '''
  if position:
    board[position] = marker

  print( '   |   |   ')
  print( ' {} | {} | {} '.format( board["1"], board["2"], board["3"] ) )
  print( '___|___|___')
  print( '   |   |   ')
  print( ' {} | {} | {} '.format( board["4"], board["5"], board["6"] ) )
  print( '___|___|___')
  print( '   |   |   ')
  print( ' {} | {} | {} '.format( board["7"], board["8"], board["9"] ) )
  print( '   |   |   ')

  return board

def checkWin(board):
  '''
    DOCSTRING: checks the board if there are any win conditions
    INPUT: board
    OUTPUT: boolean whether win condition is satisfied
  '''
  flag = False
  if board["1"] == board["2"] == board["3"]:
    flag = True
  elif board["4"] == board["5"] == board["6"]:
    flag = True
  elif board["7"] == board["8"] == board["9"]:
    flag = True
  elif board["1"] == board["4"] == board["7"]:
    flag = True
  elif board["2"] == board["5"] == board["8"]:
    flag = True
  elif board["3"] == board["6"] == board["9"]:
    flag = True
  elif board["1"] == board["5"] == board["9"]:
    flag = True
  elif board["3"] == board["5"] == board ["7"]:
    flag = True
  return flag


def replay():
  '''
    DOCSTRING: restarts the game
  '''
  response = input('Would you like to play again? Yes or No? ')
  if response == 'Yes':
    ticTacToe()
  else:
    pass

def ticTacToe():
  marker = input("Please pick a marker 'X' or 'O'? ").upper()
  board = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
  }
  numTurns = 0

  # checks if the correct marker was selected
  if marker == 'X' or marker == 'O':
    printBoard(board)

    while True:
      # once all positions were are filled its a Draw
      if numTurns == 9:
        print('Draw!')
        replay()
        break

      position = input(f"It is {marker}'s turn. Please enter a number: ")
      # checks if input position is within 1 to 9
      if not position in board:
        print(f'You inputted {position}. Please select a integer from 1 to 9.')
        continue
      # checks if position is already taken
      elif isinstance(board[position], str):
        print('This position has already been selected. Please selected another one.')
        continue

      printBoard(board, position, marker)
      
      # checks win condition
      if checkWin(board):
        print(f'Player {marker} is the winner!')
        replay()
        break

      # toggle between Player X and Player O
      if marker == 'X':
        marker = 'O'
      elif marker == 'O':
        marker = 'X'

      # keeps track of number of turns passed
      numTurns += 1

  # rerun application if incorrect marker chosen
  else:
    print(f'You selected {marker}. Please select the correct marker.')
    ticTacToe()

ticTacToe()