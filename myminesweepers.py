# created by: Ohiosumua Daniel Omozuanfo
# This is my program to solve a minesweeper problem
# of a given board, breaking the problem into an array
# of values

import pprint
import numpy as np
import random


class minesweepersolver:

    # Todo: Integrate the board variables so it can accept input data instead of hardcoding

    def __init__(self):
        # the variable for the unknown part of the cell
        u = 'U'
        F = 'F'
        O = 'O'
        

        row = []
        col = []
            
        # the board that will be solved
        # 0 for cells that are empty
        # 1 to n for cells that have numbers of mine around them
        # u for cells that are unknown and not yet revealed
        # f for cells that are flagged
        # O for cells that should be opened
        self.board = [
            [u, u, 1, 0, u, u],
            [u, u, 1, 0, 0, 1],
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
        # finePrint = pprint.PrettyPrinter(width=45, compact=False)
        # find_UCells(board)
        # open_cell(board)
        # guess_flagcell(board)
        # finePrint.pprint(board)

    # this method opens cell based on guessing randomly

    def guess_opencell(self):

        num = self.find_N(self.board)
        if num:
            n, pos = num
        else:
            return True
        
        for i in range(len(pos)):
            resol = pos[i]
            row, col = resol

            count_unknown = self.check_value(row, col, self.u)
            mines = self.mine_left(n[i], row, col)

            if count_unknown > mines:
                draw = random.choice([0, count_unknown])

                unknown_cell = self.get_multPos(row, col, self.u)
                print(unknown_cell)
                if unknown_cell:
                    pos_x, pos_y = unknown_cell.pop(draw)
                else:
                    None
                self.flag_cell(pos_x, pos_y)

                return
        


    # this method flags cell based on guessing the most likely is the flag


    def guess_flagcell(self):

        num = self.find_N(self.board)
        if num:
            n, pos = num
        else:
            return True
        
        for i in range(len(pos)):
            resol = pos[i]
            row, col = resol

            count_unknown = self.check_value(row, col, self.u)
            mines = self.mine_left(n[i], row, col)

            if mines == 1 and count_unknown == 2:
                draw = random.choice([0, 1])

                unknown_cell = self.get_multPos(row, col, self.u)
                print(unknown_cell)
                if unknown_cell:
                    pos_x, pos_y = unknown_cell.pop(draw)
                else:
                    None
                self.flag_cell(pos_x, pos_y)

                return
        

    # this method opens the cell that are not mines


    def open_cell(self):

        num = self.find_N(self.board)
        if num:
            n, pos = num
        else:
            return True

        for i in range(len(pos)):
            resol = pos[i]
            row, col = resol

            count_flags = self.check_value(row, col, self.F)

            if n[i] == count_flags:
                t = n[i]
                while t > 0:
                    pos_local = self.get_Pos(row, col, self.u)
                    if pos_local:
                        pos_x, pos_y = pos_local
                    else:
                        None
                    self.make_open(pos_x, pos_y)

                    t -= 1
        return(board)


    # this method finds the cell with mines and flags them


    def find_UCells(self):
        
        num = self.find_N(self.board)
        if num:
            n, pos = num
        else:
            return True

        for i in range(len(pos)):
            resol = pos[i]
            row, col = resol

            count_unknown = self.check_value(row, col, self.u)
            count_flags = self.check_value(row, col, self.F)

            if n[i] == count_unknown + count_flags:
                t = n[i]
                while t > 0:
                    pos_local = self.get_Pos(row, col, self.u)
                    if pos_local:
                        pos_x, pos_y = pos_local
                    else:
                        None
                    self.flag_cell(pos_x, pos_y)
                    t -= 1
        return board


    # # this meathod finds more than one unknown and returns them

    def get_multPos(self, cell_x, cell_y, value):
        position_x: int = ()
        position_y: int = ()
        positions = []
        if self.in_range_height(cell_x, 0) and self.in_range_width(cell_y, -1) and self.in_cell(cell_x, cell_y, 0, -1, value) == value:
            position_x = cell_x + 0
            position_y = cell_y - 1
            positions.append([position_x, position_y])
        if self.in_range_height(cell_x, 0) and self.in_range_width(cell_y, 1) and self.in_cell(cell_x, cell_y, 0, 1, value) == value:
            position_x = cell_x + 0
            position_y = cell_y + 1
            positions.append([position_x, position_y])       
        if self.in_range_height(cell_x, -1) and self.in_range_width(cell_y, 0) and self.in_cell(cell_x, cell_y, -1, 0, value) == value:
            position_x = cell_x - 1
            position_y = cell_y + 0
            positions.append([position_x, position_y])       
        if self.in_range_height(cell_x, 1) and self.in_range_width(cell_y, 0) and self.in_cell(cell_x, cell_y, 1, 0, value) == value:
            position_x = cell_x + 1
            position_y = cell_y + 0
            positions.append([position_x, position_y])       
        if self.in_range_height(cell_x, -1) and self.in_range_width(cell_y, -1) and self.in_cell(cell_x, cell_y, -1, -1, value) == value:
            position_x = cell_x - 1
            position_y = cell_y - 1
            positions.append([position_x, position_y])       
        if self.in_range_height(cell_x, -1) and self.in_range_width(cell_y, 1) and self.in_cell(cell_x, cell_y, -1, 1, value) == value:
            position_x = cell_x - 1
            position_y = cell_y + 1
            positions.append([position_x, position_y])       
        if self.in_range_height(cell_x, 1) and self.in_range_width(cell_y, -1) and self.in_cell(cell_x, cell_y, 1, -1, value) == value:
            position_x = cell_x + 1
            position_y = cell_y - 1
            positions.append([position_x, position_y])       
        if self.in_range_height(cell_x, 1) and self.in_range_width(cell_y, 1) and self.in_cell(cell_x, cell_y, 1, 1, value) == value:
            position_x = cell_x + 1
            position_y = cell_y + 1
            positions.append([position_x, position_y])       
        return positions


    # this meathod finds the nunber of mines left next to a numbered cell


    def mine_left(self, num_cell, cell_x, cell_y):
        f = 'F'
        num_f = self.check_value(cell_x, cell_y, f)
        mines = num_cell - num_f
        return mines


    # this meathod checks for a value around the cell passed to it


    def check_value(self, cell_x, cell_y, value):
        dig_count = 0
        if self.in_range_height(cell_x, -1) and self.in_range_width(cell_y, -1) and self.in_cell(cell_x, cell_y, -1, -1, value) == value:
            dig_count += 1
        if self.in_range_height(cell_x, -1) and self.in_range_width(cell_y, 1) and self.in_cell(cell_x, cell_y, -1, 1, value) == value:
            dig_count += 1
        if self.in_range_height(cell_x, 1) and self.in_range_width(cell_y, -1) and self.in_cell(cell_x, cell_y, 1, -1, value) == value:
            dig_count += 1
        if self.in_range_height(cell_x, 1) and self.in_range_width(cell_y, 1) and self.in_cell(cell_x, cell_y, 1, 1, value) == value:
            dig_count += 1
        if self.in_range_height(cell_x, 0) and self.in_range_width(cell_y, -1) and self.in_cell(cell_x, cell_y, 0, -1, value) == value:
            dig_count += 1
        if self.in_range_height(cell_x, 0) and self.in_range_width(cell_y, 1) and self.in_cell(cell_x, cell_y, 0, 1, value) == value:
            dig_count += 1
        if self.in_range_height(cell_x, -1) and self.in_range_width(cell_y, 0) and self.in_cell(cell_x, cell_y, -1, 0, value) == value:
            dig_count += 1
        if self.in_range_height(cell_x, 1) and self.in_range_width(cell_y, 0) and self.in_cell(cell_x, cell_y, 1, 0, value) == value:
            dig_count += 1
        return dig_count


    # gets the postition of the unknown crossair


    def get_Pos(self, cell_x, cell_y, value):
        position_x: int = ()
        position_y: int = ()
        positions = ()
        if self.in_range_height(cell_x, 0) and self.in_range_width(cell_y, -1) and self.in_cell(cell_x, cell_y, 0, -1, value) == value:
            position_x = cell_x + 0
            position_y = cell_y - 1
            positions = position_x, position_y
            return positions
        if self.in_range_height(cell_x, 0) and self.in_range_width(cell_y, 1) and self.in_cell(cell_x, cell_y, 0, 1, value) == value:
            position_x = cell_x + 0
            position_y = cell_y + 1
            positions = position_x, position_y
            return positions
        if self.in_range_height(cell_x, -1) and self.in_range_width(cell_y, 0) and self.in_cell(cell_x, cell_y, -1, 0, value) == value:
            position_x = cell_x - 1
            position_y = cell_y + 0
            positions = position_x, position_y
            return positions
        if self.in_range_height(cell_x, 1) and self.in_range_width(cell_y, 0) and self.in_cell(cell_x, cell_y, 1, 0, value) == value:
            position_x = cell_x + 1
            position_y = cell_y + 0
            positions = position_x, position_y
            return positions
        if self.in_range_height(cell_x, -1) and self.in_range_width(cell_y, -1) and self.in_cell(cell_x, cell_y, -1, -1, value) == value:
            position_x = cell_x - 1
            position_y = cell_y - 1
            positions = position_x, position_y
            return positions
        if self.in_range_height(cell_x, -1) and self.in_range_width(cell_y, 1) and self.in_cell(cell_x, cell_y, -1, 1, value) == value:
            position_x = cell_x - 1
            position_y = cell_y + 1
            positions = position_x, position_y
            return positions
        if self.in_range_height(cell_x, 1) and self.in_range_width(cell_y, -1) and self.in_cell(cell_x, cell_y, 1, -1, value) == value:
            position_x = cell_x + 1
            position_y = cell_y - 1
            positions = position_x, position_y
            return positions
        if self.in_range_height(cell_x, 1) and self.in_range_width(cell_y, 1) and self.in_cell(cell_x, cell_y, 1, 1, value) == value:
            position_x = cell_x + 1
            position_y = cell_y + 1
            positions = position_x, position_y
            return positions


    # opens the cell that should be open


    def make_open(self, cell_x, cell_y):
        o = 'O'
        self.board[cell_x][cell_y] = o


    # flags the cell that should have a mine


    def flag_cell(self, cell_x, cell_y):
        f = 'F'
        self.board[cell_x][cell_y] = f


    # check if a cell has unknown value


    def in_cell(self, cell_x, cell_y, num_x, num_y, value):
        pos_x: int = int(cell_x) + num_x
        pos_y: int = int(cell_y) + num_y
        board_value = self.board[pos_x][pos_y]
        if board_value == value:
            return value
        else:
            return False

    # check if the point is in the range of the board array
    # todo: intergrate the range method to know the width and heigth of the board


    def in_range_height(self, point, num):
        if point + num == -1 or point + num >= 12:
            return False
        else:
            return True


    def in_range_width(self, point, num):
        if point + num == -1 or point + num >= 6:
            return False
        else:
            return True

    # this method takes the values in a board and store it in individual variables for the soluctions


    def find_N(self):
        N = [1, 2, 3, 4, 5, 6, 7, 8]
        n = []
        locate = []

        for k in range(len(N)):
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] == k and k > 0:
                        n.append(k)
                        locate.append((i, j))
                    else:
                        continue

        return (n, locate)


    
