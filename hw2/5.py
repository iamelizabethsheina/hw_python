max_num = 0  # максимальное число в последовательности
count_max = 1  # количество элементов, равных максимальному числу

# считываем числа до 0 и находим максимальное число
num = int(input())
while num != 0:
    if num > max_num:
        max_num = num
        count_max = 1
    elif num == max_num:
        count_max += 1
    num = int(input())

print(count_max)  # выводим ответ на задачу
