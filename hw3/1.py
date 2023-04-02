def can_eat(knight_pos, other_pos):
    """
    Функция can_eat проверяет, может ли конь съесть другую фигуру
    на шахматной доске.

    Аргументы:
    - knight_pos: кортеж с координатами коня (x, y)
    - other_pos: кортеж с координатами другой фигуры (x, y)

    Возвращает: True, если конь может съесть другую фигуру, иначе False.
    """
    # Проверяем, что расстояние между x и y координатами коня и другой фигуры
    # соответствует правилам хода коня на шахматной доске
    dx = abs(knight_pos[0] - other_pos[0])
    dy = abs(knight_pos[1] - other_pos[1])
    if dx == 1 and dy == 2 or dx == 2 and dy == 1:
        return True
    else:
        return False



result = can_eat((1, 2), (2, 4))
print(result) # True

result = can_eat((4, 4), (6, 5))
print(result) # True
