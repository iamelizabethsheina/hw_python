prev = int(input())
max_len = 1
current_len = 1

while True:
    n = int(input())
    if n == 0:
        break # вводим числа, пока не равно 0
    if n > prev:
        current_len += 1
        #если след число больше, то прибавляем к длине
    else:
        max_len = max(max_len, current_len)
        current_len = 1
    prev = n

max_len = max(max_len, current_len)
print(max_len)
