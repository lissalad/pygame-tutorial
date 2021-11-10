from random import randint
import pygame
pygame.init()

screen = pygame.display.set_mode([500,500])
clock = pygame.time.Clock()


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
   self.x = randint(50, 400)
   self.y = -64

# -------------- SPRITES -------------------- #
apple = Apple()

# ----------- GAME LOOP ---------------- #
running = True 
while running: 
	# Looks at events 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
	
	# -------- CLEAR --------------------------- #
  screen.fill((255, 255, 255))
      
  # ------------- DRAW --------------------------- #
  apple.move() 
  apple.render(screen)

  # --------- UPDATE --------------------------- #
  pygame.display.flip()
  clock.tick(60)
