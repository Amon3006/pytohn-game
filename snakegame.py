import pygame
import random
import os
pygame.init()






################################### COLORS ###################################3

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0,255,0)
blue = (0,0,255)
welcome_back_color = (148,161,246)
welcome_text_color = (0, 153,0)
snaked = pygame.image.load('snakedbody.png')

################################## Screen size ##################################

screen_width = 900
screen_hieght = 700
fps = 60


##################################### MUSIC ##############################
pygame.mixer.init()



################################### Game Tile ###################################

gameWindow = pygame.display.set_mode((screen_width,screen_hieght))
pygame.display.set_caption("snake game")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,60)

################################### BACKGROUND #############################

bgimg = pygame.image.load('background.jpg')
bgimg = pygame.transform.scale(bgimg, (screen_width,screen_hieght)).convert_alpha()

########################## uitility functions ######################################

# def plot_snake(gameWindow, color, snk_list, snake_size):
#     for x,y in snk_list:
#         # pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        gameWindow.blit(snaked,(x,y))
        

def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

########################## Welcome Screen ##########################################

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(welcome_back_color)
        text_screen("Welcome To Snake Game",welcome_text_color,screen_width/5,screen_hieght/3)
        text_screen("press enter to play", welcome_text_color, screen_width / 5 +30, screen_hieght/3 +70 )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.load('Swoosh.mp3')
                    pygame.mixer.music.play()
                    gameloop()
        pygame.display.update()
        clock.tick(fps)


##############################creating a gameloop ####################################3

def gameloop():
    # COLORS
    white = (255, 255, 255)
    red = (255, 0, 0)
    black = (0, 0, 0)

    # in gane variables
    velocity_x, velocity_y = 0, 0
    snake_x, snake_y = 45, 55
    snake_size = 30
    fps = 60

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_hieght / 2)

    snk_list = []
    snk_length = 1

    init_vlocity = 5

    score = 0

    # game specific variables
    exit_game = False
    game_over = False

    ######## check if hiscore file exist ########3
    if (not os.path.exists("hiscore.txt")):
        with open("hiscore.txt","w") as f:
            f.write("0")

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    while not exit_game:
        if game_over:

            with open("hiscore.txt","w+") as f:
                f.write(str(hiscore))

            gameWindow.fill(white)
            text_screen("Game OVer!,",red,screen_width*0.3,screen_hieght*0.5) 
            text_screen("Please Enter to restart",red,screen_width*0.22,screen_hieght*0.4) 

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load('Swoosh.mp3')
                        pygame.mixer.music.play()
                        gameloop()



        else:

            if abs(snake_x-food_x)<20 and abs(snake_y-food_y)<20:
                score+=10
                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20, screen_hieght/2)
                snk_length += 5

                pygame.mixer.music.load('Beep Short .mp3')
                pygame.mixer.music.play()

                if score > int(hiscore):
                    hiscore = score

            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0,0))
            text_screen("Score:" + str(score)+"  Hiscore:" + str(hiscore), red, 20, 20)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            plot_snake(gameWindow,black, snk_list, snake_size)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)


            if snake_x< 0 :
                snake_x = screen_width

            if snake_x > screen_width:
                snake_x = 0
                
            if snake_y < 0 :
                snake_y = screen_hieght

            if snake_y>screen_hieght:
                snake_y= 0

            if len(snk_list) > snk_length:
                del snk_list[0]


            if head in snk_list[:-1]:
                game_over = True


            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        velocity_x += init_vlocity
                        velocity_y = 0

                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        velocity_x -= init_vlocity
                        velocity_y =0

                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        velocity_y -= init_vlocity
                        velocity_x = 0

                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        velocity_y += init_vlocity
                        velocity_x = 0

                    if event.key == pygame.K_s or event.key == pygame.K_h:
                        score+=10


        pygame.display.update()
        clock.tick(fps)

        snake_x += velocity_x
        snake_y += velocity_y


    pygame.quit()
    quit()

welcome()

