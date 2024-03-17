from pygame import *

WIDTH, HEIGHT = 800, 600
BG_COLOR = (204, 255, 229)
window = display.set_mode((WIDTH, HEIGHT)) # створення вікна

background = transform.scale(image.load('background.png'), (WIDTH, HEIGHT)) # завантиження картинки

sprite1 = transform.scale(image.load('sprite1.png'), (100, 100))
sprite2 = transform.scale(image.load('sprite2.png'), (100, 100))
x1, y1 = 15, 200
x2, y2 = 670, 450

timer = time.Clock() # створення таймеру

while True:
    for e in event.get(): # проходження по списку подій (е)
        if e.type == QUIT: # тип полії - закриття вікна
            quit() # зупинення пайгейму
            exit(0) # зупенняє весь код
    #window.fill(BG_COLOR) # запевнення вікна кольром
    window.blit(background, (0, 0)) # відображення картинки
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    keys = key.get_pressed()
    if keys[K_w]:
        y1 -= 5
    if keys[K_s]:
        y1 += 5
    if keys[K_a]:
        x1 -= 5
    if keys[K_d]:
        x1 += 5
    if keys[K_UP]:
        y2 -= 5
    if keys[K_DOWN]:
        y2 += 5
    if keys[K_LEFT]:
        x2 -= 5
    if keys[K_RIGHT]:
        x2 += 5

    display.update() # оновленя
    timer.tick(60) # вказання частоти кадрів