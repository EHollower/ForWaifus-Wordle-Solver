import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Wordle")

def main():
      clock = pygame.time.Clock()
      while True:
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
            #draw all the elements required to make a wordle api
            #update everything
            pygame.display.update()
            clock.tick(60)

if __name__ == '__main__':
      main()