import pygame

# Start Screen


class Game:
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.SCREEN_W, self.SCREEN_H = 800, 800
        self.screen = pygame.Surface((self.SCREEN_W, self.SCREEN_H))
        self.window = pygame.display.set_mode((self.SCREEN_W, self.SCREEN_H))
        self.back_ground = pygame.image.load('bg image.jpg')
        self.font_name = '8-BIT WONDER.TTF'
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)

    def game_loop(self):
        pygame.display.set_caption('Agriadventure')
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            self.screen.fill(self.BLACK)
            self.draw_text('Thanks for Playing', 20, self.SCREEN_W/2, self.SCREEN_H/2)
            self.window.blit(self.back_ground, (0, 0))
            self.window.blit(self.screen, (0, 0))
            pygame.display.update()
            pygame.display.flip()
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True

    # Reset the keys

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)
