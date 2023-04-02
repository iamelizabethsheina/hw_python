
def can_eat(knight_pos, other_pos):
    # Вычисляем разницу между координатами коня и другой фигуры
    dx = abs(knight_pos[0] - other_pos[0])
    dy = abs(knight_pos[1] - other_pos[1])
    # Проверяем, является ли разница достаточной для того, чтобы конь смог съесть фигуру
    return (dx == 1 and dy == 2) or (dx == 2 and dy == 1)
    result = can_eat((2, 1), (4, 2))
    print(result) # Вывод: True