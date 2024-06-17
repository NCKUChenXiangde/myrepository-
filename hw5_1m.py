#統計系116陳祥德H24124068
import random

def print_board(board):
    """
    Print the current state of the Minesweeper board.
    """
    print("    a   b   c   d   e   f   g   h   i")
    print("  +---+---+---+---+---+---+---+---+---+")
    for row in range(1, 10):
        print(f"{row} | ", end="")
        for col in range(1, 10):
            if (row, col) in board['revealed']:
                print(board['cells'][(row, col)], end=" | ")
            else:
                print(" ", end=" | ")
        print("\n  +---+---+---+---+---+---+---+---+---+")


def create_board():
    """
    Create an empty Minesweeper board.
    """
    board = {'cells': {}, 'revealed': set(), 'mines': set()}
    for row in range(1, 10):
        for col in range(1, 10):
            board['cells'][(row, col)] = " "
    return board


def place_mines(board, num_mines, first_move):
    """
    Place mines randomly on the board, excluding the first move cell and its neighbors.
    """
    mines_placed = 0
    while mines_placed < num_mines:
        row = random.randint(1, 9)
        col = random.randint(1, 9)
        if abs(row - first_move[0]) > 1 or abs(col - first_move[1]) > 1:
            if (row, col) not in board['mines']:
                board['cells'][(row, col)] = "M"
                board['mines'].add((row, col))
                mines_placed += 1


def calculate_numbers(board):
    """
    Calculate the number of mines around each non-mine cell and update the board.
    """
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for row in range(1, 10):
        for col in range(1, 10):
            if board['cells'][(row, col)] != "M":
                mine_count = 0
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (1 <= r <= 9 and 1 <= c <= 9 and 
                        board['cells'][(r, c)] == "M"):
                        mine_count += 1
                board['cells'][(row, col)] = str(mine_count) if mine_count > 0 else " "


def main():
    """
    Main function to play Minesweeper game.
    """
    board = create_board()
    print_board(board)
    
    first_move = input("Enter your first move (e.g., 'a5'): ")
    row = int(first_move[1])
    col = ord(first_move[0]) - ord('a') + 1
    place_mines(board, 10, (row, col))
    calculate_numbers(board)
    
    # Reveal the first move and its neighbors
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            r, c = row + dr, col + dc
            if 1 <= r <= 9 and 1 <= c <= 9:
                board['revealed'].add((r, c))
    print_board(board)
    
    while True:
        move = input("Enter your move (e.g., 'b6'): ")
        row = int(move[1])
        col = ord(move[0]) - ord('a') + 1
        if (row, col) in board['revealed']:
            print("Cell already revealed. Try another move.")
            continue
        if board['cells'][(row, col)] == "M":
            print("Game over! You hit a mine.")
            break
        board['revealed'].add((row, col))
        print_board(board)
        
        if len(board['revealed']) == 81 - 10:  # All non-mine cells revealed
            print("Congratulations! You've cleared the minefield.")
            break

main()
