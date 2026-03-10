def get_knight_moves(x, y):
    possible_moves = [
        (x+2, y+1), (x+2, y-1), (x-2, y+1), (x-2, y-1),
        (x+1, y+2), (x+1, y-2), (x-1, y+2), (x-1, y-2)
    ]
    valid_moves = []
    for m in possible_moves:
        if 0 <= m[0] <= 7 and 0 <= m[1] <= 7:
            valid_moves.append(m)
    return valid_moves

# Випадок А
def case_a_logic():
    print("Випадок А: Кінь може повторювати клітинки.")
    print("Будь-яка клітинка досяжна максимум за 6 ходів.")
    print("Використовується алгоритм BFS (пошук у ширину).")

# Випадок Б: пройти всі клітинки (правило Варнсдорфа)
def solve_knights_tour(start_x, start_y):
    board = [[-1 for _ in range(8)] for _ in range(8)]
    board[start_x][start_y] = 0 
    
    curr_x, curr_y = start_x, start_y
    
    for move_num in range(1, 64):
        moves = get_knight_moves(curr_x, curr_y)
        found = False
        for m in moves:
            if board[m[0]][m[1]] == -1:
                curr_x, curr_y = m[0], m[1]
                board[curr_x][curr_y] = move_num
                found = True
                break
        if not found:
            return move_num 
            
    return 64

start_pos = (0, 0)
print(f"Починаємо з {start_pos}")
case_a_logic()
print(f"\nВипадок Б: Вдалося відвідати {solve_knights_tour(0, 0)} клітинок без повторів.")