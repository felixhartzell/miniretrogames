import random
import sys
import readchar
import threading
import time

#Variables
piece_active = False
current_piece = 0
main_block_cords = 0
map = 0
user_input = 0

#Define piece types and their block positions
#1 = T piece
#2 = I piece
#3 = L piece
#4 = Mirrored L piece
#5 = Block Piece
#6 = S piece
#7 = Mirrored S piece
piece_types = {
    "1": [(-1, 0), (0, 1), (1, 0)],
    "2": [(0, 1), (0, -1), (0, -2)],
    "3": [(0, 1), (1, 0), (2, 0)],
    "4": [(0, 1), (-1, 0), (-2, 0)],
    "5": [(1, 0), (0, 1), (1, 1)],
    "6": [(0, -1), (1, 0), (1, 1)],
    "7": [(0, -1), (-1, 0), (-1, 1)]
}

def input_handler():
    global user_input
    while True:
        character = readchar.readkey()
        if character == "a":
            user_input = "a"
        elif character == "d":
            user_input = "d"
        else:
            user_input = "0"
        time.sleep(0.2)

input_thread = threading.Thread(target=input_handler, daemon=True)
input_thread.start()

#Make the map
def make_map():
    global map
    map = [[0] * 10 for _ in range(20)]
make_map()

def assign_piece():
    #Assign piece to the main point
    global current_piece
    global piece_active
    current_piece = piece_types[f"{random.randint(1, 7)}"]
    piece_active = True
    assign_global_coords()

def assign_global_coords():
    global main_block_cords
    main_block_cords = {
    "1": [5, 18],
    "2": [5 + current_piece[0][0], 18 + current_piece[0][1]],
    "3": [5 + current_piece[1][0], 18 + current_piece[1][1]],
    "4": [5 + current_piece[2][0], 18 + current_piece[2][1]],
    }
    main_frame_loop()

def check_piece_active():
    if not piece_active:
        assign_piece()
    else:
        main_frame_loop()

def main_frame_loop():
    global map
    global user_input
    for i in range(4):
        map[main_block_cords[f"{i + 1}"][1]][main_block_cords[f"{i + 1}"][0]] = 1
    sys.stdout.write("\033[H")
    for i in range(20):
        print(f"\033[92m{map[19 - i]}\033[92m")
    for i in range(4):
        map[main_block_cords[f"{i + 1}"][1]][main_block_cords[f"{i + 1}"][0]] = 0
    if user_input == "a":
        choice = -1
    elif user_input == "d":
        choice = 1
    else:
        choice = 0
    user_input = 0
    for k in range(4):
        main_block_cords[f"{k + 1}"][0] += choice
        main_block_cords[f"{k + 1}"][1] -= 1
    for f in range(20):
        for i in range(10):
            checking = map[f][i]
            if checking == 1:
                for t in range(4):
                    if main_block_cords[f"{t + 1}"][0] == i:
                        if main_block_cords[f"{t + 1}"][1] == f:
                            go_back_twin()
    for j in range(4):
        if main_block_cords[f"{j + 1}"][1] == 0:
            stop_it()
    time.sleep(0.5)

def go_back_twin():
    global main_block_cords
    for i in range(4):
        main_block_cords[f"{i + 1}"][1] += 1
    stop_it()

def stop_it():
    global map
    global piece_active
    for i in range(4):
        map[main_block_cords[f"{i + 1}"][1]][main_block_cords[f"{i + 1}"][0]] = 1
    piece_active = False
    check_piece_active()
while True:
    check_piece_active()