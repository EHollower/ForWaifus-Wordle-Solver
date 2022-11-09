import pygame
from dictionary import wordle_dictionary
from assets.colors import colors_arr
from assets.tiles import Tiles
from assets.letters import Letters
from assets.animations import Animations
from sys import exit

#This will initialize the Wordle game/game window
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Wordle!")
icon = pygame.image.load("assets/imgs/icon.png")
pygame.display.set_icon(icon)

#title of the game
title = pygame.image.load("assets/imgs/title.png").convert()
#font of each letter
font = pygame.font.SysFont('Clear Sans', 40)

def main():
      animations = Animations(screen, title, font)
      tiles = Tiles(5, 6)
      letters = Letters(tiles.coord, 5, 6)
      clock = pygame.time.Clock()
      while True:
            screen.fill(colors_arr[1])
            screen.blit(title, (300, 25))
            tiles.draw(screen)
            letters.draw(screen, font)

            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                  if event.type ==  pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                              letters.delete_letter()

                        key_pressed = event.unicode.upper()
                        if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                              animations.insert_animation(tiles, letters)
                              letters.insert_letter(key_pressed)
                        

            pygame.display.update()
            clock.tick(60)

if __name__ == '__main__':
      main()