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
Greyy = "#3a3a3d"
Black = "#121213"
White = "#ffffff"
Red = "#cc0000"

#text that will be used in game window
img = pygame.image.load("assets/title.png").convert()
font = pygame.font.SysFont('Clear Sans', 40)

#matrix in whitch it is stored every color for each tile on the screen
colorTiles = [[Greyy for i in range(10)] for i in range(10)]

#count number of green tiles this time
greenTiles = 0

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
                        if color == Greyy:
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

def draw_outcome(letter, i, wordle, answer, greenTiles):
      n = len(wordle)
      greenTiles = 0
      for j in range(n):
            if answer[j] == wordle[j]:
                  colorTiles[i][j] = Green
                  wordle[j] = '?'
                  greenTiles += 1
      
      for j in range(n):
            if answer[j] in wordle and colorTiles[i][j] == Greyy:
                  colorTiles[i][j] = Yellow
            elif colorTiles[i][j] == Greyy:
                  colorTiles[i][j] = Grey

      for j in range(n):
            x, y = letter.mat[i][j][0], letter.mat[i][j][1]
            color = colorTiles[i][j]
            tile = pygame.Rect(x, y, 60, 60)
            pygame.draw.rect(screen, color, tile)
            TextSur = font.render(letter.str[i][j], True, White)
            TextRect = TextSur.get_rect()
            TextRect.center = (x + 30, y + 30)
            screen.blit(TextSur, TextRect)
            time.sleep(0.3)
            pygame.display.update()


def victory_screen():
      TextSur = font.render("YOU Guessed the Wordle\nPlay again?", True, White)
      TextRect = TextSur.get_rect()
      TextRect.center = (400, 300)
      screen.blit(TextSur, TextRect)
      pygame.display.update()

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
                                    draw_outcome(letter, letter.y, list(currWordle), letter.str[letter.y], greenTiles)
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
                                    
            if greenTiles == letter.width:
                  print("IN")
                  victory_screen()
                  return
            #update everything
            pygame.display.update()
            clock.tick(60)
      return

if __name__ == '__main__':
      main()