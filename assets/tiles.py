import pygame
import time
from assets.colors import colors_arr

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
      def draw(self, screen, color):
            for i in range(self.height):
                  for j in range(self.width):
                        x, y = self.coord[i][j][0], self.coord[i][j][1]
                        tile = pygame.Rect(x, y, 60, 60)
                        if color[i][j] == colors_arr[7] or color[i][j] == colors_arr[6]:
                              pygame.draw.rect(screen, color[i][j], tile, 2)
                              continue
                        pygame.draw.rect(screen, color[i][j], tile)

      #function will be used to make and animation when a letter is pressed
      def draw_insert_animation(self, ic, jc, screen, color, img):
            dx, dy = 60, 60
            for rep in range(5):
                  screen.fill(colors_arr[1])
                  screen.blit(img, (310, 25))
                  for i in range(self.height):
                        for j in range(self.width):
                              if i == ic and j == jc:
                                    dx += 2
                                    dy += 2
                                    x, y = self.coord[i][j][0] - rep * 2, self.coord[i][j][1] - rep * 2
                                    tile = pygame.Rect(x, y, dx, dy)
                                    pygame.draw.rect(screen, color[i][j], tile, 2)
                                    continue
                              x, y = self.coord[i][j][0], self.coord[i][j][1]
                              tile = pygame.Rect(x, y, 60, 60)
                              if color[i][j] == colors_arr[7] or color[i][j] == colors_arr[6]:
                                    pygame.draw.rect(screen, color[i][j], tile, 2)
                                    continue
                              pygame.draw.rect(screen, color[i][j], tile)

                  pygame.display.update()
                  time.sleep(0.01)
