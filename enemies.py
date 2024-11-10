# enemies.py

import pygame
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Anglerfish(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.original_image = image
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 100)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
        self.speed_x = random.randint(-3, -1)
        self.speed_y = random.choice([-0.5, 0.5])  # Slight bobbing effect

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y * random.choice([-1, 1])
        if self.rect.right < 0:
            # Respawn off the right side
            self.rect.x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 100)
            self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)

class GiantEel(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.original_image = image
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 200)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
        self.speed_x = random.randint(-2, -1)
        self.speed_y = 0  # Eel moves horizontally

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y * random.choice([-1, 1])
        if self.rect.right < 0:
            # Respawn off the right side
            self.rect.x = SCREEN_WIDTH
            self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)

class Jellyfish(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.original_image = image
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-150, -40)
        self.speed_x = random.choice([-0.5, 0.5])
        self.speed_y = random.randint(1, 2)

    def update(self):
        self.rect.x += self.speed_x * random.choice([-1, 1])
        self.rect.y += self.speed_y
        if self.rect.top > SCREEN_HEIGHT:
            # Respawn above the screen
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randint(-150, -40)
