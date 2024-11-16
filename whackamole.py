import pygame
import random


def main():
    try:
        pygame.init()

        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        mole_x, mole_y = 0, 0
        new_pos = mole_image.get_rect(topleft=(mole_x, mole_y))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    row = y // 32
                    col = x // 32
                    new_x = random.randrange(0, 640, 32)
                    new_y = random.randrange(0, 512, 32)
                    new_pos = (new_x, new_y)
            screen.fill("light green")
            grid_cols = 20
            grid_rows = 16
            square_size = 32
            height = 512
            width = 640
            for i in range(1, grid_cols):
                pygame.draw.line(screen, 'black', (i*square_size, 0), (i*square_size, height))
            for i in range(1, grid_rows):
                pygame.draw.line(screen, 'black', (0, i*square_size), (width, i*square_size))
            screen.blit(mole_image, new_pos)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()



if __name__ == "__main__":
    main()
