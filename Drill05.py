from pico2d import *\

import random
import math

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
hand_arrow = load_image('hand_arrow.png')
character = load_image('run_animation.png')




running = True
x = 640
y = 512
cursor_x = 300
cursor_y = 300
dirX = 0
dirY = 0
frame = 0
time_count = 0
look = 1

while running:
    clear_canvas()

    lenth = math.sqrt((cursor_x - x) ** 2)+math.sqrt((cursor_y - y) ** 2)
    x_dist = (cursor_x - x) / lenth
    y_dist = (cursor_y - y) / lenth

    x += x_dist * 20
    y += y_dist * 20

    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    if(cursor_x > x):
        character.clip_draw(frame * 100, 0, 100, 102, x, y, 100, 100)
    elif (cursor_x < x):
        character.clip_composite_draw(frame * 100, 0, 100, 102, 0, 'h', x, y, 100, 100)

    hand_arrow.draw_now(cursor_x, cursor_y)

    update_canvas()
    frame = (frame + 100) % 8
    time_count += 1
    if(x > cursor_x - 50 and x < cursor_x + 50 and y > cursor_y - 50 and y < cursor_y + 50):
        cursor_x = random.randint(100, 1100)
        cursor_y = random.randint(100, 1000)

    delay(0.08)

close_canvas()