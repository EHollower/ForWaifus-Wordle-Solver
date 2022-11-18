"""
The following program is a standard implementaion of the wordle game without the solver
This program was made first to test some interactions/animations more easly than with game.py 
"""

import pygame
import random

from assets.animations import *
from assets.interface import *
from assets.letters import *
from assets.colors import *
from assets.tiles import *

from dictionary import wordle_dictionary

#This will initialize the Wordle game/game window
pygame.init()
configs = GameConfig()

#classes the will be used to draw/animate the wordle game
animations = Animations()
tiles = Tiles(5, 6)
letters = Letters(tiles.coord, 5, 6)

def main():
      wordle = random.choice(wordle_dictionary)

      run, score = True, 0
      animations.turn_on()
      last = 0
      while run:
            configs.screen_init_(score, run)

            letters.permute() #permutes the table up by one row if the number of guesses is bigger than 6
            tiles.draw_table(configs.screen) #draws the table of guesses
            letters.draw(configs.screen, configs.font) #draws each letter inside the table of guesses

            for event in pygame.event.get():
                  #close the program
                  if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                  
                  if event.type ==  pygame.KEYDOWN:
                        #delete letter
                        if event.key == pygame.K_BACKSPACE:
                              letters.delete_letter()
                        
                        if event.key == pygame.K_RETURN:
                              now = pygame.time.get_ticks()
                              
                              #verify if the guess made is a word contained in the dictionary of words that we have
                              if "".join(letters.str[letters.y]) in wordle_dictionary:
                                    score += 1
                                    run = outcome(wordle, letters.str[letters.y])
                                    animations.outcome_animation(configs, tiles, letters, score)
                                    letters.enter_guess()
                                    continue
                                    
                              if now - last >= 300:
                                    animations.worng_animation(configs, tiles, letters, score)
                                    last = pygame.time.get_ticks()

                        key_pressed = event.unicode.upper()
                        if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                              animations.insert_animation(configs, tiles, letters, score)
                              letters.insert_letter(key_pressed)
                        
            configs.update_screen()
            

      while True:
            configs.screen_init_(score, run)

            tiles.draw_table(configs.screen)
            letters.draw(configs.screen, configs.font)

            for event in pygame.event.get():
                  #close the program
                  if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

            configs.update_screen()

if __name__ == '__main__':
      main()