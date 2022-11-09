import pygame
import time
from assets.colors import colors_arr, colorTile

#this class will be used to draw the animation of the Worlde game
class Animations:
      def __init__(self, screen, title, font):
            self.screen = screen
            self.title = title
            self.font = font

      #this funtion will be used to draw the animation when you insert a new letter
      def insert_animation(self, tiles, letters):
            height, width = tiles.height, tiles.width
            dx, dy = 60, 60
            for rep in range(5):
                  self.screen.fill(colors_arr[1])
                  self.screen.blit(self.title, (300, 25))
                  letters.draw(self.screen, self.font)
                  for i in range(height):
                        for j in range(width):
                              if i == letters.y and j == letters.x:
                                    if i % 2 == 0: dx += 1
                                    if i % 2 == 0: dy += 1
                                    x, y = tiles.coord[i][j][0] - rep * 2, tiles.coord[i][j][1] - rep * 2
                                    tile = pygame.Rect(x, y, dx, dy)
                                    pygame.draw.rect(self.screen, colorTile[i][j], tile, 2)
                                    continue
                              x, y = tiles.coord[i][j][0], tiles.coord[i][j][1]
                              tile = pygame.Rect(x, y, 60, 60)
                              if colorTile[i][j] == colors_arr[7] or colorTile[i][j] == colors_arr[6]:
                                    pygame.draw.rect(self.screen, colorTile[i][j], tile, 2)
                                    continue
                              pygame.draw.rect(self.screen, colorTile[i][j], tile)
                  pygame.display.update()
                  #.sleep(0.008)