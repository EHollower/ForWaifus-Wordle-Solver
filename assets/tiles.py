import pygame
import time
from assets.colors import colors_arr

#class will be used to draw a Wordle table of height x width
class Tiles:
      #will initialize the coordinates on the screen of each tile
      def __init__(self, width, height):
            self.width, self.height = width, height
            self.mat = [[[0, 0] for i in range(width)] for i in range(height)]

            for i in range(self.height):
                  for j in range(self.width):
                        if i == 0 and j == 0:
                              self.mat[i][j][0], self.mat[i][j][1] = 210, 100
                        elif i > 0 and j == 0:
                              self.mat[i][j][0], self.mat[i][j][1] = self.mat[i - 1][j][0], self.mat[i - 1][j][1] + 65
                        else:
                              self.mat[i][j][0], self.mat[i][j][1] = self.mat[i][j - 1][0] + 65, self.mat[i][j - 1][1]

      #function will be used to draw each tile of the Wordle table
      def draw(self, screen, color):
            for i in range(self.height):
                  for j in range(self.width):
                        x, y = self.mat[i][j][0], self.mat[i][j][1]
                        tile = pygame.Rect(x, y, 60, 60)
                        if color[i][j] == colors_arr[6]:
                              pygame.draw.rect(screen, color[i][j], tile, 2)
                              continue
                        pygame.draw.rect(screen, color[i][j], tile)


      def draw_animation(self, i, j, screen, color):
            dx, dy = 60, 60
            for p in range(5):
                  dx += 3
                  dy += 3
                  x, y = self.mat[i][j][0] - p * 2, self.mat[i][j][1] - p * 2
                  tile = pygame.Rect(x, y, dx, dy)
                  screen.fill(colors_arr[1])
                  pygame.draw.rect(screen, color[i][j], tile, 2)
                  pygame.display.update()
                  time.sleep(0.01)
