# python3
__author__ = 'kwheelerj'

from prototype import valid, find_empty
from tkinter import Tk, Frame, LabelFrame, Label, Button
from time import sleep


class Board:

    def __init__(self, window, file="input.txt"):
        self.nums = []
        data = open(file, 'r')
        for line in data:
            arr = []
            for word in line.split():
                arr.append(int(word))
            self.nums.append(arr)
        self.window = window
        self.window.title("Sudoku Solver (backtracking)")
        self.main_frame = Frame(self.window, padx=10, pady=10)
        self.units = [[Unit(self.nums[i][j], i, j) for j in range(9)] for i in range(9)]
        self.draw()

    def draw(self):
        self.main_frame.grid(row=0, column=0)
        for i in range(9):
            for j in range(9):
                self.units[i][j].draw(self.main_frame)

        button_frame = Frame(self.window, padx=15, pady=15)
        button_frame.grid(row=1, column=0)
        button = Button(button_frame, text="Solve", command=self.solve)
        button.pack()

    def solve(self):
        result_frame = Frame(self.window, padx=20, pady=20)
        if self.solve_gui():
            result = "good"
        else:
            result = "bad"
        result_frame.grid(row=2, column=0)
        Label(result_frame, text=result).pack()

    def solve_gui(self):
        find = find_empty(self.nums)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if valid(self.nums, i, (row, col)):
                self.nums[row][col] = i
                self.units[row][col].number = i
                self.units[row][col].draw(self.main_frame, verbose=True, color="green")

                if self.solve_gui():
                    return True
                self.nums[row][col] = 0
                self.units[row][col].number = 0
                self.units[row][col].draw(self.main_frame, verbose=True, color="red")
        return False


class Unit:

    def __init__(self, number, row, col):
        self.number = number
        self.row = row
        self.col = col

    def draw(self, mf, verbose=False, color="SystemButtonFace"):
        unit_frame = LabelFrame(mf, padx=10, pady=10, bg=color)
        unit_frame.grid(row=self.row, column=self.col)
        if verbose:
            mf.update()
            sleep(0.05)
        Label(unit_frame, text=("  " if self.number == 0 else str(self.number))).pack()
        if verbose:
            mf.update()
            sleep(0.1)
            unit_frame.configure(bg="SystemButtonFace", fg="SystemButtonFace")
            mf.update()
            sleep(0.05)


if __name__ == '__main__':
    root = Tk()
    board = Board(root)
    root.mainloop()
