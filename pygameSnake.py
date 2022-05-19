import pygame
import time
import random

pygame.init()

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)

dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake by Samo')

gameOver = False

x1 = dis_width/2
y1 = dis_height/2
snakeSq = 10
x1c = 0
y1c = 0

clock = pygame.time.Clock()
snakeSpeed = 10

font = pygame.font.SysFont("comicsansms", 50)
skoreFont = pygame.font.SysFont("comicsansms", 35)


def skore(skore):
    value = skoreFont.render("Tvoje skóre: " + str(skore), True, red)
    dis.blit(value, [0, 0])


def mSnake(snakeSq, snakeL):
    for x in snakeL:
        pygame.draw.rect(dis, black, [x[0], x[1], snakeSq, snakeSq])


def message(msg, color):
    messg = font.render(msg, True, color)
    dis.blit(messg, [dis_width/3, dis_height/3])


def gameLoop():
    gameOver = False
    gameClose = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1c = 0
    y1c = 0

    snakeL = []
    snakeD = 1

    fx = round(random.randrange(0, dis_width - snakeSq) / 10.0) * 10.0
    fy = round(random.randrange(0, dis_height - snakeSq) / 10.0) * 10.0

    while not gameOver:
        while gameClose == True:
            dis.fill(white)
            message("Prehral si!", red)
            skore(snakeD - 1)
            pygame.display.set_caption('Q = Pre vypnutie | C = Znovu')
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1c = -snakeSq
                    y1c = 0
                elif event.key == pygame.K_RIGHT:
                    x1c = snakeSq
                    y1c = 0
                elif event.key == pygame.K_UP:
                    y1c = -snakeSq
                    x1c = 0
                elif event.key == pygame.K_DOWN:
                    y1c = snakeSq
                    x1c = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            gameClose = True

        x1 += x1c
        y1 += y1c
        dis.fill(white)


        pygame.draw.rect(dis, green, [fx, fy, snakeSq, snakeSq])
        snakeH = []
        snakeH.append(x1)
        snakeH.append(y1)
        snakeL.append(snakeH)
        print("fx:", fx, "| fy:", fy, "| x1:", x1, "| y1:", y1)

        if len(snakeL) > snakeD:
            del snakeL[0]

        for x in snakeL[:-1]:
            if x == snakeH:
                gameClose = True


        mSnake(snakeSq, snakeL)
        skore(snakeD - 1)
        pygame.display.update()

        if x1 == fx and y1 == fy:
            fx = round(random.randrange(0, dis_width - snakeSq) / 10.0) * 10.0
            fy = round(random.randrange(0, dis_height - snakeSq) / 10.0) * 10.0
            snakeD += 1

        clock.tick(snakeSpeed)

    pygame.quit()
    quit()


gameLoop()
