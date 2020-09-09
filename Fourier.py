import pygame
import math
import os
import random

os.environ['SDL_VIDEO_CENTERED'] = '1'

fps = 60
display_height = 800
display_width = 1200
number = 6
drawing_line = []

colors = []


def main():
    print(colors)
    clock = pygame.time.Clock()
    display = pygame.display.set_mode((display_width, display_height))
    time = 0
    for j in range(number):
        colors.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    while True:
        display.fill([255, 255, 255])

        x = 400
        y = 400
        exit_handler()
        for i in range(number):
            prev_x = x
            prev_y = y
            n = i * 2 + 1
            radius = 150 * (4 / (n * math.pi))
            x += radius * math.cos(n * time)
            y += radius * math.sin(n * time)

            pygame.draw.circle(display, colors[i], (int(prev_x), int(prev_y)), int(radius), 2)

            pygame.draw.line(display, (0, 0, 0), (int(prev_x), int(prev_y)), (int(x), int(y)), 2)

        drawing_line.insert(0, int(y))

        pygame.draw.line(display, (0, 0, 0), (int(x), int(y)), (750, drawing_line[0]), 2)


        curve_x = 750
        curve_y =  drawing_line[0]

        for j in range(len(drawing_line)):
            prev_curve_x = curve_x
            prev_curve_y = curve_y

            curve_x = 750+j
            curve_y = drawing_line[j]

            pygame.draw.line(display, (0, 0, 0), (prev_curve_x, prev_curve_y), (curve_x, curve_y), 2)

        time += 0.01
        pygame.display.update()
        clock.tick(fps)


def exit_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
            
if __name__ == '__main__':
    main()
