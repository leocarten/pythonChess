from tkinter import *
from tkinter.ttk import *

firstPick = ""
secondPick = ""
result_var = ""
possibleMoves = []
chess_pieces = {'b': 'bb.png', 'k': 'bk.png', 'n': 'bn.png', 'p': 'bp.png', 'q': 'bq.png', 'r': 'br.png',
                'B': 'wb.png', 'K': 'wk.png', 'N': 'wn.png', 'P': 'wp.png', 'Q': 'wq.png', 'R': 'wr.png'}

# This handles the on click method
class uiChessboard:
    def __init__(self, fenString, possibleMovesList):
        self.root = Tk()
        global possibleMoves
        possibleMoves = possibleMovesList
        self.create_chessboard(fenString)
        self.root.mainloop()

    def handle_click(self, button, row, col):
        global firstPick, secondPick, possibleMoves, result_var
        nums = "12345678"
        letter = "abcdefgh"
        if firstPick == "":
            result_var = StringVar()
            firstPick = f"{letter[col]}{nums[row]}"  # Adjust row index here
        elif secondPick == "":
            secondPick = f"{letter[col]}{nums[row]}"  # Adjust row index here
            print(f"Here are the two picks: {firstPick}, {secondPick}")
            if firstPick + secondPick in possibleMoves:
                self.root.destroy()  # Destroy the existing root window
                result_var = f"{firstPick}{secondPick}"
                print(f"Here is what the player picked [{result_var}]")

            firstPick = ""
            secondPick = ""

    
    def getMoveChosen(self):
        global result_var
        print(f"Here is what the player picked [{result_var}]")
        return result_var

    def close_window(self):
        self.root.destroy()

    def flip_fen(self, original_fen):
        rows = original_fen.split('/')
        flipped_rows = [''.join(reversed(row)) for row in rows]
        flipped_fen = '/'.join(flipped_rows)
        return flipped_fen

    def create_chessboard(self, fenString):
        fenString = self.flip_fen(fenString)
        if self.root.winfo_exists():  # Check if the root window still exists
            self.root.title("Chessboard")
            for widget in self.root.winfo_children():
                widget.destroy()

            row = fenString.split("/")
            buttons = [[None for _ in range(8)] for _ in range(8)]
            for i in range(7, -1, -1):  # Iterate through rows in reverse order
                r = row[7 - i]  # Get the row in reverse order
                col = 0
                for j in range(len(r)-1, -1, -1):  # Iterate through each character of the row from right to left
                    square = r[j]
                    if square.isdigit():
                        for _ in range(int(square)):
                            color = "white" if (i + col) % 2 == 0 else "black"
                            button = Button(self.root, text='', compound='center',
                                            command=lambda row=i, col=col: self.handle_click(button, row, col))
                            button.grid(row=i, column=col, padx=2, pady=2, ipady=20)
                            buttons[i][col] = button
                            col += 1
                    else:
                        color = "white" if (i + col) % 2 == 0 else "black"
                        photo = PhotoImage(file=chess_pieces[square])
                        button = Button(self.root, text='', image=photo,
                                        command=lambda row=i, col=col: self.handle_click(button, row, col))
                        button.image = photo
                        button.grid(row=i, column=col)
                        buttons[i][col] = button
                        col += 1




def main():
    FEN = "r1bk3r/p2pBpNp/n4n2/1p1NP2P/6P1/3P4/P1P1K3/q5b1"
    possibleMoves = ["a1a2", "a3b2"]
    chessboardGUI = uiChessboard(FEN,possibleMoves)
    move = chessboardGUI.getMoveChosen()
    FEN = "8/8/8/8/8/8/8/8"
    possibleMoves = ["a1a2"]
    chessboardGUI = uiChessboard(FEN, possibleMoves)
    move = chessboardGUI.getMoveChosen()

if __name__ == "__main__":
    main()
