import pygame
import random
from dictionary import wordle_dictionary
from assets.colors import colors_arr, colorTemp, colorTile
from assets.tiles import Tiles
from assets.letters import Letters
from assets.animations import Animations
from sys import argv, exit, stderr
from inspect import signature

#This will initialize the Wordle game/game window
pygame.init()
screen = pygame.display.set_mode((800, 700))
pygame.display.set_caption("Wordle!")
icon = pygame.image.load("assets/imgs/icon.png")
pygame.display.set_icon(icon)

#title of the game
title = pygame.image.load("assets/imgs/title.png").convert()
#font of each letter
font = pygame.font.SysFont('Clear Sans', 40)

#classes the will be used to draw/animate the Wordle game
animations = Animations(screen, title, font)
tiles = Tiles(5, 6)
letters = Letters(tiles.coord, 5, 6)

run = True

def outcome(wordle, guess):
      global run
      freq = [0 for i in range(27)]
      n, code = len(wordle), 0
      for i in range(n):
            freq[ord(wordle[i]) - ord('A')] += 1

      for i in range(n):
            if guess[i] == wordle[i]:
                  colorTemp[i] = colors_arr[2]
                  code = code * 3 + 2
                  continue
            if freq[ord(guess[i]) - ord('A')] >= 1:
                  colorTemp[i] = colors_arr[3]
                  code = code * 3 + 1
                  continue
            colorTemp[i] = colors_arr[5]
            code = code * 3
      g = open("communication.txt", "w")
      g.write(str(code))
      g.close()

      if colorTemp.count(colors_arr[2]) == n:
            run = False

def main(wordle):
      #wordle = random.choice(wordle_dictionary)
      clock = pygame.time.Clock()
      while run:
            letters.permute()
            animations.screen_init()
            tiles.draw_table(screen)
            letters.draw(screen, font)
            f = open("communication.txt", "r")
            guess = f.read()
            f.close()
            if len(guess) == 5:                                
                  for ch in guess:
                        animations.insert_animation(tiles, letters)
                        letters.insert_letter(ch)
                        clock.tick(60)
                  outcome(wordle, letters.str[letters.y])
                  animations.outcome_animation(tiles, letters)
                  letters.enter_guess()
                  
            animations.event()                 

            pygame.display.update()
            clock.tick(60)

      while True:
            screen.fill(colors_arr[1])
            screen.blit(title, (300, 25))

            textsur = font.render("Total number of guesses:", True, colors_arr[0])
            textrect = textsur.get_rect()
            textrect.center = (370, 530)
            screen.blit(textsur, textrect)

            cntsur = font.render(str(animations.count), True, colors_arr[0])
            cntrect = cntsur.get_rect()
            cntrect.center = (370, 570)
            screen.blit(cntsur, cntrect)

            tiles.draw_table(screen)
            letters.draw(screen, font)
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        pygame.quit()
                        animations.p.terminate()
                        exit()
            pygame.display.update()
            clock.tick(60)

if __name__ == '__main__':
      main(random.choice(wordle_dictionary))