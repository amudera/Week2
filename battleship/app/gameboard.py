#!/usr/bin/env python3

from pprint import pprint
from random import randint

BLANK = '~'
SHIP = 'S'
MISS = 'M'
HIT = 'H'
class Gameplay:
    def __init__(self, width=5,height=5,row_cord=0,col_cord=0,turn=26):
        self.width = width
        self.height = height
        self.row_cord = row_cord
        self.col_cord = col_cord
        self.turn = turn

        grid = []
        for row_index in range(height):
            new_row = []
            for col_index in range(width):
                new_row.append(BLANK)
            grid.append(new_row)
        self.grid=grid
    
    def opening(self):
        print("Welcome to Battleships!")
        print("You will be playing against the computer")
    
    def random_cords(self):
        self.row_cord = randint(0, self.width - 1)
        self.col_cord = randint(0, self.width - 1)
        return self.grid, (self.row_cord, self.col_cord)

    def play(self,turns):
        print("Input Co-ordinates")
        row_input = input("Input Row: ")
        col_input = input("Input Column: ")
        for tries in range(self.turn):
            if int(row_input) == self.row_cord and int(col_input) == self.col_cord:
                print("YOU WIN!Thanks for playing")
                break
                quit()
            elif self.grid[int(row_input)][int(col_input)] == MISS:
                 print("You have already tried that")
                 break
            else:
                print("TRY AGAIN!")
                self.grid[int(row_input)][int(col_input)] = MISS
                pprint(self.grid)
                return self.grid
    
    def attempts(self):
        self.turn -= 1 
        print("You have " + str(self.turn) + " attempts")
        if self.turn == 0:
            print("GAME OVER")
            quit()
    
example = Gameplay()
print(example.random_cords) 
