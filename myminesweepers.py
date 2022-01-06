# created by: Ohiosumua Daniel Omozuanfo
# This is my program to solve a minesweeper problem
# of a given board, breaking the problem into an array
# of values

import pprint
import numpy as np

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


def open_cell(board):
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

        count_flags = check_value(row, col, F)

        if n[i] == count_flags:
            t = n[i]
            while t > 0:
                pos_local = get_Pos(row, col, u)
                if pos_local:
                    pos_x, pos_y = pos_local
                else:
                    None
                make_open(pos_x, pos_y)

                t -= 1
    return(board)

def find_UCells(board):
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

        count_unknown = check_value(row, col, u)
        count_flags = check_value(row, col, F)

        if n[i] == count_unknown + count_flags:
            t = n[i]
            while t > 0:
                pos_local = get_Pos(row, col, u)
                if pos_local:
                    pos_x, pos_y = pos_local
                else:
                    None
                flag_cell(pos_x, pos_y)
                t -= 1
    return board


def check_value(cell_x, cell_y, value):
    dig_count = 0
    if in_range_height(cell_x, -1) and in_range_width(cell_y, -1) and in_cell(cell_x, cell_y, -1, -1, value) == value:
        dig_count += 1
    if in_range_height(cell_x, -1) and in_range_width(cell_y, 1) and in_cell(cell_x, cell_y, -1, 1, value) == value:
        dig_count += 1
    if in_range_height(cell_x, 1) and in_range_width(cell_y, -1) and in_cell(cell_x, cell_y, 1, -1, value) == value:
        dig_count += 1
    if in_range_height(cell_x, 1) and in_range_width(cell_y, 1) and in_cell(cell_x, cell_y, 1, 1, value) == value:
        dig_count += 1
    if in_range_height(cell_x, 0) and in_range_width(cell_y, -1) and in_cell(cell_x, cell_y, 0, -1, value) == value:
        dig_count += 1
    if in_range_height(cell_x, 0) and in_range_width(cell_y, 1) and in_cell(cell_x, cell_y, 0, 1, value) == value:
        dig_count += 1
    if in_range_height(cell_x, -1) and in_range_width(cell_y, 0) and in_cell(cell_x, cell_y, -1, 0, value) == value:
        dig_count += 1
    if in_range_height(cell_x, 1) and in_range_width(cell_y, 0) and in_cell(cell_x, cell_y, 1, 0, value) == value:
        dig_count += 1
    return dig_count


# gets the postition of the unknown crossair


def get_Pos(cell_x, cell_y, value):
    position_x: int = ()
    position_y: int = ()
    positions = ()
    if in_range_height(cell_x, 0) and in_range_width(cell_y, -1) and in_cell(cell_x, cell_y, 0, -1, value) == value:
        position_x = cell_x + 0
        position_y = cell_y - 1
        positions = position_x, position_y
        return positions
    if in_range_height(cell_x, 0) and in_range_width(cell_y, 1) and in_cell(cell_x, cell_y, 0, 1, value) == value:
        position_x = cell_x + 0
        position_y = cell_y + 1
        positions = position_x, position_y
        return positions
    if in_range_height(cell_x, -1) and in_range_width(cell_y, 0) and in_cell(cell_x, cell_y, -1, 0, value) == value:
        position_x = cell_x - 1
        position_y = cell_y + 0
        positions = position_x, position_y
        return positions
    if in_range_height(cell_x, 1) and in_range_width(cell_y, 0) and in_cell(cell_x, cell_y, 1, 0, value) == value:
        position_x = cell_x + 1
        position_y = cell_y + 0
        positions = position_x, position_y
        return positions
    if in_range_height(cell_x, -1) and in_range_width(cell_y, -1) and in_cell(cell_x, cell_y, -1, -1, value) == value:
        position_x = cell_x - 1
        position_y = cell_y - 1
        positions = position_x, position_y
        return positions
    if in_range_height(cell_x, -1) and in_range_width(cell_y, 1) and in_cell(cell_x, cell_y, -1, 1, value) == value:
        position_x = cell_x - 1
        position_y = cell_y + 1
        positions = position_x, position_y
        return positions
    if in_range_height(cell_x, 1) and in_range_width(cell_y, -1) and in_cell(cell_x, cell_y, 1, -1, value) == value:
        position_x = cell_x + 1
        position_y = cell_y - 1
        positions = position_x, position_y
        return positions
    if in_range_height(cell_x, 1) and in_range_width(cell_y, 1) and in_cell(cell_x, cell_y, 1, 1, value) == value:
        position_x = cell_x + 1
        position_y = cell_y + 1
        positions = position_x, position_y
        return positions


# opens the cell that should be open


def make_open(cell_x, cell_y):
    o = 'O'
    board[cell_x][cell_y] = o

# flags the cell that should have a mine


def flag_cell(cell_x, cell_y):
    f = 'F'
    board[cell_x][cell_y] = f


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


finePrint = pprint.PrettyPrinter(width=45, compact=False)
find_UCells(board)
open_cell(board)
finePrint.pprint(board)
