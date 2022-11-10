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
            for rep in range(10):
                  last = pygame.time.get_ticks()
                  self.screen.fill(colors_arr[1])
                  self.screen.blit(self.title, (300, 25))
                  letters.draw(self.screen, self.font)
                  for i in range(height):
                        for j in range(width):
                              if i == letters.y and j == letters.x:
                                    tiles.draw_tile(self.screen, tiles.coord[i][j][0] - 5, tiles.coord[i][j][1] - 3, 60 + rep + 1, colorTile[i][j])
                                    continue
                              tiles.draw_tile(self.screen, tiles.coord[i][j][0], tiles.coord[i][j][1], 60, colorTile[i][j])
                  pygame.display.update()
                  pygame.time.delay(5)

      #used for drawing the aniamtion when an invalid move is made troughout 
      def worng_animation(self, tiles, letters):
            height, width = tiles.height, tiles.width
            offset = [[[0, 0] for i in range(width)] for i in range(height)]
            for rep in range(3):
                  for rep in range(10):
                        self.screen.fill(colors_arr[1])
                        self.screen.blit(self.title, (300, 25))
                        for i in range(height):
                              for j in range(width):
                                    if i == letters.y:
                                          offset[i][j][0], offset[i][j][1] = rep + 1, 0
                                          tiles.draw_tile(self.screen, tiles.coord[i][j][0] + (rep + 1), tiles.coord[i][j][1], 60, colorTile[i][j])
                                          continue
                                    offset[i][j][0], offset[i][j][1] = 0, 0
                                    tiles.draw_tile(self.screen, tiles.coord[i][j][0], tiles.coord[i][j][1], 60, colorTile[i][j])
                        letters.draw_offset(self.screen, self.font, offset)
                        pygame.display.update()
                        pygame.time.delay(8)

                  for rep in range(10):
                        self.screen.fill(colors_arr[1])
                        self.screen.blit(self.title, (300, 25))
                        for i in range(height):
                              for j in range(width):
                                    if i == letters.y:
                                          offset[i][j][0], offset[i][j][1] = -(rep + 1), 0 
                                          tiles.draw_tile(self.screen, tiles.coord[i][j][0] - (rep + 1), tiles.coord[i][j][1], 60, colorTile[i][j])
                                          continue
                                    offset[i][j][0], offset[i][j][1] = 0, 0
                                    tiles.draw_tile(self.screen, tiles.coord[i][j][0], tiles.coord[i][j][1], 60, colorTile[i][j])
                        letters.draw_offset(self.screen, self.font, offset)
                        pygame.display.update()
                        pygame.time.delay(8)
