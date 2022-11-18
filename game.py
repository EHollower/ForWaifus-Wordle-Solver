"""
The following program is ment to work as the interface for the wordle game

How does it work: -> we will use the pygame library to draw on the screen,the wordle game and animate it as we like
                  -> it waits for solver.exe to give input and puts it on the screen
                  -> it gives as a response a base 3 number based on the coloring of the guess

If you wish to play our implementaion of the wordle game we have a shell.py that does not interact the solver.exe

Disclaimer: 
It implements the buggy version of the worlde game as we were requested to do !!!

Most of the functionalities of the program are partitioned into classes such to reduce the spaghetti code and imporve readability
We used pygame since we are the the most familiar with libarary for such things and its functionalities/work with python programs
"""

#libaries/assets that we will need for the wordle game and solver
import pygame
import random
import subprocess

"""
all of these imports are used to clear up the code and imporve readability such that we can make changes to the code fast and avoid making spaghetti code in the process
assets.interactor is the main way we intercat with the solver
assets.animation is tries to create the original wordle animations, implemented beacause -> we thought it would be fun to implement them in python
                                                                                         -> it would make for a much better presentation of how the solver interacts without pumping all the inputs on the screen in the same time
assets.interface was made to clear up the code it more or less handles everything related to the program/program window without making the code more unreadable
assets.tiles/letters/colors are used to create mimic/create the wordle game, as close as we could
dictionary contains a list with all the words in cuvinte_wordle.txt
"""
from assets.interactor import *
from assets.animations import *
from assets.interface import *
from assets.letters import *
from assets.colors import *
from assets.tiles import *
from dictionary import *

#here we initialize the game window
pygame.init()
configs = GameConfig()

#classes the will be used to draw/animate the wordle game
animations = Animations()
tiles = Tiles(5, 6)
letters = Letters(tiles.coord, 5, 6)

def main(wordle):
      #creates a new process (the solver) that will interact with 
      subprocess.Popen(["solver"], shell=True)
      clear_data()

      run, score = True, 0 
      #to turn off use animations.turn_off()
      animations.turn_on()
      while run:
            #draw everything that we have/updated until we reach the final 
            #in case of an an extarnal input 
            configs.event_handle_solver()
            configs.screen_init_(score, run)

            letters.permute() #permutes the table up by one row if the number of guesses is bigger than 6
            tiles.draw_table(configs.screen) #draws the table of guesses
            letters.draw(configs.screen, configs.font) #draws each letter inside the table of guesses

            guess = get_word() #interacts with the solver
            #if we have another guess insert it
            if len(guess) == 5:
                  #add 1 more guess to the score
                  score += 1                                
                  for ch in guess:
                        animations.insert_animation(configs, tiles, letters, score)
                        letters.insert_letter(ch)

                        if animations.active:
                              configs.update_screen(60)

                  run = outcome(wordle, letters.str[letters.y])
                  animations.outcome_animation(configs, tiles, letters, score)
                  letters.enter_guess()
            
            configs.update_screen()

      while True:
            configs.event_handle_solver()
            configs.screen_init_(score, run)

            tiles.draw_table(configs.screen)
            letters.draw(configs.screen, configs.font)

            configs.update_screen()

if __name__ == '__main__':
      wordle = random.choice(wordle_dictionary)
      main(wordle)