import pygame
import time
import random

pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set display dimensions
dis_width = 800
dis_height = 600

# Set the size of snake block
block_size = 20

# Set the speed of the snake
snake_speed = 10


# Create a font for displaying score
font_style = pygame.font.SysFont(None, 50)

# Function to display the score
def score(score):
    value = font_style.render("Your Score: " + str(score), True, black)
    dis.blit(value, [0, 0])

# Function to create the snake
def our_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], block_size, block_size])

# Function to display a message when the game is over
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Function to the game loop
def gameLoop():
    game_over = False
    game_close = False

    # Initial position of snake
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Initial change in position of snake
    x1_change = 0
    y1_change = 0

    # Snake's body (initially just the head)
    snake_list = []
    length_of_snake = 1

    # Position of food
    foodx = round(random.randrange(0, dis_width - block_size) / block_size) * block_size
    foody = round(random.randrange(0, dis_height - block_size) / block_size) * block_size

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, red, [foodx, foody, block_size, block_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(block_size, snake_list)
        score(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - block_size) / block_size) * block_size
            foody = round(random.randrange(0, dis_height - block_size) / block_size) * block_size
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Initialize display
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

gameLoop()


#When you run this code, a window will pop up with the game.
#  Use the arrow keys to control the snake. 
# The objective is to eat the red food, which will increase the length of the snake. 
# If the snake collides with itself or the window edges, the game ends.
#  You can restart the game by pressing 'C' or quit by pressing 'Q' when the game is over.