import pygame
import random
import time


class Winners:
    def __init__(self, snake):
        player1screen = pygame.image.load(f'Player_{snake}_Wins copy.jpg').convert()
        screen.blit(player1screen, (0, 0))
        pygame.display.update()
        time.sleep(5)
        pygame.quit()


class Colors:
    # Constant RGB Values in tuple form
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)


class Snake1:
    def __init__(self, screen_parameter):
        self.screen = screen_parameter

    def draw(self):
        if (Snake1.snake_x, Snake1.snake_y) == (Food.food_x, Food.food_y):
            Food.food_x = random.randint(0, 49) * 10
            Food.food_y = random.randint(0, 49) * 10
            Snake1.snake_blocks.append([Snake1.snake_x, Snake1.snake_y])
        # For each snake block's coordinate:
        for i in range(len(Snake1.snake_blocks)):
            # Draw the block
            pygame.draw.rect(self.screen, Colors.BLUE,
                             (Snake1.snake_blocks[i][0], Snake1.snake_blocks[i][1], 10, 10))
        pygame.draw.rect(self.screen, Colors.RED, (Food.food_x, Food.food_y, 10, 10))

    # Original and variable starting x and y place of the snake head
    snake_x = 240
    snake_y = 240

    # List of snake blocks
    snake_blocks = [[snake_x, snake_y]]

    # Original snake direction
    snake_direction = "R"


class Snake2:
    def __init__(self, screen_parameter):
        self.screen = screen_parameter

    def draw(self):
        if (Snake2.snake_x, Snake2.snake_y) == (Food.food_x, Food.food_y):
            Food.food_x = random.randint(0, 49) * 10
            Food.food_y = random.randint(0, 49) * 10
            Snake2.snake_blocks.append([Snake2.snake_x, Snake2.snake_y])
        # For each snake block's coordinate:
        for i in range(len(Snake2.snake_blocks)):
            # Draw the block
            pygame.draw.rect(self.screen, Colors.GREEN,
                             (Snake2.snake_blocks[i][0], Snake2.snake_blocks[i][1], 10, 10))
        pygame.draw.rect(self.screen, Colors.RED, (Food.food_x, Food.food_y, 10, 10))

    # Original and variable starting x and y place of the snake head
    snake_x = 100
    snake_y = 100

    # List of snake blocks
    snake_blocks = [[snake_x, snake_y]]

    # Original snake direction
    snake_direction = "L"


class Food:
    """
    The original starting place of the food
    The placement of the food must be a multiple of 10, so that the snake with width and height 10 can eat it properly
    """
    food_x = random.randint(0, 49)*10
    food_y = random.randint(0, 49)*10


def snake_move1():
    # If the user attempts to move upward
    if Snake1.snake_direction == "U":
        if Snake1.snake_y == 0:
            Winners(snake=2)

        # and part of the snakes body is above the snake's head...
        if ([Snake1.snake_x, Snake1.snake_y - 10] in Snake1.snake_blocks) or ([Snake1.snake_x, Snake1.snake_y - 10]
                                                                              in Snake2.snake_blocks):
            # Die
            Winners(snake=2)
        # else:
        Snake1.snake_y -= 10

    if Snake1.snake_direction == "D":
        if Snake1.snake_y == 500:
            Winners(snake=2)

        if ([Snake1.snake_x, Snake1.snake_y + 10] in Snake1.snake_blocks) or ([Snake1.snake_x, Snake1.snake_y + 10]
                                                                              in Snake2.snake_blocks):
            Winners(snake=2)
        Snake1.snake_y += 10

    if Snake1.snake_direction == "L":
        if Snake1.snake_x == 0:
            Winners(snake=2)
        if ([Snake1.snake_x - 10, Snake1.snake_y] in Snake1.snake_blocks) or ([Snake1.snake_x - 10, Snake1.snake_y]
                                                                              in Snake2.snake_blocks):
            Winners(snake=2)
        Snake1.snake_x -= 10

    if Snake1.snake_direction == "R":
        if Snake1.snake_x == 500:
            Winners(snake=2)
        if ([Snake1.snake_x + 10, Snake1.snake_y] in Snake1.snake_blocks) or ([Snake1.snake_x + 10, Snake1.snake_y]
                                                                              in Snake2.snake_blocks):
            Winners(snake=2)
        Snake1.snake_x += 10

    # After changing the coordinates of the snake's head, append the new head to the list of snake blocks
    Snake1.snake_blocks.insert(0, [Snake1.snake_x, Snake1.snake_y])
    # and delete the last block of the snake
    Snake1.snake_blocks.pop(-1)


def snake_move2():
    # If the user attempts to move upward
    if Snake2.snake_direction == "U":
        if Snake2.snake_y == 0:
            Winners(snake=1)
        # and part of the snakes body is above the snake's head...
        if ([Snake2.snake_x, Snake2.snake_y - 10] in Snake2.snake_blocks) or ([Snake2.snake_x, Snake2.snake_y - 10]
                                                                              in Snake1.snake_blocks):
            # Die
            Winners(snake=1)
        # else:
        Snake2.snake_y -= 10

    if Snake2.snake_direction == "D":
        if Snake2.snake_y == 500:
            Winners(snake=1)
        if ([Snake2.snake_x, Snake2.snake_y + 10] in Snake2.snake_blocks) or ([Snake2.snake_x, Snake2.snake_y + 10]
                                                                              in Snake1.snake_blocks):
            Winners(snake=1)
        Snake2.snake_y += 10

    if Snake2.snake_direction == "L":
        if Snake2.snake_x == 0:
            Winners(snake=1)
        if ([Snake2.snake_x - 10, Snake2.snake_y] in Snake2.snake_blocks) or ([Snake2.snake_x - 10, Snake2.snake_y]
                                                                              in Snake1.snake_blocks):
            Winners(snake=1)
        Snake2.snake_x -= 10

    if Snake2.snake_direction == "R":
        if Snake2.snake_x == 500:
            Winners(snake=1)
        if ([Snake2.snake_x + 10, Snake2.snake_y] in Snake2.snake_blocks) or ([Snake2.snake_x + 10, Snake2.snake_y]
                                                                              in Snake1.snake_blocks):
            Winners(snake=1)
        Snake2.snake_x += 10

    # After changing the coordinates of the snake's head, append the new head to the list of snake blocks
    Snake2.snake_blocks.insert(0, [Snake2.snake_x, Snake2.snake_y])
    # and delete the last block of the snake
    Snake2.snake_blocks.pop(-1)


# Display
pygame.init()
screen = pygame.display.set_mode((500, 500))
screen.fill(Colors.BLACK)

# Main Game Loop
running = True
while running:
    screen.fill(Colors.BLACK)
    snake_drawer1 = Snake1(screen)
    snake_drawer2 = Snake2(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_w and Snake1.snake_direction != "D":
                Snake1.snake_direction = "U"
                snake_move1()
            if event.key == pygame.K_s and Snake1.snake_direction != "U":
                Snake1.snake_direction = "D"
                snake_move1()
            if event.key == pygame.K_a and Snake1.snake_direction != "R":
                Snake1.snake_direction = "L"
                snake_move1()
            if event.key == pygame.K_d and Snake1.snake_direction != "L":
                Snake1.snake_direction = "R"
                snake_move1()
            if event.key == pygame.K_UP and Snake2.snake_direction != "D":
                Snake2.snake_direction = "U"
                snake_move2()
            if event.key == pygame.K_DOWN and Snake2.snake_direction != "U":
                Snake2.snake_direction = "D"
                snake_move2()
            if event.key == pygame.K_LEFT and Snake2.snake_direction != "R":
                Snake2.snake_direction = "L"
                snake_move2()
            if event.key == pygame.K_RIGHT and Snake2.snake_direction != "L":
                Snake2.snake_direction = "R"
                snake_move2()
    snake_drawer1.draw()
    snake_drawer2.draw()
    pygame.display.update()
