import pygame
import time
from assets.colors import colors_arr, colorTile

#classed will be used draw the letters pressed so far
class Letters:
      #initialize to find the coordinates on the screen in witch a letter should be placed if typed
      def __init__(self, coord, width, height):
            self.width, self.height = width, height
            self.x = self.y = 0
            self.coord = coord
            self.str = [["" for i in range(self.width)] for i in range(self.height)]

      #inserting a new letter
      def insert_letter(self, letter):
            if self.x < self.width:
                  self.str[self.y][self.x] = letter
                  colorTile[self.y][self.x] = colors_arr[6]
                  self.x += 1

      def delete_letter(self):
            if self.x >= 1:
                  self.x -= 1
                  self.str[self.y][self.x] = ""
                  colorTile[self.y][self.x] = colors_arr[7]

      #will draw all the current letters pressed so far
      def draw(self, screen, font):
            height, width = self.height, self.width
            for i in range(height):
                  for j in range(width):
                        x, y = self.coord[i][j][0], self.coord[i][j][1]
                        textsur = font.render(self.str[i][j], True, colors_arr[0])
                        textrect = textsur.get_rect()
                        textrect.center = (x + 30, y + 30)
                        screen.blit(textsur, textrect)

      #will be used to draw the letters when we are using animations.worng_animation
      def draw_offset(self, screen, font, offset):
            height, width = self.height, self.width
            for i in range(height):
                  for j in range(width):
                        x, y = self.coord[i][j][0] + offset[i][j][0], self.coord[i][j][1] + offset[i][j][1]
                        textsur = font.render(self.str[i][j], True, colors_arr[0])
                        textrect = textsur.get_rect()
                        textrect.center = (x + 30, y + 30)
                        screen.blit(textsur, textrect)