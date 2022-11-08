import pygame
import time
import random
from dictionary import wordle_dictionary
from assets.tiles import Tiles
from assets.colors import colors_arr
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Wordle!")
icon = pygame.image.load("assets/imgs/icon.png")
pygame.display.set_icon(icon)

colorTiles = [[colors_arr[6] for i in range(10)] for i in range(10)]

def main():
      tiles = Tiles(5, 6)
      clock = pygame.time.Clock()
      while True:
            screen.fill(colors_arr[1])
            tiles.draw(screen, colorTiles)

            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                  if event.type ==  pygame.KEYDOWN:
                        tiles.draw_animation(0, 0, screen, colorTiles)
                        

            pygame.display.update()
            clock.tick(60)

if __name__ == '__main__':
      main()