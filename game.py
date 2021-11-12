from random import randint, choice
import pygame
pygame.init()

screen = pygame.display.set_mode([500,500])
clock = pygame.time.Clock()
lanes = [93, 218, 343]


# ------------ CLASSES -------------------- #
class GameObject(pygame.sprite.Sprite):
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    self.surf = pygame.image.load(image)
    self.x = x
    self.y = y

  def render(self, screen):
    screen.blit(self.surf, (self.x, self.y))

class Apple(GameObject):
 def __init__(self):
   super(Apple, self).__init__(0, 0, './images/apple.png')
   self.dx = 0
   self.dy = (randint(0, 200) / 100) + 1
   self.reset()

 def move(self):
   self.x += self.dx
   self.y += self.dy
   if self.y > 500: 
     self.reset()

 def reset(self):
   self.x = choice(lanes)
   self.y = -64

class Strawberry(GameObject):
 def __init__(self):
   super(Strawberry, self).__init__(0, 0, './images/strawberry.png')
   self.dy = 0
   self.dx = (randint(0, 200) / 100) + 1
   self.reset()

 def move(self):
   self.x += self.dx
   self.y += self.dy
   if self.x > 500: 
     self.reset()

 def reset(self):
   self.y = choice(lanes)
   self.x = -64

class Player(GameObject):
  def __init__(self):
    super(Player, self).__init__(0, 0, './images/player.png')
    self.dx = 0
    self.dy = 0
    self.pos_x = 1
    self.pos_y = 1 
    self.reset()

  def left(self):
    if self.pos_x > 0:
      self.pos_x -= 1
      self.update_dx_dy()

  def right(self):
    if self.pos_x < len(lanes) - 1:
      self.pos_x += 1
      self.update_dx_dy()

  def up(self):
    if self.pos_y > 0:
      self.pos_y -= 1
      self.update_dx_dy()

  def down(self):
    if self.pos_y < len(lanes) - 1:
      self.pos_y += 1
      self.update_dx_dy()

  def move(self):
    self.x -= (self.x - self.dx) * 0.25
    self.y -= (self.y - self.dy) * 0.25

  def reset(self):
    self.x = lanes[self.pos_x]
    self.y = lanes[self.pos_y]
    self.dx = self.x
    self.dy = self.y

  def update_dx_dy(self):
    self.dx = lanes[self.pos_x]
    self.dy = lanes[self.pos_y]


# -------------- SPRITES -------------------- #
apple = Apple()
strawberry = Strawberry()
player = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(strawberry)
all_sprites.add(apple)

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
  for entity in all_sprites:
    entity.move()
    entity.render(screen)

  # --------- UPDATE --------------------------- #
  pygame.display.flip()
  clock.tick(60)
