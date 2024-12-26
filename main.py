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
    loadingImages() # Doing this one once before while loop
    running = True
    
    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False

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