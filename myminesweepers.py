# created by: Ohiosumua Daniel Omozuanfo
# This is my program to solve a minesweeper problem
# of a given board, breaking the problem into an array
# of values

import pprint
import pandas
import numpy
# import pandas

# the variable for the unknown part of the cell
u = 'U'

# the board that will be solved
# 0 for cells that are empty
# 1 to n for cells that have numbers of mine around them
# u for cells that are unknown and not yet revealed
# f for cells that are flagged
# O for cells that should be opened
board = [
    [u, u, 1, 0, 0, 0],
    [u, u, 1, 0, 0, 0],
    [u, 4, 1, 0, 0, 0],
    [u, 2, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, u],
    [1, 1, 0, 0, 1, 1],
    [u, 1, 0, 0, 0, 0],
    [u, 3, 1, 0, 0, 0],
    [u, u, 2, 1, 1, 0],
    [u, u, u, u, 1, 0],
    [u, u, 2, 1, 1, 0],
    [u, u, 1, 0, 0, 0],
]

# Todo: Integrate the board variables so it can accept input data instead of hardcoding


def find_diagonals(board):
    # the variable for the unknown cells
    u = 'U'
    F = 'F'
    O = 'O'

    row = []
    col = []

    num = find_N(board)
    if num:
        n, pos = num
    else:
        return True

    for i in range(len(pos)):
        resol = pos[i]
        row, col = resol
        dig_count = 0
        if in_range_height(row, -1) and in_range_width(col, -1) and in_cell(row, col, -1, -1, u) == u:
            if check_crossair(row, col, u) == u:
                dig_count += 1
        if in_range_height(row, -1) and in_range_width(col, 1) and in_cell(row, col, -1, 1, u) == u:
            if check_crossair(row, col, u) == u:
                dig_count += 1
        if in_range_height(row, 1) and in_range_width(col, -1) and in_cell(row, col, 1, -1, u) == u:
            print(row, col)
            if check_crossair(row, col, u) == u:
                dig_count += 1
        if in_range_height(row, 1) and in_range_width(col, 1) and in_cell(row, col, 1, 1, u) == u:
            if check_crossair(row, col, u) == u:
                dig_count += 1
        if check_no_U(n[i], dig_count) == True:
            pos_x, pos_y = get_digPos(row, col, u)
            flag_cell(pos_x, pos_y)
        else:
            print('mismatch')
    return board

# gets the postition of the unknown crossair


def get_crossPos(cell_x, cell_y, value):
    position_x = ()
    position_y = ()
    if in_range_height(cell_x, 0) and in_range_width(cell_y, -1) and in_cell(cell_x, cell_y, 0, -1, value) == value:
        position_x = cell_x + 0
        position_y = cell_y - 1
        return position_x, position_y
    elif in_range_height(cell_x, 0) and in_range_width(cell_y, 1) and in_cell(cell_x, cell_y, 0, 1, value) == value:
        position_x = cell_x + 0
        position_y = cell_y + 1
        return position_x, position_y
    elif in_range_height(cell_x, -1) and in_range_width(cell_y, 0) and in_cell(cell_x, cell_y, -1, 0, value) == value:
        position_x = cell_x - 1
        position_y = cell_y + 0
        return position_x, position_y
    elif in_range_height(cell_x, 1) and in_range_width(cell_y, 0) and in_cell(cell_x, cell_y, 1, 0, value) == value:
        position_x = cell_x + 1
        position_y = cell_y + 0
        return position_x, position_y
    else:
        return 0, 0

# gets the postion of the unknown diagonals


def get_digPos(cell_x, cell_y, value):
    position_x = ()
    position_y = ()
    if in_range_height(cell_x, -1) and in_range_width(cell_y, -1) and in_cell(cell_x, cell_y, -1, -1, value) == value:
        position_x = cell_x - 1
        position_y = cell_y - 1
        return position_x, position_y
    elif in_range_height(cell_x, -1) and in_range_width(cell_y, 1) and in_cell(cell_x, cell_y, -1, 1, value) == value:
        position_x = cell_x - 1
        position_y = cell_y + 1
        return position_x, position_y
    elif in_range_height(cell_x, 1) and in_range_width(cell_y, -1) and in_cell(cell_x, cell_y, 1, -1, value) == value:
        position_x = cell_x + 1
        position_y = cell_y - 1
        return position_x, position_y
    elif in_range_height(cell_x, 1) and in_range_width(cell_y, 1) and in_cell(cell_x, cell_y, 1, 1, value) == value:
        position_x = cell_x + 1
        position_y = cell_y + 1
        return position_x, position_y
    else:
        return None

# opens the cell that should be open


def open_cell(cell_x, cell_y):
    o = 'O'
    u = 'U'
    found_pos = get_crossPos(cell_x, cell_y, u)
    pos_x, pos_y = found_pos
    board[pos_x][pos_y] = o

# flags the cell that should have a mine


def flag_cell(cell_x, cell_y):
    f = 'F'
    board[cell_x][cell_y] = f


# check if the number of bombs is more than the unkown


def check_no_U(num_of_N, num_of_U):
    if num_of_N == num_of_U:
        return True
    else:
        return False

# check if the diagonalls of a cell location has unknown


def check_diagonals(cell_x, cell_y, value):
    if in_range_height(cell_x, -1) and in_range_width(cell_y, -1) and in_cell(cell_x, cell_y, -1, -1, value) == value:
        return False
    elif in_range_height(cell_x, -1) and in_range_width(cell_y, 1) and in_cell(cell_x, cell_y, -1, 1, value) == value:
        return False
    elif in_range_height(cell_x, 1) and in_range_width(cell_y, -1) and in_cell(cell_x, cell_y, 1, -1, value) == value:
        return False
    elif in_range_height(cell_x, 1) and in_range_width(cell_y, 1) and in_cell(cell_x, cell_y, 1, 1, value) == value:
        return False
    else:
        return value

# check if the crossair of a cell location has unkown


def check_crossair(cell_x, cell_y, value):
    if in_range_height(cell_x, 0) and in_range_width(cell_y, -1) and in_cell(cell_x, cell_y, 0, -1, value) == value:
        return False
    elif in_range_height(cell_x, 0) and in_range_width(cell_y, 1) and in_cell(cell_x, cell_y, 0, 1, value) == value:
        return False
    elif in_range_height(cell_x, -1) and in_range_width(cell_y, 0) and in_cell(cell_x, cell_y, -1, 0, value) == value:
        return False
    elif in_range_height(cell_x, 1) and in_range_width(cell_y, 0) and in_cell(cell_x, cell_y, 1, 0, value) == value:
        return False
    else:
        return value

# check if a cell has unknown value


def in_cell(cell_x, cell_y, num_x, num_y, value):
    pos_x: int = int(cell_x) + num_x
    pos_y: int = int(cell_y) + num_y
    board_value = board[pos_x][pos_y]
    if board_value == value:
        return value
    else:
        return False

# check if the point is in the range of the board array
# todo: intergrate the range method to know the width and heigth of the board


def in_range_height(point, num):
    if point + num == -1 or point + num >= 12:
        return False
    else:
        return True


def in_range_width(point, num):
    if point + num == -1 or point + num >= 6:
        return False
    else:
        return True

# this method takes the values in a board and store it in individual variables for the soluctions


def find_N(board):
    N = [1, 2, 3, 4, 5, 6, 7, 8]
    n = []
    locate = []

    for k in range(len(N)):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == k and k > 0:
                    n.append(k)
                    locate.append((i, j))
                else:
                    continue

    return (n, locate)


finePrint = pprint.PrettyPrinter(width=40, compact=True)
find_diagonals(board)
finePrint.pprint(board)
