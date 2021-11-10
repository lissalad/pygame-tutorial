import pygame
pygame.init()

screen = pygame.display.set_mode([500,500])

# ------------ CLASSES -------------------- #
class GameObject(pygame.sprite.Sprite):
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    self.surf = pygame.image.load(image)
    self.x = x
    self.y = y

  def render(self, screen):
    screen.blit(self.surf, (self.x, self.y))

# -------------- SPRITES -------------------- #
apple = GameObject(200, 300, './images/apple.png')
strawberry = GameObject(120, 300, './images/strawberry.png')

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
  fruit = 'a';
  for i in range(0,3):
    for e in range(0,3):
      x = 500/3 * (e+.5)-32
      y = 500/3 *(i+.5) -32
      if fruit == 'a':
        apple = GameObject(x, y, './images/apple.png')
        apple.render(screen)
        fruit = 's'
      else:
        strawberry = GameObject(x, y, './images/strawberry.png')
        strawberry.render(screen)
        fruit='a'
  # Update the window
  pygame.display.flip()