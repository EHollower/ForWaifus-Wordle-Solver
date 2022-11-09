import pygame
from dictionary import wordle_dictionary
from assets.colors import colors_arr
from assets.tiles import Tiles
from assets.letters import Letters
from sys import exit

#This will initialize the Wordle game/game window
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Wordle!")
icon = pygame.image.load("assets/imgs/icon.png")
pygame.display.set_icon(icon)

#this grid will tell what each tile color should be throughout the Worlde game
colorTiles = [[colors_arr[7] for i in range(10)] for i in range(10)]

#title of the game
img = pygame.image.load("assets/imgs/title.png").convert()
#font of each letter
font = pygame.font.SysFont('Clear Sans', 40)

def main():
      tiles = Tiles(5, 6)
      letters = Letters(tiles.coord, 5, 6)
      clock = pygame.time.Clock()
      while True:
            screen.fill(colors_arr[1])
            screen.blit(img, (310, 25))
            tiles.draw(screen, colorTiles)
            letters.draw(screen, font)

            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                  if event.type ==  pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                              if letters.x >= 1:
                                    letters.str[letters.y][letters.x - 1] = ""
                                    colorTiles[letters.y][letters.x - 1] = colors_arr[7]
                                    letters.x -= 1

                        key_pressed = event.unicode.upper()
                        if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                              if letters.x < letters.width:
                                    tiles.draw_insert_animation(letters.y, letters.x, screen, colorTiles, img)
                                    letters.insert_letter(letters.y, letters.x, key_pressed)
                                    colorTiles[letters.y][letters.x] = colors_arr[6]
                                    letters.x += 1
                        

            pygame.display.update()
            clock.tick(60)

if __name__ == '__main__':
      main()