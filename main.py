import random

#Variables
piece_active = False
current_piece = 0
main_block_cords = 0
map = 0

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

#Make the map
def make_map():
    global map
    map = [[0] * 10 for _ in range(20)]
    print(map)
make_map()

def assign_piece():
    #Assign piece to the main point
    global current_piece
    current_piece = piece_types[f"{random.randint(1, 7)}"]
    assign_global_coords()

def assign_global_coords():
    print (f"\033[91m{current_piece}\033[91m")
    global main_block_cords
    main_block_cords = {
    "1": [5, 19],
    "2": [5 + current_piece[0][0], 19 + current_piece[0][1]],
    "3": [5 + current_piece[1][0], 19 + current_piece[1][1]],
    "4": [5 + current_piece[2][0], 19 + current_piece[2][1]],
    }
    main_frame_loop()

def check_piece_active():
    if not piece_active:
        assign_piece()

def main_frame_loop():
    user_input = input("Input(a/d): ").lower()
    if user_input == "a":
        choice = -1
    else:
        choice = 1
    for i in range(4):
        main_block_cords[f"{i + 1}"][0] += choice
    for i in range(4):
        main_block_cords[f"{i + 1}"][1] -= 1
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
    main_frame_loop()

def go_back_twin():
    for i in range(4):
        main_block_cords[f"{i + 1}"][1] += 1
    stop_it()

def stop_it():
    for i in range(4):
        map[main_block_cords[f"{i + 1}"][1]][main_block_cords[f"{i + 1}"][0]] = 1
    map_printing()
    check_piece_active()
def map_printing():
    for i in range(20):
        print(f"\033[92m{map[19 - i]}\033[92m")
check_piece_active()