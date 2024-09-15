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

    for i in mat:
        print(i)

    return mat

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
    compress_matrix = compress(matrix)
    merge_matrix, changed = merge(compress_matrix)
    if changed:
        compress(merge_matrix)
    return merge_matrix

def move_right(matrix):
    matrix_reverse = [row[::-1] for row in matrix]
    compress_matrix = compress(matrix_reverse)
    merge_matrix, changed = merge(compress_matrix)
    if changed:
        compress(merge_matrix)
    return [row[::-1] for row in merge_matrix]

def move_up(matrix):
    matrix_transpose = [[matrix[j][i] for j in range(4)] for i in range(4)]
    compress_matrix = compress(matrix_transpose)
    merge_matrix, changed = merge(compress_matrix)
    if changed:
        compress(merge_matrix)
    return [[merge_matrix[j][i] for j in range(4)] for i in range(4)]

def move_down(matrix):
    matrix_transpose = [[matrix[j][i] for j in range(4)] for i in range(4)]
    matrix_reverse = [row[::-1] for row in matrix_transpose]
    compress_matrix = compress(matrix_reverse)
    merge_matrix, changed = merge(compress_matrix)
    if changed:
        compress(merge_matrix)
    merge_matrix_reverse = [row[::-1] for row in merge_matrix]
    return [[merge_matrix_reverse[j][i] for j in range(4)] for i in range(4)]

if __name__ == '__main__':
    matrix=[[2,2,0,8], 
            [2,2,2,2], 
            [2,2,4,0], 
            [2,0,8,0]]
    print(move_down(matrix))