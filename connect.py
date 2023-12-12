import tkinter as tk

# Constants
EMPTY = '.'
PLAYER1 = 'X'
PLAYER2 = 'O'
ROWS = 6
COLS = 7

# Initialize the game board
def create_board():
    return [[EMPTY] * COLS for _ in range(ROWS)]

# Check if a column is full
def is_column_full(board, col):
    return board[0][col] != EMPTY

# Drop a piece in a column
def drop_piece(board, col, player):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = player
            return True
    return False

# Check for a win
def check_win(board, player):
    # Check for horizontal win
    for row in range(ROWS):
        for col in range(COLS - 3):
            if all(board[row][col + i] == player for i in range(4)):
                return True

    # Check for vertical win
    for row in range(ROWS - 3):
        for col in range(COLS):
            if all(board[row + i][col] == player for i in range(4)):
                return True

    # Check for diagonal win (top-left to bottom-right)
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True

    # Check for diagonal win (bottom-left to top-right)
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if all(board[row - i][col + i] == player for i in range(4)):
                return True

    return False

class ConnectFourGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect Four")

        self.board = create_board()
        self.current_player = PLAYER1
        self.winner = None

        self.canvas = tk.Canvas(root, width=COLS * 80, height=(ROWS + 1) * 80)
        self.canvas.pack()
        self.draw_board()

        self.canvas.bind("<Button-1>", self.on_click)

    def draw_board(self):
        self.canvas.delete("all")
        for row in range(ROWS):
            for col in range(COLS):
                x1, y1 = col * 80, (row + 1) * 80
                x2, y2 = (col + 1) * 80, (row + 2) * 80
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="blue", fill="white")

                if self.board[row][col] == PLAYER1:
                    self.canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, outline="blue", fill="red")
                elif self.board[row][col] == PLAYER2:
                    self.canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, outline="blue", fill="yellow")

        if self.winner:
            self.canvas.create_text(COLS * 40, ROWS * 40, text=f"Player {self.winner} wins!", font=("Helvetica", 24))

    def on_click(self, event):
        if self.winner:
            return

        col = event.x // 80
        if col < 0 or col >= COLS or is_column_full(self.board, col):
            return

        if drop_piece(self.board, col, self.current_player):
            self.draw_board()
            if check_win(self.board, self.current_player):
                self.winner = self.current_player
                self.draw_board()
            else:
                self.current_player = PLAYER2 if self.current_player == PLAYER1 else PLAYER1

if __name__ == "__main__":
    root = tk.Tk()
    game = ConnectFourGUI(root)
    root.mainloop()
