import pygame
pygame.init()

screen = pygame.display.set_mode([500,500])

running = True 
while running: 
	# Looks at events 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
	
	# -------- CLEAR --------------------------- #
  screen.fill((255, 255, 255))
      
# ------------- DRAW --------------------------- #


# ----------- Update the display ---------------- #
  pygame.display.flip()






# ------------- GRAY GRID ------------------------#
  for i in range(0,3):
    for e in range(0,3):
      color = (90, 90, 90)
      position = (500/3 * (e+.5), 500/3 *(i+.5))
      pygame.draw.circle(screen, color, position, 60)

# --------------- FIVE ----------------------- #
  color = (230, 60, 20)
  position = (83, 83)
  pygame.draw.circle(screen, color, position, 50)

  color = (250, 160, 20)
  position = (417, 83)
  pygame.draw.circle(screen, color, position, 50) 

  color = (250, 220, 20)
  position = (250, 250)
  pygame.draw.circle(screen, color, position, 50)

  color = (50, 250, 140)
  position = (83, 417)
  pygame.draw.circle(screen, color, position, 50)

  color = (50, 250, 240)
  position = (417, 417)
  pygame.draw.circle(screen, color, position, 50)

# ------------- SAMPLE CIRCLE ---------------------- #
  color = (255, 0, 255)
  position = (250, 250)
  pygame.draw.circle(screen, color, position, 75)