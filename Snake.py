import pygame
import os
import random

SCREEN_TITLE = "Snake"
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 780

WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
RED_COLOR = (255, 40, 0)

gameScreen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
gameScreen.fill(WHITE_COLOR)

current_path = os.path.dirname(__file__)

clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.SysFont("comicsans", 75)


class Game:

    TICK_SPEED = 10

    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        self.gameScreen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.gameScreen.fill(BLACK_COLOR)
        pygame.display.set_caption(SCREEN_TITLE)

    def runGameLoop(self):
        isGameRunning = True

        player = SNAKE(WHITE_COLOR, 570, 360, 0, 5, 30, 30)

        while isGameRunning:
            gameScreen.fill(BLACK_COLOR)

            player.move()
            player.pos()

            
            clock.tick(self.TICK_SPEED)

class GameObject:

    def __init__(self, color, x, y, width, height):
        self.color = color
        self.xPos = x
        self.yPos = y
        self.width = width
        self.height = height
        
    def food(self):
        pass


class SNAKE(GameObject):

    body = []
    turns = {}
    posx = [570, 570, 570, 570, 570]
    posy = [360, 360, 360, 360, 360]

    def __init__(self, color, x, y, direction, length, width, height):
        super().__init__(color, x, y, width, height)

        self.length = length
        self.direction = direction

    def move(self):

        print(self.direction)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if self.direction != 2 != 1 and event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.direction = 1           
                elif self.direction != 1 and event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.direction = 2                    
                elif self.direction != 4 and event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.direction = 3                        
                elif self.direction != 3 and event.key == pygame.K_DOWN or event.key == pygame.K_s: 
                    self.direction = 4                          
                print(event)
                print(self.turns)

        if self.direction == 1:
            self.xPos += 30
        if self.direction == 2:
            self.xPos -= 30
        if self.direction == 3:
            self.yPos -= 30
        if self.direction == 4:
            self.yPos += 30

        if self.xPos < 0:
            self.xPos = 1200
        elif self.xPos == 1200:
            self.xPos = 0
        if self.yPos < 0:
            self.yPos = 780
        elif self.yPos== 780:
            self.yPos = 0

    def pos(self):

        self.posx.insert(0, self.xPos)
        self.posy.insert(0, self.yPos)

        if len(self.posx) > self.length:
            self.posx.pop(self.length)
        if len(self.posy) > self.length:
            self.posy.pop(self.length)
        #for n in self.posx and self.posy:
        self.drawLength()

        print(self.posx)
        print(self.posy)
        
    def drawLength(self):
        
        pygame.draw.rect(gameScreen, WHITE_COLOR, [self.posx[0], self.posy[0], 30, 30])

        pygame.display.update()



       
        



        

        
        

    #def Move(self, xDirection, yDirection):





newGame = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
newGame.runGameLoop()
