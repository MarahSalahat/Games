import pygame
import time
import random

# Window size
WIDTH = 800
HEIGHT = 600

# Colors
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
PURPLE =(147, 112, 219)

# Snake block size
BLOCK_SIZE = 20

# Game speed
FPS = 15

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.body = [(WIDTH/2, HEIGHT/2)]
        self.direction = 'RIGHT'

    def move(self):
        x, y = self.body[0]
        if self.direction == 'RIGHT':
            x += BLOCK_SIZE
        elif self.direction == 'LEFT':
            x -= BLOCK_SIZE
        elif self.direction == 'UP':
            y -= BLOCK_SIZE
        elif self.direction == 'DOWN':
            y += BLOCK_SIZE
        self.body.insert(0, (x, y))
        self.body.pop()

    def draw(self):
        for block in self.body:
            pygame.draw.circle(window, PURPLE, (block[0]+BLOCK_SIZE//2, block[1]+BLOCK_SIZE//2), BLOCK_SIZE//2)

    def begin(self):
        font = pygame.font.SysFont("comicsansms", 48)
        text = font.render('Eat more.Grow more ;)', True, YELLOW)
        text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
        window.blit(text, text_rect)
        pygame.display.update()
        time.sleep(2)
    

    def game_over(self):
        font = pygame.font.SysFont("comicsansms", 50)
        text = font.render('Game Over!', True, YELLOW)
        text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
        window.blit(text, text_rect)
        pygame.display.update()
        time.sleep(2)
     
class Food:
    def __init__(self):
        self.x = random.randrange(BLOCK_SIZE, WIDTH-BLOCK_SIZE, BLOCK_SIZE)
        self.y = random.randrange(BLOCK_SIZE, HEIGHT-BLOCK_SIZE, BLOCK_SIZE)

    def draw(self):
        pygame.draw.rect(window, YELLOW, (self.x, self.y, BLOCK_SIZE/2, BLOCK_SIZE/2))

def game_loop():
    snake = Snake()
    food = Food()
    snake.begin()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.direction = 'RIGHT'
                elif event.key == pygame.K_LEFT:
                    snake.direction = 'LEFT'
                elif event.key == pygame.K_UP:
                    snake.direction = 'UP'
                elif event.key == pygame.K_DOWN:
                    snake.direction = 'DOWN'

        snake.move()

        if snake.body[0][0] < 0 or snake.body[0][0] >= WIDTH or snake.body[0][1] < 0 or snake.body[0][1] >= HEIGHT:
            snake.game_over()
            pygame.quit()
            
            quit()

        if snake.body[0] == (food.x, food.y):
            food = Food()
            snake.body.append(snake.body[-1])

        window.fill(BLACK)
        snake.draw()
        food.draw()
        pygame.display.update()

        clock.tick(FPS)

game_loop()

