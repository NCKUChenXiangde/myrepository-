統計系116陳祥德
import random

# 定義遊戲板大小和地雷數量
ROWS = 9
COLS = 9
NUM_MINES = 10

# 定義單元格的狀態
EMPTY = ' '
MINE = '*'
FLAG = 'F'

# 初始化遊戲板
def initialize_board():
    board = [[EMPTY] * COLS for _ in range(ROWS)]
    return board

# 放置地雷
def place_mines(board, first_row, first_col):
    safe_cells = [(first_row + i, first_col + j) for i in range(-1, 2) for j in range(-1, 2)]
    safe_cells = [(r, c) for (r, c) in safe_cells if 0 <= r < ROWS and 0 <= c < COLS]
    safe_cells.append((first_row, first_col))
    cells = [(r, c) for r in range(ROWS) for c in range(COLS) if (r, c) not in safe_cells]
    mines = random.sample(cells, NUM_MINES)
    for (row, col) in mines:
        board[row][col] = MINE

# 檢查單元格周圍的地雷數量
def count_mines_around(board, row, col):
    count = 0
    for i in range(max(0, row - 1), min(ROWS, row + 2)):
        for j in range(max(0, col - 1), min(COLS, col + 2)):
            if board[i][j] == MINE:
                count += 1
    return count

# 更新遊戲板上每個單元格的狀態
def update_board(board):
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] != MINE:
                count = count_mines_around(board, i, j)
                if count > 0:
                    board[i][j] = str(count)

# 印出遊戲板
def print_board(board, reveal=False):
    print("   " + "  ".join(chr(ord('a') + i) for i in range(COLS)))
    print("  +" + "---+" * COLS)
    for i in range(ROWS):
        row_str = f"{i + 1} | {' | '.join(board[i][j] if board[i][j] != MINE or reveal else EMPTY for j in range(COLS))} |"
        row_str = row_str.replace(' 10 ', '10 ')
        print(row_str)
        print("  +" + "---+" * COLS)

# 游戲逻辑
def minesweeper():
    board = initialize_board()

    # 要求第一次展開的單元格是 '0'
    first_action = input("Enter the first coordinates (e.g., 'a5'): ")
    first_row = int(first_action[1]) - 1
    first_col = ord(first_action[0]) - ord('a')
    print(f"You chose cell {first_action}.")

    # 放置地雷並更新遊戲板
    place_mines(board, first_row, first_col)
    update_board(board)
    print_board(board)

    # 之後的動作與之前相同
    while True:
        action = input("Enter the coordinates (e.g., 'a5') or 'q' to quit: ")
        if action.lower() == 'q':
            break
        else:
            row = int(action[1]) - 1
            col = ord(action[0]) - ord('a')
            print(f"You chose cell {action}.")
            # 在這裡添加遊戲邏輯，處理用戶的輸入和更新遊戲板
            board = initialize_board()  # 每次輸入值後重新初始化遊戲板
            place_mines(board, row, col)  # 根據玩家輸入的座標放置地雷
            update_board(board)  # 更新遊戲板狀態
            print_board(board)  # 印出新的遊戲板

# 主程式
if __name__ == "__main__":
    minesweeper()






