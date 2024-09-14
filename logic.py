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
    print(matrix)
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

if __name__ == '__main__':
    matrix=start_game()
    merge_matrix=compress(matrix)
    merge(merge_matrix)