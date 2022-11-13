import pygame
from assets.colors import colors_arr, colorTemp, colorTile
from sys import exit

#this class will be used to draw the animation of the Worlde game
class Animations:
      def __init__(self, screen, title, font):
            self.screen = screen
            self.title = title
            self.font = font
            self.count = 0

      def screen_init(self):
            self.screen.fill(colors_arr[1])
            self.screen.blit(self.title, (300, 25))

            textsur = self.font.render("Number of guesses:", True, colors_arr[0])
            textrect = textsur.get_rect()
            textrect.center = (370, 530)
            self.screen.blit(textsur, textrect)
            
            cntsur = self.font.render(str(self.count), True, colors_arr[0])
            cntrect = cntsur.get_rect()
            cntrect.center = (370, 570)
            self.screen.blit(cntsur, cntrect)

      def event(self):
             for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()  

      #this funtion will be used to draw the animation when you insert a new letter
      def insert_animation(self, tiles, letters):
            height, width = tiles.height, tiles.width
            lx, ly = letters.x, letters.y
            #zoom out
            for rep in range(10):
                  self.event()   
                  self.screen_init()
                  for i in range(height):
                        for j in range(width):
                              x, y = tiles.coord[i][j][0], tiles.coord[i][j][1]
                              color = colorTile[i][j]
                              if i == ly and j == lx:
                                    tiles.draw_tile(self.screen, x - 5, y - 3, 60 + rep + 1, color)
                                    continue
                              tiles.draw_tile(self.screen, x, y, 60, color)

                  letters.draw(self.screen, self.font)
                  pygame.display.update()
                  pygame.time.Clock().tick(200)

      #this will draw the animation when a word is guessed
      def outcome_animation(self, tiles, letters):
            self.count += 1
            height, width = tiles.height, tiles.width
            ly = letters.y
            #zoom in
            for lx in range(width):
                  for rep in range(30):
                        self.event() 
                        self.screen_init()
                        for i in range(height):
                              for j in range(width):
                                    x, y = tiles.coord[i][j][0], tiles.coord[i][j][1]
                                    color = colorTile[i][j]
                                    if i == ly and j == lx:
                                          tiles.draw_tile(self.screen, x + rep, y + rep + 1, 60 - (rep + 1) * 2, color)
                                          continue
                                    tiles.draw_tile(self.screen, x, y, 60, color)

                        letters.draw(self.screen, self.font)
                        pygame.display.update()
                        pygame.time.Clock().tick(200)


                  
                  #zoom out
                  for rep in range(30):
                        self.event()
                        self.screen_init()
                        for i in range(height):
                              for j in range(width):
                                    x, y = tiles.coord[i][j][0], tiles.coord[i][j][1]
                                    txt = letters.str[i][j]
                                    color = colorTile[i][j]
                                    if i == ly and j == lx:
                                          tiles.draw_tile(self.screen, x + (29 - rep + 1), y, (rep + 1) * 2, colorTemp[j])
                                          colorTile[i][j] = colorTemp[j]
                                          letters.draw_letter(self.screen, x, y, txt, self.font)
                                          continue
                                    tiles.draw_tile(self.screen, x, y, 60, color)
                                    letters.draw_letter(self.screen, x, y, txt, self.font)

                        pygame.display.update()
                        pygame.time.Clock().tick(200)


      #used for drawing the aniamtion when an invalid move is made troughout 
      def worng_animation(self, tiles, letters):
            height, width = tiles.height, tiles.width
            ly = letters.y
            offset = [[[0, 0] for i in range(width)] for i in range(height)]
            #wigle around 3 times
            for rep in range(3):
                  #shift left
                  for rep in range(10):
                        self.event()
                        self.screen_init()
                        for i in range(height):
                              for j in range(width):
                                    x, y = tiles.coord[i][j][0], tiles.coord[i][j][1]
                                    color = colorTile[i][j]
                                    if i == ly:
                                          offset[i][j][0], offset[i][j][1] = rep + 1, 0
                                          tiles.draw_tile(self.screen, x + (rep + 1), y, 60, color)
                                          continue
                                    offset[i][j][0], offset[i][j][1] = 0, 0
                                    tiles.draw_tile(self.screen, x, y, 60, colorTile[i][j])
                        
                        letters.draw_offset(self.screen, self.font, offset)
                        pygame.display.update()
                        pygame.time.Clock().tick(200)

                  #shift right
                  for rep in range(10):
                        self.screen_init()
                        for i in range(height):
                              for j in range(width):
                                    if i == letters.y:
                                          offset[i][j][0], offset[i][j][1] = -(rep + 1), 0 
                                          tiles.draw_tile(self.screen, tiles.coord[i][j][0] - (rep + 1), tiles.coord[i][j][1], 60, colorTile[i][j])
                                          continue
                                    offset[i][j][0], offset[i][j][1] = 0, 0
                                    tiles.draw_tile(self.screen, tiles.coord[i][j][0], tiles.coord[i][j][1], 60, colorTile[i][j])
                        letters.draw_offset(self.screen, self.font, offset)
                        pygame.display.update()
                        pygame.time.Clock().tick(200)