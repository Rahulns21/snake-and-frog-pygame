import pygame, sys, random
from pygame.math import Vector2 as Vector

class Snake:
    def __init__(self) -> None:
        self.body = [Vector(5, 10), Vector(4, 10), Vector(3, 10)]
        self.direction = Vector(1, 0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, snake_color, block_rect)

    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

class Fruit:
    def __init__(self) -> None:
        self.randomise()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(frog_img, fruit_rect)
        # pygame.draw.rect(screen, fruit_color, fruit_rect)

    def randomise(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector(self.x, self.y)

class Main:
    def __init__(self) -> None:
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomise()
            self.snake.add_block()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number:
            self.game_over()

        if not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()

pygame.init()
app_name = 'Snake and Frog' # modify pygame window title 
pygame.display.set_caption(app_name) 
cell_size = 30
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
fps = 60
green_bg = (101, 254, 8)
fruit_color = (159, 43, 104)
snake_color = (255, 8, 0)
frog = pygame.image.load('graphics/bluefrog.png').convert_alpha()
frog_img = pygame.transform.scale(frog, (30, 30))

main_game = Main()

SCREEN_UPDATE = pygame.USEREVENT
SNAKE_SPEED = 100 # increase or decrease snake speed
pygame.time.set_timer(SCREEN_UPDATE, SNAKE_SPEED)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector(0, 1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector(1, 0)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector(-1, 0)

    screen.fill(green_bg)
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(fps)