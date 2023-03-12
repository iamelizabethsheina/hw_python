x = int(input())

divisors = 0
for i in range(1, x+1):
    if x % i == 0:
        divisors += 1
# находим делитель, если делится без остатка, то в переменную делителя добавляем 1
print(divisors)
