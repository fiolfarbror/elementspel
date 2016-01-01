#/usr/bin/env python

#kattonauter
#Import Modules
import os, pygame
from pygame.locals import *
if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'


def draw_board(boardSurface, boardColors):
    """
    Draws the game board onto a surface.
    The board position 0,0 is the upper left corner.
    The screen position 0,0 is also the upper left corner.
    Increasing X coordinate moves to the right.
    Increasing Y coordinate moves to the bottom. 
    """
    boardSurface.fill((250,250,250))
    for y in range(0,11):
        for x in range(0,11):
            boardSurface.fill(boardColors[x][y], # Color
                              Rect(x*40+1, y*40+1, 38, 38)) # Rect upper left 
                                                            # corner and size 


def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""
#Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Elementspel')
    pygame.mouse.set_visible(1)

    boardsize = 11
    squaresize = 40
#boardColors is a 2-dimensional array that contains which color each
#square of the board should have.
    boardColors = [[0 for j in range(boardsize)] for i in range(boardsize)]    
    for y in range(0,11):
        for x in range(0,11):
            #This is a bit crude. I use the RGB values directly.
            #We probably don't want it to work like that later.
            #For now there's a color shift across the board, we
            #will remove it once you understand how the board indexing
            #works.
            boardColors[x][y] = (30+x*10,30,30)

#The picture of the game board itself
    boardSurface = pygame.Surface((boardsize*squaresize, boardsize*squaresize))
    boardSurface = boardSurface.convert()
    boardSurface.fill((0,0,0))
    draw_board(boardSurface, boardColors)

#Create The Backgound
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 150, 150))

#Display The Background
#This is only the first time, it will be redrawn in the Main Loop below.
    screen.blit(background, (0, 0))
    screen.blit(boardSurface,(10,10))
    pygame.display.flip()


    clock = pygame.time.Clock()


#Main Loop
    while 1:
        clock.tick(60)

        #Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return

        #Draw a new board
        draw_board(boardSurface, boardColors)

        #Paste the drawing of the background and the board on the screen
        screen.blit(background, (0, 0))
        screen.blit(boardSurface,(10,10))
        
        #Show the screen to the player
        pygame.display.flip()




if __name__ == '__main__': main()
