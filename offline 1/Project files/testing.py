def main():
    global screen, clock
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    bird = Bird(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    pipes = [Pipe(SCREEN_WIDTH)]
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flap()

        bird.update()
        pipes = [pipe for pipe in pipes if not pipe.is_off_screen()]
        pipes.append(Pipe(SCREEN_WIDTH))

        for pipe in pipes:
            pipe.update()

        screen.blit(bg_img, (0, 0))
        bird.draw(screen)
        for pipe in pipes:
            pipe.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()