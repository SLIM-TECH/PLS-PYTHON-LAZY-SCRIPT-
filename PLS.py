from colorama import Fore, init
import os

init()

banner = r'''
 ____  __   __ _____  _   _   ___   _   _   _         _     _______   __  ____    ____  ____   ___  ____   _____
|  _ \ \ \ / /|_   _|| | | | / _ \ | \ | | | |       / \   |__  /\ \ / / / ___|  / ___||  _ \ |_ _||  _ \ |_   _|
| |_) | \ V /   | |  | |_| || | | ||  \| | | |      / _ \    / /  \ V /  \___ \ | |    | |_) | | | | |_) |  | |
|  __/   | |    | |  |  _  || |_| || |\  | | |___  / ___ \  / /_   | |    ___) || |___ |  _ <  | | |  __/   | |
|_|      |_|    |_|  |_| |_| \___/ |_| \_| |_____|/_/   \_\/____|  |_|   |____/  \____||_| \_\|___||_|      |_|
'''

functions = r'''
1. Часы консольные
2. Змейка
3. Игра 2048
4. Генератор паролей
5. Калькулятор
6. Викторина
'''

print(Fore.RED + banner)
print(Fore.CYAN + 'HELLO YOU DONT PROGRAMER PYTHON?')
print(Fore.GREEN + functions)

a = input('>>> ')

if a == '1':
    with open('clock.py', 'w', encoding='utf-8') as f:
        f.write('''
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
    return digits.get(digit, ["     "] * 5)

def display_time():
    while True:
        try:
            now = datetime.now().strftime("%H:%M:%S")
            lines = ["" for _ in range(5)]
            for char in now:
                ascii_char = get_ascii_digit(char)
                for i in range(5):
                    lines[i] += ascii_char[i] + "  "

            print("\\033[H\\033[J", end="")
            for line in lines:
                print(line.center(50))

            time.sleep(1)
        except KeyboardInterrupt:
            print("\\nЧасы остановлены")
            break

if __name__ == "__main__":
    display_time()
''')
    print(Fore.GREEN + "Файл clock.py создан!")

elif a == '2':
    with open('snake.py', 'w', encoding='utf-8') as f:
        f.write('''
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

def game_loop():
    pygame.init()
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)

    dis_width = 600
    dis_height = 400
    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Змейка')

    clock = pygame.time.Clock()
    snake_block = 10
    snake_speed = 15

    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont("comicsansms", 35)

    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block)

    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 6, dis_height / 3])

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
                        game_loop()

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

if __name__ == "__main__":
    game_loop()
''')
    print(Fore.GREEN + "Файл snake.py создан!")

elif a == '3':
    with open('game2048.py', 'w', encoding='utf-8') as f:
        f.write('''
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
import random
import sys

def main():
    SIZE = 4
    TILE_SIZE = 100
    GAP = 10
    WIDTH = SIZE * (TILE_SIZE + GAP) + GAP
    HEIGHT = WIDTH + 50  # Extra space for score
    
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("2048")
    
    FONT = pygame.font.Font(None, 60)
    SMALL_FONT = pygame.font.Font(None, 36)
    BACKGROUND_COLOR = (187, 173, 160)
    TEXT_COLOR = (119, 110, 101)
    
    TILE_COLORS = {
        0: (205, 193, 180),
        2: (238, 228, 218),
        4: (237, 224, 200),
        8: (242, 177, 121),
        16: (245, 149, 99),
        32: (246, 124, 95),
        64: (246, 94, 59),
        128: (237, 207, 114),
        256: (237, 204, 97),
        512: (237, 200, 80),
        1024: (237, 197, 63),
        2048: (237, 194, 46)
    }

    def new_game():
        board = [[0] * SIZE for _ in range(SIZE)]
        add_random_tile(board)
        add_random_tile(board)
        return board, 0

    def add_random_tile(board):
        empty_cells = [(r, c) for r in range(SIZE) for c in range(SIZE) if board[r][c] == 0]
        if empty_cells:
            r, c = random.choice(empty_cells)
            board[r][c] = 2 if random.random() < 0.9 else 4

    def draw_board(board, score):
        screen.fill(BACKGROUND_COLOR)
        
        # Draw score
        score_text = SMALL_FONT.render(f"Score: {score}", True, TEXT_COLOR)
        screen.blit(score_text, (20, 10))
        
        # Draw tiles
        for row in range(SIZE):
            for col in range(SIZE):
                value = board[row][col]
                color = TILE_COLORS.get(value, (60, 58, 50))
                rect = pygame.Rect(
                    col * (TILE_SIZE + GAP) + GAP,
                    row * (TILE_SIZE + GAP) + GAP + 50,  # Offset for score
                    TILE_SIZE, TILE_SIZE
                )
                pygame.draw.rect(screen, color, rect, border_radius=5)
                if value:
                    text = FONT.render(str(value), True, (0, 0, 0) if value < 8 else (255, 255, 255))
                    text_rect = text.get_rect(center=rect.center)
                    screen.blit(text, text_rect)

    def move(board, direction):
        new_board = [row.copy() for row in board]
        moved = False
        score = 0
        
        if direction == "left":
            for row in new_board:
                for i in range(SIZE - 1):
                    for j in range(i + 1, SIZE):
                        if row[i] == 0 and row[j] != 0:
                            row[i], row[j] = row[j], row[i]
                            moved = True
                        elif row[i] != 0 and row[i] == row[j]:
                            row[i] *= 2
                            row[j] = 0
                            score += row[i]
                            moved = True
                            break
        elif direction == "right":
            for row in new_board:
                row.reverse()
                for i in range(SIZE - 1):
                    for j in range(i + 1, SIZE):
                        if row[i] == 0 and row[j] != 0:
                            row[i], row[j] = row[j], row[i]
                            moved = True
                        elif row[i] != 0 and row[i] == row[j]:
                            row[i] *= 2
                            row[j] = 0
                            score += row[i]
                            moved = True
                            break
                row.reverse()
        elif direction == "up":
            for col in range(SIZE):
                column = [new_board[row][col] for row in range(SIZE)]
                for i in range(SIZE - 1):
                    for j in range(i + 1, SIZE):
                        if column[i] == 0 and column[j] != 0:
                            column[i], column[j] = column[j], column[i]
                            moved = True
                        elif column[i] != 0 and column[i] == column[j]:
                            column[i] *= 2
                            column[j] = 0
                            score += column[i]
                            moved = True
                            break
                for row in range(SIZE):
                    new_board[row][col] = column[row]
        elif direction == "down":
            for col in range(SIZE):
                column = [new_board[row][col] for row in range(SIZE)]
                column.reverse()
                for i in range(SIZE - 1):
                    for j in range(i + 1, SIZE):
                        if column[i] == 0 and column[j] != 0:
                            column[i], column[j] = column[j], column[i]
                            moved = True
                        elif column[i] != 0 and column[i] == column[j]:
                            column[i] *= 2
                            column[j] = 0
                            score += column[i]
                            moved = True
                            break
                column.reverse()
                for row in range(SIZE):
                    new_board[row][col] = column[row]
        
        return new_board, moved, score

    def is_game_over(board):
        for row in board:
            if 0 in row:
                return False
        for row in board:
            for i in range(SIZE - 1):
                if row[i] == row[i + 1]:
                    return False
        for col in range(SIZE):
            for row in range(SIZE - 1):
                if board[row][col] == board[row + 1][col]:
                    return False
        return True

    board, score = new_game()
    running = True
    
    while running:
        draw_board(board, score)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                moved = False
                if event.key == pygame.K_LEFT:
                    board, moved, delta_score = move(board, "left")
                elif event.key == pygame.K_RIGHT:
                    board, moved, delta_score = move(board, "right")
                elif event.key == pygame.K_UP:
                    board, moved, delta_score = move(board, "up")
                elif event.key == pygame.K_DOWN:
                    board, moved, delta_score = move(board, "down")
                elif event.key == pygame.K_n:
                    board, score = new_game()
                    continue
                elif event.key == pygame.K_q:
                    running = False
                
                if moved:
                    score += delta_score
                    add_random_tile(board)
                    if is_game_over(board):
                        draw_board(board, score)
                        font = pygame.font.Font(None, 48)
                        text = font.render("Game Over! Press N for new game", True, (255, 0, 0))
                        text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
                        screen.blit(text, text_rect)
                        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
''')
    print(Fore.GREEN + "Файл game2048.py создан!")

elif a == '4':
    with open('password_generator.py', 'w', encoding='utf-8') as f:
        f.write('''
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
import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation
    
    while True:
        password = ''.join(random.choice(chars) for _ in range(length))
        if (any(c.islower() for c in password) and \
           (any(c.isupper() for c in password) and \
           (not use_digits or any(c.isdigit() for c in password)) and \
           (not use_special_chars or any(c in string.punctuation for c in password)):
            return password

def main():
    print("Генератор паролей")
    try:
        length = int(input("Длина пароля (8-32): "))
        length = max(8, min(32, length))
        use_digits = input("Использовать цифры? (y/n): ").lower() == 'y'
        use_special = input("Использовать спецсимволы? (y/n): ").lower() == 'y'
        
        count = int(input("Сколько паролей сгенерировать? (1-20): "))
        count = max(1, min(20, count))
        
        print("\\nСгенерированные пароли:")
        for _ in range(count):
            print(generate_password(length, use_digits, use_special))
    except ValueError:
        print("Ошибка: введите корректные числа")

if __name__ == "__main__":
    main()
''')
    print(Fore.GREEN + "Файл password_generator.py создан!")

elif a == '5':
    with open('calculator.py', 'w', encoding='utf-8') as f:
        f.write('''
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
def calculate():
    print("Калькулятор")
    print("Доступные операции: +, -, *, /, ^ (степень), % (остаток)")
    
    while True:
        try:
            num1 = float(input("Первое число: "))
            operator = input("Оператор: ")
            num2 = float(input("Второе число: "))
            
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Ошибка: деление на ноль!")
                    continue
                result = num1 / num2
            elif operator == '^':
                result = num1 ** num2
            elif operator == '%':
                result = num1 % num2
            else:
                print("Неизвестный оператор")
                continue
            
            print(f"Результат: {result}")
            
            if input("Продолжить? (y/n): ").lower() != 'y':
                break
        except ValueError:
            print("Ошибка: введите числа корректно")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    calculate()
''')
    print(Fore.GREEN + "Файл calculator.py создан!")

elif a == '6':
    with open('quiz.py', 'w', encoding='utf-8') as f:
        f.write('''
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
import random

questions = [
    {
        "question": "Какая столица Франции?",
        "options": ["Лондон", "Берлин", "Париж", "Мадрид"],
        "answer": 2
    },
    {
        "question": "Сколько планет в Солнечной системе?",
        "options": ["7", "8", "9", "10"],
        "answer": 1
    },
    {
        "question": "Кто написал 'Войну и мир'?",
        "options": ["Достоевский", "Толстой", "Чехов", "Тургенев"],
        "answer": 1
    },
    {
        "question": "Какое самое глубокое озеро в мире?",
        "options": ["Виктория", "Байкал", "Каспийское", "Танганьика"],
        "answer": 1
    },
    {
        "question": "В каком году человек впервые полетел в космос?",
        "options": ["1957", "1961", "1969", "1975"],
        "answer": 1
    }
]

def run_quiz():
    random.shuffle(questions)
    score = 0
    
    print("Викторина! Ответьте на 5 вопросов.")
    
    for i, q in enumerate(questions[:5], 1):
        print(f"\\nВопрос {i}: {q['question']}")
        for j, option in enumerate(q['options'], 1):
            print(f"{j}. {option}")
        
        while True:
            try:
                user_answer = int(input("Ваш ответ (1-4): "))
                if 1 <= user_answer <= 4:
                    break
                print("Введите число от 1 до 4")
            except ValueError:
                print("Введите число!")
        
        if user_answer - 1 == q['answer']:
            print("Правильно!")
            score += 1
        else:
            print(f"Неправильно! Правильный ответ: {q['options'][q['answer']]}")
    
    print(f"\\nВаш результат: {score}/5 ({score * 20}%)")
    if score == 5:
        print("Отлично! Вы знаток!")
    elif score >= 3:
        print("Хороший результат!")
    else:
        print("Попробуйте ещё раз!")

if __name__ == "__main__":
    run_quiz()
''')
    print(Fore.GREEN + "Файл quiz.py создан!")

else:
    print(Fore.RED + "Неверный выбор. Попробуйте снова.")