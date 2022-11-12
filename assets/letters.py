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

      #continue the game if you did not guess the word in 6 tires
      def permute(self):
            if self.y == self.height:
                  height, width = self.height, self.width
                  for i in range(height):
                        for j in range(width):
                              if i + 1 < height:
                                    self.str[i][j] = self.str[i + 1][j]
                                    colorTile[i][j] = colorTile[i + 1][j]
                              else:
                                    self.str[i][j] = ""
                                    colorTile[i][j] = colors_arr[7]
                  self.y -= 1

      #inserting a new letter
      def insert_letter(self, letter):
            if self.x < self.width:
                  self.str[self.y][self.x] = letter
                  colorTile[self.y][self.x] = colors_arr[6]
                  self.x += 1

      #deleting a letter
      def delete_letter(self):
            if self.x >= 1:
                  self.x -= 1
                  self.str[self.y][self.x] = ""
                  colorTile[self.y][self.x] = colors_arr[7]

      #entering a whole word
      def enter_guess(self):
            self.y += 1
            self.x = 0

      def draw_letter(self, screen, x, y, txt, font):
            textsur = font.render(txt, True, colors_arr[0])
            textrect = textsur.get_rect()
            textrect.center = (x + 30, y + 30)
            screen.blit(textsur, textrect)

      #will draw all the current letters pressed so far
      def draw(self, screen, font):
            height, width = self.height, self.width
            for i in range(height):
                  for j in range(width):
                        x, y = self.coord[i][j][0], self.coord[i][j][1]
                        txt = self.str[i][j]
                        self.draw_letter(screen, x, y, txt, font)

      #will be used to draw the letters when we are using animations.worng_animation
      def draw_offset(self, screen, font, offset):
            height, width = self.height, self.width
            for i in range(height):
                  for j in range(width):
                        x, y = self.coord[i][j][0] + offset[i][j][0], self.coord[i][j][1] + offset[i][j][1]
                        txt = self.str[i][j]
                        self.draw_letter(screen, x, y, txt, font)