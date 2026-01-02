# Snake Game using terminal

# Import statements
import sys
import time
import random
from operator import index

import readchar
import threading

apple_cords = []
exists_apple = 0
apple_x = 0
apple_y = 0
apple_has_been_eaten = 0
direction = 0

def input_handling():
    global direction
    while True:
        key = readchar.readkey()
        if key == "w" or "s" or "a" or "d":
            direction = key
        time.sleep(0.1)

# Create main 15x17 gamegrid
def create_grid():
    global map_grid
    map_grid = [['□'] * 17 for _ in range(15)]

# Define initial snake
def create_snake():
    global snake_cords
    snake_cords = [[8, 7]]

def print_grid():
    global apple_cords
    global map_grid
    global snake_cords
    for i in snake_cords:
        map_grid[i[1]][i[0]] = "*"
    map_grid[apple_cords[1]][apple_cords[0]] = "$"
    sys.stdout.write("\033[H")
    for i in map_grid:
        print(i)
    for i in map_grid:
        for j in range(17):
            i[j] = "□"

def move_snake():
    global snake_cords
    global apple_has_been_eaten
    index = 1
    if apple_has_been_eaten:
        snake_tail = snake_cords[len(snake_cords) - 1].copy()
    if direction == "w":
        for i in snake_cords:
            if index == len(snake_cords):
                snake_cords[0][1] -= 1
                break
            snake_cords[len(snake_cords) - index][0] = snake_cords[len(snake_cords) - index - 1][0]
            snake_cords[len(snake_cords) - index][1] = snake_cords[len(snake_cords) - index - 1][1]
            index += 1
    elif direction == "s":
        for i in snake_cords:
            if index == len(snake_cords):
                snake_cords[0][1] += 1
                break
            snake_cords[len(snake_cords) - index][0] = snake_cords[len(snake_cords) - index - 1][0]
            snake_cords[len(snake_cords) - index][1] = snake_cords[len(snake_cords) - index - 1][1]
            index += 1
    elif direction == "d":
        for i in snake_cords:
            if index == len(snake_cords):
                snake_cords[0][0] += 1
                break
            snake_cords[len(snake_cords) - index][0] = snake_cords[len(snake_cords) - index - 1][0]
            snake_cords[len(snake_cords) - index][1] = snake_cords[len(snake_cords) - index - 1][1]
            index += 1
    elif direction == "a":
        for i in snake_cords:
            if index == len(snake_cords):
                snake_cords[0][0] -= 1
                break
            snake_cords[len(snake_cords) - index][0] = snake_cords[len(snake_cords) - index - 1][0]
            snake_cords[len(snake_cords) - index][1] = snake_cords[len(snake_cords) - index - 1][1]

            index += 1
    if apple_has_been_eaten:
        snake_cords.append(snake_tail)
        apple_has_been_eaten = 0
    for i in snake_cords:
        if i[1] > 14:
            end_game()
        elif i[1] < 0:
            end_game()
        elif i[0] < 0:
            end_game()
        elif i[0] > 16:
            end_game()
def create_apple():
    global apple_cords
    global snake_cords
    apple_cords = []
    apple_true = 0
    while apple_true == 0:
        apple_true = 1
        apple_x = random.randint(0, 16)
        apple_y = random.randint(0, 14)
        for i in snake_cords:
            if i[0] == apple_x:
                if i[1] == apple_y:
                    apple_true = 0
    apple_cords.append(apple_x)
    apple_cords.append(apple_y)

def apple_eaten_check():
    global snake_cords
    global exists_apple
    global apple_cords
    global apple_has_been_eaten
    if snake_cords[0][0] == apple_cords[0]:
        if snake_cords[0][1] == apple_cords[1]:
            exists_apple = 0
            apple_cords = []
            apple_has_been_eaten = 1

def self_collision_check():
    global snake_cords
    for i in snake_cords:
        count = 0
        for j in snake_cords:
            if i == j:
                count += 1
            if count == 2:
                end_game()

def end_game():
    print("You Lost!")
    time.sleep(1)
    quit()

# Setup
create_grid()
create_snake()
create_apple()

thread0 = threading.Thread(target=input_handling)
thread0.daemon = True
thread0.start()

while True:
    time.sleep(1)
    move_snake()
    apple_eaten_check()
    if exists_apple == 0:
        exists_apple = 1
        create_apple()
    self_collision_check()
    print_grid()