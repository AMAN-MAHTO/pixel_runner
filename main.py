import pygame
from random import randint, uniform, choice
from sys import exit  # --- sys provide excess to different system command


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_jump = pygame.image.load("graphics/Player/jump.png").convert_alpha()
        player_walk1 = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
        player_walk2 = pygame.image.load("graphics/Player/player_walk_2.png").convert_alpha()
        self.player_walk = [player_walk1, player_walk2]
        self.player_index = 0
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound("audio/jump.mp3")
        self.jump_sound.set_volume(0.5)

    def jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()

    def player_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation(self):
        if self.rect.bottom == 300:
            self.player_index += 0.1
            if self.player_index >= 2:
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

        else:
            self.image = self.player_jump

    def update(self):
        self.jump()
        self.player_gravity()
        self.animation()


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == "snail":
            snail_frame1 = pygame.image.load(
                "graphics/snail/snail1.png").convert_alpha()
            snail_frame2 = pygame.image.load(
                "graphics/snail/snail2.png").convert_alpha()
            self.frames = [snail_frame1, snail_frame2]
            y_pos = 300
        else:
            fly_frame1 = pygame.image.load(
                "graphics/Fly/Fly1.png").convert_alpha()
            fly_frame2 = pygame.image.load(
                "graphics/Fly/Fly2.png").convert_alpha()
            self.frames = [fly_frame1, fly_frame2]
            y_pos = 210

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))

    def animation(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def move(self):
        self.rect.x -= 4

    def delete(self):
        if self.rect.midright == -100:
            self.kill()

    def update(self):
        self.animation()
        self.move()
        self.delete()


def display_score(start_time):
    score = pygame.time.get_ticks()//1000 - start_time//1000
    score_surf = font.render(f'Score: {score}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(600, 50))
    screen.blit(score_surf, score_rect)
    return score


def collision_sprite():
    # --- True - delete the obstacle sprite
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()  # -- empyt the obstacle group
        return False
    else:
        return True


pygame.init()
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))  
pygame.display.set_caption("runner")  
clock = pygame.time.Clock()
start_time = 0
ground_pox = 300
game_active = False
score = 0

bg_music = pygame.mixer.Sound("audio/music.wav")
bg_music.play(loops = -1)

#group
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()


# text
font = pygame.font.Font(None, 35)
game_name = font.render("Pixel Runner", False, (111, 196, 169))
game_name_rect = game_name.get_rect(center=(400, 80))
game_message = font.render("Press Space To Run", False, (111, 196, 169))
game_message_rect = game_message.get_rect(center=(400, 320))

# baground image load
sky_surface = pygame.image.load("graphics/Sky.png").convert_alpha()
land_surface = pygame.image.load("graphics/ground.png").convert_alpha()

# intro
player_stand = pygame.image.load("graphics/player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)  # -- surface,angle,scale
player_stand_rect = player_stand.get_rect(center=(screen_width//2, screen_height//2))


# timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)


while True:
    for event in pygame.event.get():  # event loop -- check all event happening
        if event.type == pygame.QUIT:
            pygame.quit()  # ---- close the pygame window but the loop is still runing --- error video system not initialized
            exit()  # ---- while loop also end remmoving the error

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(
                    Obstacle(choice(["fly", "snail", "snail", "snail"])))

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True

            start_time = pygame.time.get_ticks()

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(land_surface, (0, 300))
        # screen.blit(snail_surface,snail_rect)

        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        game_active = collision_sprite()

        # score
        score = display_score(start_time)

    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)

        score_message = font.render(
            f"Your Score: {score}", False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center=(400, 80))
        if score == 0:
            screen.blit(game_name, game_name_rect)
        else:
            screen.blit(score_message, score_message_rect)

        screen.blit(game_message, game_message_rect)

    pygame.display.update()
    clock.tick(60)
