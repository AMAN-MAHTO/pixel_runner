import pygame
from random import randint,choice
from sys import exit  # --- sys provide excess to different system command

def display_score(start_time):
    score = pygame.time.get_ticks()//1000 - start_time//1000
    score_surf = font.render(f'Score: {score}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (600,50))
    screen.blit(score_surf,score_rect)
    return score

def obstacle_movement(obstacle_list):
    game_active = True
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            
            if obstacle_rect.bottom == 300: screen.blit(snail_surface1,obstacle_rect)
            else: screen.blit(fly_surface1,obstacle_rect)
        
        
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else: return []

def collision(player_rect,obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            if player_rect.colliderect(obstacle_rect): return False
    
    return True

pygame.init()  # ----- like starting car with keys
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))  # ---- playing surface
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
snail_rect = snail_surface1.get_rect(midbottom = (screen_width,300))

player_surface = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha() 
player_rect = player_surface.get_rect(midbottom=(80,300))
player_stand = pygame.image.load("graphics/player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2) #-- surface,angle,scale
player_stand_rect = player_stand.get_rect(center = (screen_width//2,screen_height//2))


fly_surface1 = pygame.image.load("graphics/Fly/Fly1.png").convert_alpha()
fly_surface2 = pygame.image.load("graphics/Fly/Fly2.png").convert_alpha()

#text surfaces
game_name = font.render("Pixel Runner",False,(111,196,169))
game_name_rect = game_name.get_rect(center  = (400,80))
game_message = font.render("Press Space To Run",False,(111,196,169))
game_message_rect = game_message.get_rect(center  = (400,320))

#timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)


#variables
snail_x_pos = screen_width
start_time = 0
ground_pox = 300
game_active = False
player_gravity = 0
score =0
obstacle_rect_list = []

while True:
    for event in pygame.event.get():  # event loop -- check all event happening
        if event.type == pygame.QUIT:
            pygame.quit()  # ---- close the pygame window but the loop is still runing --- error video system not initialized
            exit()  # ---- while loop also end remmoving the error

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= ground_pox:
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= ground_pox:
                    player_gravity = -20

            if event.type == obstacle_timer:
                if randint(0,2):
                    obstacle_rect_list.append(snail_surface1.get_rect(midbottom = (screen_width+randint(100,400),300)))
                else:
                    obstacle_rect_list.append(fly_surface1.get_rect(midbottom = (screen_width+randint(100,400),200)))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = screen_width
            start_time = pygame.time.get_ticks()
        
        

    
    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(land_surface, (0, 300))
        screen.blit(snail_surface1,snail_rect)
        # 
        
        # snail_rect.left -= 4
        # if snail_rect.right <=0: snail_rect.left = screen_width
        
        #obstacle
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        print(obstacle_rect_list)

        #player
        if player_rect.bottom < ground_pox-2 or player_gravity < 0:
            
            player_gravity += 1
            player_rect.y += player_gravity
            if player_rect.bottom > ground_pox:
                player_rect.bottom = ground_pox
                
        screen.blit(player_surface,player_rect)
        
        
        #collision
        game_active = collision(player_rect,obstacle_rect_list)
            
        

        
        #score
        score = display_score(start_time)
        

    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80,300)
        score_message = font.render(f"Your Score: {score}",False,(111,196,169))
        score_message_rect = score_message.get_rect(center = (400,80))
        if score == 0:
            screen.blit(game_name,game_name_rect)
        else:
            screen.blit(score_message,score_message_rect)

        screen.blit(game_message,game_message_rect)
        
        

    

    pygame.display.update()
    clock.tick(60)
