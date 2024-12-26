# This class is repsonsible for storing information about the current state of a chess game. 
# It will also be responsible for determining the valid moves at the current state. It will also keep a move log.

class GameState():
    def __init__(self):
        # board is a 8x8 2d list, contains 2 characters
        # The first character represent for color of pieces, "b" or "w" which means black or white
        # The second character represent for type of pieces, "K" for King, "Q" or Queen, "N" for Knight, "R" for Rook, "B" for Bishop and "P" for Pawn
        # The "--" represent empty space, no piece on it
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.whiteMoving = True
        self.transferedLog = []