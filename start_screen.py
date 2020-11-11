import pygame
import sys

mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()

# setting basics of the screen and some components
screenW = 700
screenH = 700
window = pygame.display.set_mode((screenW, screenH))
start_background = pygame.image.load('bg image 700x700.png')
option_screen = pygame.image.load('option screen.png')
black = (0, 0, 0)
white = (255, 255, 255)
tittle_color = (91, 109, 84)
pygame.display.set_caption('Agriadventure')
font = pygame.font.Font('8-BIT WONDER.TTF', 45)

tittlex = 90
tittley = 120
startx = 90
starty = 250
optionx = 90
optiony = 350
tittle2x = 200
tittle2y = 120
click = False


def option_text(x, y):
    option = font.render("Option", True, white)
    window.blit(option, (x, y))


def start_text(x, y):
    start = font.render("Start", True, white)
    window.blit(start, (x, y))


def tittle_text(x, y):
    tittle = font.render("Agriadventure", True, (91, 109, 84))
    window.blit(tittle, (x, y))


def option_titlle(x, y):
    tittle2 = font.render("Options", True, tittle_color)
    window.blit(tittle2, (x, y))


# Start Screen
def main_menu():
    global click
    while True:
        window.fill((0, 0, 0))
        mx, my = pygame.mouse.get_pos()

        start = pygame.Rect(90, 250, 200, 50)
        option = pygame.Rect(90, 350, 200, 50, )
        if start.collidepoint((mx, my)):
            if click:
                game()
        if option.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(window, (90, 90, 90), start)
        pygame.draw.rect(window, (255, 0, 0), option)

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
                    tittle_text(tittlex, tittley)
                    start_text(startx, starty)
                    option_text(optionx, optiony)
                    pygame.display.update()
                    mainClock.tick(60)


def game():
    running = True
    while running:
        window.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


def options():
    running = True
    while running:
        window.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        window.blit(option_screen, (0, 0))
        option_titlle(tittle2x, tittle2y)
        pygame.display.update()
        mainClock.tick(60)


main_menu()
