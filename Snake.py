import pygame
import os

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

    TICK_SPEED = 4

    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        self.gameScreen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.gameScreen.fill(BLACK_COLOR)
        pygame.display.set_caption(SCREEN_TITLE)

    def runGameLoop(self):
        isGameRunning = True

        direction = 0
        gameScreen.fill(BLACK_COLOR)



        player = SNAKE(WHITE_COLOR, 570, 360, 3, 30, 30)

        while isGameRunning:
            gameScreen.fill(BLACK_COLOR)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    isGameRunning = False
                elif event.type == pygame.KEYDOWN:
                    if direction != 2 and event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        direction = 1                      
                    elif direction != 1 and event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        direction = 2
                    elif direction != 4 and event.key == pygame.K_UP or event.key == pygame.K_w:
                        direction = 3                        
                    elif direction != 3 and event.key == pygame.K_DOWN or event.key == pygame.K_s: 
                        direction = 4                          
                print(event)


            player.move(direction)
            player.drawLength()

            clock.tick(self.TICK_SPEED)

class GameObject:

    def __init__(self, color, x, y, width, height):
        self.color = color
        self.xPos = x
        self.yPos = y
        self.width = width
        self.height = height
        

class SNAKE(GameObject):


    def __init__(self, color, x, y, length, width, height):
        super().__init__(color, x, y, width, height)

        self.length = length

    def move(self, direction):

        self.direction = direction

        if direction == 1:
            self.xPos += 30
        if direction == 2:
            self.xPos -= 30
        if direction == 3:
            self.yPos -= 30
        if direction == 4:
            self.yPos += 30

    def drawLength(self):

        pygame.draw.rect(gameScreen, WHITE_COLOR, [self.xPos, self.yPos, 30, 30])
        
        pygame.display.update()

        

    #def Move(self, xDirection, yDirection):





newGame = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
newGame.runGameLoop()