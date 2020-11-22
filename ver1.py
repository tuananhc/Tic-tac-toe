def player_position(): 
    position = input('Your move: ')
    while int(position) not in range(1,10) or not position.isdigit():
        print('Invalid move!')
        position = input('Your move: ')
    position = int(position)
    return position

def full_board_check(board): 
    if ' ' not in board: 
        print("No more moves available!")
        return False

def replay():
    answer = input('Do you want to play again?\nY or N? ')
    while answer not in 'yYnN':
        print('Invalid input!')
        answer = input('Do you want to play again?\nY or N? ')
    if answer.upper() == 'Y':
        return True
    else:
        return False

def space_check(board, position):
    while board[position] == ' ':
        print("Can't place here!")
        player_position()

def player_marker():
    marker_1 = input('Do you want to be X or O? ').upper()
    while marker_1 not in ('X','O'):
        print('Choose a valid marker')
        marker_1 = input('Do you want to be X or O? ').upper()
    marker_2 = 'X' if marker_1 == 'O' else 'O'
    return marker_1, marker_2

def win_check(board,mark):
    if board[0:3]==[mark, mark, mark] or board[3:6]==[mark, mark, mark] or board [6:9] ==[mark,mark,mark]:
        return False
    elif [board[0],board[3],board[6]]==[mark, mark, mark] or [board[1],board[4],board[7]]==[mark, mark, mark] or [board[2],board[5],board[8]]==[mark, mark, mark]:
        return False
    elif [board[0],board[4],board[8]]==[mark, mark, mark] or [board[2],board[4],board[6]]==[mark, mark, mark]:
        return False

def place_marker(board, marker, position):
    while space_check(board, position):
        board[position - 1] = marker

def display_board(board):
    print(board[6] + ' ' + '|' + ' ' + board[7] + ' ' + '|' + ' ' + board[8])
    print(board[3] + ' ' + '|' + ' ' + board[4] + ' ' + '|' + ' ' + board[5])
    print(board[0] + ' ' + '|' + ' ' + board[1] + ' ' + '|' + ' ' + board[2])

def tic_tac_toe():
    print('Welcone to tic tac toe')
    while True:
        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        player_marker()
        demoboard = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        display_board(demoboard)
        print('-' * 9)
        turn = 1
        marker_1, marker_2 = player_marker()
        while turn > 0: 
            if turn % 2 != 0: 
                #Player 1 turn
                if not full_board_check(board):
                    break
                position = player_position()
                while not space_check(board,position):
                    player_position()
                while not space_check(board,position):
                    player_position()
                place_marker(board,marker_1,position)
                display_board(board)
                print('-' * 9)
                if not win_check(board, marker_1):
                    break
                if not win_check(board, marker_2):
                    break
                turn += 1
            else: 
                #Player 2 turn
                if not full_board_check(board):
                    break
                position = player_position()
                while not space_check(board,position):
                    player_position()
                while not space_check(board,position):
                    player_position()
                place_marker(board,marker_2,position)
                display_board(board)
                print('-' * 9)
                if not win_check(board, marker_1):
                    break
                if not win_check(board, marker_2):
                    break
                turn += 1
    print('Bye')
    return

tic_tac_toe()