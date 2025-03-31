from colorama import Fore, init
init()

baner = r'''
 ____  __   __ _____  _   _   ___   _   _   _         _     _______   __  ____    ____  ____   ___  ____   _____
|  _ \ \ \ / /|_   _|| | | | / _ \ | \ | | | |       / \   |__  /\ \ / / / ___|  / ___||  _ \ |_ _||  _ \ |_   _|
| |_) | \ V /   | |  | |_| || | | ||  \| | | |      / _ \    / /  \ V /  \___ \ | |    | |_) | | | | |_) |  | |
|  __/   | |    | |  |  _  || |_| || |\  | | |___  / ___ \  / /_   | |    ___) || |___ |  _ <  | | |  __/   | |
|_|      |_|    |_|  |_| |_| \___/ |_| \_| |_____|/_/   \_\/____|  |_|   |____/  \____||_| \_\|___||_|      |_|

'''

function = r'''
1. Часы консольные
2. Змейка
3. 
'''

print(Fore.RED + baner)
print(Fore.CYAN + 'HELLO YOU DONT PROGRAMER PYTHON?')
print(Fore.GREEN + function)

a = input('>>> ')

if a == '1':
    with open('main1.py', 'w') as f:
        f.write('''# -*- coding: utf-8 -*-
# _____  _   _  ___  ____     ____   ___   ____   _____   __  __     _     ____   _____   ___  _   _   ____   _      ____
#|_   _|| | | ||_ _|/ ___|   / ___| / _ \ |  _ \ | ____| |  \/  |   / \   |  _ \ | ____| |_ _|| \ | | |  _ \ | |    / ___|
#  | |  | |_| | | | \___ \  | |    | | | || | | ||  _|   | |\/| |  / _ \  | | | ||  _|    | | |  \| | | |_) || |    \___ \
#  | |  |  _  | | |  ___) | | |___ | |_| || |_| || |___  | |  | | / ___ \ | |_| || |___   | | | |\  | |  __/ | |___  ___) |
#  |_|  |_| |_||___||____/   \____| \___/ |____/ |_____| |_|  |_|/_/   \_\|____/ |_____| |___||_| \_| |_|    |_____||____/
#
#
# ____   _      ____       ____  __   __ _____  _   _   ___   _   _         _         _     _______   __        ____    ____  ____   ___  ____   _____
#|  _ \ | |    / ___|  _  |  _ \ \ \ / /|_   _|| | | | / _ \ | \ | |       | |       / \   |__  /\ \ / /       / ___|  / ___||  _ \ |_ _||  _ \ |_   _|
#| |_) || |    \___ \ (_) | |_) | \ V /   | |  | |_| || | | ||  \| |       | |      / _ \    / /  \ V /        \___ \ | |    | |_) | | | | |_) |  | |
#|  __/ | |___  ___) | _  |  __/   | |    | |  |  _  || |_| || |\  |       | |___  / ___ \  / /_   | |          ___) || |___ |  _ <  | | |  __/   | |
#|_|    |_____||____/ (_) |_|      |_|    |_|  |_| |_| \___/ |_| \_| _____ |_____|/_/   \_\/____|  |_|   _____ |____/  \____||_| \_\|___||_|      |_|
#                                                                   |_____|                             |_____|
#Код был напечатан python lazy script что я называю PLS автор: Марлен.
#The code was printed in Python as a lazy script that I call PLS. Author: Marlen.

import time
from datetime import datetime
def get_ascii_digit(digit):
    digits = {
        '0': [" 000 ", "0   0", "0   0", "0   0", " 000 "],
        '1': ["  1  ", " 11  ", "  1  ", "  1  ", " 111 "],
        '2': [" 222 ", "2   2", "  2  ", " 2   ", "22222"],
        '3': [" 333 ", "    3", " 333 ", "    3", " 333 "],
        '4': ["   4 ", "  44 ", " 4 4 ", "44444", "   4 "],
        '5': ["55555", "5    ", " 555 ", "    5", "5555 "],
        '6': [" 666 ", "6    ", "6666 ", "6   6", " 666 "],
        '7': ["77777", "   7 ", "  7  ", " 7   ", "7    "],
        '8': [" 888 ", "8   8", " 888 ", "8   8", " 888 "],
        '9': [" 999 ", "9   9", " 9999", "    9", " 999 "],
        ':': ["   ", " # ", "   ", " # ", "   "],
    }
    return digits[digit]

def display_time():
    while True:
        now = datetime.now().strftime("%H:%M:%S")
        lines = ["" for _ in range(5)]
        for char in now:
            ascii_char = get_ascii_digit(char)
            for i in range(5):
                lines[i] += ascii_char[i] + "  "

        print("\033[H\033[J", end="")

        for line in lines:
            print(line)

        time.sleep(1)

display_time()
''')

elif a == '2':
    with open('main2', 'w') as f:
        f.write('''# -*- coding: utf-8 -*-
# _____  _   _  ___  ____     ____   ___   ____   _____   __  __     _     ____   _____   ___  _   _   ____   _      ____
#|_   _|| | | ||_ _|/ ___|   / ___| / _ \ |  _ \ | ____| |  \/  |   / \   |  _ \ | ____| |_ _|| \ | | |  _ \ | |    / ___|
#  | |  | |_| | | | \___ \  | |    | | | || | | ||  _|   | |\/| |  / _ \  | | | ||  _|    | | |  \| | | |_) || |    \___ \
#  | |  |  _  | | |  ___) | | |___ | |_| || |_| || |___  | |  | | / ___ \ | |_| || |___   | | | |\  | |  __/ | |___  ___) |
#  |_|  |_| |_||___||____/   \____| \___/ |____/ |_____| |_|  |_|/_/   \_\|____/ |_____| |___||_| \_| |_|    |_____||____/
#
#
# ____   _      ____       ____  __   __ _____  _   _   ___   _   _         _         _     _______   __        ____    ____  ____   ___  ____   _____
#|  _ \ | |    / ___|  _  |  _ \ \ \ / /|_   _|| | | | / _ \ | \ | |       | |       / \   |__  /\ \ / /       / ___|  / ___||  _ \ |_ _||  _ \ |_   _|
#| |_) || |    \___ \ (_) | |_) | \ V /   | |  | |_| || | | ||  \| |       | |      / _ \    / /  \ V /        \___ \ | |    | |_) | | | | |_) |  | |
#|  __/ | |___  ___) | _  |  __/   | |    | |  |  _  || |_| || |\  |       | |___  / ___ \  / /_   | |          ___) || |___ |  _ <  | | |  __/   | |
#|_|    |_____||____/ (_) |_|      |_|    |_|  |_| |_| \___/ |_| \_| _____ |_____|/_/   \_\/____|  |_|   _____ |____/  \____||_| \_\|___||_|      |_|
#                                                                   |_____|                             |_____|
#Код был напечатан python lazy script что я называю PLS автор: Марлен.
#The code was printed in Python as a lazy script that I call PLS. Author: Marlen.
import pygame
import time
import random

pygame.init()

# Определяем цвета
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Устанавливаем размеры экрана
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Змейка на Python')

# Устанавливаем скорость игры
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

# Шрифты
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Функции для работы с текстом
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():  # Главная функция игры
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            dis.fill(blue)
            message("Ты проиграл! Нажми Q-выход или C-играть заново", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, yellow, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
''')