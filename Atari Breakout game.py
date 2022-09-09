from turtle import width
import pygame, random, time

pygame.init()

#pygame.draw.rectangle

screenWidth = 1920
screenHeight = 1080
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Atari Breakout")

clock = pygame.time.Clock()
#FPS, for setting a constant screen refresh rate

black = (0, 0, 0)
white = (255, 255, 255)
darkGrey = (96,96,96)
lightGrey = (160,160,160)
darkRed = (200,0,0)
lightRed = (255,0,0)
darkGreen = (0,200,0)
lightGreen = (0,255,0)

#while True:
#    for event in pygame.event.get():
#        print(event)
#    pygame.draw.rect(screen,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),(0,0,1920,1080))
#    pygame.display.update()

class Paddle:
    def __init__(self, screen, colour, x, y, width, height):
        self.screen = screen
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def setXPos(self):
        position = pygame.mouse.get_pos()
        xPosition = position[0]
        if xPosition >= 100 and xPosition <= 1820:
            self.x = xPosition - self.width/2

    def getXPos(self):
        return self.x
    
    def getYPos(self):
        return self.y

    def drawPaddle(self):
        pygame.draw.rect(self.screen, self.colour, (self.x, self.y, self.width, self.height))


class Ball:
    def __init__(self, screen, colour, x, y, diameter):
        self.screen = screen
        self.colour = colour
        self.x = x
        self.y = y
        self.diameter = diameter
        self.width = diameter
        self.height = diameter
        self.xVelocity = random.randint(3, 10)
        self.yVelocity = random.randint(3, 5)
        self.flag = False

    def ballMovement(self, paddle):
        self.x += self.xVelocity
        self.y += self.yVelocity
        if self.x >= 1920-self.diameter or self.x <= 0:
            self.xVelocity *= -1
        if self.y >= 1080-self.diameter or self.y <= 0:
            self.yVelocity *= -1
        # if self.y+self.diameter >= paddle.getYPos():
        #     if self.x+self.diameter >= paddle.getXPos() and self.x+self.diameter <= paddle.getXPos():
        #         self.yVelocity *= -1
        #         self.xVelocity *= -1
        if detectCollision(self, paddle):
            if (self.y <= paddle.y) and (self.y + self.height >= paddle.y + paddle.height):
                self.xVelocity *= -1
                self.x += self.xVelocity * 5
                print("x")
            else:
                self.yVelocity *= -1
                self.y += self.yVelocity * 5
                print("y")


    def drawBall(self):
        pygame.draw.rect(self.screen, self.colour, (self.x, self.y, self.diameter, self.diameter), 0, 100)

def detectCollision(object1, object2):
    if (object1.y+object1.height >= object2.y and object1.y+object1.height <= object2.y+object2.height) or (object1.y >= object2.y and object1.y <= object2.y+object2.height) :
        if (object1.x+object1.width >= object2.x and object1.x+object1.width <= object2.x+object2.width) or (object1.x >= object2.x and object1.x <= object2.x+object2.width):
            return True
    return False

def gameLoop():
    paddle = Paddle(screen, darkRed, (screenWidth/2)-100, 900, 200, 100)
    ball = Ball(screen, darkGreen, (screenWidth/2)-15, 700, 30)
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEMOTION:
                paddle.setXPos()

        ball.ballMovement(paddle)

        screen.fill((darkGrey))
        paddle.drawPaddle()
        ball.drawBall()
        pygame.display.update()

gameLoop()
