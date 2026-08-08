import pygame
import time
import sys

pygame.init()

# Create game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Spritesheet Animation")

clock = pygame.time.Clock()

i = 0
while i < 100:
    i += 1
    time.sleep(0.1)
    clock.tick(60)


pygame.quit()
sys.exit()
