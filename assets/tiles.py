import pygame
import time
from assets.colors import colors_arr, colorTile

#class will be used to draw a Wordle table of height x width
class Tiles:
      #will initialize the coordinates on the screen of each tile
      def __init__(self, width, height):
            self.width, self.height = width, height
            self.coord = [[[0, 0] for i in range(width)] for i in range(height)]

            for i in range(self.height):
                  for j in range(self.width):
                        if i == 0 and j == 0:
                              self.coord[i][j][0], self.coord[i][j][1] = 210, 100
                        elif i > 0 and j == 0:
                              self.coord[i][j][0], self.coord[i][j][1] = self.coord[i - 1][j][0], self.coord[i - 1][j][1] + 65
                        else:
                              self.coord[i][j][0], self.coord[i][j][1] = self.coord[i][j - 1][0] + 65, self.coord[i][j - 1][1]

      #function will be used to draw each tile of the Wordle table
      def draw(self, screen):
            height, width = self.height, self.width
            for i in range(height):
                  for j in range(width):
                        x, y = self.coord[i][j][0], self.coord[i][j][1]
                        tile = pygame.Rect(x, y, 60, 60)
                        if colorTile[i][j] == colors_arr[7] or colorTile[i][j] == colors_arr[6]:
                              pygame.draw.rect(screen, colorTile[i][j], tile, 2)
                              continue
                        pygame.draw.rect(screen, colorTile[i][j], tile)