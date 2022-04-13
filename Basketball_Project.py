import pygame
import time
from random import randint

pygame.init()
screen_width = 940
screen_height = 742
display_output = [screen_width, screen_height]
screen = pygame.display.set_mode(display_output)
pygame.display.set_caption("Basketball game")
clock = pygame.time.Clock()
court = pygame.image.load("basketball_court(4).jpg")

screen_display = pygame.display
text_x = 15
text_y = 15
font = pygame.font.Font('freesansbold.ttf', 40)
green = (0,255,0)

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [300, screen_height/2])



basket_width = 125
basket_pos_x = 450
basket_pos_y = 600
basket_y_line = basket_pos_y + 17
basket_x_start_co = basket_pos_x + 40
basket_x_end_co = basket_pos_x + 85
basket = pygame.image.load('basket.png')
basket_speed_x = 10
present_basket_speed_x = 0

ball_size = 100
ball_position_x = 50
ball_position_y = 50
ball_x_co = ball_position_x + 50
ball_y_co = ball_position_y + 50
speed_dir_x = 0
speed_dir_y = 4
basketball = pygame.image.load('basketball.png')

score = 0
play_game = True

def display():
    display_court()
    display_basketball(ball_position_x, ball_position_y)
    display_basket(basket_pos_x, basket_pos_y)


def display_court():
    screen.blit(court, (0, 0))


def display_basketball(pos_x, pos_y):
    screen.blit(basketball, (pos_x, pos_y))
    update_ball_pos()


def display_basket(pos_x, pos_y):
    screen.blit(basket, (pos_x, pos_y))


def check_for_score(x):
    if ball_y_co in range(basket_y_line-(int(speed_dir_y)//2), basket_y_line+(int(speed_dir_y)//2)):
        if ball_x_co in range(basket_x_start_co-1, basket_x_end_co+1):
            x += 1
        else:
            if x == 0:
                x == 0
            else:
                x -= 1  
    return x


def finish(x):
    if x == 10:
        message_to_screen("YOU WIN!!!!, CONGRATS!!", green)
        pygame.display.update()
        # win = font.render("YOU WIN!", True, (255, 255, 255), "green")
        # screen.blit(win, (text_x , text_y))
        # screen_display.set_caption("YOU WIN !")
        time.sleep(2)
        pygame.quit()
        quit()

def display_score(sco, text_pos_x, text_pos_y):
    score_disp = font.render("Score: " + str(sco), True, (0, 0, 0),"yellow")
    screen.blit(score_disp, (text_pos_x, text_pos_y))


def check_for_event():
    global play_game, present_basket_speed_x
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play_game = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        present_basket_speed_x = - basket_speed_x
    elif keys[pygame.K_RIGHT]:
        present_basket_speed_x = basket_speed_x
    else:
        present_basket_speed_x = 0


def enforce_border():
    global basket_pos_x
    if basket_pos_x > (screen_width-basket_width):
        basket_pos_x = screen_width-basket_width
    if basket_pos_x < 0:
        basket_pos_x = 0


def random_ball_initialise():
    global ball_position_y, ball_position_x, speed_dir_y
    if ball_position_y > (screen_height + ball_size):
        speed_dir_y = 3
        ball_position_x = randint(10, 880)
        ball_position_y = 0


def update_basket_score_region():
    global basket_x_start_co, basket_x_end_co
    basket_x_start_co = basket_pos_x + 40
    basket_x_end_co = basket_pos_x + 85


def update_ball_pos():
    global ball_x_co, ball_y_co, basket_pos_x, ball_position_y, speed_dir_y
    ball_x_co = ball_position_x + 50
    ball_y_co = ball_position_y + 50
    basket_pos_x += present_basket_speed_x
    ball_position_y += int(speed_dir_y)
    speed_dir_y += (speed_dir_y*0.02)
    random_ball_initialise()


def initialise_event():
    check_for_event()
    enforce_border()


while play_game:
    clock.tick(60)
    initialise_event()
    display()
    update_basket_score_region()
    score = check_for_score(score)
    display_score(score, text_x, text_y)
    finish(score)
    pygame.display.flip()
pygame.quit()