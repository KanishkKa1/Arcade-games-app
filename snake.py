# Snake game

import pygame
from pygame.locals import *
from pygame import mixer
import time
import random

# Size of block of snake and to update length
SIZE = 40


# Define apple
class Apple:
    # Default call
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("apple.jpg").convert()
        self.apple_x = 200
        self.apple_y = 160

    # Draw apple
    def apple_draw(self):
        self.parent_screen.blit(self.image, (self.apple_x, self.apple_y))
        # Update the full display screen to the screen
        pygame.display.flip()

    # Call for movement
    def move(self):
        self.apple_x = random.randint(1, 19) * SIZE
        self.apple_y = random.randint(1, 14) * SIZE


# Define snake
class Snake:
    # Default  call
    def __init__(self, parent_screen):
        # screen initialization
        self.parent_screen = parent_screen

        # snake Loader
        self.image = pygame.image.load("block.jpg").convert()
        self.direction = 'rest'

        self.length = 1
        self.x = [SIZE]
        self.y = [SIZE]

    # Direction update
    def move_left(self):
        self.direction = 'left'

    # Direction update
    def move_right(self):
        self.direction = 'right'

    # Direction update
    def move_up(self):
        self.direction = 'up'

    # Direction update
    def move_down(self):
        self.direction = 'down'

    # Movement update
    def walk(self):
        # update body
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # update direction of head
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        # Call for snake
        self.draw_snake()

    # Defining the drawing for snake
    def draw_snake(self):
        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))

        # Update the full display screen to the screen
        pygame.display.flip()

    # Increase length of snake
    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)


# Define the working of the game
class Game:
    # Here we have to initialize data
    def __init__(self):
        # Initialize the pygame
        pygame.init()

        # Title and icon display
        pygame.display.set_caption("Snake game")
        self.icon = pygame.image.load('snake.png')
        pygame.display.set_icon(self.icon)

        # Screen creation
        self.screen = pygame.display.set_mode((800, 600))

        # Call for sound
        mixer.init()
        # mixer.music.load("bg_music.wav")
        # mixer.music.play(-1)

        # snake calling
        self.snake = Snake(self.screen)
        self.snake.draw_snake()

        # Apple calling
        self.apple = Apple(self.screen)
        self.apple.apple_draw()

    # Background loader
    def render_background(self):
        bg = pygame.image.load("background.png")
        self.screen.blit(bg, (0, 0))

    # Define reset
    def reset(self):
        self.snake = Snake(self.screen)
        self.apple = Apple(self.screen)

    # Define the collision
    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    # Calling for screen update
    def play(self):
        # Background update
        self.render_background()

        # Call for movement update of snake
        self.snake.walk()

        # Call for update of apple
        self.apple.apple_draw()

        # Update score
        self.display_score()

        # Update the full display screen to the screen
        pygame.display.flip()

        # snake eating apple scenario
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.apple_x, self.apple.apple_y):
            sound_score = mixer.Sound("ding.wav")
            mixer.Sound.play(sound_score)
            self.snake.increase_length()
            self.apple.move()

        # Check for collision of snake with itself
        for i in range(2, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                sound_die = mixer.Sound("crash.wav")
                mixer.Sound.play(sound_die)
                raise "Collision Occurred"

        # snake colliding with the boundaries of the window
        if not (0 <= self.snake.x[0] <= 1000 and 0 <= self.snake.y[0] <= 800):
            sound_die = mixer.Sound("crash.wav")
            mixer.Sound.play(sound_die)
            raise "Hit the boundary error"

    # Define the score
    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(
            f"Score: {self.snake.length}", True, (200, 200, 200))
        self.screen.blit(score, (650, 15))

    # Define the game over dialogue box
    def game_over(self):
        # Background update
        self.render_background()

        # Display font
        font = pygame.font.SysFont('arial', 30)

        # Game over
        line1 = font.render(
            f"Game is over! Your score is {self.snake.length}", True, (255, 255, 255))
        self.screen.blit(line1, (150, 150))

        # Replay
        line2 = font.render(
            "To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.screen.blit(line2, (150, 200))

        # Stop music
        mixer.music.pause()

        # Update the full display screen to the screen
        pygame.display.flip()

    # code will run here
    def run(self):
        # Application of the loop
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                # Exit Code
                if event.type == QUIT:
                    running = False
                    pygame.mixer.pause()

                if event.type == KEYDOWN:
                    # ESCAPE ARROW KEY is pressed
                    if event.key == K_ESCAPE:
                        running = False

                    # ENTER KEY is pressed
                    if event.key == K_RETURN:
                        # Start music
                        mixer.music.unpause()
                        pause = False

                    # when game is in action
                    if not pause:
                        # LEFT ARROW KEY is pressed
                        if event.key == K_LEFT:
                            self.snake.move_left()

                        # RIGHT ARROW KEY is pressed
                        if event.key == K_RIGHT:
                            self.snake.move_right()

                        # UP ARROW KEY is pressed
                        if event.key == K_UP:
                            self.snake.move_up()

                        # DOWN ARROW KEY is pressed
                        if event.key == K_DOWN:
                            self.snake.move_down()

            # if self.boundary:
            #    running = False

            try:
                if not pause:
                    self.play()

            except Exception as e:
                self.game_over()
                pause = True
                self.reset()

            # Time for refreshing
            time.sleep(.25)


# Main code
if __name__ == '__main__':
    game = Game()
    game.run()
