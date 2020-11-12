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
credits_screen = pygame.image.load('option screen.png')
player_stand = pygame.image.load('stand.png')
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

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Just text def


def guide_tittle(x, y):
    guide = font.render("Guide", True, white)
    window.blit(guide, (x, y))


guideX = 450
guideY = 350


def option_text(x, y):
    option = font.render("Option", True, white)
    window.blit(option, (x, y))


optionx = 90
optiony = 350


def credit_text(x, y):
    t_credit = font.render("Credits", True, white)
    window.blit(t_credit, (x, y))


creditsX = 90
creditsY = 450


def credits(x, y):
    credits_names = font4.render('''Made by:Isaiah Gonzalez
Marcello Bobadilla '''
                                 , True, white)
    window.blit(credits_names, (x, y))


credits_nameX = 50
credits_nameY = 350


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


tittle2x = 150
tittle2y = 75


def text_speed(x, y):
    t_speed = font2.render("Text Speed", True, white)
    window.blit(t_speed, (x, y))


textspeedx = 200
textspeedy = 190


def controls_text(x, y):
    t_controls = font2.render("Control", True, white)
    window.blit(t_controls, (x, y))


controlx = 250
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


def wasd_text(x, y):
    t_wasd = font2.render("WASD", True, white)
    window.blit(t_wasd, (x, y))


wasdX = 100
wasdY = 520


def arrow_keys_text(x, y):
    t_arrow_k = font2.render("Arrow Keys", True, white)
    window.blit(t_arrow_k, (x, y))


arrowX = 350
arrowY = 520


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Start Screen

def main_menu():
    global click
    mixer.music.play()

    while True:
        window.fill((0, 0, 0))

        mx, my = pygame.mouse.get_pos()

        start = pygame.Rect(90, 250, 250, 50)
        option = pygame.Rect(90, 350, 250, 50)
        credits = pygame.Rect(90, 450, 280, 50)
        guide = pygame.Rect(450, 350, 200, 50)
        if start.collidepoint((mx, my)):
            if click:
                game()
        if option.collidepoint((mx, my)):
            if click:
                options()
        if credits.collidepoint((mx, my)):
            if click:
                credit()
        if guide.collidepoint((mx, my)):
            if click:
                guides()

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
                    window.blit(player_stand, (0, 0))
                    tittle_text(tittlex, tittley)
                    start_text(startx, starty)
                    option_text(optionx, optiony)
                    credit_text(creditsX, creditsY)
                    guide_tittle(guideX, guideY)
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
        wasd_text(wasdX, wasdY)
        arrow_keys_text(arrowX, arrowY)
        pygame.display.update()
        mainClock.tick(60)


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
        credits(credits_nameX, credits_nameY)
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

        window.blit(credits_screen, (0, 0))
        pygame.display.update()
        mainClock.tick(60)


main_menu()
