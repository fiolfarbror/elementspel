#/usr/bin/env python


#Import Modules
import os, pygame
from pygame.locals import *
if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'


def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""
#Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Elementspel')
    pygame.mouse.set_visible(1)

#Create The Backgound
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 150, 150))
#Display The Background
    screen.blit(background, (0, 0))
    pygame.display.flip()


    clock = pygame.time.Clock()


    i = 0
#Main Loop
    while 1:
        clock.tick(60)
        i = i + 1
        print "Hej, kaka" + str(i)
    #Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return


    #Draw Everything
        screen.blit(background, (0, 0))
        pygame.display.flip()




if __name__ == '__main__': main()
