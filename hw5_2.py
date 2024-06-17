#統計系116陳祥德H24124068
import random

def create_board(length):
    board = []
    for _ in range(length):
        if random.random() < 0.3:
            board.append('P')  # Penalty square
        else:
            board.append('_')  # Safe square
    return board

def move_player(pos, steps, board):
    new_pos = pos + steps
    if new_pos < len(board):
        if board[new_pos] == 'P':
            print("Oops! Player landed on a penalty square. Skipping turn.")
            return pos
        else:
            return new_pos
    else:
        return pos

def check_win(pos_a, pos_b):
    if pos_a >= len(board) and pos_b >= len(board):
        print("Both players win!")
        return True
    elif pos_a >= len(board):
        print("Player A wins!")
        return True
    elif pos_b >= len(board):
        print("Player B wins!")
        return True
    else:
        return False

def print_board(board, pos_a, pos_b):
    for i, square in enumerate(board):
        if i == pos_a and i == pos_b:
            print("X", end=' ')
        elif i == pos_a:
            print("A", end=' ')
        elif i == pos_b:
            print("B", end=' ')
        elif square == 'P':
            print("P", end=' ')
        elif square == '_':
            print("_", end=' ')
        else:
            print(square, end=' ')
    print()

def main():
    global board
    board_length = 30
    board = create_board(board_length)
    pos_a, pos_b = 0, 0

    while not check_win(pos_a, pos_b):
        input("Player A: Press Enter to roll the dice...")
        roll_a = random.randint(1, 6)
        print("Dice roll for Player A:", roll_a)
        pos_a = move_player(pos_a, roll_a, board)

        input("Player B: Press Enter to roll the dice...")
        roll_b = random.randint(1, 6)
        print("Dice roll for Player B:", roll_b)
        pos_b = move_player(pos_b, roll_b, board)

        print_board(board, pos_a, pos_b)

main()







