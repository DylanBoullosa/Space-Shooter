import pygame
import sys
import time
import random



pygame.font.init()
pygame.mixer.init()




SHOOT_SOUND = pygame.mixer.Sound("shoot.wav")
EXPLOSION_SOUND = pygame.mixer.Sound("explosion.wav")
ENEMY_SHOOT_SOUND = pygame.mixer.Sound("enemy_shoot.wav")




WIDTH, HEIGHT = 1100, 850
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooters")




PLAYER_WIDTH = 300
PLAYER_HEIGHT = 300
PLAYER_VEL = 15




ENEMY_WIDTH = 300
ENEMY_HEIGHT = 300
ENEMY_VEL = 7




BULLET_WIDTH = 100
BULLET_HEIGHT = 150
BULLET_VEL = 12




ENEMY_BULLET_WIDTH = 200
ENEMY_BULLET_HEIGHT = 300
ENEMY_BULLET_VEL = 12




SPACESHIP_IMG = pygame.transform.scale(pygame.image.load("spaceship.png"), (PLAYER_WIDTH, PLAYER_HEIGHT))
ASTEROID_IMG = pygame.transform.scale(pygame.image.load("enemy.png"), (ENEMY_WIDTH, ENEMY_HEIGHT))
BULLET_IMG = pygame.transform.scale(pygame.image.load("bullet.png"), (BULLET_WIDTH, BULLET_HEIGHT))
ENEMY_BULLET_IMG = pygame.transform.scale(pygame.image.load("enemy_bullet.png"), (ENEMY_BULLET_WIDTH, ENEMY_BULLET_HEIGHT))




FONT = pygame.font.SysFont("fixed", 30)




BUTTON_WIDTH = 200
BUTTON_HEIGHT = 80
RESTART_BUTTON = pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 + 50, BUTTON_WIDTH, BUTTON_HEIGHT)
BUTTON_COLOR = (50, 200, 50)
BUTTON_TEXT_COLOR = (255, 255, 255)




class Enemy:
  def __init__(self, x, y):
      self.rect = pygame.Rect(x, y, ENEMY_WIDTH, ENEMY_HEIGHT)
      self.bullets = []




  def move(self):
      self.rect.y += ENEMY_VEL




  def shoot(self):
      bullet_width = ENEMY_BULLET_WIDTH * 0.15
      bullet_height = ENEMY_BULLET_HEIGHT * 0.15




      bullet_x = self.rect.x + (ENEMY_WIDTH // 2) - (bullet_width // 2)
      bullet_y = self.rect.y + ENEMY_HEIGHT




      bullet = pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height)
      self.bullets.append(bullet)




      # Play enemy shoot sound
      ENEMY_SHOOT_SOUND.play()




  def update_bullets(self):
      for bullet in self.bullets[:]:
          bullet.y += ENEMY_BULLET_VEL
          if bullet.y > HEIGHT:
              self.bullets.remove(bullet)
          pygame.draw.rect(WIN, (0, 0, 0), bullet, 2)




  def draw(self):
      WIN.blit(ASTEROID_IMG, (self.rect.x, self.rect.y))
      for bullet in self.bullets:
          WIN.blit(ENEMY_BULLET_IMG, (bullet.x, bullet.y))




class ScrollingBackground:
  def __init__(self, images, speed=1):
      self.images = images
      self.speed = speed
      self.y1 = 0
      self.y2 = -HEIGHT
      self.y3 = -HEIGHT * 2




  def update(self):
      self.y1 += self.speed
      self.y2 += self.speed
      self.y3 += self.speed




      if self.y1 >= HEIGHT:
          self.y1 = self.y3 - HEIGHT
      if self.y2 >= HEIGHT:
          self.y2 = self.y1 - HEIGHT
      if self.y3 >= HEIGHT:
          self.y3 = self.y2 - HEIGHT




  def draw(self):
      WIN.blit(self.images[0], (0, self.y1))
      WIN.blit(self.images[1], (0, self.y2))
      WIN.blit(self.images[2], (0, self.y3))




BG_IMAGES = [
  pygame.transform.scale(pygame.image.load("bk1.png"), (WIDTH, HEIGHT)),
  pygame.transform.scale(pygame.image.load("bk2.png"), (WIDTH, HEIGHT)),
  pygame.transform.scale(pygame.image.load("bk3.png"), (WIDTH, HEIGHT))
]




bg = ScrollingBackground(BG_IMAGES, speed=1)




def draw(player, elapsed_time, enemies, bullets):
  bg.update()
  bg.draw()




  time_text = FONT.render(f"Time : {round(elapsed_time)}s", 1, "white")
  WIN.blit(time_text, (10, 10))




  WIN.blit(SPACESHIP_IMG, (player.x , player.y))




  if enemies:
      for enemy in enemies:
          WIN.blit(ASTEROID_IMG, (enemy.rect.x, enemy.rect.y))
          for bullet in enemy.bullets:
              WIN.blit(ENEMY_BULLET_IMG, (bullet.x, bullet.y))




  for bullet in bullets:
      WIN.blit(BULLET_IMG, (bullet.x, bullet.y))    




  pygame.display.update()

# for menu
def main():
    # Your game logic here
    print("Running the game logic...")
    player = pygame.Rect(400, 700, PLAYER_WIDTH, PLAYER_HEIGHT)
    bullets = []
    enemies = []
    elapsed_time = 0

    # Game loop
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)  # 60 FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw(player, elapsed_time, enemies, bullets)

        elapsed_time += 1 / 60  # increment the elapsed time
        pygame.display.update()

def initialize_game():
    # Any game initialization code
    print("Initializing game...")



def game_logic():
  pygame.mixer.music.load("background_music.mp3")
  pygame.mixer.music.set_volume(0.5)
  pygame.mixer.music.play(-1)




  run = True
  enemy_count = 0
  player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT - 20, PLAYER_WIDTH, PLAYER_HEIGHT)
  clock = pygame.time.Clock()
  start_time = time.time()
  elapsed_time = 0




  enemy_add_increment = 2000
  enemies = []
  bullets = []
  hit = False




  while run:
      enemy_count += clock.tick(60)
      elapsed_time = time.time() - start_time




      if enemy_count > enemy_add_increment:
          for _ in range(3):
              enemy_x = random.randint(0, WIDTH - ENEMY_WIDTH)
              enemy = Enemy(enemy_x, -ENEMY_HEIGHT)
              enemies.append(enemy)




          enemy_add_increment = max(200, enemy_add_increment - 50)
          enemy_count = 0




      for enemy in enemies:
          enemy.move()
          if random.randint(1, 100) < 2:
              enemy.shoot()
          enemy.update_bullets()




      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              run = False
              break




      keys = pygame.key.get_pressed()
      if keys[pygame.K_a] and player.x - PLAYER_VEL >= -PLAYER_WIDTH // 3:
         player.x -= PLAYER_VEL
      if keys[pygame.K_d] and player.x + PLAYER_VEL + PLAYER_WIDTH <= WIDTH + PLAYER_WIDTH // 3:
          player.x += PLAYER_VEL
      if keys[pygame.K_w] and player.y - PLAYER_VEL >= -PLAYER_HEIGHT // 3:
          player.y -= PLAYER_VEL
      if keys[pygame.K_s] and player.y + PLAYER_VEL + PLAYER_HEIGHT <= HEIGHT + PLAYER_HEIGHT // 3:
          player.y += PLAYER_VEL


      if keys[pygame.K_SPACE]:
          bullet_x = player.x + (PLAYER_WIDTH // 2) - (BULLET_WIDTH // 2) + 34
          bullet_y = player.y + (PLAYER_WIDTH // 2) - (BULLET_WIDTH // 2) - 50
          bullet = pygame.Rect(bullet_x, bullet_y, BULLET_WIDTH, BULLET_HEIGHT)
          bullets.append(bullet)
          SHOOT_SOUND.play()




      for bullet in bullets[:]:
          bullet.y -= BULLET_VEL
          if bullet.y < 0:
              bullets.remove(bullet)




      for bullet in bullets[:]:
          for enemy in enemies[:]:
              hitbox_width = ENEMY_WIDTH * 0.2
              hitbox_height = ENEMY_HEIGHT * 0.2
              hitbox_x = enemy.rect.x + (ENEMY_WIDTH - hitbox_width) / 2
              hitbox_y = enemy.rect.y + (ENEMY_HEIGHT - hitbox_height) / 2
              enemy_hitbox = pygame.Rect(hitbox_x, hitbox_y, hitbox_width, hitbox_height)


              pygame.draw.rect(WIN, (0, 0, 0), enemy_hitbox, 2)


              if bullet.colliderect(enemy_hitbox):
                  bullets.remove(bullet)
                  enemies.remove(enemy)
                  EXPLOSION_SOUND.play()
                  break


          bullet_hitbox = pygame.Rect(bullet.x, bullet.y, BULLET_WIDTH, BULLET_HEIGHT)
          pygame.draw.rect(WIN, (0, 0, 0), bullet_hitbox, 2)


      hitbox_width = PLAYER_WIDTH * 0.2
      hitbox_height = PLAYER_HEIGHT * 0.2
      hitbox_x = player.x + (PLAYER_WIDTH - hitbox_width) / 2
      hitbox_y = player.y + (PLAYER_HEIGHT - hitbox_height) / 2
      player_hitbox = pygame.Rect(hitbox_x, hitbox_y, hitbox_width, hitbox_height)


      pygame.draw.rect(WIN, (0, 0, 0), player_hitbox, 2)




      for enemy in enemies:
          hitbox_width = ENEMY_WIDTH * 0.2
          hitbox_height = ENEMY_HEIGHT * 0.2
          hitbox_x = enemy.rect.x + (ENEMY_WIDTH - hitbox_width) / 2
          hitbox_y = enemy.rect.y + (ENEMY_HEIGHT - hitbox_height) / 2
          enemy_hitbox = pygame.Rect(hitbox_x, hitbox_y, hitbox_width, hitbox_height) 


          pygame.draw.rect(WIN, (0, 0, 0), enemy_hitbox, 2)
         
          if player_hitbox.colliderect(enemy_hitbox):
              hit = True
              break




          for enemy in enemies:
              for enemy_bullet in enemy.bullets[:]:
                 
                  enemy_bullet_hitbox = pygame.Rect(enemy_bullet.x, enemy_bullet.y, BULLET_WIDTH, BULLET_HEIGHT)
                  pygame.draw.rect(WIN, (0, 0, 0), enemy_bullet_hitbox, 2)  # Yellow for enemy bullet hitbox


                  if enemy_bullet.colliderect(player_hitbox):
                      hit = True
                      enemy.bullets.remove(enemy_bullet)
                      EXPLOSION_SOUND.play()
                      break




      if hit:
          pygame.mixer.music.stop()
          lost_text = FONT.render("You Died", 1, "white")
          WIN.blit(lost_text, (WIDTH / 2 - lost_text.get_width() / 2 + 0.5, HEIGHT / 2 - lost_text.get_height() / 2))




          # Draw the restart button
          pygame.draw.rect(WIN, BUTTON_COLOR, RESTART_BUTTON)
          restart_text = FONT.render("Restart", 1, BUTTON_TEXT_COLOR)
          WIN.blit(restart_text, (RESTART_BUTTON.x + (RESTART_BUTTON.width - restart_text.get_width()) / 2 + 0.5, RESTART_BUTTON.y + 25))




          pygame.display.update()




          # Wait for the player to click the restart button
          waiting = True
          while waiting:
              for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                      pygame.quit()
                      return
                  if event.type == pygame.MOUSEBUTTONDOWN:
                      if RESTART_BUTTON.collidepoint(event.pos):
                          main()  # Restart the game
                          return




          pygame.time.delay(4000)
          break




      print(f"Player: {player}, Enemies : {len(enemies)}, Bullets: {len(bullets)}")
      draw(player, elapsed_time, enemies, bullets)




  pygame.quit()

def restart_game():
    # Reset necessary game variables or functions
    pass  # Example function to clear states when restarting


def main():
    print("Initializing the game...")
    initialize_game()  # Call any initialization logic here
    game_logic()  # Start the game loop


if __name__ == "__main__":
  main()



