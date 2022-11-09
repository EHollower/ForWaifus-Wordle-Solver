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
            for i in range(self.height):
                  for j in range(self.width):
                        x, y = self.coord[i][j][0], self.coord[i][j][1]
                        TextSur = font.render(self.str[i][j], True, colors_arr[0])
                        TextRect = TextSur.get_rect()
                        TextRect.center = (x + 30, y + 30)
                        screen.blit(TextSur, TextRect)