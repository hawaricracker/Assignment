import random

class Minesweeper:
    def __init__(self, row, col, num_mines):
        self.row = row
        self.col = col
        self.num_mines = num_mines
        self.board = [['O' for i in range(col)] for j in range(row)]
        self.show_board = [['?' for i in range(self.col)] for j in range(self.row)]

        for mine in range(num_mines):
            x = random.randint(0, row - 1)
            y = random.randint(0, col - 1)
            while self.board[x][y] == 'X':
                x = random.randint(0, row - 1)
                y = random.randint(0, col - 1)
            self.board[x][y] = 'X'
    
    def print_board(self):
        for i in range(self.row):
            print("|", end="")
            for j in range(self.col):
                print(self.show_board[i][j], end="|")
            print()

    def check_win(self):
        cnt = 0
        for i in range(self.row):
            for j in range(self.col):
                if self.show_board[i][j] == 'O':
                    cnt += 1
        if cnt == self.row * self.col - self.num_mines:
            return True
        return False
    
    def start(self):
        print("Game started!")
        self.print_board()

        while True:
            print("Enter coordinates (row and column) to reveal a cell (e.g., 1 2):")
            x, y = map(int, input().split())
            if x < 0 or x >= self.row or y < 0 or y >= self.col:
                print("Invalid coordinates! Try again.")
                continue
            if self.board[x][y] == 'X':
                print("Game Over! You hit a mine.")
                self.show_board[x][y] = 'X'
                self.print_board()
                break
            else:
                self.show_board[x][y] = 'O'
                self.print_board()
                if self.check_win():
                    print("Congratulations! You cleared the board.")
                    break

row, col = map(int, input("Enter number of rows and columns: ").split())
num_mines = int(input("Enter number of mines: "))
board = Minesweeper(row, col, num_mines)
board.start()
