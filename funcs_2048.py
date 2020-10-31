# 2048 from Kattis
"""temp_board = []
new_board = []
# int_list = [int(j) for j in input().split()]
for _ in range(4):
    temp_board.append([int(j) for j in input().split()])
direction = input()"""

def new_merge_right(board: list):
    board = omit_zeros(board)
    # merges like numbers(right to left)
    for y in range(4):
        for x in range(len(board[y]) - 1, -1, -1):
            if x > 0 and board[y][x] == board[y][x - 1]:
                board[y][x - 1] = board[y][x] * 2
                del board[y][x]
    # adds new zeros to the beginning
    for item in board:
        new_zero = 4 - len(item)
        for _ in range(new_zero):
            item.insert(0, 0)


def new_merge_left(board: list):
    board = omit_zeros(board)
    # merges like numbers(right to left)
    for y in range(4):
        for x in range(len(board[y])):
            if x < len(board[y]) - 1 and board[y][x] == board[y][x + 1]:
                board[y][x + 1] = board[y][x] * 2
                del board[y][x]
    # adds new zeros to the beginning
    for item in board:
        new_zero = 4 - len(item)
        for _ in range(new_zero):
            item.insert(3, 0)


def new_merge_up(board: list):
    for y in range(4):
        for x in range(4):
            if y < 3 and board[y][x] == 0 and board[y + 1][x] != 0:
                board[y][x] = board[y + 1][x]
                board[y + 1][x] = 0
    for y in range(4):
        for x in range(4):
            if y < 3 and board[y + 1][x] == board[y][x]:
                board[y][x] = board[y + 1][x] * 2
                board[y + 1][x] = 0
    for _ in range(2):
        # double checking
        for y in range(4):
            for x in range(4):
                if y < 3 and board[y][x] == 0 and board[y + 1][x] != 0:
                    board[y][x] = board[y + 1][x]
                    board[y + 1][x] = 0


def new_merge_down(board: list):
    for y in range(3, -1, -1):
        for x in range(4):
            if y > 0 and board[y][x] == 0 and board[y - 1][x] != 0:
                board[y][x] = board[y - 1][x]
                board[y - 1][x] = 0
    for y in range(3, -1, -1):
        for x in range(4):
            if y > 0 and board[y - 1][x] == board[y][x]:
                board[y][x] = board[y - 1][x] * 2
                board[y - 1][x] = 0
    for _ in range(2):
        # double checking
        for y in range(3, -1, -1):
            for x in range(4):
                if y > 0 and board[y][x] == 0 and board[y - 1][x] != 0:
                    board[y][x] = board[y - 1][x]
                    board[y - 1][x] = 0


def omit_zeros(board):
    for item in board:
        while 0 in item:
            item.remove(0)
    return board

def print_board(board):
    print(board)

"""def check_direction():
    if direction == "0":
        new_merge_left(temp_board)
    if direction == "1":
        new_merge_up(temp_board)
    if direction == "2":
        new_merge_right(temp_board)
    if direction == "3":
        new_merge_down(temp_board)"""

if __name__ == "__main__":
    check_direction()
    for item_ in temp_board:
        for k in range(len(item_)):
            item_[k] = str(item_[k])
    for item in temp_board:
        print(' '.join(item))
