prev = int(input())
max_len = 1
current_len = 1

while True:
    n = int(input())
    if n == 0:
        break
    if n > prev:
        current_len += 1
    else:
        max_len = max(max_len, current_len)
        current_len = 1
    prev = n

max_len = max(max_len, current_len)
print(max_len)
