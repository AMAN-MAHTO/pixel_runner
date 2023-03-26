import pygame
from sys import exit  # --- sys provide excess to different system command

pygame.init()  # ----- like starting car with keys
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode(
    (screen_width, screen_height))  # ---- playing surface
pygame.display.set_caption("runner")  # ---- tittle name
# ----- time in game important to make it speed on differnt operating system same
clock = pygame.time.Clock()

# convert_alpha conver the image to something that python can eassly work with -- makse code fast

#font load
font = pygame.font.Font(None,35)

#image load
sky_surface = pygame.image.load("graphics/Sky.png").convert_alpha()
land_surface = pygame.image.load("graphics/ground.png").convert_alpha()
snail_surface1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_surface2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()

player_surface = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()

fly_surface1 = pygame.image.load("graphics/Fly/Fly1.png").convert_alpha()
fly_surface2 = pygame.image.load("graphics/Fly/Fly2.png").convert_alpha()

score_surface = font.render('My Game',False,"Black")

#rectangle
player_rect = player_surface.get_rect(midbottom=(80,300))
snail_rect = snail_surface1.get_rect(midbottom = (screen_width,300))
score_rect = score_surface.get_rect(center = (400,50))

#variables
snail_x_pos = screen_width
jump = False
jump_floor = 300
jump_cieling = 100
falling =False
player_gravity = 0

while True:
    for event in pygame.event.get():  # event loop -- check all event happening
        if event.type == pygame.QUIT:
            pygame.quit()  # ---- close the pygame window but the loop is still runing --- error video system not initialized
            exit()  # ---- while loop also end remmoving the error

    #     if event.type == pygame.MOUSEMOTION:
    #         if player_rect.collidepoint(event.pos):
    #             print("mouse collision")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                
                jump = True
                # falling = False
                player_gravity = 0

    # # draw all our elements
    # update everthing

    screen.blit(sky_surface, (0, 0))
    screen.blit(land_surface, (0, 300))
    screen.blit(snail_surface1,snail_rect)
    pygame.draw.rect(screen,"Pink",score_rect)
    pygame.draw.rect(screen,"Pink",score_rect,50)
    screen.blit(score_surface,score_rect)
    
    snail_rect.left -= 4
    if snail_rect.right <=0: snail_rect.left = screen_width

    #player
    player_gravity += 0.2
    if jump:
        player_rect.top -= player_gravity
        if player_rect.top <= jump_cieling:
            falling = True
            jump =False
    if falling:
        player_rect.bottom += player_gravity
        if player_rect.bottom >= jump_floor:
            falling = False
    
    screen.blit(player_surface,player_rect)
    
    

    # if player_rect.colliderect(snail_rect):
    #     print("cls")

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print("mouse")
    
    

    pygame.display.update()
    clock.tick(60)
