import random
from random import randint, choice
import pygame
pygame.init()

height = 667
width = 375
swimmer_height = None
screen = pygame.display.set_mode([width,height])
clock = pygame.time.Clock()

counter = 0
lanes_y = [0,0,0,0]
lanes_x = [0,0]

lanes = [93, 218, 343]
bg = pygame.image.load("./images/underwater.png")


# ------------ CLASSES -------------------- #
class GameObject(pygame.sprite.Sprite):
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    self.surf = pygame.image.load(image)
    self.x = x
    self.y = y
    self.rect = self.surf.get_rect() # add 

  def render(self, screen):
    self.rect.x = self.x
    self.rect.y = self.y
    screen.blit(self.surf, (self.x, self.y))


class Bomb(GameObject):
  def __init__(self, image):
    super(Bomb, self).__init__(0, 0, image)
    self.dy = lanes_x[-1]
    self.dx = (randint(0, 200) / 100) + 1
    self.direction = ""
    self.reset()
    self.w = self.surf.get_width()
    self.h =self.surf.get_height()

  def get_random_direction(self):
    directions = ["down", "up", "left", "right"]
    self.direction = random.choice(directions)

  def reset(self):
    self.get_random_direction()
    self.surf = pygame.transform.rotate(self.surf, 46)

    if self.direction == "down":
      self.x = choice(lanes_x)
      self.y = height + self.surf.get_height()
    elif self.direction == "up":
      self.x = choice(lanes_x)
      self.y = 0 - self.surf.get_height()
    elif self.direction == "left":
      self.y = choice(lanes_y)
      self.x = width + self.surf.get_width()
    elif self.direction == "right":
      self.y = choice(lanes_y)
      self.x = 0 - self.surf.get_width()

  def move(self):
    if self.direction == "left":
      self.y -= self.dy
      self.x -= self.dx
      if self.x < 0 - self.surf.get_width(): 
        self.reset()
    elif self.direction == "right":
      self.y += self.dy
      self.x += self.dx  
      if self.x > width + self.surf.get_width(): 
        self.reset()    
    elif self.direction == "down":
      self.x -= self.dy
      self.y -= self.dx
      if self.y < 0 - self.surf.get_height(): 
        self.reset()
    elif self.direction == "up":
      self.x += self.dy
      self.y += self.dx  
      if self.y > height + self.surf.get_height(): 
        self.reset()  

      
  def get_random_direction(self):
    directions = ["down", "up", "left", "right"]
    self.direction = random.choice(directions)

class Apple(GameObject):
  def __init__(self):
   super(Apple, self).__init__(0, 0, './images/apple.png')
   self.dx = 0
   self.dy = (randint(0, 200) / 100) + 1
   self.direction = "up"
   self.reset()

  def reset(self):
    if self.direction == "down":
      self.x = choice(lanes_x)
      self.y = height + self.surf.get_height()
    elif self.direction == "up":
      self.x = choice(lanes_x)
      self.y = 0 - self.surf.get_height()

  def move(self):
    if self.direction == "down":
      self.x -= self.dx
      self.y -= self.dy
      if self.y < 0 - self.surf.get_height(): 
        self.direction = "up"
        self.reset()
    elif self.direction == "up":
      self.x += self.dx
      self.y += self.dy  
      if self.y > height + self.surf.get_height():
        self.direction = "down"
        self.reset()    

class Strawberry(GameObject):
  def __init__(self):
   super(Strawberry, self).__init__(0, 0, './images/strawberry.png')
   self.dy = 0
   self.dx = (randint(0, 200) / 100) + 1
   self.direction = "right"
   self.reset()

  def reset(self):
    if self.direction == "left":
      self.y = choice(lanes_y)
      self.x = width + self.surf.get_width()
    elif self.direction == "right":
      self.y = choice(lanes_y)
      self.x = 0 - self.surf.get_width()

  def move(self):
    if self.direction == "left":
      self.y -= self.dy
      self.x -= self.dx
      if self.x < 0 - self.surf.get_width():
        self.direction = "right"
        self.reset()
    elif self.direction == "right":
      self.y += self.dy
      self.x += self.dx  
      if self.x > width + self.surf.get_width(): 
        self.direction = "left"
        self.reset()    

class Fish(GameObject):
  def __init__(self, image, speed):
   super(Fish, self).__init__(0, 0, image)
   self.dy = 0
   self.dx = (randint(0, speed / 100) + 1)
   self.direction = "right"
   self.reset()

  def flip(self):
    if(self.direction == "right"):
      self.surf = pygame.transform.flip(self.surf, True,False)
      self.direction = "left"
    elif(self.direction == "left"):
      self.surf = pygame.transform.flip(self.surf, True,False)
      self.direction = "right"

  def reset(self):
    self.flip()
    if self.direction == "left":
      self.y = choice(lanes_y)
      self.x = width + self.surf.get_width()
    elif self.direction == "right":
      self.y = choice(lanes_y)
      self.x = 0 - self.surf.get_width()
  
  def move(self):
    if self.direction == "left":
      self.y -= self.dy
      self.x -= self.dx
      if self.x < 0 - self.surf.get_width():
        self.reset()
    elif self.direction == "right":
      self.y += self.dy
      self.x += self.dx  
      if self.x > width + self.surf.get_width(): 
        self.reset()    



class Player(GameObject):
  def __init__(self):
    super(Player, self).__init__(1,1, './images/shark.png')
    self.dx = 0
    self.dy = 0
    self.pos_x = 1
    self.pos_y = 1
    self.reset()

  def left(self):
    if self.pos_x > 0:
      self.pos_x -= 1
      self.update_dx_dy()
      self.surf = pygame.transform.flip(self.surf, True,False)

  def right(self):
    if self.pos_x < len(lanes_x) - 1:
      self.pos_x += 1
      self.update_dx_dy()
      self.surf = pygame.transform.flip(self.surf, True,False)


  def up(self):
    if self.pos_y > 0:
      self.pos_y -= 1
      self.update_dx_dy()

  def down(self):
    if self.pos_y < len(lanes_y) - 1:
      self.pos_y += 1
      self.update_dx_dy()

  def move(self):
    self.x -= (self.x - self.dx) * 0.06
    self.y -= (self.y - self.dy) * 0.03

  def reset(self):
    self.x = lanes_x[self.pos_x]
    self.y = lanes_y[self.pos_y]
    self.dx = self.x
    self.dy = self.y

  def update_dx_dy(self):
    self.dx = lanes_x[self.pos_x]
    self.dy = lanes_y[self.pos_y]

# -------------- SPRITES -------------------- #
apple = Apple()
strawberry = Strawberry()
player = Player()
bottle = Bomb("./images/bottle.png")
fish1 = Fish("./images/fish1.png", 100)
# fish2 = Fish("./images/fish2.png", 300)
# fish3 = Fish("./images/fish3.png",200)
fish4 = Fish("./images/fish4.png", 100)
# fish5 = Fish("./images/fish5.png", 300)
fish6 = Fish("./images/fish6.png",200)


all_sprites = pygame.sprite.Group()
all_sprites.add(player)
# all_sprites.add(apple)
# all_sprites.add(strawberry)
all_sprites.add(fish1)
# all_sprites.add(fish2)
# all_sprites.add(fish3)
all_sprites.add(fish4)
# all_sprites.add(fish5)
all_sprites.add(fish6)

all_sprites.add(bottle)

# fruit_sprites = pygame.sprite.Group()
# fruit_sprites.add(apple)
# fruit_sprites.add(strawberry)

fish_sprites = pygame.sprite.Group()
fish_sprites.add(fish1)
# fish_sprites.add(fish2)
# fish_sprites.add(fish3)
fish_sprites.add(fish4)
# fish_sprites.add(fish5)
fish_sprites.add(fish6)

# ---------- SET VERTICAL LANES --------------- #
num_v = 3
player_height = player.surf.get_height()
offset=player_height/num_v
lanes_y = [offset, height/num_v-offset, height*(2/num_v)-offset]

# ---------- SET HORIZONTAL LANES --------------- #
num_h = 2
player_width = player.surf.get_width()
offset = player_width/num_h
lanes_x = [player_width*.2, width-player_width*1.2]

# ----------- GAME LOOP ---------------- #
running = True 
while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      elif event.key == pygame.K_LEFT:
        player.left()
      elif event.key == pygame.K_RIGHT:
        player.right()
      elif event.key == pygame.K_UP:
        player.up()
      elif event.key == pygame.K_DOWN:
        player.down()
	
	# -------- CLEAR --------------------------- #
  screen.fill((255, 255, 255))
      
  # ------------- DRAW --------------------------- #
  screen.blit(bg, (0, 0))

  for entity in all_sprites:
    entity.move()
    entity.render(screen)

    # fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
    # if fruit:
    #   fruit.reset()

    fish = pygame.sprite.spritecollideany(player, fish_sprites)
    if fish:
      fish.reset()

    if pygame.sprite.collide_rect(player, bottle):
      print(counter)
      counter += 1
      if counter > 10:
        running = False


  # --------- UPDATE --------------------------- #
  pygame.display.flip()
  clock.tick(60)


# ------ IDEAS ------------------------- #

# keep score
# lives
# eating sound effects
# fix overlapping fish
# no spawn on bottle
# more fish over time
# pause method?
# gifs?