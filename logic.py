'''
- messages
- array con 4 filas
- agregar un 2 de forma aleatoria
- movimientos
- condicional si se acaba el juego o no
'''
import random
def start_game():
    mat = []

    for i in range(4):
        mat.append([0] * 4)

    print("Commands are as follows : ")  
    print("'W' or 'w' : Move Up")  
    print("'S' or 's' : Move Down")  
    print("'A' or 'a' : Move Left")  
    print("'D' or 'd' : Move Right")

    add_new_2(mat)
    add_new_2(mat)

    print_matrix(mat)

    return mat

def print_matrix(matrix):
    for i in matrix:
        print(i)

def add_new_2(game_matrix):
    while True:
        random_row = random.randint(0,3)
        random_index = random.randint(0,3)
        if game_matrix[random_row][random_index] == 0:
            game_matrix[random_row][random_index] = 2
            break

def compress(matrix):
    for row in matrix:
        number_row_zero = row.count(0)
        for index in range(number_row_zero):
            row.remove(0)
        row += [0] * number_row_zero
    return matrix

def merge(matrix):
    changed = False  
    for i in range(4):  
        for j in range(3):  
            if matrix[i][j] == matrix[i][j + 1] and matrix[i][j] != 0:  
                matrix[i][j] *= 2  
                matrix[i][j + 1] = 0  
                changed = True  
    return matrix, changed

def move_left(matrix):
    mat_copy = [row.copy() for row in matrix]
    compress_matrix = compress(mat_copy)
    merge_matrix, changed = merge(compress_matrix)
    if changed:
        compress(merge_matrix)
    return merge_matrix, changed

def move_right(matrix):
    matrix_reverse = reverse(matrix)
    compress_matrix = compress(matrix_reverse)
    merge_matrix, changed = merge(compress_matrix)
    if changed:
        compress(merge_matrix)
    return reverse(merge_matrix), changed

def move_up(matrix):
    matrix_transpose = transpose(matrix)
    compress_matrix = compress(matrix_transpose)
    merge_matrix, changed = merge(compress_matrix)
    if changed:
        compress(merge_matrix)
    return transpose(merge_matrix), changed

def move_down(matrix):
    matrix_transpose = transpose(matrix)
    matrix_reverse = reverse(matrix_transpose)
    compress_matrix = compress(matrix_reverse)
    merge_matrix, changed = merge(compress_matrix)
    if changed:
        compress(merge_matrix)
    merge_matrix_reverse = reverse(merge_matrix)
    return transpose(merge_matrix_reverse), changed

def transpose(matrix):
    return [[matrix[j][i] for j in range(4)] for i in range(4)]

def reverse(matrix):
    return [row[::-1] for row in matrix]

def game_status(matrix):
    changed = []
    is_zero_in_row = []
    func_list = (move_left,move_right, move_up, move_down)
    
    for row in matrix:
        if 0 not in row:
            is_zero_in_row.append(False)
        else: 
            is_zero_in_row.append(True)

    if True not in is_zero_in_row:
        for i in range(4):
            mat_copy = [row.copy() for row in matrix]
            merge_matrix, is_matrix_changed = func_list[i](mat_copy)
            changed.append(is_matrix_changed)
        if True not in changed:
            return "GAME OVER"
        else: 
            return "GAME NOT OVER"

if __name__ == '__main__':
    start_game()