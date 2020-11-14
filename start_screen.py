import pygame
import sys
from pygame import mixer
from pygame.locals import *

pygame.mixer.init()
mainClock = pygame.time.Clock()

pygame.init()

# setting basics of the screen and some components
screenW = 700
screenH = 700
window = pygame.display.set_mode((screenW, screenH))
start_background = pygame.image.load('images/bg image 700x700.png')
option_screen = pygame.image.load('images/option screen.png')
credits_screen = pygame.image.load('images/credistScreen.png')
play_info = pygame.image.load('images/guideScreen.png')
player_stand = pygame.image.load('stand2.png')
black = (0, 0, 0)
white = (255, 255, 255)
tittle_color = (91, 109, 84)
pygame.display.set_caption('Agriadventure')
font = pygame.font.Font('8-BIT WONDER.TTF', 45)
font2 = pygame.font.Font('8-BIT WONDER.TTF', 30)
font3 = pygame.font.Font('8-BIT WONDER.TTF', 60)
font4 = pygame.font.Font('8-BIT WONDER.TTF', 15)
mixer.music.load('background music.mp3')
click = False
logo = pygame.image.load('images/Logo.png')
pygame.display.set_icon(logo)
WalkRight = [pygame.image.load('playerIMG/R1.png'), pygame.image.load('playerIMG/R2.png')]
WalkLeft = [pygame.image.load('playerIMG/L1.png'), pygame.image.load('playerIMG/L2.png')]
WalkDown = [pygame.image.load('playerIMG/D1.png'), pygame.image.load('playerIMG/D2.png')]
WalkUp = [pygame.image.load('playerIMG/UP1.png'), pygame.image.load('playerIMG/UP2.png')]
Stand = pygame.image.load('playerIMG/stand.png')
start_screen = pygame.image.load('images/mainGameScreen.png')
walkCount = 0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Just text def


def guide_tittle(x, y):
    guide = font.render("Guide", True, white)
    window.blit(guide, (x, y))


guideX = 90
guideY = 350


def credit_text(x, y):
    t_credit = font.render("Credits", True, white)
    window.blit(t_credit, (x, y))


creditsX = 90
creditsY = 450


def start_text(x, y):
    start = font.render("Start", True, white)
    window.blit(start, (x, y))


startx = 90
starty = 250


def tittle_text(x, y):
    tittle = font.render("Agriadventure", True, (91, 109, 84))
    window.blit(tittle, (x, y))


tittlex = 90
tittley = 120

# Start Screen


def main_menu():
    global click
    mixer.music.play()

    while True:
        window.fill((0, 0, 0))

        mx, my = pygame.mouse.get_pos()

        start = pygame.Rect(90, 250, 250, 50)
        credits = pygame.Rect(90, 450, 280, 50)
        guide = pygame.Rect(90, 350, 200, 50)
        if start.collidepoint((mx, my)):
            if click:
                game()
        if credits.collidepoint((mx, my)):
            if click:
                credit()
        if guide.collidepoint((mx, my)):
            if click:
                guides()

        pygame.draw.rect(window, (90, 90, 90), start)

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

                    window.blit(start_background, (0, 0))
                    window.blit(player_stand, (0, 0))
                    tittle_text(tittlex, tittley)
                    start_text(startx, starty)
                    credit_text(creditsX, creditsY)
                    guide_tittle(guideX, guideY)
                    pygame.display.update()
                    mainClock.tick(60)


def game():
    mainClock.tick(6)
    global walkCount
    left = False
    right = False
    up = False
    down = False
    x = 191
    y = 638
    width = 32
    height = 32
    vel = 3

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        # Movement
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x > vel:
            x -= vel
            left = True
            right = False
        elif keys[pygame.K_RIGHT] and x < 700 - width - vel:
            x += vel
            left = False
            right = True
        else:
            right = False
            left = False
            walkCount = 0
        if keys[pygame.K_UP] and y > vel:
            y -= vel
            up = True
            down = False
        elif keys[pygame.K_DOWN] and y < 700 - height - vel:
            y += vel
            up = False
            down = True
        else:
            up = False
            down = False
            walkCount = 0

        window.blit(start_screen, (0, 0))
        if walkCount + 1 >= 4:
            walkCount = 0
        if left:
            window.blit(WalkLeft[walkCount//3], (x, y))
            walkCount += 1
        elif right:
            window.blit(WalkRight[walkCount//3], (x, y))
            walkCount += 1
        if up:
            window.blit(WalkUp[walkCount//3], (x, y))
            walkCount += 1
        elif down:
            window.blit(WalkDown[walkCount//3], (x, y))
            walkCount += 1
        else:
            window.blit(Stand, (x, y))
        # print(Stand, (x, y))
        pygame.display.update()


def credit():
    running = True
    while running:
        window.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        window.blit(credits_screen, (0, 0))
        pygame.display.update()
        mainClock.tick(60)


def guides():
    running = True
    while running:
        window.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        window.blit(play_info, (0, 0))
        pygame.display.update()
        mainClock.tick(60)


main_menu()
