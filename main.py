# This is the main file
import pygame
import os

#Screen Variables
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PISTIS")

SCREEN_COLOR = (255,255,255) #White
FPS = 60 #Frames Per Second

SHARK_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))

def draw_window():
    WIN.fill(SCREEN_COLOR)

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    draw_window()

    keys_pressed = pygame.key.get_pressed()
    (keys_pressed)

    pygame.quit()

if __name__ == "__main__":
    main()



