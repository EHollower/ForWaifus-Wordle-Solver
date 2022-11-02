import pygame
import time
import random
from dictionary import wordle_dictionary
from sys import exit

#initialize game window, title and icon
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Wordle!")
icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)

#colors thats will be used
Green = "#538d4e"
Yellow = "#b59f3b"
Grey = "#3a3a3c"
Black = "#121213"
White = "#ffffff"
Red = "#cc0000"

#text that will be used in game window
img = pygame.image.load("assets/title.png").convert()
font = pygame.font.SysFont('Clear Sans', 40)

#matrix in whitch it is stored every color for each tile on the screen
colorTiles = [[Grey for i in range(10)] for i in range(10)]

#class will be used for drawing each tile on the screen
class Tiles:
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

      def draw(self):
            for i in range(self.height):
                  for j in range(self.width):
                        x, y = self.mat[i][j][0], self.mat[i][j][1]
                        color = colorTiles[i][j]
                        tile = pygame.Rect(x, y, 60, 60)
                        if color == Grey:
                              pygame.draw.rect(screen, color, tile, 2)
                              continue
                        pygame.draw.rect(screen, color, tile)

      def draw_wrong(self, i):
            for j in range(self.width):
                  x, y = self.mat[i][j][0], self.mat[i][j][1]
                  color = Red
                  tile = pygame.Rect(x, y, 60, 60)
                  pygame.draw.rect(screen, color, tile)


class Letters:
      def __init__(self, mat, width, height):
            self.width, self.height = width, height
            self.x = self.y = 0
            self.mat = mat
            self.str = [["" for i in range(self.width)] for i in range(self.height)]

      def draw(self):
            for i in range(self.height):
                  for j in range(self.width):
                        x, y = self.mat[i][j][0], self.mat[i][j][1]
                        TextSur = font.render(self.str[i][j], True, White)
                        TextRect = TextSur.get_rect()
                        TextRect.center = (x + 30, y + 30)
                        screen.blit(TextSur, TextRect)

      # def draw_outcome(self, color, y, Wordle):
      #       for x in range(self.width):
      #             if Wordle[x] == self.str[y][x]:
      #                   self.color[y][x] = Green
      #                   color[y][x] = Green
      #                   temp = list(Wordle)
      #                   temp[x] = '?'
      #                   Wordle = "".join(temp)

      #       for x in range(self.width):
      #             if self.str[y][x] in Wordle and self.color[y][x] == Black:
      #                   self.color[y][x] = Yellow
      #                   color[y][x] = Yellow
      #             elif self.color[y][x] == Black:
      #                   self.color[y][x] = Grey
      #                   color[y][x] = Grey

      #       for x in range(self.width):
      #             pygame.draw.rect(screen, self.color[y][x], pygame.Rect(self.mat[y][x][0], self.mat[y][x][1], 60, 60))
      #             text = font.render(self.str[y][x], True, White, self.color[y][x])
      #             screen.blit(text, (self.mat[y][x][0] + 20, self.mat[y][x][1] + 15))
      #             pygame.display.update()
      #             time.sleep(0.3)
      #       return

def main():
      clock = pygame.time.Clock()
      table = Tiles(5, 6)
      letter = Letters(table.mat, 5, 6)
      currWordle = random.choice(wordle_dictionary)
      print(currWordle)
      while True:
            #draw all the elements required to make a wordle api
            screen.fill(Black)
            screen.blit(img, (310, 25))
            table.draw()
            letter.draw()
            #events
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                  if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                              if letter.x >= 1:
                                    letter.str[letter.y][letter.x - 1] = ""
                                    letter.x -= 1

                        if event.key == pygame.K_RETURN:
                              if letter.x == 5 and letter.y < 6 and "".join(letter.str[letter.y]) in wordle_dictionary:
                                    letter.y += 1
                                    letter.x = 0
                              else:
                                    table.draw_wrong(letter.y)
                                    letter.draw()
                                    pygame.display.update()
                                    time.sleep(0.5)
                                    
                        key_pressed = event.unicode.upper()
                        if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                              if letter.x < letter.width:
                                    letter.str[letter.y][letter.x] = key_pressed
                                    letter.x += 1
                        
            #update everything
            pygame.display.update()
            clock.tick(60)
      return

if __name__ == '__main__':
      main()