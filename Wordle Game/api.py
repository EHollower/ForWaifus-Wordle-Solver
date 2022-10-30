import pygame
from sys import exit

#initialize game window
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Wordle!")
icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)


#colors thats will be used
Green = "#538d4e"
Yellow = "#b59f3b"
Grey = "#3a3a3c"
Black = "#121213"
White = "#ffffff"

img = pygame.image.load("assets/title.png").convert()

def main():
      clock = pygame.time.Clock()
      while True:
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
            #draw all the elements required to make a wordle api
            screen.fill(Black)
            screen.blit(img, (310, 25))
            #update everything
            pygame.display.update()
            clock.tick(60)

if __name__ == '__main__':
      main()