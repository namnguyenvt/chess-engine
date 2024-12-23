import pygame
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Hello Pygame')
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    text = font.render('Hello Pygame', True, (0, 255, 0))
    text_rect = text.get_rect(center=(400, 300))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))
        screen.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()