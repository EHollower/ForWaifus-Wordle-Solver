import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Wordle!")
icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)

background = pygame.image.load("assets/tiles.png")
background_rect = background.get_rect(center = (400, 300))

Green = "#538d4e"
Yellow = "#b59f3b"
Grey = "#3a3a3c"

def main():
      clock = pygame.time.Clock()
      while True:
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
            #draw all the elements required to make a wordle api
            screen.fill("#121213")
            screen.blit(background, background_rect)
            #update everything
            pygame.display.update()
            clock.tick(60)

if __name__ == '__main__':
      main()