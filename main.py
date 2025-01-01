# This the main file that runs the program and displaying GameState on the screen

import pygame as pg
import engine as chessEngine

# Initialize some of important data, size, height and width
Height = Width = 512 # Size of the chess board
DIMENSION = 8 # 8x8 block chess board
FPS = 15 # For later game edit about animation
SqSize = Height // DIMENSION 
IMAGES = {}


'''
Initialize global dictionary for import images
'''
def loadingImages():
    pieces = ["wp", "wR", "wQ", "wN", "wK", "wB", "bR", "bQ", "bp", "bN", "bK", "bB"]
    for piece in pieces:
        IMAGES[piece] = pg.transform.scale(pg.image.load("assets/images/" + piece + ".png"), (SqSize, SqSize))

def main():
    pg.init()
    screen = pg.display.set_mode((Width, Height))
    clock = pg.time.Clock()
    screen.fill(pg.Color("white"))
    gs = chessEngine.GameState()
    validMoves = gs.getValidMoves()
    moveMade = False # Flag variable for when a move is made

    loadingImages() # Doing this one once before while loop
    running = True
    SqSelected = () # No square is selected, keep track of the last click of the user (tuple: (col, row))
    PlayerClicks = [] # Keep track on player's click (two tuples: [(6, 4), (4, 4)])
    
    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
            # Mouse handler
            elif e.type == pg.MOUSEBUTTONDOWN:
                mouseLocation = pg.mouse.get_pos() # Get x, y of the mouse 
                mouseCol = mouseLocation[0] // SqSize  # Get the location column by the block in the nearest down number
                mouseRow = mouseLocation[1] // SqSize  # Get the location row by the block in the nearest down number
                # Append for the 1st and 2nd click
                '''Reset to empty tuple and array'''
                if SqSelected == (mouseRow, mouseCol):
                    SqSelected = ()
                    PlayerClicks = []
                else:
                    SqSelected = (mouseRow, mouseCol)
                    PlayerClicks.append(SqSelected)
                if len(PlayerClicks) == 2: # After 2nd Click
                    move = chessEngine.Move(PlayerClicks[0], PlayerClicks[1], gs.board)
                    print(move.getChessNotation())
                    if move in validMoves:
                        gs.makingMove(move) 
                        moveMade = True
                    gs.makingMove(move)
                    SqSelected = () # Reset user clicks
                    PlayerClicks = []
            # Key handler
            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_z: # Check undo if the key "z" is pressed
                    gs.undoMove()
                    moveMade = True
        if moveMade:
            validMoves = gs.getValidMoves()
            moveMade = False

        drawGameState(screen, gs)
        clock.tick(FPS)
        pg.display.flip()

def drawGameState(screen, gs):
    drawChessBoard(screen)
    drawChessPieces(screen, gs.board)

def drawChessBoard(screen):
    # 174, 198, 207: pastel blue
    pastelBlue = pg.Color(174, 198, 207)
    colors = [pastelBlue, pg.Color("pink")]
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = colors[((row + col) % 2)]
            pg.draw.rect(screen, color, pg.Rect(col * SqSize, row * SqSize, SqSize, SqSize))

def drawChessPieces(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            if piece != "--":
                screen.blit(IMAGES[piece], pg.Rect(col * SqSize, row * SqSize, SqSize, SqSize))

if __name__ == "__main__":
    main()