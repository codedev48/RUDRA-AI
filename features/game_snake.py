import pygame
import random


def play_snake():

    pygame.init()

    width, height = 600, 400
    block = 10

    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("RUDRA Snake Game")

    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 25)

    def draw_text(text, x, y):
        label = font.render(text, True, (255, 255, 255))
        win.blit(label, (x, y))

    def spawn_food(snake):
        while True:
            food = (
                random.randrange(0, width, block),
                random.randrange(0, height, block)
            )
            if food not in snake:
                return food

    def game_loop():

        snake = [(100, 50)]
        snake_dir = (block, 0)
        score = 0
        level = 1
        speed = 8   # 🔥 Slow start

        food = spawn_food(snake)

        run = True

        while run:
            clock.tick(speed)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    return None  # 🔥 only exit snake

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and snake_dir != (block, 0):
                snake_dir = (-block, 0)
            elif keys[pygame.K_RIGHT] and snake_dir != (-block, 0):
                snake_dir = (block, 0)
            elif keys[pygame.K_UP] and snake_dir != (0, block):
                snake_dir = (0, -block)
            elif keys[pygame.K_DOWN] and snake_dir != (0, -block):
                snake_dir = (0, block)

            head = (
                snake[0][0] + snake_dir[0],
                snake[0][1] + snake_dir[1]
            )

            # Wall collision
            if (
                head[0] < 0 or head[0] >= width or
                head[1] < 0 or head[1] >= height
            ):
                return score

            # Self collision
            if head in snake:
                return score

            snake.insert(0, head)

            if head == food:
                score += 1
                food = spawn_food(snake)

                # 🔥 Increase level every 5 points
                if score % 5 == 0:
                    level += 1
                    speed += 2   # gradual speed increase

            else:
                snake.pop()

            win.fill((0, 0, 0))

            pygame.draw.rect(win, (255, 0, 0), (*food, block, block))

            for segment in snake:
                pygame.draw.rect(win, (0, 255, 0), (*segment, block, block))

            draw_text(f"Score: {score}", 10, 10)
            draw_text(f"Level: {level}", 10, 35)

            pygame.display.update()

    # -------- GAME OVER LOOP -------- #

    while True:
        final_score = game_loop()

        if final_score is None:
            return  # 🔥 Exit cleanly to Rudra

        win.fill((0, 0, 0))
        draw_text("GAME OVER", width // 2 - 80, height // 2 - 30)
        draw_text(f"Final Score: {final_score}", width // 2 - 90, height // 2)
        draw_text("Press R to Restart or Q to Quit", width // 2 - 160, height // 2 + 40)

        pygame.display.update()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    return

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        waiting = False
                    elif event.key == pygame.K_q:
                        pygame.display.quit()
                        return