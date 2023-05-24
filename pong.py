import pygame, sys, random

def oppo_animation():
    if oppo.top < ball.y:
        oppo.top += oppo_speed
    if oppo.bottom > ball.y:
        oppo.bottom -= oppo_speed
    if oppo.top <= 0:
        oppo.top = 0
    if oppo.bottom >= screen_height:
        oppo.bottom = screen_height

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >=screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >=screen_width:
        ball_restart()
    if ball.colliderect(player) or ball.colliderect(oppo):
        ball_speed_x *= -1

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_x *= random.choice((1,-1))
    ball_speed_y *= random.choice((1,-1))


pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 960

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

ball = pygame.Rect(screen_width//2 - 15,screen_height//2 - 15,30,30)
oppo = pygame.Rect(screen_width - 20, screen_height//2 - 70,10,140)
player = pygame.Rect(10, screen_height//2 -70,10,140)

bg_color = pygame.Color('gray12')
light_grey = (200,200,200)

ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0
oppo_speed = 20


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player_speed +=7
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player_speed -=7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player_speed -=7
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player_speed +=7

    screen.fill(bg_color)

    ball_animation()
    player_animation()
    oppo_animation()
    
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.rect(screen,light_grey,oppo)
    pygame.draw.ellipse(screen,light_grey, ball)
    pygame.draw.aaline(screen,light_grey,(screen_width/2,0),(screen_width/2,screen_height))

    pygame.display.flip()
    clock.tick(60)