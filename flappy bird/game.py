import pygame
import random

pygame.init()

screen = pygame.display.set_mode((500,700))
black = (0, 0, 0)
green = (0, 204, 00)
red = (255, 0, 0)

bg = pygame.image.load('background.jpg')
bird = pygame.image.load('bird1.png')
birdup = pygame.image.load('bird2.png')

run = True
game = False
alive = True
clock = pygame.time.Clock()

birdx = 50
birdy = 300
yvel = 0
bird_up = False

obs_w = 70
obs_h = random.randint(150, 450)
obs_vel = -4
obs_x = 500

score = 0
font = pygame.font.SysFont('ubuntu', 32)
font1 = pygame.font.SysFont('arial', 40)

def drawscore(score):
    display = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(display, (10, 10))

def drawobs(height):
    pygame.draw.rect(screen, green, (obs_x, 0, obs_w, height))
    bottom_y = height + 150
    bottom_obstacle_height = 635 - bottom_y
    pygame.draw.rect(screen, green, (obs_x, bottom_y, obs_w, bottom_obstacle_height))

def collision_dect(obs_x, obs_h, birdy, bottom_obstacle_height):
    if obs_x >= 50 and obs_x <= (50+ 64):
        if birdy <= obs_h or birdy >= (bottom_obstacle_height -64):
            return True
        return False


def drawbird(x, y):
    if bird_up == False:
        screen.blit(bird, (x, y))
    else:
        screen.blit(birdup, (x, y))

while run:
    clock.tick(60)

    screen.fill(black)

    screen.blit(bg, (0,0))
      
    if alive == True:

        if game == False:
            msg = font.render("PRESS SPACE BAR TO START", True, (255, 255, 255))
            screen.blit(msg, (20, 50))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game = True



        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        yvel = -6
                        bird_up = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        yvel = 6
                        bird_up = False


            birdy += yvel

            if birdx <= 0:
                birdx = 0
            if birdy >= 571:
                birdy = 571

            obs_x += obs_vel
            if obs_x <= -10:
                obs_x = 500
                obs_h = random.randint(200, 450)
                score += 1
            drawobs(obs_h)
            
            collision = collision_dect(obs_x, obs_h, birdy, obs_h + 150)
            if collision == True:
                alive = False


            drawbird(birdx, birdy)
            drawscore(score)

    else:
        msg2 = font1.render("YOU DIED!!", True, (224, 0, 0))
        msg3 = font.render("Press space bar to play again", True, (0, 0, 0))
        msg4 = font.render(f"Your Score is {score}", True, (255, 255, 255))
        screen.blit(msg2, (130, 50))
        screen.blit(msg3, (50, 100))
        screen.blit(msg4, (120, 150))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    obs_x = -20
                    alive = True
                    score = -1


    pygame.display.update()

pygame.quit()
