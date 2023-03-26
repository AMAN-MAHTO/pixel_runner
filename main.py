import pygame
from sys import exit #--- sys provide excess to different system command

pygame.init()  #----- like starting car with keys
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height)) #---- playing surface
pygame.display.set_caption("runner") #---- tittle name
clock = pygame.time.Clock() # ----- time in game important to make it speed on differnt operating system same 



sky_surface = pygame.image.load("graphics/Sky.png")
land_surface = pygame.image.load("graphics/ground.png")
snail_surface1 = pygame.image.load("graphics/snail/snail1.png")
snail_surface2 = pygame.image.load("graphics/snail/snail2.png")

fly_surface1 = pygame.image.load("graphics/fly/fly1.png")

fly_surface1 = pygame.image.load("graphics/Fly/Fly1.png")
fly_surface2 = pygame.image.load("graphics/Fly/Fly2.png")
move = 0
current_time = 0
skip_time = 0

def animation(image1,image2,x,y,speed):
    global current_time,skip_time
    if current_time - skip_time < speed:
        screen.blit(image1,(x,y))
    elif current_time - skip_time < speed*2 :
        screen.blit(image2,(x,y))
    else:
        screen.blit(image2,(x,y))
        skip_time = pygame.time.get_ticks()
    current_time = pygame.time.get_ticks()


while True: 
    for event in pygame.event.get():  #event loop -- check all event happening 
        if event.type == pygame.QUIT:
            pygame.quit() #---- close the pygame window but the loop is still runing --- error video system not initialized
            exit() #---- while loop also end remmoving the error
    # draw all our elements
    # update everthing
    screen.blit(sky_surface,(0,0))
    screen.blit(land_surface,(0,300))
    move += 0.5
    snail_x = screen_width-move
    if snail_x < -100:
        move = 0

    animation(snail_surface1,snail_surface2,snail_x,250,200)
    animation(fly_surface1,fly_surface2,snail_x,100,200)
    
    

    pygame.display.update()
    clock.tick(60)

