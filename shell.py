import pygame
import random
from dictionary import wordle_dictionary
from assets.colors import colors_arr, colorTemp, colorTile
from assets.tiles import Tiles
from assets.letters import Letters
from assets.animations import Animations
from sys import exit

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
      n = len(wordle)
      for j in range(n):
            colorTemp[j] = colors_arr[7]
            if guess[j] == wordle[j]:
                  colorTemp[j] = colors_arr[2]
      
      for j in range(n):
            if guess[j] in wordle and colorTemp[j] == colors_arr[7]: colorTemp[j] = colors_arr[3]
            elif colorTemp[j] == colors_arr[7]: colorTemp[j] = colors_arr[5]

      if colorTemp.count(colors_arr[2]) == n:
            run = False

def main():
      wordle = random.choice(wordle_dictionary)
      print(wordle)
      clock = pygame.time.Clock()
      last = 0
      while run:
            letters.permute()
            animations.screen_init()
            tiles.draw_table(screen)
            letters.draw(screen, font)
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                  
                  if event.type ==  pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                              letters.delete_letter()
                        
                        if event.key == pygame.K_RETURN:
                              now = pygame.time.get_ticks()
                              
                              if "".join(letters.str[letters.y]) in wordle_dictionary:
                                    outcome(wordle, letters.str[letters.y])
                                    animations.outcome_animation(tiles, letters)
                                    letters.enter_guess()
                                    continue
                                    
                              if now - last >= 300:
                                    animations.worng_animation(tiles, letters)
                                    last = pygame.time.get_ticks()

                        key_pressed = event.unicode.upper()
                        if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                              animations.insert_animation(tiles, letters)
                              letters.insert_letter(key_pressed)
                        

            pygame.display.update()
            clock.tick(60)

      while True:
            animations.screen_init()

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
                        exit()
            pygame.display.update()
            clock.tick(60)

if __name__ == '__main__':
      main()