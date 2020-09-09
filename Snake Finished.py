import pygame
import os
import random

# Screen Setup
SCREEN_TITLE = "Snake - By: Matthew Volpe"
SCREEN_WIDTH = 1201
SCREEN_HEIGHT = 781

# Colors
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
RED_COLOR = (255, 40, 0)
YELLOW_COLOR = (254, 220, 86)
GREY_COLOR = (51, 51, 51)
JADE_COLOR = (0, 204, 255)

# Sets up display
gameScreen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
gameScreen.fill(WHITE_COLOR)

# Access the folder that this file is in, for finding pictures or images if needed
current_path = os.path.dirname(__file__)

# Sets up ingame tick speed
clock = pygame.time.Clock()

# Text display font and size
pygame.font.init()
font = pygame.font.SysFont("Comic sans", 50)
bigfont = pygame.font.SysFont("Comic sans", 75)


# Game class setup
class Game:

    TICK_SPEED = 60
    startingLength = 4
    isGameRunning = True
    highScoreMem = 0


    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        self.gameScreen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.gameScreen.fill(BLACK_COLOR)
        pygame.display.set_caption(SCREEN_TITLE)


    # Grid background
    def grid(self):
        for n in range(41):
            xPos = n * 30
            pygame.draw.line(self.gameScreen, GREY_COLOR, (xPos, 0), (xPos, 781), 1)

        for n in range(27):
            yPos = n * 30
            pygame.draw.line(self.gameScreen, GREY_COLOR, (0, yPos), (1201, yPos), 1)


    # Game loop
    def runGameLoop(self):
        endGame = True
        self.isGameRunning = True
        # Instance of SNAKE
        player = SNAKE(WHITE_COLOR, 570, 360, 0, self.startingLength, 30, 30)
        player.posx = [570]
        player.posy = [360]

        # Instance of FOOD
        food = Food(RED_COLOR, 300, 300, 31, 31)
        food.randFood()
        food.drawFood()

        while self.isGameRunning:
            
            newGame.grid()

            player.move()
            
            food.drawFood()
            
            player.pos()
            
            # Collision for the food object
            if food.xPos == player.xPos and food.yPos == player.yPos:
                food.randFood()
                player.length += 1

            # Checks if food will appear behind snake and relocates if necessary
            for n in range(player.length):
                if n < len(player.posx) or n < len(player.posy):
                    if food.xPos == player.posx[n] and food.yPos == player.posy[n]:
                        food.randFood()
                    else:
                        continue
                else:
                    continue

            clock.tick(self.TICK_SPEED)
            if self.isGameRunning == False:
                break
            pygame.time.delay(85)
            gameScreen.fill(BLACK_COLOR)

        # Game over logic and restart
        text = bigfont.render("You Lose. Press Space to try again!", True, YELLOW_COLOR)
        newGame.gameScreen.blit(text, (150, 330))
        pygame.display.update()
        while endGame:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        endGame = False
                elif event.type == pygame.QUIT:
                    pygame.quit()

        newGame.runGameLoop()

            
class GameObject:

    def __init__(self, color, x, y, width, height):
        self.color = color
        self.xPos = x
        self.yPos = y
        self.width = width
        self.height = height
    

class Food(GameObject):

    def __init__(self, color, x, y, width, height):
        super().__init__(color, x, y, width, height)


    # Uses random function to determine a new x and y position for the food object
    def randFood(self):

        self.xPos = random.randrange(0, 39, 1) * 30
        self.yPos = random.randrange(0, 25, 1) * 30


    # Draws the food object to the screen
    def drawFood(self):

        pygame.draw.rect(gameScreen, RED_COLOR, [self.xPos + 1, self.yPos + 1, 29, 29])


class SNAKE(GameObject):

    posx = [570]
    posy = [360]


    def __init__(self, color, x, y, direction, length, width, height):
        super().__init__(color, x, y, width, height)

        self.length = length
        self.direction = direction


    # Sets direction based on input and moves the snake around the screen
    def move(self):

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

        # Moves the snake in the specified direction
        if self.direction == 1:
            self.xPos += 30
        if self.direction == 2:
            self.xPos -= 30
        if self.direction == 3:
            self.yPos -= 30
        if self.direction == 4:
            self.yPos += 30

        # Allows the snake to wrap around the screen
        if self.xPos < 0:
            self.xPos = 1200
        elif self.xPos == 1200:
            self.xPos = 0
        if self.yPos < 0:
            self.yPos = 780
        elif self.yPos== 780:
            self.yPos = 0

    # Keeps track of the position of each snake segment as an array
    # and draws a segment to the screen for each member in the array.
    # Sets the length of the array based on length of snake body
    def pos(self):

        self.posx.insert(0, self.xPos)
        self.posy.insert(0, self.yPos)

        if len(self.posx) > self.length:
            self.posx.pop(self.length)
        if len(self.posy) > self.length:
            self.posy.pop(self.length)

        
        for n in range(self.length):

            if n < len(self.posx) or n < len(self.posy):
                self.drawLength(n)
                self.detectCollision(n)
            elif n > len(self.posx) or n > len(self.posy):
                break

        self.score()
        self.highScoreTrack() 
        pygame.display.update()
    

    # Function to draw snake to screen
    def drawLength(self, n):
        
        pygame.draw.rect(gameScreen, JADE_COLOR, [self.posx[n], self.posy[n], 30, 30])


    # Function to detect collision by running through the posx and posy arrays and checking for any similar values
    def detectCollision(self, n):
        if self.posx[0] != self.posx[1] or self.posy[0] != self.posy[1]:
            if n > 0:
                if self.xPos == self.posx[n] and self.yPos == self.posy[n]:
                    newGame.isGameRunning = False


    # Funtion to display current score
    def score(self):

        self.scoreTrack = self.length - newGame.startingLength
        self.scoreTrack = str(self.scoreTrack)
        score = "Score: " + self.scoreTrack
        text = font.render(score, True, YELLOW_COLOR)
        newGame.gameScreen.blit(text, (20, 15))


    # Keeps track of highest score reached
    def highScoreTrack(self):
        scr = int(self.scoreTrack)
        
        if scr > newGame.highScoreMem:
            newGame.highScoreMem = scr
        highScr = str(newGame.highScoreMem)
        highScore = "High Score: " + highScr
        text = font.render(highScore, True, YELLOW_COLOR)
        newGame.gameScreen.blit(text, (925, 15))


# Instance of Game object
newGame = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
newGame.runGameLoop()