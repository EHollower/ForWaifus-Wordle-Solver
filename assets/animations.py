import pygame
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
                                    dx += 1
                                    dy += 1
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
                  pygame.time.wait(8)

      #used for drawing the aniamtion when an invalid move is made troughout 
      def worng_animation(self, tiles, letters):
            height, width = tiles.height, tiles.width
            offset = [[[0, 0] for i in range(width)] for i in range(height)]
            for k in range(3):
                  for rep in range(10):
                        self.screen.fill(colors_arr[1])
                        self.screen.blit(self.title, (300, 25))
                        for i in range(height):
                              for j in range(width):
                                    if i == letters.y:
                                          offset[i][j][0], offset[i][j][1] = (rep + 1) * 1, 0 
                                          x, y = tiles.coord[i][j][0] + (rep + 1) * 1, tiles.coord[i][j][1]
                                          tile = pygame.Rect(x, y, 60,60)
                                          pygame.draw.rect(self.screen, colorTile[i][j], tile, 2)
                                          continue
                                    offset[i][j][0], offset[i][j][1] = 0, 0
                                    x, y = tiles.coord[i][j][0], tiles.coord[i][j][1]
                                    tile = pygame.Rect(x, y, 60, 60)
                                    if colorTile[i][j] == colors_arr[7] or colorTile[i][j] == colors_arr[6]:
                                          pygame.draw.rect(self.screen, colorTile[i][j], tile, 2)
                                          continue
                                    pygame.draw.rect(self.screen, colorTile[i][j], tile)
                        letters.draw_offset(self.screen, self.font, offset)
                        pygame.display.update()
                        pygame.time.wait(5)

                  for rep in range(10):
                        self.screen.fill(colors_arr[1])
                        self.screen.blit(self.title, (300, 25))
                        for i in range(height):
                              for j in range(width):
                                    if i == letters.y:
                                          offset[i][j][0], offset[i][j][1] = -((rep + 1) * 1), 0 
                                          x, y = tiles.coord[i][j][0] - (rep + 1) * 1, tiles.coord[i][j][1]
                                          tile = pygame.Rect(x, y, 60,60)
                                          pygame.draw.rect(self.screen, colorTile[i][j], tile, 2)
                                          continue
                                    offset[i][j][0], offset[i][j][1] = 0, 0
                                    x, y = tiles.coord[i][j][0], tiles.coord[i][j][1]
                                    tile = pygame.Rect(x, y, 60, 60)
                                    if colorTile[i][j] == colors_arr[7] or colorTile[i][j] == colors_arr[6]:
                                          pygame.draw.rect(self.screen, colorTile[i][j], tile, 2)
                                          continue
                                    pygame.draw.rect(self.screen, colorTile[i][j], tile)
                        letters.draw_offset(self.screen, self.font, offset)
                        pygame.display.update()
                        pygame.time.wait(5)
