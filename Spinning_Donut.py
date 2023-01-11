import pygame
import math


pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)


WIDTH = 1920
HEIGHT = 1080
X_start, Y_start = 0, 0

x_seperator = 10
y_seperator = 20

rows = HEIGHT // y_seperator
columns = WIDTH // x_seperator
screen_size = rows * columns

# positioning the doughnut in the middle
x_offset = columns / 2
y_offset = rows / 2

# rotation animation
A, B = 0, 0

theta_spacing = 10
phi_spacing = 1

# Used in the animation to  show shades (smallest ==  darkest, largest == brightest)
characters = ".,-~:;=!*#$@"
screen = pygame.display.set_mode((WIDTH, HEIGHT))

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DOUGHNUT")
font = pygame.font.SysFont("Arial", 18, bold=True)


def text_display(letter, x_start, y_start):
    text = font.render(str(letter), True, white)
    display_surface.blit(text, (x_start, y_start))


run = True
while run:

    screen.fill((black))

    doughnut_fill = [0] * screen_size
    background_fill = [' '] * screen_size  # Fills empty space

    for j in range(0, 628, theta_spacing):
        for i in range(0, 628, phi_spacing):
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(x_offset + 40 * D * (l * h * m - t * n))  # 3D x coordinate after rotation
            y = int(y_offset + 20 * D * (l * h * n + t * m))  # 3D y coordinate after rotation
            o = int(x + columns * y)
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if rows > y and y > 0 and x > 0 and columns > x and D > doughnut_fill[o]:
                doughnut_fill[o] = D
                background_fill[o] = characters[N if N > 0 else 0]

    if Y_start == (rows * y_seperator) - y_seperator:
        Y_start = 0

    # resets image and redraws
    for i in range(len(background_fill)):
        A += 0.00004
        B += 0.00002
        if i == 0 or i % columns:
            text_display(background_fill[i], X_start, Y_start)
            X_start += x_seperator

        else:
            Y_start += y_seperator
            X_start = 0
            text_display(background_fill[i], X_start, Y_start)
            X_start += x_seperator

    pygame.display.update()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
