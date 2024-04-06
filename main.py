import pygame
from player import Player



window = pygame.display.set_mode((700, 500))
fps = pygame.time.Clock()

background = pygame.transform.scale(
    pygame.image.load("../../../../../Downloads/background.png"), (700, 500)
)

roma = Player(100, 100, 50, 50, "sprite1.png", 10)
roma2 = Player2(100, 100, 50, 50, "sprite2.png", 10)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if roma.hitbox.colliderect(roma.hitbox):
        print("ПРОГРАВ!!")
    roma.move()
    roma2.move()
    window.blit(background, (0, 0))
    roma.draw(window)
    roma2.draw(window)
    pygame.display.flip()
    fps.tick(60)

