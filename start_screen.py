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
start_background = pygame.image.load('bg image 700x700.png')
option_screen = pygame.image.load('option screen.png')
black = (0, 0, 0)
white = (255, 255, 255)
tittle_color = (91, 109, 84)
pygame.display.set_caption('Agriadventure')
font = pygame.font.Font('8-BIT WONDER.TTF', 45)
font2 = pygame.font.Font('8-BIT WONDER.TTF', 30)
font3 = pygame.font.Font('8-BIT WONDER.TTF', 60)
mixer.music.load('background music.mp3')
click = False


def option_text(x, y):
    option = font.render("Option", True, white)
    window.blit(option, (x, y))


optionx = 90
optiony = 350


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


def option_titlle(x, y):
    tittle2 = font3.render("Options", True, tittle_color)
    window.blit(tittle2, (x, y))


tittle2x = 175
tittle2y = 75


def text_speed(x, y):
    t_speed = font2.render("Text Speed", True, white)
    window.blit(t_speed, (x, y))


textspeedx = 225
textspeedy = 190


def controls_text(x, y):
    t_controls = font2.render("Control", True, white)
    window.blit(t_controls, (x, y))


controlx = 265
controly = 400


def slow(x, y):
    t_slow = font2.render("Slow", True, white)
    window.blit(t_slow, (x, y))


slowx = 75
slowy = 300


def medium(x, y):
    t_medium = font2.render("Medium", True, white)
    window.blit(t_medium, (x, y))


mediumx = 275
mediumy = 300


def fast(x, y):
    t_fast = font2.render("Fast", True, white)
    window.blit(t_fast, (x, y))


fastx = 525
fasty = 300


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Start Screen

def main_menu():
    global click
    mixer.music.play()

    while True:
        window.fill((0, 0, 0))

        mx, my = pygame.mouse.get_pos()

        start = pygame.Rect(90, 250, 250, 50)
        option = pygame.Rect(90, 350, 250, 50, )
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
        text_speed(textspeedx, textspeedy)
        controls_text(controlx, controly)
        slow(slowx, slowy)
        medium(mediumx, mediumy)
        fast(fastx, fasty)
        pygame.display.update()
        mainClock.tick(60)


main_menu()
