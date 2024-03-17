from pygame import *

WIDTH, HEIGHT = 800, 600
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Sace Shooter")

clock = time.Clock()

background = transform.scale(image.load('background.jpg'), (WIDTH, HEIGHT))

while True:
    window.blit(background, (0, 0))

    display.update()
    clock.tick(60)