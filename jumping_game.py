import pygame
import gamebox
import random
camera = gamebox.Camera(800, 500)

dino = gamebox.from_color(100, 350, 'white', 40, 60)
platform = gamebox.from_color(0, 396, "black", 2000, 30)
# platform.right = camera.right

# cactus_one = gamebox.from_color(600, 355, "red", 30, 50)
# cactus_two = gamebox.from_color(500, 350, "dark red", 35, 60)
cactus = [
    gamebox.from_color(500, 350, "dark red", 35, 60),
    gamebox.from_color(600, 355, "red", 30, 50)
]
# camera_speed = 3
# game_on = False
# score = 0
# dino.speed_x = 1
# dino.speed_y = 1
# gravity = .1
# time = 0

# def general(keys):
#     camera.clear("dim grey")
#     camera.draw(dino)
#     camera.draw(platform)
#
#     camera.draw(cactus_one)
#     camera.draw(cactus_two)
#
#     camera.display()

# def cactus(keys):

#     camera.draw(cactus_one)
#     camera.draw(cactus_two)
counter = 0
def tick(keys):
    global counter
    camera.clear("dim grey")
    dino.speedy += 2

    # Dino's jump and camera movement

    if dino.bottom_touches(platform):  # taken from ground_jumping.py example
        dino.speedy = 0
        if pygame.K_SPACE in keys:
            dino.speedy = -20
            dino.speedx = 5
            platform.speedx = 5

    dino.move_speed()
    platform.move_speed()

    dino.move_to_stop_overlapping(platform)  # taken from ground_jumping.py example

    camera.x += 5

    # ---------cactus and new cactus

    counter += 1
    if counter % 50 == 0:
        new_cactus = gamebox.from_color(random.randint(600, 500),random.randint(355, 350), "black", random.randint(35, 30), 10)
        cactus.append(new_cactus)
        # gamebox.from_color(500, 350, "dark red", 35, 60),
        # gamebox.from_color(600, 355, "red", 30, 50)

    for cacti in cactus:
        if dino.bottom_touches(cactus):
            dino.yspeed = 0
            # if pygame.K_UP in keys or pygame.K_SPACE in keys:
            #     character.yspeed = -20
        if dino.touches(cactus):
            dino.move_to_stop_overlapping(cactus)
        camera.draw(cacti)



    camera.draw(dino)
    camera.draw(platform)
    camera.draw(cactus)
    camera.display()

gamebox.timer_loop(60, tick)
