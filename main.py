import pygame
import random
import sys

# Khởi tạo Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zombie Shooter")
clock = pygame.time.Clock()

# Load background map
try:
    background_img = pygame.image.load("assets/map.png").convert()
    background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
except Exception:
    background_img = None

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        try:
            self.image = pygame.image.load("assets/player.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (50, 50))
        except Exception:
            self.image = pygame.Surface((50, 50))
            self.image.fill(GREEN)
        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT//2))
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Giới hạn di chuyển của player trong cửa sổ game
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

# Zombie class
class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        try:
            self.image = pygame.image.load("assets/zombie.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (40, 40))
        except Exception:
            self.image = pygame.Surface((40, 40))
            self.image.fill(RED)
        x = random.choice([0, WIDTH])
        y = random.randint(0, HEIGHT)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = random.randint(1, 3)

    def update(self):
        direction = pygame.math.Vector2(player.rect.center) - pygame.math.Vector2(self.rect.center)
        if direction.length() != 0:
            direction = direction.normalize()
        self.rect.x += int(direction.x * self.speed)
        self.rect.y += int(direction.y * self.speed)

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, dir):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=pos)
        self.speed = 10
        self.direction = dir

    def update(self):
        self.rect.x += int(self.direction[0] * self.speed)
        self.rect.y += int(self.direction[1] * self.speed)
        # Xóa viên đạn khi ra ngoài màn hình
        if self.rect.x < 0 or self.rect.x > WIDTH or self.rect.y < 0 or self.rect.y > HEIGHT:
            self.kill()

# Hàm reset game
def reset_game():
    global player, player_group, bullets, zombies, score, game_over
    player = Player()
    player_group = pygame.sprite.Group(player)
    bullets = pygame.sprite.Group()
    zombies = pygame.sprite.Group()
    score = 0
    game_over = False

# Sprite groups
player = Player()
player_group = pygame.sprite.Group(player)
bullets = pygame.sprite.Group()
zombies = pygame.sprite.Group()

SPAWN_ZOMBIE = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_ZOMBIE, 1500)

score = 0
font = pygame.font.SysFont(None, 36)

def draw_score():
    score_surf = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_surf, (10, 10))

rapid_fire = False
rapid_fire_timer = 0
rapid_fire_interval = 100  # ms
slow_active = False
slow_timer = 0
slow_duration = 3000  # ms
bomb_count = 3

def draw_instructions():
    instr = [
        "SPACE: Rapid Fire | B: Bomb ({} left) | S: Slow Zombie".format(bomb_count),
        "WASD: Move | Mouse: Shoot | R: Restart"
    ]
    for i, text in enumerate(instr):
        surf = font.render(text, True, WHITE)
        screen.blit(surf, (10, 40 + i*30))

game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SPAWN_ZOMBIE and not game_over:
            zombies.add(Zombie())
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mx, my = pygame.mouse.get_pos()
            direction = pygame.math.Vector2(mx - player.rect.centerx, my - player.rect.centery)
            if direction.length() != 0:
                direction = direction.normalize()
            bullets.add(Bullet(player.rect.center, (direction.x, direction.y)))
        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_SPACE:
                rapid_fire = True
                rapid_fire_timer = pygame.time.get_ticks()
            if event.key == pygame.K_b and bomb_count > 0:
                bomb_count -= 1
                zombies.empty()
            if event.key == pygame.K_s:
                slow_active = True
                slow_timer = pygame.time.get_ticks()
        if event.type == pygame.KEYUP and not game_over:
            if event.key == pygame.K_SPACE:
                rapid_fire = False
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_r:
                reset_game()
                bomb_count = 3

    if not game_over:
        player_group.update()
        bullets.update()
        # Skill: Slow zombie
        if slow_active:
            for z in zombies:
                z.speed = 1
            if pygame.time.get_ticks() - slow_timer > slow_duration:
                slow_active = False
                for z in zombies:
                    z.speed = random.randint(1, 3)
        else:
            for z in zombies:
                if z.speed == 1:
                    z.speed = random.randint(1, 3)
        zombies.update()

        # Skill: Rapid Fire
        if rapid_fire:
            now = pygame.time.get_ticks()
            if now - rapid_fire_timer > rapid_fire_interval:
                mx, my = pygame.mouse.get_pos()
                direction = pygame.math.Vector2(mx - player.rect.centerx, my - player.rect.centery)
                if direction.length() != 0:
                    direction = direction.normalize()
                bullets.add(Bullet(player.rect.center, (direction.x, direction.y)))
                rapid_fire_timer = now

        # Va chạm đạn và zombie
        for bullet in bullets:
            hit_zombies = pygame.sprite.spritecollide(bullet, zombies, True)
            if hit_zombies:
                bullet.kill()
                score += len(hit_zombies)

        # Va chạm zombie và player
        if pygame.sprite.spritecollide(player, zombies, False):
            game_over = True

    if background_img:
        screen.blit(background_img, (0, 0))
    else:
        screen.fill(BLACK)
    player_group.draw(screen)
    bullets.draw(screen)
    zombies.draw(screen)
    draw_score()
    draw_instructions()
    if game_over:
        over_surf = font.render("Game Over!", True, RED)
        screen.blit(over_surf, (WIDTH//2 - 80, HEIGHT//2 - 20))
        retry_surf = font.render("Nhấn R để chơi lại", True, WHITE)
        screen.blit(retry_surf, (WIDTH//2 - 120, HEIGHT//2 + 20))
    pygame.display.flip()
    clock.tick(60)
