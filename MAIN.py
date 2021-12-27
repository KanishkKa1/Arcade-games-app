import pygame
import random
import pygame_menu
import os
from pygame import mixer
from pygame_menu.examples import create_example_window
from typing import Tuple, Any
# --- constants ---
pygame.init()

#white = (255, 255, 255)
mixer.music.load("background.wav")
mixer.music.play(-1)

# assigning values to X and Y variable
WIDTH = 900
HEIGHT = 600
# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 5
# --- class ---


class Button(object):

    def __init__(self, position, size, color, text):

        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = pygame.Rect((0, 0), size)

        font = pygame.font.SysFont(None, 32)
        text = font.render(text, True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = self.rect.center

        self.image.blit(text, text_rect)

        # set after centering text
        self.rect.topleft = position

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return self.rect.collidepoint(event.pos)


def stage1(screen):

    button1 = Button((315, 115), (300, 75), (0, 255, 0), "SNAKE GAME")
    button2 = Button((315, 215), (300, 75), (0, 255, 0), "FLAPPY BIRD")
    # (position, size, color, text) -> None
    button3 = Button((315, 315), (300, 75), (0, 255, 0), "SPACE INVADERS")
    button4 = Button((315, 415), (300, 75), (255, 0, 0), "EXIT")

    # - mainloop -

    clock = pygame.time.Clock()
    running = True
    font = pygame.font.SysFont("comicsansms", 45)

    text = font.render("Arcade Roosters", True, (0, 100, 0))

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if button1.is_clicked(event):
                # go to stage2
                stage2(screen)
            # if button2.is_clicked(event)
            if button2.is_clicked(event):
                stage3(screen)
            if button3.is_clicked(event):
                stage4(screen)
            if button4.is_clicked(event):
                # exit
                pygame.quit()
                exit()

        # - draws -
        screen.fill((255, 255, 0))
        screen.blit(text,
                    (450 - text.get_width() // 2, 75 - text.get_height() // 2))
        button1.draw(screen)
        button2.draw(screen)
        button3.draw(screen)
        button4.draw(screen)
        pygame.display.flip()

        # - FPS -
        clock.tick(FPS)


def stage2(screen):

    button1 = Button((315, 215), (200, 75), (0, 255, 0), "PLAY")
    button2 = Button((315, 315), (200, 75), (255, 0, 0), "BACK")

    # - mainloop -

    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if button1.is_clicked(event):
                os.system('snake.py')

            if button2.is_clicked(event):
                return

        # - draws -

        screen.fill((0, 255, 255))
        button1.draw(screen)
        button2.draw(screen)
        pygame.display.flip()

        # - FPS -
        clock.tick(FPS)


def stage3(screen):
    button1 = Button((315, 215), (200, 75), (0, 255, 0), "PLAY")
    button2 = Button((315, 315), (200, 75), (255, 0, 0), "BACK")

    # - mainloop -

    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if button1.is_clicked(event):
                os.system('flappy.py')
            if button2.is_clicked(event):
                return

        # - draws -

        screen.fill((0, 255, 0))
        # button1.draw(screen)
        button1.draw(screen)
        button2.draw(screen)
        pygame.display.flip()

        # - FPS -

        clock.tick(FPS)


def stage4(screen):
    button1 = Button((315, 215), (200, 75), (255, 0, 0), "PLAY")
    button2 = Button((315, 315), (200, 75), (255, 0, 0), "BACK")

    # - mainloop -

    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if button1.is_clicked(event):
                os.system('space.py')
            if button2.is_clicked(event):
                return

        # - draws -

        screen.fill((0, 255, 0))
        # button1.draw(screen)
        button1.draw(screen)
        button2.draw(screen)
        pygame.display.flip()

        # - FPS -

        clock.tick(FPS)


'''
def stage3(screen):

    button2 = Button((215, 5), (100, 100), (0, 0, 255), "BACK")

    # - mainloop -

    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if button2.is_clicked(event):
                return

        # - draws -

        screen.fill((128, 128, 128))
        button2.draw(screen)
        pygame.display.flip()

        # - FPS -

        clock.tick(FPS)
'''
# --- main ---

# - init -


pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arcade Roosters")

# - start -

stage1(screen)

# - end -

pygame.quit()
