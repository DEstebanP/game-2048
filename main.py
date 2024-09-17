import logic

def run_game():
    mat = logic.start_game()
    moves = ["A", "D", "W", "S"]
    while True:
        while True:
            move = input("Press the command: ").upper()
            if move not in moves:
                print("TRY AGAIN, THE MOVE IS NOT CORRECT")
            else:
                break    
        if move == "A":
            matrix, changed = logic.move_left(mat)
        elif move == "D":
            matrix, changed = logic.move_right(mat)
        elif move == "W":
            matrix, changed = logic.move_up(mat)
        elif move == "S":
            matrix, changed = logic.move_down(mat)
        if mat != matrix:
            mat = matrix
            logic.add_new_2(mat)

        is_over = logic.game_status(mat)
        if is_over == "GAME OVER":
            print(is_over)
            logic.print_matrix(mat)
            break
        else:
            logic.print_matrix(mat)

if __name__ == "__main__":
    run_game()
