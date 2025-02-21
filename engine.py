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

    # Takes a Move as a parameter
    def makingMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.piecesMoved
        self.transferedLog.append(move) # Log the move so we can undo it later
        self.whiteMoving = not self.whiteMoving # Swap player 

    # Undo the last move 
    def undoMove(self):
        if len(self.transferedLog) != 0: # Make sure that there is a move to undo
            move = self.transferedLog.pop()
            self.board[move.startRow][move.startCol] = move.piecesMoved
            self.board[move.endRow][move.endCol] = move.piecesCaptured
            self.whiteMoving = not self.whiteMoving # Switch turn back

    # All moves considering checks
    def getValidMoves(self):
        return self.getAllPossibleMoves()  # Not worry about checking 

    # All moves without considering checks
    def getAllPossibleMoves(self):
        moves = []
        for row in range(len(self.board)): # number of rows
            for col in range(len(self.board[row])): # number of cols in given rows
                turn = self.board[row][col][0]
                if (turn == "w" and self.whiteMoving) and (turn == "b" and not self.whiteMoving):
                    piece = self.board[row][col][1]
                    if piece == "p":
                        self.getPawnMoves(row, col, moves)
                    elif piece == "R":
                        self.getRookMoves(row, col, moves)
        return moves

    "Get all the possilbe pawn moves locate at row and col, also save it to the list"
    def getPawnMoves(self, row, col, moves):
        if self.whiteMoving: # white pawns move
            if self.board[row - 1][col] == "--": # 1 square pawn advance
                moves.append(Move((row, col), (row - 1, col), self.board))
                if row == 6 and self.board[row - 2][col] == "--": # 2 square pawn advance
                    

    "Get all the possilbe rook moves locate at row and col, also save it to the list"
    def getRookMoves(self, row, col, moves):
        pass

class Move():
    # Map keys to values
    # Key: value

    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}


    # Initialize all move, from start to end location row and column, and also create a 2d list contain location of piece start move and end move
    def __init__(self, startSQ, endSQ, board):
        self.startRow = startSQ[0]
        self.startCol = startSQ[1]
        self.endRow = endSQ[0]
        self.endCol = endSQ[1]
        self.piecesMoved = board[self.startRow][self.startCol]
        self.piecesCaptured = board[self.endRow][self.endCol]
        self.moveID = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol
        print(self.moveID)

    """
    Overriding the equals method
    """
    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False

    def getChessNotation(self):
        # Adding to make this like real life chess notation 
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, row, col):
        return self.colsToFiles[col] + self.rowsToRanks[row]