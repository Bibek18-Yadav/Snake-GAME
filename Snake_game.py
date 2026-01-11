import pygame
import random

# Start the pygame engine
pygame.init()

# Setup screen dimensions
screen_width=600
screen_height=400
my_screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("My First Snake Game")

# Setting up my colors
color_white=(255,255,255)
color_black=(0,0,0)
color_red=(255,0,0)
color_green=(0,255,0)

# Game settings
game_timer=pygame.time.Clock()
block_size=10
move_speed=15

# Set the font for the score and messages
my_font=pygame.font.SysFont("comicsansms",25)

def display_the_score(current_score):
    # This draws the score on the top left corner
    text=my_font.render("Points: "+str(current_score),True,color_black)
    my_screen.blit(text,[5,5])

def draw_the_snake_body(snake_list):
    # Loop through the list to draw each part of the snake
    for part in snake_list:
        pygame.draw.rect(my_screen,color_green,[part[0],part[1],block_size,block_size])

def start_the_main_game():
    # Setting up game state variables
    is_game_over=False
    is_lose_screen=False

    # Snake starting position (middle of screen)
    x_pos=300
    y_pos=200

    # These track where the snake is moving
    x_move=0
    y_move=0

    snake_body_parts=[]
    length_of_snake=1

    # Put the first apple in a random spot
    apple_x=round(random.randrange(0,screen_width - block_size)/10.0)*10.0
    apple_y=round(random.randrange(0,screen_height - block_size)/10.0)*10.0

    while is_game_over==False:

        # This loop runs when you lose
        while is_lose_screen==True:
            my_screen.fill(color_white)
            lose_msg=my_font.render("You Lost! Press P to Play Again or Q to Quit",True,color_red)
            my_screen.blit(lose_msg,[screen_width/6,screen_height/3])
            display_the_score(length_of_snake - 1)
            pygame.display.update()

            # Check if player wants to restart or leave
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        is_game_over=True
                        is_lose_screen=False
                    if event.key==pygame.K_p:
                        start_the_main_game() # Restart the function

        # Checking for keyboard inputs
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                is_game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_move=-block_size
                    y_move=0
                elif event.key==pygame.K_RIGHT:
                    x_move=block_size
                    y_move=0
                elif event.key==pygame.K_UP:
                    y_move=-block_size
                    x_move=0
                elif event.key==pygame.K_DOWN:
                    y_move=block_size
                    x_move=0

        # Check if snake hits the walls
        if x_pos>=screen_width or x_pos<0 or y_pos>=screen_height or y_pos< 0:
            is_lose_screen = True

        # Move the snake position
        x_pos=x_pos+x_move
        y_pos=y_pos+y_move
        
        my_screen.fill(color_white)
        
        # Draw the apple
        pygame.draw.rect(my_screen,color_red,[apple_x, apple_y, block_size, block_size])

        # Logic for snake growth
        snake_head_pos=[]
        snake_head_pos.append(x_pos)
        snake_head_pos.append(y_pos)
        snake_body_parts.append(snake_head_pos)

        # Delete the tail as it moves
        if len(snake_body_parts)>length_of_snake:
            del snake_body_parts[0]

        # Check if snake hits itself
        for segment in snake_body_parts[:-1]:
            if segment==snake_head_pos:
                is_lose_screen=True

        draw_the_snake_body(snake_body_parts)
        display_the_score(length_of_snake-1)

        pygame.display.update()

        # Check if snake eats the apple
        if x_pos==apple_x and y_pos==apple_y:
            apple_x=round(random.randrange(0,screen_width-block_size)/10.0)*10.0
            apple_y=round(random.randrange(0,screen_height-block_size)/10.0)*10.0
            length_of_snake=length_of_snake+1

        game_timer.tick(move_speed)

    pygame.quit()
    quit()

# Start the game for the first time
start_the_main_game()