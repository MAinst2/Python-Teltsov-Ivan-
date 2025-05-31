import random

# Создаем пустую сетку 3×3 как вложенный список
grid = [[' ' for _ in range(3)] for _ in range(3)]
row_keys = ['A', 'B', 'C']
col_keys = ['1', '2', '3']

# Функция для вывода сетки в терминале
def show_grid():
    print("   1   2   3")
    for r_idx in range(3):
        print(f"{row_keys[r_idx]}  {grid[r_idx][0]} | {grid[r_idx][1]} | {grid[r_idx][2]}")
        if r_idx < 2:
            print("  ---+---+---")
    print()

# Функция для проверки победы
def check_victory(sign):
    # Проверяем строки
    for row in grid:
        if all(cell == sign for cell in row):
            return True
    # Проверяем столбцы
    for c_idx in range(3):
        if all(grid[r_idx][c_idx] == sign for r_idx in range(3)):
            return True
    # Проверяем диагонали
    if grid[0][0] == grid[1][1] == grid[2][2] == sign:
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] == sign:
        return True
    return False

# Функция для проверки ничьи
def check_tie():
    return all(grid[r_idx][c_idx] != ' ' for r_idx in range(3) for c_idx in range(3))

# Функция для ввода хода игрока
def get_player_move(sign):
    while True:
        turn_input = input(f"Игрок {sign}, введите ход (например, A1): ").upper().strip()
        if len(turn_input) == 2 and turn_input[0] in row_keys and turn_input[1] in col_keys:
            row_idx = row_keys.index(turn_input[0])
            col_idx = col_keys.index(turn_input[1])
            if grid[row_idx][col_idx] == ' ':
                grid[row_idx][col_idx] = sign
                break
        print("Некорректный ход, попробуйте еще раз.")

# Основной блок программы
participants = ['X', 'O']
# Случайным образом выбираем первого игрока
active_player = random.choice(participants)
print(f"Первым ходит {active_player}\n")

show_grid()
while True:
    get_player_move(active_player)
    show_grid()
    if check_victory(active_player):
        print(f"Игрок {active_player} победил!")
        break
    if check_tie():
        print("Ничья!")
        break
    # Меняем активного игрока
    active_player = 'O' if active_player == 'X' else 'X'
