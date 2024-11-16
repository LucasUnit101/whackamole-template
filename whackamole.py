import pygame
import random


def main():
    try:
        pygame.init()
        # random.randrange(low, high)
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_row = 0
        mole_col = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        row = y // 32
                        col = x // 32
                        if row == mole_row and col == mole_col:
                            mole_row = random.randint(0, 15)
                            mole_col = random.randrange(0, 19)


            screen.fill("light green")
            for vertical in range(0, 20):
                x = vertical * 32
                pygame.draw.line(screen,"dark green", (x, 0), (x, 512))
            for horizontal in range(0, 16):
                y = horizontal * 32
                pygame.draw.line(screen,"dark green", (0, y), (640, y))
            screen.blit(mole_image, mole_image.get_rect(topleft = (mole_col * 32, mole_row * 32)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()

